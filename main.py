from pyspark.sql import SparkSession

from dataframe_utils.transforms import count_per_skill


def main():
    spark = SparkSession.builder.appName("pyspark-example-app").getOrCreate()

    input_df = spark.read.json("data")

    skills_count_df = count_per_skill(input_df)

    skills_count_df.write.csv("output_data")


if __name__ == '__main__':
    main()
