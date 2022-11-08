import pandas as pd

pd.set_option('display.max_columns', 8)

general_hospitals = pd.read_csv(
    r"C:\Users\reshv\PycharmProjects\Data Analysis for Hospitals\Data Analysis for Hospitals\task\test\general.csv")
prenatal_hospitals = pd.read_csv(
    r"C:\Users\reshv\PycharmProjects\Data Analysis for Hospitals\Data Analysis for Hospitals\task\test\prenatal.csv")
sport_hospitals = pd.read_csv(
    r"C:\Users\reshv\PycharmProjects\Data Analysis for Hospitals\Data Analysis for Hospitals\task\test\sports.csv")

prenatal_hospitals = prenatal_hospitals.rename(columns={'HOSPITAL': 'hospital', 'Sex': 'gender'})
sport_hospitals = sport_hospitals.rename(columns={'Hospital': 'hospital', 'Male/female': 'gender'})

all_hospitals = pd.concat([general_hospitals, prenatal_hospitals, sport_hospitals], ignore_index=True)
all_hospitals = all_hospitals.drop(columns=['Unnamed: 0'])
print(all_hospitals.sample(n=20, random_state=30))