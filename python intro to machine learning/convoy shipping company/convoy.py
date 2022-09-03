# Write your code here
import pandas as pd
import sqlite3


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

    def to_sql(self):
        vehicle_series = pd.read_csv(f"{self.file_name}[CHECKED].csv")
        conn = sqlite3.connect(f"{self.file_name}.s3db")
        cursor = conn.cursor()
        number_of_records = 0
        cursor.execute('''
        		CREATE TABLE IF NOT EXISTS convoy (
        			vehicle_id integer PRIMARY KEY,
        			engine_capacity integer NOT NULL,
        			fuel_consumption integer NOT NULL,
        			maximum_load integer NOT NULL
        			);
                       ''')
        for row in vehicle_series.itertuples():
            number_of_records += 1
            cursor.execute('''
                        INSERT INTO convoy (vehicle_id, engine_capacity, fuel_consumption, maximum_load)
                        VALUES (?,?,?,?)
                        ''',
                           (row.vehicle_id,
                            row.engine_capacity,
                            row.fuel_consumption,
                            row.maximum_load)
                           )
        conn.commit()
        if number_of_records == 1:
            print(f"1 record was inserted into {self.file_name}.s3db")
        else:
            print(f"{number_of_records} records were inserted into {self.file_name}.s3db")


if __name__ == "__main__":
    print("Input file name")
    while True:
        name = input()
        if name.endswith(".xlsx"):
            name = name[0: -5]
            converter = Converter(name)
            converter.save_csv()
            converter.correct()
            break
        elif name.endswith("[CHECKED].csv"):
            name = name[0: -13]
            converter = Converter(name)
            break
        elif name.endswith(".csv"):
            name = name[0: -4]
            converter = Converter(name)
            converter.correct()
            break
    converter.to_sql()
