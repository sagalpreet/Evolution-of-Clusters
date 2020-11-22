from synthnet import *
from simulation import *
from detcom import *
import matplotlib.pyplot as plt
import numpy as np
from networkx.generators.community import LFR_benchmark_graph

def af(G):
    G = add_feature_vector(G, [('uniform', (0, 1))]*5)

def av(G, l=0, u=1):
    G = add_vulnerability_of_node(G, 'uniform', l, u)

def aa(G):
    G = add_age_to_edges(G)
   
def make_init_connections(G, threshold=0.5):
    nodes = list(G.nodes)
    for i in range(len(nodes)-1):
        for j in range(i+1, len(nodes)):
            x1, x2 = G.nodes[nodes[i]]['feature'], G.nodes[nodes[j]]['feature']
            prod = (x1*x2)/(np.linalg.norm(x1)*np.linalg.norm(x2))
            commonality = np.sum(prod)
            if(commonality>threshold):
                G.add_edge(nodes[i], nodes[j])



def show(G):
    nx.draw(G, with_labels=True)
    plt.show()

def get_angle(x, y):
    return np.sum(x*y)/(np.linalg.norm(x)*np.linalg.norm(y))

def get_commonness(G, u, v):
    return get_angle(G.nodes[u]['feature'], G.nodes[v]['feature'])

def get_empty_graph(n):
    G = nx.Graph()
    G.add_nodes_from(list(range(n)))
    return G

def commonness_between(G, group1, group2):
    ar = []
    for u in group1:
        for v in group2:
            ar.append(get_commonness(G, u, v))
    return ar


def analyse(G, clusters):
    commonness = []
    for i in range(len(clusters)):
        ar = []
        for j in range(len(clusters)):
            if j < i:
                ar.append(None)
            else:
                ar.append(commonness_between(G, clusters[i], clusters[j]))
        commonness.append(ar)
    return commonness

def ppanalyse(y, func):
    n = len(y)
    for i in range(-1, n):
        if i<0:
            print(" "*5, end=' ')
        else:
            print(f"{i}".center(5), end=' ')
    print()
    for i in range(n):
        for j in range(-1, n):
            if j<0:
                print(f"{i}".rjust(5), end=' ')
            else:
                if y[i][j]:
                    print(f"{func(y[i][j])}     "[:5], end=' ')
                else:
                    print(" "*5, end=' ')
        print()
