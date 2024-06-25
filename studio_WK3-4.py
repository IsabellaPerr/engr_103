# declares a function which calculates cost of a given amount of electricity at a set cost. all units are in USD and
# kWh

def avg_ele_cost(ele_used, cost):
    return round(ele_used * cost)


# declares a function which calculates the amount of electricity used each year in kWh with a given MPGe assuming they
# have driven 15,000 miles, then rounds the answer to the nearest whole number

def avg_ele_used(MPGe):
    return round(15000 * (33705 / 1000) / MPGe)


MPGe = float(input("Enter MPGe \n"))

# year_energy = avg_ele_used(MPGe)
# cost_per_year_cheap = avg_ele_cost(year_energy, 0.1)
# cost_per_year_expensive = avg_ele_cost(year_energy, 0.13)

print(f"Amount of energy in kWh each year is: {avg_ele_used(MPGe)}. \n")
print(f"The cost per year at 0.1 per kWh is {avg_ele_cost(avg_ele_used(MPGe), 0.1)}.\n")
print(f"The cost per year at 0.13 is {avg_ele_cost(avg_ele_used(MPGe), 0.13)}. \n")
