import extract
import pandas as pd

df = pd.json_normalize(extract.data)    #   converts to dataframe
df.to_csv('output.csv', index=False) # index=False prevents writing row numbers as a column
transformed_data = df

print("JSON successfully converted to CSV.")
