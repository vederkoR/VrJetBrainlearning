import pandas as pd

pd.set_option('display.max_columns', 8)

general_hospitals = pd.read_csv(
    r"C:\Users\reshv\PycharmProjects\Data Analysis for Hospitals\Data Analysis for Hospitals\task\test\general.csv")
prenatal_hospitals = pd.read_csv(
    r"C:\Users\reshv\PycharmProjects\Data Analysis for Hospitals\Data Analysis for Hospitals\task\test\prenatal.csv")
sport_hospitals = pd.read_csv(
    r"C:\Users\reshv\PycharmProjects\Data Analysis for Hospitals\Data Analysis for Hospitals\task\test\sports.csv")

print(general_hospitals.head(20))
print(prenatal_hospitals.head(20))
print(sport_hospitals.head(20))
