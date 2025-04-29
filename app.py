from pulp import LpProblem, LpVariable, LpMaximize, LpStatus, value
import matplotlib.pyplot as plt

# Create the LP model
model = LpProblem("Crop_Yield_Optimization", LpMaximize)

# Decision variables
wheat = LpVariable("Wheat", lowBound=0)
corn = LpVariable("Corn", lowBound=0)
rice = LpVariable("Rice", lowBound=0)

# Yield per hectare
yield_per_hectare = {'Wheat': 3, 'Corn': 4, 'Rice': 5}

# Resource usage
land_required = {'Wheat': 1, 'Corn': 1, 'Rice': 1}
water_required = {'Wheat': 10, 'Corn': 20, 'Rice': 30}

# Resource limits
total_land = 100
total_water = 2000

# Objective function: Maximize total yield
model += (wheat * yield_per_hectare['Wheat'] +
          corn * yield_per_hectare['Corn'] +
          rice * yield_per_hectare['Rice']), "Total_Yield"

# Constraints
model += wheat + corn + rice <= total_land, "Land_Constraint"
model += (wheat * water_required['Wheat'] +
          corn * water_required['Corn'] +
          rice * water_required['Rice']) <= total_water, "Water_Constraint"

# Solve the model
model.solve()

# Display results
print("Status:", LpStatus[model.status])
print(f"Optimal area for Wheat: {wheat.varValue:.2f} hectares")
print(f"Optimal area for Corn: {corn.varValue:.2f} hectares")
print(f"Optimal area for Rice: {rice.varValue:.2f} hectares")
print(f"Maximum Yield: {value(model.objective):.2f} tons")

# Pie chart of land allocation
labels = ['Wheat', 'Corn', 'Rice']
areas = [wheat.varValue, corn.varValue, rice.varValue]

plt.figure(figsize=(6, 6))
plt.pie(areas, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#f4d03f', '#58d68d', '#5dade2'])
plt.title('Optimal Land Allocation (hectares)')
plt.show()
