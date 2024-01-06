import json
import numpy as np 
from sys import maxsize 
from itertools import permutations

with open('Input data/level0.json', 'r') as f:
	data = json.load(f)

#print(data)

N = data["n_neighbourhoods"]  #No.of neighbourhoods
R = data["n_restaurants"]     #No.of restaurants
dist_mat =[]
r_dist = []

for i in data['restaurants'].values():
	#print(i['neighbourhood_distance'])
	r_dist.append(0)
	r_dist.extend(i['neighbourhood_distance'])
	#print(r_dist)
	dist_mat.append(r_dist)
	k = 1

for i in data['neighbourhoods'].values():
	temp = []
	temp.append(r_dist[k])
	temp.extend(i['distances'])
	dist_mat.append(temp)
	k+=1

f.close()
#print(dist_mat)

visited = [0] * 21
cost = 0
mapping = {0:'r0',1:'n0',2:'n1',3:'n2',4:'n3',5:'n4',6:'n5',7:'n6',8:'n7',9:'n8',10:'n9',
           11:'n10',12:'n11',13:'n12',14:'n13',15:'n14',16:'n15',17:'n16',18:'n17',19:'n18',20:'n19',21:'r0'}
res = []
def travellingsalesman(c):
    global cost
    adj_vertex = 999
    min_val = 10000
    visited[c] = 1
    res.append(mapping[(c)])
    print(c - 1, end = " ")
    for k in range(21):
        if (dist_mat[c][k] != 0 and visited[k] == 0):
            if (dist_mat[c][k] < min_val):
                min_val = dist_mat[c][k]
                adj_vertex = k
    if (min_val != 999):
        cost = cost + min_val
    if (adj_vertex == 999):
        adj_vertex = 0
        print(adj_vertex + 1, end = " ")
        cost += dist_mat[c][adj_vertex]
        return
    travellingsalesman(adj_vertex)
    
print("Shortest Path: ", end = " ")
travellingsalesman(0)
print("\nMinimum Cost: ", cost)

output = {"v0": {'path':res}}

with open("level0_output.json”", "w") as outfile:
    json.dump(output, outfile)
     