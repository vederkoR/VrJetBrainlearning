import json

dict_buses = {}
stops = {}
starts = set()
finishes = set()
for bus in json.loads(input()):
    dict_buses.setdefault(bus["bus_id"], [False, False])
    if bus["stop_type"] == "S":
        dict_buses[bus["bus_id"]][0] = True
        starts.add(bus["stop_name"])
    elif bus["stop_type"] == "F":
        dict_buses[bus["bus_id"]][1] = True
        finishes.add(bus["stop_name"])
    stops.setdefault(bus["stop_name"], 0)
    stops[bus["stop_name"]] += 1
error_line = None
for k, v in dict_buses.items():
    if not (v[0] and v[1]):
        error_line = k
        continue

if error_line:
    print(f"There is no start or end stop for the line: {error_line}.")
else:
    transfer_list = []
    for k, v in stops.items():
        if v > 1:
            transfer_list.append(k)
    finish_list = sorted(list(finishes))
    start_list = sorted(list(starts))
    transfer_list.sort()
    print(f"Start stops: {len(start_list)}", start_list)
    print(f"Transfer stops: {len(transfer_list)}", transfer_list)
    print(f"Finish stops: {len(finish_list)}", finish_list)

