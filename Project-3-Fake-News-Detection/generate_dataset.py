import pandas as pd
import random

real_news = [
    "Government launches new policy",
    "India wins cricket match",
    "New Hospital open in Delhi",
    "Scientists develop vaccine",
    "University announces scholarships",
    "Stock market rises today"
]

fake_news = [
    "Aliens found in Mumbai",
    "Dragon seen in Gujarat",
    "Time Traveler arrested",
    "Humans living on Mars",
    "Invisible city discovered",
    "Dinosaurs return to Earth" 
]

data = []

for i in range(100):
    if random.choice([True,False]):
        text = random.choice(real_news)
        label = "REAL"
    else:
        text = random.choice(fake_news)
        label = "Fake"
    data.append([text,label])

df = pd.DataFrame(data,columns=["text","label"])

df.to_csv(r"Project-3-Fake-News-Detection\dataset.csv",index=False)

print("Dataset created successflly")