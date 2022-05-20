import json
import re

json_str = input()
standards = {
    "bus_id": list(range(10_000)),
    "stop_id": list(range(1000)),
    "stop_name": re.compile(r"[A-Z][\w ]*?\s(Road|Avenue|Boulevard|Street)"),
    "next_stop": list(range(1000)),
    "stop_type": {"S", "O", "F", ""},
    "a_time": re.compile(r"([0-1]\d|2[0-3]):[0-5]\d")
}
bus_id_er = 0
stop_id_er = 0
stop_name_er = 0
next_stop_er = 0
stop_type_er = 0
a_time_er = 0
bus_json_data = json.loads(json_str)
for bus in bus_json_data:
    if bus["bus_id"] not in standards["bus_id"]:
        bus_id_er += 1
    if bus["stop_id"] not in standards["stop_id"]:
        stop_id_er += 1
    if type(bus["stop_name"]) != str:
        stop_name_er += 1
    else:
        if not (re.fullmatch(standards["stop_name"], bus["stop_name"])):
            stop_name_er += 1
            # print(bus["stop_name"])
    if bus["next_stop"] not in standards["next_stop"]:
        next_stop_er += 1
    if bus["stop_type"] not in standards["stop_type"]:
        stop_type_er += 1
    if type(bus["a_time"]) != str:
        a_time_er += 1
    else:
        if not re.fullmatch(standards["a_time"], bus["a_time"]):
            a_time_er += 1
total_er = stop_name_er + stop_type_er + a_time_er
print(f"Type and required field validation: {total_er} errors")
# print(f"bus_id: {bus_id_er}")
# print(f"stop_id: {stop_id_er}")
print(f"stop_name: {stop_name_er}")
# print(f"next_stop: {next_stop_er}")
print(f"stop_type: {stop_type_er}")
print(f"a_time: {a_time_er}")

