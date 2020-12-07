# CPE 400 Final Project - Faulty Network

## This acts as README for github as well as Code Explaination document

## Idea
My network uses a psuedo-machine learning idea. If a node/router is very unreliable, the paths to that node get an increased weight.

After updating the weights, Dijkstra's path is found. This is novel because you would not usually use a more global algorithm like Dijkstra's for a nonstable network.

You would typically use a decentrailized algorithm. However, since faulty nodes are being discouraged from being used within the path since the weights are increased, Dijkstra's path can work.

However, if Dijkstra's path does manage to pick a failed node, BellmanFord is then run to see if a path exists in the faulty network.

However, from my own testing of the algorithm it's not likely that Bellman's is needed, unless a lot of the routers fail. Or if a node that is usually reliable actually happens to fail.

The reason this is psuedo-machine learning is because instead of a user entering the probabilities, a network could learn the probabilities of each node over time, adjusting each iteration if the router failed or succeeded. However, for the scope of this project, and per the project instructions, the probabilities are user input and that is what is used to update the weights of the paths.


## Instructions to run
To complete this project I used Python 3.9.0, thus that is the python version I suggest, but any python 3 would work.

Python dependencies:

```bash
pip install networkx 
```

```bash
pip install matplotlib 
```

```bash
pip install statistics 
```

You may also have to install (I don't use it but sometimes python needs it)
```bash
pip install numpy 
```

To run the program:
```bash
python3 network.py 
```

For the number of nodes, source node, and destination node, enter an integer.
The source and destination source node numbers must be within the range 0-number of nodes - 1.

For the probability of a node to fail, enter a float.
The probability needs to be within 0 to 1, noninclusive.
There is no rule, but I recommend entering up to 3 decimal points.

When the graph is generated, a corresponding message will be written in the terminal.
For example, after the weights are updating, the nodes with updated weights are printed.

**To continue the program you MUST _close_ the graph.**

At the end, it will ask if you want to run the program again. Enter q to quit and any other key to continue.

## Code set up:

_2) the functions and components of the code and how they are connected; 3) the functions and components of the code and their physical significance._

I used python to write this project, and so the program is set up with a main function and functions defined before it to actually do the work for the network simulation.

`get_node_amt()`:

```json
- Asks for user input for the total amount of nodes in the network, asks until valid input is submitted
- Significance: gets important info for setting up network
- Connections: called from main and saved into a variable to be used later
```

`get_src(num_nodes)`:

```json
- Asks for user input for the source node in the network, asks until valid input is submitted
- Significance: gets important info for completing search algorithm
- Connections: called from main and saved into a variable to be used later,
        uses the number of nodes we just inputted to limit valid inputs
```

`get_dest(num_nodes)`:

```json
- Asks for user input for the destination node in the network, asks until valid input is submitted
- Significance: gets important info for completing search algorithm
- Connections: it is called from main and saved into a variable to be used later, 
      uses the number of nodes we just inputted to limit valid inputs
```

`get_prob(num_nodes)`:

```json
- Asks for user input for the probablitity of each node to fail, asks until valid input is submitted
- Significance: gets important info for updating the weights as well as updating the faulty network
- Connections: it is called from main and saved into a list to be used later, 
     uses the number of nodes we just inputted to know how many probabilities to obtain from user
```

`get_num_edges(num_nodes)`:

```json
- Calculates a random number of edges in the range (total number of nodes, max number of edges) to be within the graph/network
        The max number of edges is calculated using: (num_nodes * (num_nodes - 1)) // 2 
- Significance: helps create the random graph for the newtork simulation
- Connections: it is called from create_graph in order to allow the networkx function to create a random graph to signify our network
```


`create_graph(num_nodes)`:

```json
- Creates a random graph using networkx's gnm_random_graph, using the total number of nodes
- Significance: creates the random graph for the newtork simulation, including random weights for the edges (1 to 20 inclusive)
- Connections: it is called from main and saved in a variable to be used multiple times,
            calls get_num_edges to get the number of edges to add in the graph
```

`fail_nodes(graph, fail_probs, num_nodes)`:

```json
- Takes the graph, probability of each node to fail, and the number of nodes in the graph in order to determine which nodes to fail:
            calculate max number of nodes able to fail: random integer from 0 to 80% of the nodes within the graph,
            create random threshold between 0 and 1, then for each node, if its probability is greater than that threshold, the node fails,
            failed nodes are removed from the graph
- Significance: simulates a faulty network by failing nodes
- Connections: it is called from main to update the graph that is passed to it (since python is pass by ref),
            called after weights are updated,
            returns the list of failed nodes for printing to terminal to help user see which nodes failed
```

`update_weights(graph, fail_probs)`:

```json
- Updates weights within the graph based on the failure probabilites,
            calculate average of the probabilities, then for each node, if its probability is greater than that average, the edges connected to it has its weights increased,
            the increase is the failure probability times the max weight when setting random weights, which I set as 20
- Significance: represents the novel idea I added to the faulty network, update the weights of nodes with higher failure probabilites so they are less likely to be pathed over
- Connections: called in main to update the graph that is passed to it,
            called before nodes are failed, allows Dijkstra's path to be found,
            returns the list of nodes that had their weights updated
```

`get_dijkstra(graph, src, dest)`:

```json
- Gets the shortest path using Dijkstra's algorithm in the graph from src to dest in networkx
- Significance: uses the updated weights to find a path through the network that avoids faulty nodes before they fail
- Connections: called in main to get the Dijkstra path that avoids faulty routers,
            called after weights are updated and before nodes are failed,
            returns the list of nodes in the path
```

`get_dijkstra_length(graph, src, dest)`:

```json
- Gets the shortest path length using Dijkstra's algorithm in the graph from src to dest in networkx
- Significance: allows user to see how long the path is using the weights in the graph
- Connections: called in main to get the Dijkstra path length that avoids faulty routers,
            called after weights are updated and after Dijksta path is found and before nodes are failed,
            returns an integer the length of the path
```

`check_path(dpath, failed_nodes)`:

```json
- Checks if the Dijkstra path is still valid after nodes have failed
- Significance: ensures that our path is still valid so that the packet is transmitted
- Connections: called in pathing to see if the path is vaild,
            returns true or false that the path is valid and needs to be recalculated
```

`pathing(graph, src, dest, dpath, dlength, failed_nodes)`:

```json
- Calls check_path to check Dijkstra path is valid, calls Bellman-Ford if necessary, catches error if no path exists
- Significance: ensures that our path is still valid, recalculates if needed, so that the packet is transmitted if possible
- Connections: called in main handle checking path and recalution if needed
            prints the final result and path if possible to user
```

`get_bellmanford(graph, src, dest)`:

```json
- Gets the shortest path using Bellman-Fords's algorithm in the graph from src to dest in networkx
- Significance: only called if the Dijkstra path contained failed node, failsafe for transmitting the packet throught the faulty network
- Connections: called in pathing to get the Bellman-Ford path after nodes failed,
            returns the list of nodes in the path as well as the length of that path
```

`show_graph(graph, s)`:

```json
- prints the current graph
- Significance: allows user to have better understanding of the changes during the simulation since they are given a visual
- Connections: called in main to print the graph at important points during the simulation
            s is a string passed to it to be title of the printed graph for better labeling,
            must close graph pop up before continuing program
```

## My checklist while working
- [x] enter total number of nodes, src, dest

- [x] enter failure probablity for each node

- [x] create random int for number of edges

- [x] create random graph for number of nodes and edges

- [x] print graph

- [x] update weights of each edge, based on faultiness of router (pseudo machine learning is my idea)

- [x] calculate dijkstra path

- [x] create random int for total possible number of failed nodes

- [x] calculated random threshold for head node(0 to 2 less than total nodes)

- [x] if failure prob for node is greather than threshold, add to failed nodes

- [x] remove failed nodes from graph

- [x] print updated graph

- [x] check if dijkstra path has any failed nodes

- [x] if no, done!

- [x] if yes:

- [x] try - run an algorithm that is more flexible (doesnt know everything from start), print path \*still have to pick one

- [x] catch - there is no path, sorry

- [x] continue running until user quits
