import matplotlib.pyplot as plt
import networkx as nx
from scipy.spatial import cKDTree
import numpy as np

def create_graph(df, max_d=1200.0, max_n=5):
    G = nx.Graph()

    # add nodes
    for i, (index, row) in enumerate(df.iterrows()):
        G.add_node(i, pos=(row['X'],row['Y']), height=row['Z'], bio=row['bio'])

    #add edges
    nA =  np.array(list(zip(df.X, df.Y)))
    atree = cKDTree(nA)
    distances, neighbors = atree.query(nA, k=max_n+1)
    for neigh, dist in zip(neighbors,distances):
        for n, d in zip(neigh[1:],dist[1:]):
            if d < max_d:
                G.add_edge(neigh[0], n, length=d)

    plt.figure()
    plt.title("Radius {} graph with {} nodes and {} edges".format(max_d, G.number_of_nodes(), G.number_of_edges()))
    nx.draw(G, pos=nx.get_node_attributes(G,'pos'), node_size=2)
    #plt.show()
