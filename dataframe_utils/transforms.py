from pyspark.sql.functions import col, explode, lower, concat_ws, split


def count_per_skill(df):
    """
    :param df: dataframe with schema: [name: string, technical_skills: array<string>]
    :return : dataframe with two columns - 1) skill name, 2) # of people who have that skill
    """
    # Write function logic here
    skills_count = df.select(
        col("name"),
        explode(col("technical_skills")).alias("skill_name")
    ).distinct().groupBy("skill_name").agg({"name": "count"})

    return skills_count


def lower_array(df, array_col):
    """
    this function will take an array<string> column in the passed dataframe
    and lowercase each element in the array
    :param df: input dataframe
    :param array_col: name of the array<string> column
    :return: dataframe with array<string> column with lowercased elements
    """
    return df.withColumn(array_col,
                         split(lower(concat_ws(",", col(array_col))), ","))
