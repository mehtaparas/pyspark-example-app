import pytest
from pandas.testing import assert_frame_equal
from pyspark.sql import Row

from dataframe_utils.transforms import count_per_skill

# Add fixture so SparkSession can be shared for all tests
pytestmark = pytest.mark.usefixtures("spark")


def assert_df_equals(actual_df, expected_df, sort_col):
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
    expected_row = Row("skill_name", "count")
    expected_df = spark.createDataFrame([
        expected_row("spark", 2),
        expected_row("aws", 2),
        expected_row("python", 2),
        expected_row("gcp", 1)
    ])

    actual_df = count_per_skill(input_df)

    assert_df_equals(actual_df, expected_df, "skill_name")

