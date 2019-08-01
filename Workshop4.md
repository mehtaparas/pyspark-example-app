## Workshop 4 - Interactive Coding Workshop

# Problem Statement
You are to determine if a state is cool or not given the number of people in each state and the state's coolness index. The formula to determine state coolness is given below. 

## Formula
(state_population) x (state_coolness_index) = state_total_coolness

if state_total_coolness > 50 ==> state_is_cool = true

## Data with samples
You will be given two Spark Dataframes:
1. `df_people` - this contains the total amount of people in the USA with column fields below and sample data

    | id | first_name | last_name | gender | state  |
    |----|------------|-----------|--------|--------|
    | 1  | George     | Burdell   | M      | Hawaii |
    | 2  | Marge      | Simpson   | F      | Hawaii |

2. `df_state_coolness_index` - This is the lookup table that you will use to find each state's coolness factor with column fields below and sample data point

    | state | coolness_factor |
    |-------|-----------------|
    | Hawaii|  7.654          |

For example, to determine if Hawaii is cool, we can determine that that Hawaii's population has **2** people with a coolness factor of **7.654** which results in a total_coolness of **15.308** which would yield **state_is_cool = false**

## Let's apply this to our dataset!
You will edit a function `get_workshop_dataframe` contained in `dataframe_utils/transforms.py` and it will have to return a result dataframe that contains a column `is_cool`.

If you've written your function correctly, the test case `test_workshop_4` will pass and you will have determined all the states' coolness factors!

## Useful dataframe functions/examples for this exercise

```python
######################
# Dataframe debugging#
######################
df.show()
df.dtypes # Return df column names and data types

#######################
# Dataframe operations#
#######################
# Select with a case statement; df.name => name is a column reference
new_df = df.select(df.name, when(df.age > 3, 1).otherwise(0)).show()

# Dataframe join
join_df = df1.join(df2, [join_key], how='inner')

# Dataframe aggregate operations
df_grouped = df.groupBy("age").count()

# Also note, you can perform mathematical operations between two columns

# Adding Columns
df = df.withColumn('toddler_calculation', when(df.age > 3, 1).otherwise(0)))

# User-Defined Function
#-----------------------
from pyspark.sql.functions import udf
from pyspark.sql.types import BooleanType
# Python function for UDF
def scoreToCategory(score):
    if score >= 80: return True
    elif score >= 60: return True 
    elif score >= 35: return False
    else: return False
 
# Define UDF, two parameters: function and return type
udfScoreToCategory=udf(scoreToCategory, BooleanType())
df.withColumn("category", udfScoreToCategory("score"))

```








