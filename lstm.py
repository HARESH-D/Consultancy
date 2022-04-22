import numpy as np
import pandas as pd
import seaborn as sns
import tensorflow as tf
import sklearn.metrics as metrics
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split

df1 = pd.read_csv(r"Data_set_1.csv")
df2 = pd.read_csv(r"Data_set_2.csv")
df = pd.concat([df1, df2]).reset_index(drop=True)
df_product_count = pd.DataFrame([])
df_product_count['product'] = df['product']
df_product_count['freq'] = df.groupby('product')['product'].transform('count')
print(df_product_count['freq'])
df_product_count = df_product_count.drop_duplicates(subset=["product"], keep='first', ignore_index=True)
print(df_product_count)
df_product_count = df_product_count.sort_values(by=['freq'], ascending=False)
df_product_count.to_csv("productlist.csv")
print(df_product_count)
product_list = df_product_count["product"].values
print("No of Parts: ", len(product_list))
