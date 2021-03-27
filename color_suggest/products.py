"""
This is just an example implementation. You are free to use, change or delete it :-)
"""

class Color:
    red: int
    green: int
    blue: int

    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue


class PaperProduct:
    product_id: int
    name: str
    main_color: Color

    def __init__(self, id, name, main_color):
        self.id = id
        self.name = name
        self.main_color = main_color


PRODUCTS = (
    PaperProduct(1, "Green paper", Color(65, 154, 7)),
    PaperProduct(2, "Cobalt blue sheet", Color(5, 72, 166)),
    PaperProduct(5, "Regular white paper", Color(255, 255, 255)),
    PaperProduct(9, "Black A0 sheet", Color(0, 0, 0)),
    PaperProduct(100, "Red paper", Color(253, 28, 20)),
    PaperProduct(772, "Sangria red A4", Color(148, 5, 5)),
    PaperProduct(223, "Eden Blue A3", Color(13, 77, 77)),
)
