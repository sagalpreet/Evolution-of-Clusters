import random
import networkx as nx
import numpy as np

def Simulate(G, num_time_steps, threshold, edge_strength = 0):
    '''
    Takes as parameters the networkx graph, number of time steps for which the simulation is to be run and threshold at which two nodes are to be connected
    Returns the updated graph
    edge_strength is not a parameter to be taken care of. 0 value refers to the situation in which older edges are more stronger and 1 value - the opposite
    '''

    for _ in range(num_time_steps):
        G = simulate_one_time_step(G, threshold, edge_strength)

    return G

def simulate_one_time_step(G, threshold, edge_strength):
    '''
    This function just acts as a helper function for the function Simulate
    '''

    # create a copy of graph G which is to be updated
    H = G.copy()

    # iterate over all the nodes of the Graph and update the feature vector for them on the basis of their neighbours
    for i in G.nodes:
        initial_array = G.nodes[i]['feature']
        neighbours = list(G.neighbors(i))

        if len(neighbours) == 0:
            break

        # target array is the weighted mean of feature vectors weighted over their age
        target_array = np.array([0.0 for i in range(5)])

        total_weight = 0

        if edge_strength == 0:
            for j in neighbours:
                target_array += G.nodes[j]['feature'] * G.edges[(i, j)]['age']
                total_weight += G.edges[(i, j)]['age']
                # incrementing age of each edge
                G.edges[(i, j)]['age'] += 1
        else:
            for j in neighbours:
                target_array += G.nodes[j]['feature'] / G.edges[(i, j)]['age']
                total_weight += 1 / G.edges[(i, j)]['age']
                # incrementing age of each edge
                G.edges[(i, j)]['age'] += 1
        
        target_array /= total_weight

        alpha = G.nodes[i]['vulnerability']
        
        # performing update on the feature vectors of the graph
        H.nodes[i]['feature'] = (1 - alpha) * initial_array + alpha * target_array
    
    # now iterate over all the nodes and establish links between two nodes if their feature vectors agree over certain range and they are separated by atmost one node
    # also break edges which have become weaker than the threshold

    for i in H.nodes:
        prospective = set()
        neighbours = list(H.neighbors(i))

        ''' 
        the loop below contains two blocks, depending on their relative positioning (which one first), the code changes as follows
        (1) the code removes the edges which are now below the threshold value and takes the neighbours of only remaining edges as prospectives
        (2) the code first takes all the nodes separated by one node as prospective nodes and then deletes all the immediate nodes that are below threshold now
        Currently the order is such that (2) is being followed
        '''
        for j in neighbours:
            # block 1 starts
            j_neighbours = list(H.neighbors(j)) 
            for k in j_neighbours:
                if H.has_edge(i, k) == False:
                    prospective.add(k)
            # block 1 ends

            # block 2 starts
            x1, x2 = H.nodes[i]['feature'], H.nodes[j]['feature']
            commonality = np.sum (x1 * x2) / ( np.linalg.norm(x1) * np.linalg.norm(x2) )

            if commonality < threshold:
                H.remove_edge(i, j)
            # block 2 ends
            
        
        prospective = list(prospective)
        
        for j in prospective:
            x1, x2 = H.nodes[i]['feature'], H.nodes[j]['feature']
            commonality = np.sum (x1 * x2) / ( np.linalg.norm(x1) * np.linalg.norm(x2) )

            if commonality >= threshold:
                H.add_edge(i, j)
                H.edges[(i, j)]['age'] = 1

    return H