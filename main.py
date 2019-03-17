from pyspark.sql import SparkSession

def count_per_skill(df):
    """
    :param df: dataframe with schema: [name: string, technical_skills: array<string>]
    :return : dataframe with two columns - 1) skill name, 2) distinct # of people who have that skill
    """
    # Write function logic here

    # return skills_count


if __name__ == '__main__':
    spark = SparkSession.builder.appName("pyspark-example-app")

    input_df = spark.read.json("data")

    skills_count_df = count_per_skill(df)

    skills_count_df.write.csv("output_data")
