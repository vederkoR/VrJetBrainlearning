import json

dict_buses = {}
for bus in json.loads(input()):
    dict_buses.setdefault(bus["bus_id"], 0)
    dict_buses[bus["bus_id"]] += 1
for k, v in dict_buses.items():
    print(f"bus_id: {k}, stops: {v}")

