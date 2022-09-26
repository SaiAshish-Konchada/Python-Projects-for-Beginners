from faker import Faker
import pandas as pd
fake = Faker()
data = [fake.profile() for i in range(50)]
data = pd.DataFrame(data)
data.to_csv("Fake_Profile_Dataset.csv",index=False)
print(data.head())