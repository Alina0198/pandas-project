import pandas as pd
import numpy as np

data = {
    "Ism": ["Ali", "Vali", "Sardor", "Madina"],
    "Yosh": [20, 21, 19, 22],
    "Baho": [85, 90, 78, 92]
}

df = pd.DataFrame(data)

print(df)

print("O'rtacha:", np.mean(df["Baho"]))

df["Natija"] = np.where(df["Baho"] >= 80, "O'tdi", "O'tmadi")

print(df)
