import pandas as pd
import matplotlib as mpl
import networkx as nx
import matplotlib.pyplot as plt
from pythondb import DataBase
from operator import itemgetter
from networkx.algorithms import community

class Analyze():
    def __init__(self):
        pass

    def email_network(self):
        email_fromto_list = DataBase().select_email_fromto()
        email_from_list = []
        email_to_list = []
        email_edge_list = []
        for email_fromto in email_fromto_list:
            email_from_list.append(email_fromto[0])
            email_to_list.append(email_fromto[1])
            email_edge = (email_fromto[0], email_fromto[1])
            email_edge_list.append(email_edge)

        MG = nx.MultiGraph()
        MG.add_nodes_from(email_from_list)
        MG.add_nodes_from(email_to_list)
        MG.add_edges_from(email_edge_list)

        nx.draw(MG, with_labels = True, node_size = 1400, font_size = 14, edge_color = "grey")
        plt.show()

        # sort the degrees for nodes
        temp_list = []
        node_degree_list = []
        temp_list = nx.degree(MG)
        for node in temp_list:
            node = (node[1], node[0])
            node_degree_list.append(node)

        sorted_degree_list = sorted(node_degree_list, reverse = True)
        print(sorted_degree_list)
        DataBase().create_emaildegree_table()
        for degree_info in sorted_degree_list:
            email_degree = degree_info[0]
            email_name = degree_info[1]
            DataBase().insert_emaildegree(email_degree, email_name)

    def email_site_search(self):
        email_doubtman = "Isia.Vann"
        email_doubtman_list = DataBase().select_email_doubtman(email_doubtman)
        for email in email_doubtman_list:
            print(email)

    def article_site_search(self):
        article_keyword = "Vann"
        article_keyword_list = DataBase().select_article_keyword(article_keyword)
        for article in article_keyword_list:
            print(article[0])