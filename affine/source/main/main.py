from tkinter import *

from source.main.constants import HEIGHT
from source.main.constants import MOVE
from source.main.constants import PANEL_WIDTH
from source.main.constants import SCALE
from source.main.constants import TITLE
from source.main.constants import TURN
from source.main.constants import WIDTH
from source.main.model.axis import Axis
from source.main.model.body import Body
from source.main.model.canvas import BaseCanvas
from source.main.model.projection import Projection
from source.main.service.service import draw
from source.main.service.service import mirror
from source.main.service.service import rotate
from source.main.service.service import scale
from source.main.service.service import shift


def main():
    body = Body()

    # Инициализация окна
    root = Tk()
    root.geometry(str(WIDTH + PANEL_WIDTH) + "x" + str(HEIGHT))
    root.title(TITLE)
    root.resizable(width=False, height=False)

    # Генерация полотна
    canvas = BaseCanvas(root)
    kind = IntVar()
    kind.set(Projection.oblique.value)
    draw(kind, body, canvas)

    # Перемещение
    canvas.add_label(root, "Перемещение", 705, 5)

    canvas.add_button("+", lambda: [shift(body, [MOVE, 0, 0, 0]), draw(kind, body, canvas)], 705, 25)
    canvas.add_button("-", lambda: [shift(body, [-MOVE, 0, 0, 0]), draw(kind, body, canvas)], 730, 25)
    canvas.add_label(root, "X", 770, 30)

    canvas.add_button("+", lambda: [shift(body, [0, MOVE, 0, 0]), draw(kind, body, canvas)], 705, 55)
    canvas.add_button("-", lambda: [shift(body, [0, -MOVE, 0, 0]), draw(kind, body, canvas)], 730, 55)
    canvas.add_label(root, "Y", 770, 60)

    canvas.add_button("+", lambda: [shift(body, [0, 0, MOVE, 0]), draw(kind, body, canvas)], 705, 85)
    canvas.add_button("-", lambda: [shift(body, [0, 0, -MOVE, 0]), draw(kind, body, canvas)], 730, 85)
    canvas.add_label(root, "Z", 770, 90)

    # Поворот
    canvas.add_label(root, "Поворот", 705, 115)

    canvas.add_button("+", lambda: [rotate(body, [TURN, 0., 0., 0.], Axis.x), draw(kind, body, canvas)], 705, 135)
    canvas.add_button("-", lambda: [rotate(body, [-TURN, 0., 0., 0.], Axis.x), draw(kind, body, canvas)], 730, 135)
    canvas.add_label(root, "X", 770, 140)

    canvas.add_button("+", lambda: [rotate(body, [0., TURN, 0., 0.], Axis.y), draw(kind, body, canvas)], 705, 165)
    canvas.add_button("-", lambda: [rotate(body, [0., -TURN, 0., 0.], Axis.y), draw(kind, body, canvas)], 730, 165)
    canvas.add_label(root, "Y", 770, 170)

    canvas.add_button("+", lambda: [rotate(body, [0., 0., TURN, 0.], Axis.z), draw(kind, body, canvas)], 705, 195)
    canvas.add_button("-", lambda: [rotate(body, [0., 0., -TURN, 0.], Axis.z), draw(kind, body, canvas)], 730, 195)
    canvas.add_label(root, "Z", 770, 200)

    # Масштабирование
    canvas.add_label(root, "Масштабирование", 705, 225)
    canvas.add_button("+", lambda: [scale(body, [SCALE, SCALE, SCALE, 0]), draw(kind, body, canvas)], 705, 245)
    canvas.add_button("-", lambda: [scale(body, [-SCALE, -SCALE, -SCALE, 0]), draw(kind, body, canvas)], 730, 245)

    # Отражение
    canvas.add_label(root, "Отражение", 705, 280)
    canvas.add_button("Относительно X", lambda: [mirror(body, Axis.x), draw(kind, body, canvas)], 705, 300)
    canvas.add_button("Относительно Y", lambda: [mirror(body, Axis.y), draw(kind, body, canvas)], 705, 330)
    canvas.add_button("Относительно Z", lambda: [mirror(body, Axis.z), draw(kind, body, canvas)], 705, 360)

    # Проецирование
    canvas.add_radio_buttons("Косоугольное", kind, Projection.oblique.value, 705, 400)
    canvas.add_radio_buttons("Перспективное", kind, Projection.perspective.value, 705, 430)
    canvas.add_button("Проецирование", lambda: draw(kind, body, canvas), 705, 470)

    root.mainloop()


if __name__ == "__main__":
    main()
