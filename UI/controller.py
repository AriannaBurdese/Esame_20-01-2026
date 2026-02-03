import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_create_graph(self, e):
        try:
            n_alb = int(self._view.txtNumAlbumMin.value)
        except:
            self._view.show_alert("Inserire un valore valido")
            return

        self._model.build_graph(n_alb)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Numero nodi: {self._model.get_num_nodes()}, numero archi: {self._model.get_num_edges()}"))
        self.populate_dd()
        self._view.update_page()
    def populate_dd(self):
        self._view.ddArtist.clean()
        for artist in self._model._artist_min_album:
            self._view.ddArtist.options.append(ft.dropdown.Option(text = artist.name, key = artist.id))
        self._view.btnArtistsConnected.disabled = False
        self._view.ddArtist.disabled = False
        self._view.update_page()

    def handle_connected_artists(self, e):
        idArtista = int(self._view.ddArtist.value)
        artista = self._model.id_map[idArtista]
        print("Artista selezionato:", artista)

        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Artisti direttamente collegati all'artista: {artista}"))
        viciniTuple = self._model.getSortedNeighbors(artista)
        for v in viciniTuple:
            self._view.txt_result.controls.append(ft.Text(f"{v[0]} - Numero di generi in comune: {v[1]}"))
        self._view.update_page()



