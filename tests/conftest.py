import pytest
from pyspark.sql import SparkSession

APP_NAME = "unit-testing"


@pytest.fixture(scope="session")
def spark():
    return SparkSession.builder.master("local[*]").appName(APP_NAME).getOrCreate()

