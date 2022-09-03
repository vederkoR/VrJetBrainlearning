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

    def correct(self):
        vehicle_series = pd.read_csv(f"{self.file_name}.csv")
        number_of_lines = vehicle_series.shape[0]
        number_of_rows = vehicle_series.shape[1]
        corrected_cells = 0
        for i in range(number_of_lines):
            for j in range(number_of_rows):
                if vehicle_series.iat[i, j].isnumeric():
                    continue
                else:
                    corrected_cells += 1
                    vehicle_series.iat[i, j] = ''.join(char for char in vehicle_series.iat[i, j] if char.isdigit())
        vehicle_series.to_csv(f"{self.file_name}[CHECKED].csv", index=False, header=True)
        print(f"{corrected_cells} cells were corrected in {self.file_name}[CHECKED].csv")


if __name__ == "__main__":
    print("Input file name")
    while True:
        name = input()
        if name.endswith(".xlsx"):
            name = name[0: -5]
            converter = Converter(name)
            converter.save_csv()
            break
        if name.endswith(".csv"):
            name = name[0: -4]
            converter = Converter(name)
            break
    converter.correct()
