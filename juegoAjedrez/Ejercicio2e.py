from interpreter import draw
from chessPictures import *

base = square.negative().join(square).horizontalRepeat(3)
draw(base)