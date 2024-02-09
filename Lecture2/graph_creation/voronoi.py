import matplotlib.pyplot as plt
import networkx as nx
from scipy.spatial import Voronoi, voronoi_plot_2d
import numpy as np

def create_graph(df):
    G = nx.Graph()

    # add nodes
    for i, (index, row) in enumerate(df.iterrows()):
        G.add_node(i, pos=(row['X'],row['Y']), height=row['Z'], bio=row['bio'])

    #add edges
    nA =  np.array(list(zip(df.X, df.Y)))

    vor = Voronoi(nA)
    G.add_edges_from(vor.ridge_points)

    plt.figure()
    plt.title("Using Voronoi ridges for connecting the graph results in {} nodes and {} edges".format(G.number_of_nodes(), G.number_of_edges()))
    nx.draw(G, pos=nx.get_node_attributes(G,'pos'), node_size=2)
    #plt.show()
