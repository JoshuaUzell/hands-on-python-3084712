NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

i = 0
while i < len(NAMES):
    print(NAMES[i], AGES[i])
    i += 1

age_count = 0
while age_count < len(AGES):
    print(AGES[age_count])
    age_count += 1

for name in NAMES:
    print(name)

#This is how you go through 2 lists at once
for name, age in zip(NAMES, AGES):
    print(f"{name} {age}")

#Goes through a reversed collection
for name in reversed(NAMES):
    print(name)

for i in range(5):
    print(i)

for name, age in zip(reversed(NAMES), reversed(AGES)):
    print(f"{name} {age}")

# enumerate - lets you see where exactly you are in terms of the iteration
for count, name in enumerate(NAMES):
    print(f"{count} {name}")