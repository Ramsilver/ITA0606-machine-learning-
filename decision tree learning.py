# Product Recommendation using Decision Tree

print("====== PRODUCT RECOMMENDATION SYSTEM ======\n")

# User Input
budget = input("Enter Budget (Low/Medium/High): ").lower()
category = input("Enter Category (Electronics/Fashion): ").lower()
age = input("Enter Age (Young/Adult): ").lower()

print("\n------ Decision Tree ------")

# Decision Tree Logic
if budget == "low":
    print("Budget")
    print(" └── Low")
    if category == "electronics":
        print("     └── Electronics")
        print("         └── Earbuds")
        product = "Earbuds"
    else:
        print("     └── Fashion")
        print("         └── T-Shirt")
        product = "T-Shirt"

elif budget == "medium":
    print("Budget")
    print(" └── Medium")
    if category == "electronics":
        print("     └── Electronics")
        print("         └── Laptop")
        product = "Laptop"
    else:
        print("     └── Fashion")
        print("         └── Handbag")
        product = "Handbag"

elif budget == "high":
    print("Budget")
    print(" └── High")
    if category == "electronics":
        print("     └── Electronics")
        print("         └── Gaming Laptop")
        product = "Gaming Laptop"
    else:
        print("     └── Fashion")
        print("         └── Smart Watch")
        product = "Smart Watch"

else:
    product = "No Recommendation"

print("\n==============================")
print("Recommended Product :", product)
print("==============================")

print("\nName   : Ramanathan")
print("Reg No : 192412536")