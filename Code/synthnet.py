import random
import networkx as nx
import numpy as np


def Clauset_Network(num_vertices, num_communities, cross_community_edges):
    '''
    Takes as parameters the number of vertices in the network, number of communtites to have in the network and number of cross_community edges
    Returns the list of vertices and edges, and a dictionary of communities.
    '''

    '''
    Vertices are labelled from 0 to num_vertices-1.
    Communities are labelled from 0 to num_communities.
    '''

    # store vertices and edges in form of lists
    Vertices = [i for i in range(num_vertices)]
    Edges = set()
    Degree = [0 for i in range(num_vertices)]

    # communities to be stored in a dictionary with community label as key and list of edges as value
    communities = {}
    for i in range(num_communities):
        communities[i] = []

    # generating clauset network
    for i in communities:
        for j in Vertices:
            if random.random() < num_communities / num_vertices:
                communities[i].append(j)

    for i in communities:
        for j in communities[i]:
            for _ in range(num_communities + 1):
                x = j
                while (x == j):
                    x = random.choice(communities[i])
                x, j = min(x, j), max(x, j)
                Edges.add((x, j))
                Degree[x] += 1
                Degree[j] += 1

    for i in range(cross_community_edges):
        c1 = c2 = -1
        while(c1 == c2):
            c1 = random.randint(0, num_communities - 1)
            c2 = random.randint(0, num_communities-1)
        while(True):
            x = random.choice(communities[c1])
            y = random.choice(communities[c2])
            x, y = min(x, y), max(x, y)
            if(x != y and Degree[x] >= 2 * num_communities and Degree[y] >= 2 * num_communities and ((x, y) not in Edges)):
                break
        Edges.add((x, y))

    Edges = list(Edges)

    return Vertices, Edges, communities


def add_feature_vector(G, d):
    '''
    Takes as input: a networkx graph and a list specifying the type of distribution as key and repuired parameters as values
    Gives output: a networkx graph with feature vector for each node labelled as feature and can be accessed using G.nodes[i]['feature']
    '''

    '''
    Distributions: 'normal', 'power', 'uniform'
    example: [('uniform', (lower, upper)), ('uniform', (lower, upper)), ('power', (a, lower, upper)), ('normal', (mean, deviation)), ('uniform', (lower, upper))] is a valid value for argument d
    '''

    '''
    Uniform and Power distribution will make characterstic value lie in range (lower, upper)
    but values for normal distribution characteristic depends on mean and deviation input
    '''

    '''
    This function adds feature vector to the graph
    Feature vector is a numpy array
    '''

    num_vertices = G.number_of_nodes()
    samples = []
    for i in d:
        if i[0] == 'uniform':
            lower = i[1][0]
            upper = i[1][1]
            sample = [np.random.uniform(lower, upper)
                      for i in range(num_vertices)]
        elif i[0] == 'power':
            a = i[1][0]
            lower = i[1][1]
            upper = i[1][2]
            sample = np.random.power(a, num_vertices)
            for j in range(num_vertices):
                sample[j] = sample[j] * (upper - lower) + lower
        elif i[0] == 'normal':
            mean = i[1][0]
            deviation = i[1][1]
            sample = np.random.normal(mean, deviation, num_vertices)
        else:
            raise Exception(i[0] + "is not a valid distribution type")

        samples.append(list(sample))

    x = 0
    for i in G.nodes:
        feature = []
        for it in range(5):
            feature.append(samples[it][x])
        x += 1

        feature = np.array(feature)
        G.nodes[i]['feature'] = feature

    return G

def add_vulnerability_of_node(G, distribution, lower = 0, upper = 1, a = 0):
    '''
    Takes as input: a networkx graph, the distribution type of vulnerability - alpha's distribution, lower limit, upper limit, a(required only if distribution = 'power')
    Gives output: a networkx graph with vulnerability for each node labelled as vulnerability and can be accessed using G.nodes[i]['vulnerability']
    '''

    '''
    Distributions: 'power', 'uniform'
    '''

    '''
    Uniform and Power distribution will make characterstic value lie in range (lower, upper)
    Since, the value of vulnerability must be between 0(not at all vulnerable) and 1(fully vulnerable) the lower and upper must be in accordance with this
    '''

    '''
    This function assigns vulnerability value to each node in the graph
    Vulnerability is just a floating point value in the range of 0 and 1
    '''

    if lower < 0:
        raise Exception(lower + "is not a valid value for lower limit")
    if upper > 1:
        raise Exception(upper + "is not a valid value for upper limit")
    if lower > upper:
        raise Exception("Lower limit cannot be greater than the upper limit")

    num_vertices = G.number_of_nodes()
    samples = []
    if distribution == 'uniform':
        sample = [np.random.uniform(lower, upper)
                    for i in range(num_vertices)]
    elif distribution == 'power':
        sample = np.random.power(a, num_vertices)
        for j in range(num_vertices):
            sample[j] = sample[j] * (upper - lower) + lower
    else:
        raise Exception(distribution + "is not a valid distribution type")
    
    samples.append(list(sample))

    x = 0
    for i in G.nodes:
        G.nodes[i]['vulnerability'] = sample[x]
        x += 1

    return G

def add_age_to_edges(G):
    '''
    Takes as input: a networkx graph
    Gives output: a networkx graph with each edge having a label of age (time for which the edge has existed)
    '''

    '''
    Whenever a new edge is added, its time is initialized to 1 and incremented with each time step
    '''

    for i in G.edges:
        G.edges[i]['age'] = 1

    return G