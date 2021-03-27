'''Generic Models for Color'''

def hex_to_rgb(col):
    '''Generic function to calculate RGB value from Hex'''
    return tuple(int(col[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(col):
    '''Generic function to calculate HEX value from RGB'''
    hexcol = [str(hex(pcol)[2:]).zfill(2) for pcol in col]
    return ''.join(hexcol)

class Color:
    '''Generic color class for any color'''
    red: int
    green: int
    blue: int

    def __init__(self, red=0, green=0, blue=0, hexvalue=None):
        if hexvalue:
            self.hexvalue = hexvalue.upper()
            self.red, self.green, self.blue = hex_to_rgb(hexvalue)
        else:
            self.red = red
            self.green = green
            self.blue = blue
            self.hexvalue = rgb_to_hex((red, green, blue)).upper()

    def rgb(self):
        return (self.red, self.green, self.blue)
