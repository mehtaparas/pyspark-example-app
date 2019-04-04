import pytest
from pandas.testing import assert_frame_equal
from pyspark.sql import Row

from dataframe_utils.transforms import count_per_skill, lower_array

# declare fixture so SparkSession can be shared for all tests
pytestmark = pytest.mark.usefixtures("spark")


def assert_df_equals(actual_df, expected_df, sort_col):
    """
    This function will help us compare dataframes and see if they are equal.
        * the spark dataframes are converted to pandas dataframes
        * then, they are sorted to have a consistent ordering of rows
        * then the function pandas.testing.assert_frame_equal is used compare the values of
          the two dataframes

    :param actual_df: Spark DataFrame that is result of applying function to input df
    :param expected_df: Spark DataFrame with the expected results of the function
    :param sort_col: column to sort by - needed for assert_frame_equal (compares row to row)
    :return: raises an AssertionError if test fails
    """
    actual_df_pd = actual_df.toPandas().sort_values(by=sort_col).reset_index(drop=True)
    expected_df_pd = expected_df.toPandas().sort_values(by=sort_col).reset_index(drop=True)
    assert_frame_equal(actual_df_pd, expected_df_pd)


def test_count_per_skill(spark):
    # create dataframe with test data
    input_row = Row("name", "technical_skills")
    input_df = spark.createDataFrame([
        input_row("Paras", ["spark", "aws", "python", "aws"]),
        input_row("Kendra", ["spark", "aws", "python", "gcp"])
    ])

    # create expected result
    expected_row = Row("skill_name", "count(name)")
    expected_df = spark.createDataFrame([
        expected_row("spark", 2),
        expected_row("aws", 2),
        expected_row("python", 2),
        expected_row("gcp", 1)
    ])

    actual_df = count_per_skill(input_df)

    assert_df_equals(actual_df, expected_df, "skill_name")


def test_lower_array(spark):
    # create dataframe with test data
    input_row = Row("name", "technical_skills")
    input_df = spark.createDataFrame([
        input_row("Paras", ["spark", "AWS", "Python", "aws"]),
        input_row("Kendra", ["Spark", "aws", "pYtHoN", "GCP"])
    ])

    # create dataframe with expected results
    expected_df = spark.createDataFrame([
        input_row("Paras", ["spark", "aws", "python", "aws"]),
        input_row("Kendra", ["spark", "aws", "python", "gcp"])
    ])

    actual_df = lower_array(input_df, "technical_skills")

    assert_df_equals(actual_df, expected_df, "technical_skills")
