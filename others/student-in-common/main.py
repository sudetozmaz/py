import pandas as pd

form_df = pd.read_excel("form.xlsx")
form_usr = [i for i in form_df["email"]]

top_df = pd.read_excel("Top Learners.xlsx")
top_usr = [i for i in top_df["email"]]

for i in form_usr:
    if i in top_usr:
        print(i)
