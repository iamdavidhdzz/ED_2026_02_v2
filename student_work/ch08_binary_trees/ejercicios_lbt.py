
from goodrich.ch08.linked_binary_tree import LinkedBinaryTree

def es_completo(T):
    """Retorna True si el LinkedBinaryTree T es completo."""
    if T.is_empty():
        return True

    cola = [T.root()]
    hueco_encontrado = False

    while cola:
        nodo = cola.pop(0)

        # Revisar el hijo izquierdo
        hijo_izq = T.left(nodo)
        if hijo_izq is not None:
            if hueco_encontrado:
                return False
            cola.append(hijo_izq)
        else:
            hueco_encontrado = True

        # Revisar el hijo derecho
        hijo_der = T.right(nodo)
        if hijo_der is not None:
            if hueco_encontrado:
                return False
            cola.append(hijo_der)
        else:
            hueco_encontrado = True

    return True


def camino(T, p, q):
    """Retorna el camino de p a q como string: 'H -> D -> B -> E'."""

    # Función auxiliar para obtener el camino desde la raíz hasta un nodo
    def ancestros_hasta_raiz(nodo):
        camino_nodos = []
        actual = nodo
        while actual is not None:
            camino_nodos.append(actual)
            actual = T.parent(actual)
        return camino_nodos[::-1]  # Invertir para que vaya de la raíz al nodo

    camino_p = ancestros_hasta_raiz(p)
    camino_q = ancestros_hasta_raiz(q)

    # 1. Encontrar el índice del ancestro común más bajo (LCA)
    i = 0
    while i < len(camino_p) and i < len(camino_q) and camino_p[i] == camino_q[i]:
        i += 1
    indice_lca = i - 1

    # 2. Construir el camino final
    # Subir desde 'p' hasta el LCA (incluyendo el LCA)
    p_hasta_lca = camino_p[indice_lca:][::-1]
    # Bajar desde el hijo del LCA hasta 'q'
    lca_hasta_q = camino_q[indice_lca + 1:]

    camino_completo = p_hasta_lca + lca_hasta_q

    # 3. Convertir a string formateado
    return " -> ".join(str(nodo.element()) for nodo in camino_completo)


if __name__ == "__main__":
    # Puedes poner tus pruebas adicionales aquí
    pass
