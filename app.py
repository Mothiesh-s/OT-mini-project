from pulp import LpProblem, LpVariable, LpMaximize, LpStatus, value
import matplotlib.pyplot as plt

model = LpProblem("Crop_Yield_Optimization", LpMaximize)

wheat = LpVariable("Wheat", lowBound=0)
corn = LpVariable("Corn", lowBound=0)
rice = LpVariable("Rice", lowBound=0)

yield_per_hectare = {'Wheat': 3, 'Corn': 4, 'Rice': 5}


land_required = {'Wheat': 1, 'Corn': 1, 'Rice': 1}
water_required = {'Wheat': 10, 'Corn': 20, 'Rice': 30}


total_land = 100
total_water = 2000

model += (wheat * yield_per_hectare['Wheat'] +
          corn * yield_per_hectare['Corn'] +
          rice * yield_per_hectare['Rice']), "Total_Yield"

model += wheat + corn + rice <= total_land, "Land_Constraint"
model += (wheat * water_required['Wheat'] +
          corn * water_required['Corn'] +
          rice * water_required['Rice']) <= total_water, "Water_Constraint"

model.solve()

print("Status:", LpStatus[model.status])
print(f"Optimal area for Wheat: {wheat.varValue:.2f} hectares")
print(f"Optimal area for Corn: {corn.varValue:.2f} hectares")
print(f"Optimal area for Rice: {rice.varValue:.2f} hectares")
print(f"Maximum Yield: {value(model.objective):.2f} tons")

labels = ['Wheat', 'Corn', 'Rice']
areas = [wheat.varValue, corn.varValue, rice.varValue]

plt.figure(figsize=(6, 6))
plt.pie(areas, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#f4d03f', '#58d68d', '#5dade2'])
plt.title('Optimal Land Allocation (hectares)')
plt.show()
