import pandas as pd

sq_data = pd.read_csv("data.csv")

pd.set_option('display.max_columns', None)
#print(sq_data.head(5))

#print(sq_data.value_counts())

values = sq_data["Primary Fur Color"].value_counts()

new_data = pd.DataFrame({'Primary Fur Color':values.index, 'Count':values.values})

new_data.to_csv("squirrel_count.csv")


