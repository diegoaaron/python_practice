cars = ['bmw', 'audi', 'toyota', 'subaru']

x = sorted(cars)

x.append("ferrari")

print(x)

print("--------")

print(cars)

filename = "pi_digits.txt"
print("--------------------------------------")
with open(filename) as file_object:
    lines = file_object.readlines()
    print(lines)