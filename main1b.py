import networkx as nx
import json

with open('Input data\level1b.json', 'r') as f1:
	data = json.load(f1)

N = data["n_neighbourhoods"]  #No.of neighbourhoods
R = data["n_restaurants"]     #No.of restaurants

for i in data["vehicles"].values():
     W = i["capacity"]

f1.close()

# Create a graph
G = nx.Graph()

# Add nodes (Restaurants)
for restaurant in data["restaurants"]:
    G.add_node(restaurant)
# Add nodes (neighborhoods)
for neighborhood in data['neighbourhoods']:
    G.add_node(neighborhood)

# Add edges (distances between neighborhoods & restaurant)
for restaurant, info in data['restaurants'].items():
    distances = info['neighbourhood_distance']
    for i, distance in enumerate(distances):
        G.add_edge(restaurant, f"n{i}", weight=distance)

# Add edges (distances between neighborhoods)
for neighborhood, info in data['neighbourhoods'].items():
    distances = info['distances']
    for i, distance in enumerate(distances):
        G.add_edge(neighborhood, f"n{i}", weight=distance)

# Solve the Traveling Salesman Problem (TSP)
tsp_solution = nx.approximation.traveling_salesman_problem(G)

# Display the optimized delivery route
#print("Optimized delivery route:")
#print(tsp_solution)

# Sort neighborhoods based on order quantity
neighborhoods_sorted = sorted(data['neighbourhoods'].items(), key=lambda x: x[1]['order_quantity'], reverse=True)

# Initialize variables
vehicles = []
current_vehicle = {'neighborhoods': [], 'total_order': 0}

# Assign orders to vehicles based on vehicle capacity
for neighborhood, info in neighborhoods_sorted:
    order_qty = info['order_quantity']

    # If adding this neighborhood's order exceeds capacity, start a new vehicle
    if current_vehicle['total_order'] + order_qty > W:
        vehicles.append(current_vehicle)
        current_vehicle = {'neighborhoods': [], 'total_order': 0}

    # Add neighborhood to current vehicle
    current_vehicle['neighborhoods'].append(neighborhood)
    current_vehicle['total_order'] += order_qty

# Add the last vehicle (if any remaining)
if current_vehicle['neighborhoods']:
    vehicles.append(current_vehicle)

#print(vehicles)

res = {}
# Output the delivery slots
for i, vehicle in enumerate(vehicles):
     s = "path"+(str(i+1))
     l = ['r0']
     l.extend(vehicle['neighborhoods'])
     l.append('r0')
     res[s] = l
    #print(f"Slot {i+1} - Neighborhoods: {slot['neighborhoods']}, Total Order Quantity: {slot['total_order']}")
#print(res)
     
output = {}
output["v0"] = res
print(output)

with open("level1b_output.json", "w") as outfile:
    json.dump(output, outfile)
