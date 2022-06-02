from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    figura = []
    aux =""
    for i in range(0, len(self.img)):
      for j in range(0, len(self.img[i])):
        aux = self.img[i][j] + aux
      figura.append(aux)
      aux = ""
    return Picture(figura)

  def horizontalMirror(self):
    figura = []
    for i in range(len(self.img)-1,-1,-1):
      figura.append(self.img[i])
    print(len(figura))
    print(len(self.img))
    return Picture(figura)

  def negative(self):
    figura = []
    aux = ""
    for i in range(0, len(self.img)):
      for j in range(0, len(self.img[i])):
        aux = aux + self._invColor(self.img[i][j])
      figura.append(aux)
      aux = ""
    return Picture(figura)

  def join(self, p):
    figura = []
    for i in range(0,len(self.img)):
      figura.append(self.img[i]+p.img[i])
    return Picture(figura)

  def up(self, p):
    figura = []
    aux = ""
    for i in range(0, len(p.img)):
      for j in range(0, len(p.img[i])):
        if(self.img[i][j] != " "):
          aux = aux + self.img[i][j]
        else:
          aux = aux + p.img[i][j]
      figura.append(aux)
      aux = ""
    return Picture(figura)

  def under(self, p):
    figura = []
    aux = ""
    for i in range(0, len(p.img)):
      for j in range(0, len(p.img[i])):
        if(p.img[i][j] != " "):
          aux = aux + p.img[i][j]
        else:
          aux = aux + self.img[i][j]
      figura.append(aux)
      aux = ""
    return Picture(figura)
  
  def horizontalRepeat(self, n):
    figura = []
    aux = ""
    for i in range(0, len(self.img)):
      for j in range(0, n+1):
        aux = aux + self.img[i]
      figura.append(aux)
      aux = ""
    return Picture(figura)

  def verticalRepeat(self, n):
    figura = []
    for i in range(0, n+1):
      for j in range(0, len(self.img)):
        figura.append(self.img[j])
    return Picture(figura)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)

