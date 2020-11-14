import networkx as nx
from community import community_louvain

def get_clusters(G):
    '''
    The only argument is networkx graph.
    The output is list of clusters(which in turn is a list itself)
    eg: [[1, 2, 3],[4, 5, 6], [7, 8, 9], [10, 11, 12]] indicates presence of 4 clusters having 3 nodes each 
    '''
    
    community_dict = community_louvain.best_partition(G)
    
    # Block starts: to obtain the number of communities
    mx = float('-inf')
    for i in community_dict:
        mx = max(mx, community_dict[i])
    mx += 1
    # Block ends

    clusters = [[] for i in range(mx)]

    for i in community_dict:
        clusters[community_dict[i]].append(i)
    
    return clusters
    
'''
the above algorithm doesn't consider a complete subgraph as a community
'''

def get_connected(G):
    '''
    Takes as input networkx graph
    Returns list of sets containing a connected component each
    '''
    components = list(nx.algorithms.components.connected_components(G))
    return components