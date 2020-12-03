# cpe400-final

enter total number of nodes, src, dest

enter failure probablity for each node

create random int for number of edges

create random graph for number of nodes and edges

print graph

update weights of each edge, based on faultiness of router (pseudo machine learning is my idea)

calculate dijkstra path

create random int for total possible number of failed nodes

calculated random threshold for head node(0 to 2 less than total nodes)

if failure prob for node is greather than threshold, add to failed nodes

remove failed nodes from graph

print updated graph

check if dijkstra path has any failed nodes

if no, done!

if yes:

try - run an algorithm that is more flexible (doesnt know everything from start), print path \*still have to pick one

catch - there is no path, sorry
