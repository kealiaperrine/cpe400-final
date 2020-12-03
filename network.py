import random
import networkx as nx
import matplotlib.pyplot as plt
import statistics

# gets user input for how many nodes/routers are within the network
    # returns: number of nodes (integer)
def get_node_amt():
    num_nodes = int(input("Enter the number of nodes/routers in the network: "))

    return num_nodes

# gets user input for the source or starting node
    # parameters: num_nodes = total number of nodes
    # returns: number of the src node (integer)
def get_src(num_nodes):
    src = -1
    src = int(input("Enter src node (0 to number of nodes-1): "))

    # if user inputs invalid src node, request until valid
    while src < 0 or src > (num_nodes - 1):
        src = int(input("Invalid src node. Enter src node (0 to number of nodes-1): "))

    return src

# gets user input for the destination or final node
    # parameters: num_nodes = total number of nodes
    # returns number of the dest node (integer)
def get_dest(num_nodes):
    dest = -1
    dest = int(input("Enter dest node (0 to number of nodes-1): "))

    # if user inputs invalid dest node, request until valid
    while dest < 0 or dest > (num_nodes - 1):
        dest = int(input("Invalid dest node. Enter dest node (0 to number of nodes-1): "))

    return dest    

# gets user input for the probability of failure for each node (per project specifications)
    # parameters: num_nodes = total number of nodes
    # returns list of failure probabilites (index of probability corresponds to node number)
def get_prob(num_nodes):
    fail_probs = []

    for x in range (0, num_nodes):
        prob = -1
        prob = float(input("Enter probability of node " + str(x) + " to fail (0-1): "))

        # if user inputs invalid probability, request until valid
        while prob <= 0 or prob >= 1:
            prob = float(input("Invalid probability. Reenter probability of node " + str(x) + " to fail (0-1): "))

        fail_probs.append(prob)

    return fail_probs

# randomizes the number of edges in the graph
    # parameters: total number of nodes (integer)
    # returns: total number of edges in graph (integer)
def get_num_edges(num_nodes):
    # calcuate the maximum possible number of edges in the graph based on number of nodes
    max = (num_nodes * (num_nodes - 1)) // 2 

    # randomize edges from at least one edge per node to the calculated maximum
    num_edges = random.randint(num_nodes, max)

    return num_edges

# generate a graphs, uses python library networkx 
    # parameters: total number of nodes (integer)
    # returns: networkx graph with weighted edges (represents our network and distance between routers)
def create_graph(num_nodes):
    num_edges = get_num_edges(num_nodes)

    # generates the graph with set number of nodes and edges
    graph = nx.gnm_random_graph(num_nodes, num_edges)

    # add random weights between 1 and 19 for each edge in the graph
    for (u, v) in graph.edges():
        graph.edges[u, v]['weight'] = random.randint(1, 20)

    return graph

def fail_nodes(graph, fail_probs, num_nodes):
    #create threshold for failure value:
    failed = []
    total_fail = random.randint(0, int(num_nodes*0.75))
    for x in range(0, len(fail_probs)):
        rand = random.uniform(0, 1)
        threshold = round(rand, 3)
        #print(threshold)
        
        if fail_probs[x] > threshold and total_fail > len(failed):
            failed.append(x)

    print(total_fail, failed)
    graph.remove_nodes_from(failed)
    return failed

#updates the weights within the graph based on the reliablility (kinda like machine learning)
    # parameters: graph, the failure probabilities of each node
    # returns: nothing
def update_weights(graph, fail_probs):
    avg = statistics.mean(fail_probs)
    avg = round(avg, 3)
    
    print(avg, fail_probs)
    for (fail, (u, v)) in zip(fail_probs, graph.edges()):
        if fail > avg:
            print("update", fail)
            graph.edges[u, v]['weight'] += int(fail*20)


# plots and prints the generate graph, use python libraries networkx and matplotlib
# TO-DO: not have to close graph to continue program?
    # parameters: graph (generated by networkx)
    # returns: nothing
def show_graph(graph, s):
    # plt.ioff()
    plt.title(s)
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels = True)
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels = labels)
    plt.show()
    

def main():
    num_nodes = get_node_amt()
    src = get_src(num_nodes)
    dest = get_dest(num_nodes)
    fail_probs = get_prob(num_nodes)

    graph = create_graph(num_nodes)
    print("This is your randomly created graph, before updated weights:")
    show_graph(graph, 'Random Graph')
    update_weights(graph, fail_probs)
    print("This is your randomly created graph, after updated weights and before router failures:")
    show_graph(graph, 'After Updated Weights')
    failed = fail_nodes(graph, fail_probs, num_nodes)
    print("This is your randomly created graph, after router failures:")
    show_graph(graph, 'After Router Failures'),
    print("The nodes/routers that failed are: ", failed)
    

    # print(num_nodes)
    # print(src)
    # print(dest)
    # print(fail_probs)
    # print(graph.edges)
    # for (u, v) in graph.edges():
        # print(graph.edges[u, v]['weight'])



if __name__ == "__main__":
    main()