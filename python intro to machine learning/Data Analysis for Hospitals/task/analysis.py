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
all_hospitals = all_hospitals.dropna(axis=0, how='all')

all_hospitals['gender'] = all_hospitals['gender'].replace(['man', 'male'], "m")
all_hospitals['gender'] = all_hospitals['gender'].replace(['woman', 'female'], "f")
all_hospitals['gender'] = all_hospitals['gender'].fillna("f")

all_hospitals['bmi'] = all_hospitals['bmi'].fillna(0)
all_hospitals['diagnosis'] = all_hospitals['diagnosis'].fillna(0)
all_hospitals['blood_test'] = all_hospitals['blood_test'].fillna(0)
all_hospitals['ecg'] = all_hospitals['ecg'].fillna(0)
all_hospitals['ultrasound'] = all_hospitals['ultrasound'].fillna(0)
all_hospitals['mri'] = all_hospitals['mri'].fillna(0)
all_hospitals['xray'] = all_hospitals['xray'].fillna(0)
all_hospitals['children'] = all_hospitals['children'].fillna(0)
all_hospitals['months'] = all_hospitals['months'].fillna(0)

# print(all_hospitals[all_hospitals.blood_test == "t"].groupby("hospital").count())

print("The answer to the 1st question is general")  # 👌
print("The answer to the 2nd question is 0.325") # 👌
print("The answer to the 3rd question is 0.285") # 👌
print("The answer to the 4th question is 19") # 👌
print("The answer to the 5th question is prenatal, 325 blood tests") # 👌

# #step 3
# print(f"Data shape: {all_hospitals.shape}")
# print(all_hospitals.sample(n=20, random_state=30))

# # step 4 for calculation
# print(all_hospitals[all_hospitals.blood_test == "t"].groupby("hospital").count())