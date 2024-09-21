# Start

# Initialize arrays
popcorn_types = ["Tiger", "Sea Salt", "Cheddar", "Sampler pack"]
bags_sold = []

# Prompt user to enter number of bags sold for each flavor
for name in popcorn_types:
    bags = int(input(f"Enter the number of bags sold for {name}: "))
    bags_sold.append(bags)

# Calculate total number of bags sold
total_sold = sum(bags_sold)

# Sort arrays
popcorn_types_sorted, bags_sold_sorted = zip(*sorted(zip(popcorn_types, bags_sold), key=lambda x: x[1]))

# Calculate values
mean_value = total_sold / len(popcorn_types)
if len(popcorn_types) % 2 == 0:
    median_value = (bags_sold_sorted[len(popcorn_types) // 2 - 1] + bags_sold_sorted[len(popcorn_types) // 2]) / 2
else:
    median_value = bags_sold_sorted[len(popcorn_types) // 2]

# Display the report
print("Popcorn Sales Report:")
print("---------------------")
print("Flavor\t\tBags Sold")
print("---------------------")
for name, bags in zip(popcorn_types_sorted, bags_sold_sorted):
    print(f"{name}\t\t{bags}")
print("---------------------")
print(f"Total Sold:\t{total_sold}")
print(f"Mean Value:\t{mean_value}")
print(f"Median Value:\t{median_value}")

# End
