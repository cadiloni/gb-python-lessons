class Stationery:
    title: str

    def draw(self):
        print("Drawing starts")


class Pen(Stationery):
    title = "Pen"

    def draw(self):
        print(f"{self.title} writes")


class Pencil(Stationery):
    title = "Pencil"

    def draw(self):
        print(f"{self.title} draws")


class Handle(Stationery):
    title = "Highlighter"

    def draw(self):
        print(f"{self.title} highlights")


if __name__ == '__main__':
    stationery = Stationery()
    stationery.draw()

    pen = Pen()
    pen.draw()

    pencil = Pencil()
    pencil.draw()

    handle = Handle()
    handle.draw()
