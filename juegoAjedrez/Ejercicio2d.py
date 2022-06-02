from interpreter import draw
from chessPictures import *

base = square.join(square.negative()).horizontalRepeat(3)
draw(base)