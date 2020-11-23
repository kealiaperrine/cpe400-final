# gets user input for how many nodes/routers are within the network
    # returns an intger for the number of nodes
def get_node_amt():
    # string input requested to user then coverted to integer
    num_nodes = int(input("Enter the number of nodes/routers in the network: "))

    return num_nodes

# gets user input for the source or starting node
    # takes in the total number of nodes to ensure src is within that range
    # returns integer which is the number of the src node
def get_src(num_nodes):
    # intialize src node to be invalid
    src = -1

    # string input requested to user then coverted to integer
    src = int(input("Enter src node (0 to number of nodes-1): "))

    # if user inputs invalid src node, request until valid
    while src < 0 or src > (num_nodes - 1):
        src = int(input("Invalid src node. Enter src node (0 to number of nodes-1): "))

    return src

# gets user input for the destination or final node
    # takes in the total number of nodes to ensure dest is within that range
    # returns integer which is the number of the dest node
def get_dest(num_nodes):
    # intialize dest node to be invalid
    dest = -1

    # string input requested to user then coverted to integer
    dest = int(input("Enter dest node (0 to number of nodes-1): "))

    # if user inputs invalid dest node, request until valid
    while dest < 0 or dest > (num_nodes - 1):
        dest = int(input("Invalid dest node. Enter dest node (0 to number of nodes-1): "))

    return dest    

# gets user input for the probability of failure for each node (per project specifications)
    # takes in the total number of nodes to know how many probabilities to request
    # returns list of failure probabilites, index of probability corresponds to node number
def get_prob(num_nodes):
    # initialize list to be empty
    fail_probs = []

    # obtain input for each node
    for x in range (0, num_nodes):
        #initalize probability to be invalid
        prob = -1
        prob = float(input("Enter probability of node " + str(x) + " to fail (0-1): "))

        # if user inputs invalid probability, request until valid
        while prob < 0 or prob > 1:
            prob = float(input("Invalid probability. Reenter probability of node " + str(x) + " to fail (0-1): "))

        # append valid probability to list
        fail_probs.append(prob)
    return fail_probs

def main():
    num_nodes = get_node_amt()
    src = get_src(num_nodes)
    dest = get_dest(num_nodes)
    fail_probs = get_prob(num_nodes)

    print(num_nodes)
    print(src)
    print(dest)
    print(fail_probs)


if __name__ == "__main__":
    main()