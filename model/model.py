import networkx as nx
from database.dao import DAO
from model.artist import Artist


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._artists_list = []
        self.load_all_artists()

        self._artists_list = []
        self._artist_min_album = []



    def load_all_artists(self):
        self._artists_list = DAO.get_all_artists()
        print(f"Artisti: {self._artists_list}")

    def load_artists_with_min_albums(self, n_alb):
        self._artist_min_album = DAO.get_artist_min_album(n_alb)
        print(f"Artisti: {self._artist_min_album}")


    def load_edges(self):
        self._lista_connessioni = DAO.get_edges()
        return self._lista_connessioni
        #print(f"Lista connessioni: {self._lista_connessioni}")

    def build_graph(self, n_alb):
        self._nodes = []
        self._edges = []
        self.id_map = {}
        #carico nodi e archi
        self.load_artists_with_min_albums(n_alb)
        self.load_edges()
        for artist in self._artist_min_album:
            self._nodes.append(artist)
            self.id_map[artist.id] = artist
        self._graph.add_nodes_from(self._nodes)

        for id1, id2, peso in self._lista_connessioni:
            if id1 in self.id_map and id2 in self.id_map:
                artista1 = self.id_map[id1]
                artista2 = self.id_map[id2]
                self._graph.add_edge(artista1, artista2, weight = peso)


    def get_num_nodes(self):
        return self._graph.number_of_nodes()
    def get_num_edges(self):
        return self._graph.number_of_edges()


    def getSortedNeighbors(self, a0):
        vicini = self._graph.neighbors(a0)
        viciniTuple = []
        for v in vicini:
            viciniTuple.append((v, self._graph[a0][v]["weight"]))
            viciniTuple.sort(key = lambda x: x[0].id)
        return viciniTuple










