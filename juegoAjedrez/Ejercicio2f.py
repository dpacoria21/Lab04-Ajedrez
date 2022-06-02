from interpreter import draw
from chessPictures import *
base1 = square.join(square.negative()).horizontalRepeat(3)
base2 = square.negative().join(square).horizontalRepeat(3)
baseT = Picture(base1.img + base2.img)
draw(baseT.verticalRepeat(1))