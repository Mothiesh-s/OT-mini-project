from scipy.optimize import minimize

# Define the objective function (we NEGATE it because scipy does minimization)
def objective(vars):
    x, y = vars
    # Crop yield increases with water and fertilizer but with diminishing returns
    yield_estimate = (30 * (x ** 0.5)) + (20 * (y ** 0.5)) - (0.05 * x) - (0.1 * y)
    return -yield_estimate  # maximize by minimizing the negative

# Define constraints
def constraint1(vars):
    x, y = vars
    return 1000 - x  # Water limit (≤ 1000 liters)

def constraint2(vars):
    x, y = vars
    return 500 - y   # Fertilizer limit (≤ 500 kg)

def constraint3(vars):
    x, y = vars
    return x         # Water must be ≥ 0

def constraint4(vars):
    x, y = vars
    return y         # Fertilizer must be ≥ 0

# Initial guess
initial_guess = [500, 200]

# Define constraint dictionary
cons = [{'type': 'ineq', 'fun': constraint1},
        {'type': 'ineq', 'fun': constraint2},
        {'type': 'ineq', 'fun': constraint3},
        {'type': 'ineq', 'fun': constraint4}]

# Run optimization
solution = minimize(objective, initial_guess, constraints=cons)

# Output results
water_opt, fertilizer_opt = solution.x
max_yield = -solution.fun

print(f"Optimal Water Usage: {water_opt:.2f} liters")
print(f"Optimal Fertilizer Usage: {fertilizer_opt:.2f} kilograms")
print(f"Maximum Estimated Yield: {max_yield:.2f} units")
