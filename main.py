from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, col

def count_per_skill(df):
    """
    :param df: dataframe with schema: [name: string, technical_skills: array<string>]
    :return : dataframe with two columns - 1) skill name, 2) distinct # of people who have that skill
    """
    # Write function logic here
    skills_count = (df.select(
        col("name"),
        explode(col("technical_skills")).alias("skill_name")
    ).groupBy("skill_name").agg({"name": "count"}))

    return skills_count


if __name__ == '__main__':
    spark = SparkSession.builder.appName("pyspark-example-app").getOrCreate()

    input_df = spark.read.json("data")

    skills_count_df = count_per_skill(input_df)

    skills_count_df.write.csv("output_data")
