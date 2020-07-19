import pandas as pd
import matplotlib.pyplot as plt

data1 = pd.read_csv('data.csv')
df = pd.DataFrame()
col = (data1.rates >= '2019-01-01') & (data1.rates <= '2019-01-31')
row = data1.rates_INR

plt.plot(col, row, color="PURPLE")

plt.xlabel("Year", color="RED")
plt.ylabel("Currency", color="RED")
plt.title("Currency Graph", color="RED")

plt.show()


