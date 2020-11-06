import os
from PIL import Image, ImageDraw, ImageFont

table = [
  (2010,1,51991),
  (2010,2,46584),
  (2010,3,48418),
  (2010,4,44635),
  (2010,5,44758),
  (2010,6,42574),
  (2010,7,43655),
  (2010,8,42502),
  (2010,9,42644),
  (2010,10,46972),
  (2010,11,45102),
  (2010,12,51383),
  (2011,1,52983),
  (2011,2,46180),
  (2011,3,47755),
  (2011,4,43935),
  (2011,5,44174),
  (2011,6,42300),
  (2011,7,42700),
  (2011,8,42720),
  (2011,9,42083),
  (2011,10,45816),
  (2011,11,45036),
  (2011,12,49375),
  (2012,1,52272),
  (2012,2,54462),
  (2012,3,53754),
  (2012,4,46684),
  (2012,5,45843),
  (2012,6,42624),
  (2012,7,43905),
  (2012,8,43134),
  (2012,9,42176),
  (2012,10,47086),
  (2012,11,46638),
  (2012,12,51290),
  (2013,1,56073),
  (2013,2,51433),
  (2013,3,54122),
  (2013,4,46892),
  (2013,5,45293),
  (2013,6,43147),
  (2013,7,45164),
  (2013,8,42596),
  (2013,9,42902),
  (2013,10,46016),
  (2013,11,45286),
  (2013,12,50312),
  (2014,1,51104),
  (2014,2,46643),
  (2014,3,49311),
  (2014,4,45476),
  (2014,5,45462),
  (2014,6,43229),
  (2014,7,44612),
  (2014,8,44160),
  (2014,9,43557),
  (2014,10,46462),
  (2014,11,46941),
  (2014,12,52336),
  (2015,1,58446),
  (2015,2,57375),
  (2015,3,54948),
  (2015,4,47688),
  (2015,5,46231),
  (2015,6,44636),
  (2015,7,46487),
  (2015,8,45784),
  (2015,9,44660),
  (2015,10,50100),
  (2015,11,46604),
  (2015,12,50721),
  (2016,1,54096),
  (2016,2,49454),
  (2016,3,54155),
  (2016,4,48724),
  (2016,5,48042),
  (2016,6,44483),
  (2016,7,46812),
  (2016,8,45804),
  (2016,9,44833),
  (2016,10,50350),
  (2016,11,49773),
  (2016,12,57339),
  (2017,1,68145),
  (2017,2,52538),
  (2017,3,50251),
  (2017,4,47025),
  (2017,5,48389),
  (2017,6,44393),
  (2017,7,46349),
  (2017,8,46640),
  (2017,9,46144),
  (2017,10,49452),
  (2017,11,50011),
  (2017,12,56937),
]


# Ecrire nb_deces( table, an, mois) qui rend le nombre de deces cet an et ce mois, ou -1 si l information n est pas dans la table
def nb_deces(table,an,mois):
  deathThisYear = 0
  deathThisMonth = 0
  for x in range(len(table)):
    currentEl = table[x] 
    currentYear = currentEl[0]
    currentMonth = currentEl[1]
    currentDeath = currentEl[2]
    if currentYear == an : 
      deathThisYear += currentDeath
      if currentMonth == mois :
        deathThisMonth = currentDeath
  return [deathThisYear,deathThisMonth]

def compter(table,mois1,mois2):
    dictionnaire={2010:0,2011:0,2012:0,2013:0,2014:0,2015:0,2016:0,2017:0}
    for x in range(len(table)):
      currentEl = table[x] 
      currentYear = currentEl[0]
      currentMonth = currentEl[1]
      currentDeath = currentEl[2]
      if currentMonth>=mois1 and currentMonth<=mois2:
        dictionnaire[currentYear]+=currentDeath
    return dictionnaire


def texte( c, x, y, chaine, couleur):
  font=ImageFont.truetype( "/usr/share/fonts/truetype/msttcorefonts/arial.ttf", 15)
  # remplacer par le «bon fichier»...
  c.text( (x, y), chaine, fill=couleur, font=font)
  #pour tracer une arête:
def edge( c, x1, y1, x2, y2, couleur, epaisseur):
  c.line( ( x1, y1, x2, y2), fill=couleur, width=epaisseur)

def draw():

  width=850
  #pour créer un canevas
  # width par width:
  img=Image.new("RGB", (width,width), (255,255,255))
  c = ImageDraw.Draw(img) 
  edge(c)
  # c pour canvas
  # après avoir tracé dans le canevas:
  img.show() 
  #pour afficher l'image
  img.save("dessin.png") 
  #pour la sauver au format png
  img.save("dessin.pdf") 
  #pour la sauver au format pdf
  img.save("dessin.ps") 
  #pour la sauver au format postscript
#pour tracer un texte en x, y. c est le «canevas»:



print(nb_deces(table,2017,12))
print(compter(table,11,12))