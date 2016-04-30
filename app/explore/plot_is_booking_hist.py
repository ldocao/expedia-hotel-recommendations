import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Database
df=pd.read_csv("../../../train_etienne.csv",nrows=10000)


# Distribution of is_booking 
plt.figure()
sns.distplot(df.groupby("user_id")["is_booking"].sum(),kde=False)
plt.ylabel("number of users")
plt.title("Distribution of number of booking")
plt.savefig("is_booking_hist.pdf")