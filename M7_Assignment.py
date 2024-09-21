# Start 

# Open the file ApgarMedicalBest in read mode
file = open("ApgarMedicalBest.txt", "r")

# Initialize an empty list to store patient records
patient_list = []

# Read each line in the file
for line in file:
    # Remove newline character and split the line into components
    components = line.strip().split(", ")

    # Extract the components: name, address and birth year.
    name = components[0]
    address = components[1]
    birth_year = components[2]

    # Append the patient record to the patient list
    patient_list.append((name, address, birth_year))

# Close the file
file.close()

# Print the patient list
for patient in patient_list:
    print(", ".join(patient))

# End 
