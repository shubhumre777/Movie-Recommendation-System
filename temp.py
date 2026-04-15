import random
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv("data\movies_metadata.csv")

random1 = random.randint(1 , 100)
random2 = random.randint(100 , 201)

new_df = df["original_title"].iloc[random1 : random2]

print(new_df.shape)



