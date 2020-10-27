import random
import networkx as nx

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