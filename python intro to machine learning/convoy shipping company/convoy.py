# Write your code here
import pandas as pd


class Converter:
    def __init__(self, file_name):
        self.file_name = file_name

    def save_csv(self):
        vehicle_series = pd.read_excel(f"{self.file_name}.xlsx", sheet_name='Vehicles')
        number_of_lines = vehicle_series.shape[0]
        if number_of_lines == 1:
            print(f"1 line was added to {self.file_name}.csv")
        else:
            print(f"{number_of_lines} lines were added to {self.file_name}.csv")
        vehicle_series.to_csv(f"{self.file_name}.csv", index=False, header=True)


if __name__ == "__main__":
    print("Input file name")
    while True:
        name = input()
        if name.endswith(".xlsx"):
            name = name[0: -5]
            break
    converter = Converter(name)
    converter.save_csv()
