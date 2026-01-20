import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._nodes = []
        self._edges = []
        self.id_map = {}
        self._artists_list = []
        self._lista_connessione = []
        self._list_artists_min_albums = []
        self.load_all_artists()
        self.load_connessione()

    def load_all_artists(self):
        self._artists_list = DAO.get_all_artists()
        print(f"Artisti: {self._artists_list}")

    def load_connessione(self):
        self._lista_connessione = DAO.get_connessione()
        return self._lista_connessione

    def load_artists_with_min_albums(self, min_albums):
        self._list_artists_min_albums = DAO.get_all_artists_min_albums()
        return self._list_artists_min_albums

    def build_graph(self, min_albums):
        self._graph.clear()
        self._nodes = []
        self._edges = []
        self.id_map = {}
        self.load_artists_with_min_albums(min_albums)
        #mi riempio i nodi
        for artist in self._list_artists_min_albums:
            self._nodes.append(artist)
            self.id_map[artist.id] = artist
        self._graph.add_nodes_from(self._nodes)

        for artista1, artista2,peso in self._lista_connessione:
            if artista1 in self.id_map and artista2 in self.id_map:
                a1 = self.id_map[artista1]
                a2 = self.id_map[artista2]
                if peso>0:
                    self._graph.add_edge(a1, a2, weight=peso)

    def get_num_of_nodes(self):
        return self._graph.number_of_nodes()
    def get_num_of_edges(self):
        return self._graph.number_of_edges()


