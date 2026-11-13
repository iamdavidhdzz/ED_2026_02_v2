import math


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
        # Solo matplotlib (import perezoso): no depende de networkx
        import matplotlib.pyplot as plt

        n = len(self.arreglo) - 1
        if n <= 0:
            return

        profundidad_max = math.floor(math.log2(n))
        pos = {}
        for i in range(1, n + 1):
            nivel = math.floor(math.log2(i))
            posicion_en_nivel = i - (2 ** nivel)
            nodos_en_nivel = 2 ** nivel
            ancho_nivel = 2 ** (profundidad_max - nivel + 1)
            x = (posicion_en_nivel + 0.5 - (nodos_en_nivel / 2)) * ancho_nivel
            pos[i] = (x, -nivel)

        fig, ax = plt.subplots(figsize=(8, 5))

        # Aristas (padre -> hijo)
        for i in range(2, n + 1):
            x0, y0 = pos[i // 2]
            x1, y1 = pos[i]
            ax.plot([x0, x1], [y0, y1], color="black", linewidth=1.5, zorder=1)

        # Nodos con su valor
        for i in range(1, n + 1):
            x, y = pos[i]
            ax.scatter([x], [y], s=1200, c="#ADD8E6", edgecolors="black", zorder=2)
            ax.text(x, y, str(self.arreglo[i]), ha="center", va="center",
                    fontsize=11, fontweight="bold", zorder=3)

        ax.margins(0.1)
        ax.axis("off")
        plt.tight_layout()
        plt.show()
        plt.close(fig)
