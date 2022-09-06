# Write your code here
import pandas as pd
import sqlite3
import json
from dicttoxml import dicttoxml


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
                if str(vehicle_series.iat[i, j]).isnumeric():
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
        			maximum_load integer NOT NULL,
        			score integer NOT NULL
        			);
                       ''')
        for row in vehicle_series.itertuples():
            number_of_records += 1
            points = Converter.point_calculator(row)
            cursor.execute('''
                        INSERT INTO convoy (vehicle_id, engine_capacity, fuel_consumption, maximum_load, score)
                        VALUES (?,?,?,?,?)
                        ''',
                           (row.vehicle_id,
                            row.engine_capacity,
                            row.fuel_consumption,
                            row.maximum_load,
                            points)
                           )
        conn.commit()
        conn.close()
        if number_of_records == 1:
            print(f"1 record was inserted into {self.file_name}.s3db")
        else:
            print(f"{number_of_records} records were inserted into {self.file_name}.s3db")

    @staticmethod
    def point_calculator(row):
        points = 0
        fuel_consumed = 4.5 * row.fuel_consumption
        pip_stops = fuel_consumed / row.engine_capacity
        if pip_stops <= 1:
            points += 2
        elif pip_stops <= 2:
            points += 1

        if fuel_consumed <= 230:
            points += 2
        else:
            points += 1

        if row.maximum_load >= 20:
            points += 2

        return points

    def to_json(self):
        conn = sqlite3.connect(f"{self.file_name}.s3db")
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        rows = cursor.execute('''
                        SELECT * from convoy
                        ''').fetchall()
        conn.commit()
        conn.close()
        vehicles_to_json = []
        vehicles_to_xml = []
        for row in rows:
            temp_row = dict(row)
            if temp_row["score"] > 3:
                del temp_row["score"]
                vehicles_to_json.append(temp_row)
            else:
                del temp_row["score"]
                vehicles_to_xml.append(temp_row)
        num_of_vehicles_json = len(vehicles_to_json)
        json_data_formatted = {"convoy": vehicles_to_json}
        with open(f"{self.file_name}.json", "w") as json_file:
            json.dump(json_data_formatted, json_file)
        if num_of_vehicles_json == 1:
            print(f"1 vehicle was saved into {self.file_name}.json")
        else:
            print(f"{num_of_vehicles_json} vehicles were saved into {self.file_name}.json")

        xml_total = ""
        for vehicle in vehicles_to_xml:
            xml = dicttoxml(vehicle, attr_type=False, root='vehicle')
            xml_formatted_1 = " <vehicle> " + str(xml)[2:-1] + " </vehicle> "
            xml_total += xml_formatted_1
        xml_final = "<convoy> " + xml_total + " </convoy>"
        num_of_vehicles_xml = len(vehicles_to_xml)

        with open(f"{self.file_name}.xml", "w") as xml_file:
            xml_file.write(xml_final)
        if num_of_vehicles_xml == 1:
            print(f"1 vehicle was saved into {self.file_name}.xml")
        else:
            print(f"{num_of_vehicles_xml} vehicles were saved into {self.file_name}.xml")


if __name__ == "__main__":
    print("Input file name")
    while True:
        name = input()
        if name.endswith(".xlsx"):
            name = name[0: -5]
            converter = Converter(name)
            converter.save_csv()
            converter.correct()
            converter.to_sql()
            break
        elif name.endswith("[CHECKED].csv"):
            name = name[0: -13]
            converter = Converter(name)
            converter.to_sql()
            break
        elif name.endswith(".csv"):
            name = name[0: -4]
            converter = Converter(name)
            converter.correct()
            converter.to_sql()
            break
        elif name.endswith(".s3db"):
            name = name[0: -5]
            converter = Converter(name)
            break
    converter.to_json()
