NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

JOHN = NAMES[0]
PAUL = NAMES[1]

#Gives back the names John and Paul - to the left of 2
JOHN_PAUL = NAMES[:2]

#Gives back the names George and Ringo - to the right of 2
GEORGE_RINGO = NAMES[2:]

#Gives the names in reverse order
REVERSE = NAMES[::-1] #Start:Stop:Step:-1
EVERY_OTHER = NAMES[::2] #Gives every other name besides Paul and Ringo

#Gives sum of all the ages
print(sum(AGES))
print(min(AGES))
print(max(AGES))

print(JOHN_PAUL)
print(GEORGE_RINGO)
print(REVERSE)
print(EVERY_OTHER)
