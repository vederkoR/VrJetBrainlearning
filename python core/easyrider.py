import json
import time


def time_converter(date_string):
    converted_time = time.strptime(date_string, "%H:%M")
    return converted_time


bus_data = json.loads(input())
error_list = []
lines_checked = []
for i, bus in enumerate(bus_data):
    if i == 0 or bus["bus_id"] != bus_data[i - 1]["bus_id"] or bus["bus_id"] in lines_checked:
        continue
    if time_converter(bus["a_time"]) < time_converter(bus_data[i - 1]["a_time"]):
        error_list.append((bus["bus_id"], bus["stop_name"]))
        lines_checked.append(bus["bus_id"])

print("Arrival time test:")
if not error_list:
    print("OK")
else:
    for item in error_list:
        print(f"bus_id line {item[0]}: wrong time on station {item[1]}")

