challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

a = challenge[2][1]
b = challenge[2][0]
c = challenge[3]

print(f"My {a}! The {b} do {c}!")

#The string data goes into the 2nd bracket 
d = trial[2]["goggles"]
e = trial[2]["eyes"]
f = trial[3]
print(f"My {d}! The {e} do {f}!")
