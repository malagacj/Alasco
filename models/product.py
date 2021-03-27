'''Generic Models for Products'''
from models.color import Color

class PaperProduct:
    product_id: int
    name: str
    main_color: Color

    def __init__(self, id, name, main_color):
        self.id = id
        self.name = name
        self.main_color = main_color

    def get_dict(self):
        return {'product_id': self.id,
                'name': self.name,
                'main_color': self.main_color.hexvalue
                }

    def matches_color(self, elements, hexcheck=False):
        if hexcheck:
            return self.main_color.hexvalue in elements
        else:
            return self.main_color.rgb() in elements
