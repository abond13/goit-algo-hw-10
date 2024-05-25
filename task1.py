import pulp

problem = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

problem += lemonade + fruit_juice, "Total_Production"

problem += 2 * lemonade + fruit_juice <= 100, "Water_Constraint"
problem += lemonade <= 50, "Sugar_Constraint"
problem += lemonade <= 30, "Lemon_Juice_Constraint"
problem += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"

problem.solve()

print(f"Status: {pulp.LpStatus[problem.status]}\n\n")
print(f"Lemonade: {pulp.value(lemonade):>7}")
print(f"Fruit Juice: {pulp.value(fruit_juice)}\n")