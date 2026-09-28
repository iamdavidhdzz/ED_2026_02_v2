class Heap:

    def __init__(self):
        self.arreglo = [float("-inf")]

    def insert(self, valor):
        self.arreglo.append(valor)
        i = len(self.arreglo) - 1

        while self.arreglo[i] < self.arreglo[i // 2]:
            self.arreglo[i], self.arreglo[i // 2] = (
                self.arreglo[i // 2],
                self.arreglo[i],
            )
            i = i // 2

    def remove_smallest(self):
        if len(self.arreglo) <= 1:
            return None

        if len(self.arreglo) == 2:
            return self.arreglo.pop()

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

        return minimo

    def build_heap(self, lista):
        pass
