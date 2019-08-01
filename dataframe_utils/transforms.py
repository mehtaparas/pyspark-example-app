from pyspark.sql.functions import *


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

# This is a dummy function that contains no logic. In this workshop, we will be adding the logic to make the test pass.
def filter_by_skill(dataframe,skill):
    return dataframe


def get_workshop_dataframe(df_people, df_state_coolness_index):
    """
    this function takes in a dataframe of people and dataframe of state_coolness_indices
    and computes if the state is cool
    :param df_people: people dataframe
    :param df_state_coolness_index
    """

    df_state_peeps_count = df_people.groupBy("state").count()
    df_join = df_state_peeps_count.join(df_state_coolness_index, ['state'], how = 'inner')
    df_result = df_join.withColumn("is_cool", when(col('coolness_factor') * col('count') > lit(50), 'true')
                                   .otherwise('false'))
    # df_result.show()

    return df_result
