from goodrich.ch14.graph import Graph


def vecinos(g, v):
    """Retorna una lista con los elementos de los vecinos de v."""
    lista_vecinos = []
    for e in g.incident_edges(v):
        w = e.opposite(v)
        lista_vecinos.append(w.element())
    return lista_vecinos


def dfs(g, v, d):
    """DFS desde v. Agrega a d cada vertice descubierto -> arista que lo descubrio.
    v ya debe estar en d antes de la llamada (normalmente d = {v: None}). No retorna nada.
    """
    for e in g.incident_edges(v):
        w = e.opposite(v)
        if w not in d:
            d[w] = e
            dfs(g, w, d)


def bfs(g, v):
    """BFS desde v. Retorna un dict vertice descubierto -> arista que lo descubrio (v -> None)."""
    d = {v: None}

    nivel_actual = [v]

    while len(nivel_actual) > 0:
        siguiente_nivel = []

        for u in nivel_actual:
            for e in g.incident_edges(u):
                w = e.opposite(u)
                if w not in d:
                    d[w] = e
                    siguiente_nivel.append(w)

        nivel_actual = siguiente_nivel

    return d


def alcanzables(g, v):
    """Retorna una lista con los elementos de los vertices alcanzables desde v (incluido v)."""
    diccionario_alcanzables = bfs(g, v)

    elementos = []
    for nodo in diccionario_alcanzables.keys():
        elementos.append(nodo.element())

    return elementos


if __name__ == "__main__":
    pass
