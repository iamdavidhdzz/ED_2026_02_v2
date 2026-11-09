import math
import matplotlib.pyplot as plt
import networkx as nx

class Heap:
    def __init__(self):
        self.arreglo = [float("-inf")]

    def insert(self, valor, imagen=False):
        self.arreglo.append(valor)
        i = len(self.arreglo) - 1

        while self.arreglo[i] < self.arreglo[i // 2]:
            self.arreglo[i], self.arreglo[i // 2] = (
                self.arreglo[i // 2],
                self.arreglo[i],
            )
            i = i // 2

        if imagen:
            self._mostrar_imagen()

    def remove_smallest(self, imagen=False):
        if len(self.arreglo) <= 1:
            return None

        if len(self.arreglo) == 2:
            val = self.arreglo.pop()
            if imagen:
                self._mostrar_imagen()
            return val

        minimo = self.arreglo[1]
        self.arreglo[1] = self.arreglo.pop()

        i = 1
        n = len(self.arreglo)

        while True:
            hijo_izq = 2 * i
            hijo_der = 2 * i + 1
            menor = i

            if hijo_izq < n and self.arreglo[hijo_izq] < self.arreglo[menor]:
                menor = hijo_izq

            if hijo_der < n and self.arreglo[hijo_der] < self.arreglo[menor]:
                menor = hijo_der

            if menor == i:
                break

            self.arreglo[i], self.arreglo[menor] = (
                self.arreglo[menor],
                self.arreglo[i],
            )
            i = menor

        if imagen:
            self._mostrar_imagen()

        return minimo

    def build_heap(self, lista, imagen=False):
        # 1. Copiar los elementos respetando self.arreglo[0] = -inf
        self.arreglo = [float("-inf")] + list(lista)

        # 2. Algoritmo de Floyd: hundir desde el último nodo interno hasta la raíz (1)
        n = len(self.arreglo)
        for i in range((n - 1) // 2, 0, -1):
            curr = i
            while True:
                hijo_izq = 2 * curr
                hijo_der = 2 * curr + 1
                menor = curr

                if hijo_izq < n and self.arreglo[hijo_izq] < self.arreglo[menor]:
                    menor = hijo_izq

                if hijo_der < n and self.arreglo[hijo_der] < self.arreglo[menor]:
                    menor = hijo_der

                if menor == curr:
                    break

                self.arreglo[curr], self.arreglo[menor] = (
                    self.arreglo[menor],
                    self.arreglo[curr],
                )
                curr = menor

        if imagen:
            self._mostrar_imagen()

    def _mostrar_imagen(self):
        n = len(self.arreglo) - 1
        if n <= 0:
            return

        G = nx.Graph()
        pos = {}

        for i in range(1, n + 1):
            G.add_node(i)
            if i > 1:
                G.add_edge(i // 2, i)

        profundidad_max = math.floor(math.log2(n)) if n > 0 else 0

        for i in range(1, n + 1):
            nivel = math.floor(math.log2(i))
            posicion_en_nivel = i - (2 ** nivel)
            nodos_en_nivel = 2 ** nivel

            ancho_nivel = 2 ** (profundidad_max - nivel + 1)
            x = (posicion_en_nivel + 0.5 - (nodos_en_nivel / 2)) * ancho_nivel
            y = -nivel
            pos[i] = (x, y)

        fig, ax = plt.subplots(figsize=(8, 5))
        labels = {i: str(self.arreglo[i]) for i in range(1, n + 1)}

        nx.draw_networkx_nodes(G, pos, node_color="#ADD8E6", node_size=1200, edgecolors="black", ax=ax)
        nx.draw_networkx_edges(G, pos, width=1.5, edge_color="black", ax=ax)
        nx.draw_networkx_labels(G, pos, labels=labels, font_size=11, font_weight="bold", ax=ax)

        ax.axis("off")
        plt.tight_layout()
        plt.show()
