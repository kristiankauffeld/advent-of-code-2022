def load_data():
    with open('input.txt', mode="r") as f:
        #lines = f.readlines()
        #lines = f.readline()
        lines = f.read().splitlines()
    return lines

calorie_items = load_data()
#print(calorie_items)

totals = []
currentSum = 0

for element in calorie_items:
    if element != '':
        int_value = int(element)
        currentSum += int_value
    else:
        totals.append(currentSum)
        currentSum = 0
        continue

#print(totals)
max_calorie_value = max(totals)
print("The Elf carrying the most Calories are:")
print(max_calorie_value)
