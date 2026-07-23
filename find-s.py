# Find-S Algorithm without CSV

# Dataset
concepts = [
    ["Red", "SUV", "Petrol", "Automatic"],
    ["Blue", "Sedan", "Diesel", "Manual"],
    ["Red", "SUV", "Diesel", "Automatic"],
    ["Red", "SUV", "Petrol", "Manual"]
]

target = ["Yes", "No", "Yes", "Yes"]

# Find the first positive example
S = None
for i in range(len(target)):
    if target[i].lower() == "yes":
        S = concepts[i].copy()
        break

print("Initial Specific Hypothesis:")
print(S)

# Find-S Algorithm
for i in range(len(concepts)):
    if target[i].lower() == "yes":
        for j in range(len(S)):
            if concepts[i][j] != S[j]:
                S[j] = "?"

        print("\nAfter Positive Example", i + 1)
        print(S)

print("\n==========================")
print("Final Specific Hypothesis:")
print(S)

print("\nName   : Ramanathan")
print("Reg No : 192412536")