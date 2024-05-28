from math import pi, sqrt
from common.r3 import R3
from common.tk_drawer import TkDrawer


class Edge:
    """Ребро полиэдра"""

    # Параметры конструктора: начало и конец ребра (точки в R3)

    def __init__(self, beg, fin):
        self.beg, self.fin = beg, fin


class Facet:
    """Грань полиэдра"""

    # Параметры конструктора: список вершин

    def __init__(self, vertexes):
        self.vertexes = vertexes


class Polyedr:
    """Полиэдр"""

    # Параметры конструктора: файл, задающий полиэдр

    def is_point_good(self, x, y, z):
        return 1 < x * x + y * y + z * z < 4

    def print_sum_of_good_edges(self):
        print(self.sum_of_good_edges)
        return self

    def get_sum_of_good_edges(self):
        return self.sum_of_good_edges

    def __init__(self, file):

        # списки вершин, рёбер и граней полиэдра
        self.vertexes, self.edges, self.facets = [], [], []

        self.sum_of_good_edges = 0

        # список строк файла
        with open(file) as f:
            for i, line in enumerate(f):
                if i == 0:
                    # обрабатываем первую строку; buf - вспомогательный массив
                    buf = line.split()
                    # коэффициент гомотетии
                    c = float(buf.pop(0))
                    # углы Эйлера, определяющие вращение
                    alpha, beta, gamma = (float(x) * pi / 180.0 for x in buf)
                elif i == 1:
                    # во второй строке число вершин, граней и рёбер полиэдра
                    nv, nf, ne = (int(x) for x in line.split())
                elif i < nv + 2:
                    # задание всех вершин полиэдра
                    x, y, z = (float(x) for x in line.split())
                    self.vertexes.append(
                        R3(x, y, z).rz(alpha).ry(beta).rz(gamma) * c
                    )
                else:
                    # вспомогательный массив
                    buf = line.split()
                    # количество вершин очередной грани
                    size = int(buf.pop(0))
                    # массив вершин этой грани
                    vertexes = [self.vertexes[int(n) - 1] for n in buf]
                    # задание рёбер грани
                    for n in range(size):
                        p1, p2 = vertexes[n - 1], vertexes[n]
                        r1 = p1.rz(-gamma).ry(-beta).rz(-alpha) * (1 / c)
                        r2 = p2.rz(-gamma).ry(-beta).rz(-alpha) * (1 / c)
                        # print(p1.x,p2.x,p1.y,p2.y,p1.z,p2.z)
                        # print(p1.x,p1.y,p1.z)
                        # print(p2.x,p2.y,p2.z)
                        if self.is_point_good(
                            (r1.x + r2.x) / 2,
                            (r1.y + r2.y) / 2,
                            (r1.z + r2.z) / 2,
                        ):
                            dx = p1.x - p2.x
                            dy = p1.y - p2.y
                            self.sum_of_good_edges += sqrt(dx * dx + dy * dy)

                        self.edges.append(Edge(p1, p2))
                    # задание самой грани
                    self.facets.append(Facet(vertexes))

    # Метод изображения полиэдра
    def draw(self, tk):
        tk.clean()
        for e in self.edges:
            tk.draw_line(e.beg, e.fin)
        return self
