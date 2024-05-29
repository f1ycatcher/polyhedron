#!/usr/bin/env -S python3 -B

# pashalka

from time import time
from common.tk_drawer import TkDrawer
from shadow.polyedr import Polyedr


tk = TkDrawer()
try:
    for name in [
        "testfigure1",
        "testfigure2",
        "testfigure3",
        "testfigure4",
        "ccc",
        "cube",
        "box",
        "king",
        "cow",
    ]:
        print("=============================================================")
        print(f"Начало работы с полиэдром '{name}'")
        start_time = time()
        Polyedr(f"data/{name}.geom").draw(tk).print_sum_of_good_edges()
        delta_time = time() - start_time
        print(f"Изображение полиэдра '{name}' заняло {delta_time} сек.")
        input("Hit 'Return' to continue -> ")
except (EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
