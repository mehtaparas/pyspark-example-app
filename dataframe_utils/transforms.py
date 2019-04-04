from pyspark.sql.functions import col, explode


def count_per_skill(df):
    """
    :param df: dataframe with schema: [name: string, technical_skills: array<string>]
    :return : dataframe with two columns - 1) skill name, 2) # of people who have that skill
    """
    # Write function logic here
    skills_count = df.select(
        col("name"),
        explode(col("technical_skills")).alias("skill_name")
    ).groupBy("skill_name").agg({"name": "count"})

    return skills_count