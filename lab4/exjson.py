import json

with open("/Users/nazerkeanuarova/pp2/lab4/sample-data.json") as f:
    data = json.load(f)


print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<6}")
print("-" * 80)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    descr = attributes["descr"] if attributes["descr"] else ""
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    
    print(f"{dn:<50} {descr:<20} {speed:<7} {mtu:<6}")
