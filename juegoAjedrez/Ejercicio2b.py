from interpreter import draw
from chessPictures import *
part1 = knight.join(knight.negative())
part2 = knight.negative().verticalMirror().join(knight.verticalMirror())
res = Picture(part1.img + part2.img)
draw(res)