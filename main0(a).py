#optimized code for level0

import networkx as nx
import json

with open('Input data\level1a.json', 'r') as f1:
	data = json.load(f1)

f1.close()

# Create a graph
G = nx.Graph()

# Add nodes (Restaurants)
for restaurant in data["restaurants"]:
    G.add_node(restaurant)
# Add nodes (neighborhoods)
for neighborhood in data['neighbourhoods']:
    G.add_node(neighborhood)

#print(G)

# Add edges (distances between neighborhoods & restaurant)
for restaurant, info in data['restaurants'].items():
    distances = info['neighbourhood_distance']
    for i, distance in enumerate(distances):
        G.add_edge(restaurant, f"n{i}", weight=distance)

#print(distances)
#print(G)

# Add edges (distances between neighborhoods)
for neighborhood, info in data['neighbourhoods'].items():
    distances = info['distances']
    for i, distance in enumerate(distances):
        G.add_edge(neighborhood, f"n{i}", weight=distance)

#print(distances)
#print(G)

# Solve the Traveling Salesman Problem (TSP)
tsp_solution = nx.approximation.traveling_salesman_problem(G)

# Display the optimized delivery route
print("Optimized delivery route:")
print(tsp_solution)


output = {"v0": {'path':tsp_solution}}

with open("level0_output.json", "w") as outfile:
    json.dump(output, outfile)
     