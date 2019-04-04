import pytest
from pyspark.sql import SparkSession

APP_NAME = "unit-testing"

# create a fixture that initializes a SparkSession that can be used for all tests
@pytest.fixture(scope="session")
def spark():
    return SparkSession.builder.master("local[*]").appName(APP_NAME).getOrCreate()
