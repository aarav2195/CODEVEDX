import pandas as pd
import random

data = []

for i in range(100):

    attendance = random.randint(50,100)
    marks = random.randint(40,100)
    study_hours = random.randint(1,8)

    final_performance = round(attendance * 3 + marks * 5 + study_hours * 3,2)

    data.append([attendance,marks,study_hours,final_performance])

df = pd.DataFrame(data,columns=["attendance","marks","study_hours","final_performance"])

df.to_csv("dataset.csv",index=False)

print("Dataset generated successfully!")