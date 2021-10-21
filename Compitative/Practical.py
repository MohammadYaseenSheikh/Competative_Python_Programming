import pandas as pd

one = pd.DataFrame({'Name': ['Yaseen', 'Rajat'], 'age': [19, 20]}, index=[1, 2])
two = pd.DataFrame({'Name': ['Sana', 'Labhika'], 'age': [20, 21]}, index=[3, 4])
print(pd.concat([one, two]))
