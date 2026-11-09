import math
import matplotlib.pyplot as plt
import networkx as nx

class Heap:
    def __init__(self):
        """Inicializa el min-heap con float('-inf') en la posición 0."""
        self.arreglo = [float('-inf')]

    def _sift_up(self, i):
        """Reubica el elemento en el índice i hacia arriba en el heap."""
        while i // 2 > 0:
            if self.arreglo[i] < self.arreglo[i // 2]:
                self.arreglo[i], self.arreglo[i // 2] = self.arreglo[i // 2], self.arreglo[i]
            else:
                break
            i = i // 2

    def _min_child(self, i):
        """Retorna el índice del hijo menor del nodo i."""
        if i * 2 + 1 > len(self.arreglo) - 1:
            return i * 2
        else:
            if self.arreglo[i * 2] < self.arreglo[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def _sift_down(self, i):
        """Reubica el elemento en el índice i hacia abajo en el heap."""
        while i * 2 < len(self.arreglo):
            mc = self._min_child(i)
            if self.arreglo[i] > self.arreglo[mc]:
                self.arreglo[i], self.arreglo[mc] = self.arreglo[mc], self.arreglo[i]
            else:
                break
            i = mc

    def insert(self, valor, imagen=False):
        """Inserta un valor en el heap."""
        self.arreglo.append(valor)
        self._sift_up(len(self.arreglo) - 1)
        if imagen:
            self._mostrar_imagen()

    def remove_smallest(self, imagen=False):
        """Elimina y retorna el valor mínimo del heap (la raíz)."""
        if len(self.arreglo) <= 1:
            return None

        val_min = self.arreglo[1]
        self.arreglo[1] = self.arreglo[-1]
        self.arreglo.pop()

        if len(self.arreglo) > 1:
            self._sift_down(1)

        if imagen:
            self._mostrar_imagen()

        return val_min

    def build_heap(self, lista, imagen=False):
        """Construye el heap en O(N) a partir de una lista recibida (Algoritmo de Floyd)."""
        self.arreglo = [float('-inf')] + list(lista)
        i = (len(self.arreglo) - 1) // 2
        while i > 0:
            self._sift_down(i)
            i -= 1
        if imagen:
            self._mostrar_imagen()

    def _mostrar_imagen(self):
        """Genera y dibuja una visualización jerárquica del árbol binario del heap."""
        n = len(self.arreglo) - 1
        if n <= 0:
            print("Heap vacío: No hay imagen para mostrar.")
            return

        G = nx.Graph()
        pos = {}

        # 1. Agregar nodos y aristas para el árbol binario
        for i in range(1, n + 1):
            G.add_node(i, val=self.arreglo[i])
            if i > 1:
                padre = i // 2
                G.add_edge(padre, i)

        # 2. Calcular coordenadas x, y para visualización jerárquica nivel por nivel
        profundidad_max = math.floor(math.log2(n)) if n > 0 else 0

        for i in range(1, n + 1):
            nivel = math.floor(math.log2(i))
            posicion_en_nivel = i - (2 ** nivel)
            nodos_en_nivel = 2 ** nivel

            # Asignación de x centrada simétricamente
            ancho_nivel = 2 ** (profundidad_max - nivel + 1)
            x = (posicion_en_nivel + 0.5 - (nodos_en_nivel / 2)) * ancho_nivel
            y = -nivel
            pos[i] = (x, y)

        # 3. Renderizar con Matplotlib
        fig, ax = plt.subplots(figsize=(8, 5))
        labels = {i: str(self.arreglo[i]) for i in range(1, n + 1)}

        nx.draw_networkx_nodes(G, pos, node_color="#ADD8E6", node_size=1200, edgecolors="black", ax=ax)
        nx.draw_networkx_edges(G, pos, width=1.5, edge_color="gray", ax=ax)
        nx.draw_networkx_labels(G, pos, labels=labels, font_size=11, font_weight="bold", ax=ax)

        ax.set_title("Estado actual del Heap", fontsize=13, fontweight="bold")
        ax.axis("off")
        plt.tight_layout()
        plt.show()
