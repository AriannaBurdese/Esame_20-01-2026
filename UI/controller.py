import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_create_graph(self, e):
        n_lab = int(self._view.txtNumAlbumMin.value)
        if n_lab < 1 or n_lab == str:
            self._view.show_alert("ERRORE: INSERIRE VALORE NUMERICO POSITIVO")
        self._model.build_graph()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(
            f"Numero di nodi: {self._model.get_num_of_nodes()} Numero di archi: {self._model.get_num_of_edges()}"))
        self._view.page.update()


    def handle_connected_artists(self, e):
        pass


