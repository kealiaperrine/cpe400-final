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
2) the functions and components of the code and how they are connected; 3) the functions and components of the code and their physical significance.

I used python to write this project, and so the program is set up with a main function and functions defined before it to actually do the work for the network simulation.

`get_node_amt()`:

```json
- Asks for user input for the total amount of nodes in the network, asks until valid input is submitted
- Significance: gets important info for setting up network
- Connectetions: it is called from main and saved into a variable to be used later
```

`get_src(num_nodes)`:

```json
- Asks for user input for the source node in the network, asks until valid input is submitted
- Significance: gets important info for completing search algorithm
- Connectetions: called from main and saved into a variable to be used later,
    uses the number of nodes we just inputted
```

`get_dest(num_nodes)`:

```json
- Asks for user input for the destination node in the network, asks until valid input is submitted
- Significance: gets important info for completing search algorithm
- Connectetions: it is called from main and saved into a variable to be used later, 
    uses the number of nodes we just inputted
```

`get_prob(num_nodes)`:

```json
- Asks for user input for the probablitity of each node to fail, asks until valid input is submitted
- Significance: gets important info for updating the weights as well as updating the faulty network
- Connectetions: it is called from main and saved into a list to be used later, 
    uses the number of nodes we just inputted to know how many probabilities to obtain from user
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
