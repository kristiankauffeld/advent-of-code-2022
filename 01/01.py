# --- Part 1 ---

def load_data():
    with open('input.txt', mode="r") as f:
        lines = f.read().splitlines()
    return lines

# Load the data from the input file
calorie_items = load_data()

# Create an empty list to keep track of the total amounts
totals = []

# Keep track of the current sum
currentSum = 0

for element in calorie_items:
    if element != '':
        int_value = int(element)
        currentSum += int_value
    else:
        totals.append(currentSum)
        currentSum = 0
        continue


max_calorie_value = max(totals)
print("The Elf carrying the most Calories are:")
print(max_calorie_value)

# --- PART 2 ---

# Sort the totals list in ascending order
totals.sort()

# Keep only the three largest sums
totals = totals[-3:]

# Return the sum of the totals list
print(sum(totals))
