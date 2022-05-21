import json

bus_data = json.loads(input())
all_stations = dict()
not_allowed = []
on_demand = []
for bus in bus_data:
    all_stations.setdefault(bus["stop_name"], 0)
    all_stations[bus["stop_name"]] += 1
    if bus["stop_type"] == "O":
        on_demand.append(bus["stop_name"])
    elif bus["stop_type"] == "S" or bus["stop_type"] == "F":
        not_allowed.append(bus["stop_name"])
for k, v in all_stations.items():
    if v > 1:
        not_allowed.append(k)
not_allowed = set(not_allowed)
on_demand = set(on_demand)
final_list = sorted(list(on_demand.intersection(not_allowed)))

print("On demand stops test:")
if not final_list:
    print("OK")
else:
    print("Wrong stop type:", final_list)