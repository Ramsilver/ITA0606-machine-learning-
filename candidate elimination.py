import pandas as pd
import numpy as np

# Load the dataset
data = pd.read_csv("candidate_data.csv")

# Attributes and Target
concepts = np.array(data.iloc[:, :-1])
target = np.array(data.iloc[:, -1])

# Candidate Elimination Algorithm
def candidate_elimination(concepts, target):

    specific_h = concepts[0].copy()
    general_h = [["?" for _ in range(len(specific_h))] for _ in range(len(specific_h))]

    print("Initial Specific Hypothesis:")
    print(specific_h)
    print("\nInitial General Hypothesis:")
    print(np.array(general_h))

    for i, h in enumerate(concepts):

        if target[i].lower() == "yes":
            # Update Specific Hypothesis
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    specific_h[x] = "?"
                    general_h[x][x] = "?"

        elif target[i].lower() == "no":
            # Update General Hypothesis
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    general_h[x][x] = specific_h[x]
                else:
                    general_h[x][x] = "?"

        print("\nStep", i + 1)
        print("Specific Hypothesis:", specific_h)
        print("General Hypothesis:")
        print(np.array(general_h))

    # Remove overly general rows
    final_g = [g for g in general_h if g != ["?"] * len(specific_h)]

    return specific_h, final_g

# Run the algorithm
specific, general = candidate_elimination(concepts, target)

print("\n==========================")
print("Final Specific Hypothesis:")
print(specific)

print("\nFinal General Hypothesis:")
for g in general:
    print(g)