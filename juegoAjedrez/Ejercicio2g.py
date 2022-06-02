from interpreter import draw
from chessPictures import *

mitad1 = square.under(rock.negative()).join(square.negative().under(knight.negative()).join(square.under(bishop.negative())).join(square.negative().under(queen.negative())))
mitad2 = square.under(king.negative()).join(square.negative().under(bishop.negative())).join(square.under(knight.negative())).join(square.negative().under(rock.negative()))

lineaP = mitad1.join(mitad2) #Primera linea del ajedrez
peones = square.negative().under(pawn.negative()).join(square.under(pawn.negative())).horizontalRepeat(3) #Linea de peones

base = square.join(square.negative()).horizontalRepeat(3)
aux = Picture(base.img + base.negative().img)
espacios = aux.verticalRepeat(1) #espacios de square entre cada equipo

tablero = Picture(lineaP.img + peones.img + espacios.img + peones.negative().img + lineaP.negative().img) # tablero
draw(tablero)