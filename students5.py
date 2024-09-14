import pandas as pd

students = pd.read_csv("data/students.csv")
students = students[['full_name', 'gender_age','fractions','probability','grade']]
students = pd.melt(frame=students, id_vars=['full_name','gender_age','grade'], value_vars=['fractions', 'probability'], value_name='score', var_name='exam')
students = students.drop_duplicates()
students['gender'] = students.gender_age.str[0]
students['age'] = students.gender_age.str[1:]
students = students[['full_name','exam','score','gender','age']]
name_split = students['full_name'].str.split(" ")
students['first_name'] = name_split.str.get(0)
students['last_name'] = name_split.str.get(1)

