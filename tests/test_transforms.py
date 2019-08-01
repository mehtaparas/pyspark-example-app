import pytest
from pandas.testing import assert_frame_equal
from pyspark.sql import Row

from dataframe_utils.transforms import count_per_skill, lower_array, filter_by_skill, get_workshop_dataframe

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

# Workshop 3, beginning with a test
#def test_filter_by_skill(spark):
#    # create dataframe with test data
#    input_row = Row("name", "technical_skills")
#    input_df = spark.createDataFrame([
#        input_row("Paras", ["spark", "aws", "python", "aws"]),
#        input_row("Kendra", ["spark", "aws", "python", "gcp"])
#    ])
#
#    # Create datafram with expected results. We're going to filter by AWS, so Paras' row will be returned, not Kendra's
#    expected_df = spark.createDataFrame([
#        input_row("Paras", ["spark", "aws", "python", "aws"])
#    ])
#
#    actual_df = filter_by_skill(input_df, "aws")
#
#    #arguements are two dataframes, followed by the collumn they should be ordered on
#    assert_df_equals(actual_df,expected_df,"name")

from pyspark.sql.functions import *
def test_workshop_4(spark):
    df_state_coolness_index = spark.read.csv("data/state_coolness_index.csv", header=True)
    df_people = spark.read.csv("data/people.csv", header=True)
    df_answer = spark.read.csv("data/answer.csv", header=True)
    df_answer = df_answer.withColumn('is_cool', col('is_cool').cast("boolean"))

    df_state_count = df_people.groupBy("state").count()

    df_conversion = df_state_coolness_index.join(df_state_count, ['state'], how='inner')
    
    df_conversion = df_conversion.withColumn("is_cool", when(col('coolness_factor')*col('count') > lit(50), True).otherwise(False))
    df_conversion.show()

    df_conversion = df_conversion.select(['state', 'is_cool'])

    df_conversion = get_workshop_dataframe(df_people, df_state_coolness_index)
    assert_df_equals(df_conversion, df_answer, 'state')
