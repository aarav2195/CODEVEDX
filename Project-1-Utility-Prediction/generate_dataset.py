import pandas as pd
import random
data = []
for i in range(50):
    members = random.randint(1,8)
    hours = random.randint(1,12)

    usage = (members * 25) + (hours * 15) + random.randint(-15,15)

    data.append([members,hours,usage])

df = pd.DataFrame(data,columns=["members","hours","usage"])

df.to_csv("dataset.csv",index=False)

print("Dataset Created successfully!")