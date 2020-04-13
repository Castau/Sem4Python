import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout, write_dot
import pygraphviz
import numpy as np
import webget_mod2
import networkx as nx
import gzip


url = 'https://snap.stanford.edu/data/facebook_combined.txt.gz'
sourcepath = 'F:\\Developer\\4semester\\Python\\Afleveringer\\Sem4Python\\Week9\\ThomasExercise\\Downloaded_Files\\facebook_combined.txt.gz'
destpath = './facebook.txt'

# 1. Download the data
# 2. Unpack the data
# 3 .Import the data as an undirected graph in networkx


def ex1(source_filepath, dest_filepath, block_size=65536):
    with gzip.open(source_filepath, 'rb') as s_file, \
            open(dest_filepath, 'wb') as d_file:
        while True:
            block = s_file.read(block_size)
            if not block:
                break
            else:
                d_file.write(block)
        d_file.write(block)
# webget_mod2.download(url)
# ex1(sourcepath, destpath)


# Analyse the data
# The number of nodes in the network
# The number of edges in the network
# The average degree in the network
# A visualisation of the network inside your notebook
def ex2():
    graph = nx.read_edgelist(destpath)
    # print(nx.info(graph))
    degrees = dict(graph.degree)
    nx.draw(graph, nodelist=degrees.keys(), pos=graphviz_layout(graph),
            node_size=[v * 1.2 for v in degrees.values()], width=.05, cmap=plt.cm.GnBu,
            with_labels=True, font_size=4, node_color=range(len(graph)))
    plt.show()
# ex2()


# Part 3: Find the most popular people
# extract and report the 10 people with the most connections in the network
def ex3():
    graph = nx.read_edgelist(destpath)
    return sorted(graph.degree, key=lambda x: x[1], reverse=True)[:10]


print(ex3())
