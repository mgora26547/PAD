import sys

dicts = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
         {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
         {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

print(f"Pre-sorted: {dicts}")

k = sys.argv[1]
if k in dicts[0].keys():
    dicts.sort(key=lambda x: str(x[k]))
    print(f"Sorted: {dicts}")
else:
    print("Given key doesn't exist")

