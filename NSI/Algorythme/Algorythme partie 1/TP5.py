"""
from PIL import Image,ImageDraw,ImageFont
img=Image.new('RGB',(256,256),(0,0,0))



largeur,hauteur=img.size
draw=ImageDraw.Draw(img)
draw.line((0,0,largeur,hauteur),fill=(0,255,0))

draw.line((10,20,100,200),fill=(255,0,0))
img.show()


from PIL import Image,ImageDraw,ImageFont
img=Image.new('RGB',(256,256),(0,0,0))
largeur,hauteur=img.size
draw=ImageDraw.Draw(img)

def traceDroite(nbDroites,ecart):

draw.line
traceDroite(10,20)

img.show()

from PIL import Image,ImageDraw,ImageFont

img=Image.new('RGB',(256,256),(0,0,0))
largeur,hauteur=img.size
draw=ImageDraw.Draw(img)

def cercle(x,y,rayon,couleur):
    draw.ellipse((x-rayon,y-rayon,x+rayon, y+rayon),fill=couleur)

def tracecible():


tracecible()
img.show()



from PIL import Image,ImageDraw,ImageFont

img=Image.new('RGB',(256,256),(255,255,255))
largeur,hauteur=img.size
draw=ImageDraw.Draw(img)

def rectangle(x,y,largeur,hauteur,couleur):
    draw.rectangle((x,y,x+largeur, y+hauteur),fill=couleur)

def traceEffetVisuel():




traceEffetVisuel()
img.show()
img.save("effet.png")



from PIL import Image,ImageDraw,ImageFont

img=Image.new('RGB',(256,256),(0,0,0))
largeur,hauteur=img.size
for y in range(hauteur):
    for x in range(largeur):
         img.putpixel((x,y),(255-y,0,0))
img.show()
img.save("degrade_rouge.jpg")


from PIL import Image,ImageDraw,ImageFont

img=Image.new('RGB',(256,256),(0,0,0))
largeur,hauteur=img.size
for y in range(hauteur):
    for x in range(largeur):
         img.putpixel((x,y),(0,255-x,0))
img.show()
img.save("degrade_vert.jpg")


from PIL import Image,ImageDraw,ImageFont

img=Image.new('RGB',(256,256),(0,0,0))
largeur,hauteur=img.size
for y in range(0,255,0):
    for x in range(255,0,255,width):
        if y < (x*3)/4 :
            greyScale_pixel (x,y)
img.show()
img.save("degrade_bicolor.jpg")

#ex 2 graphisme

from PIL import Image,ImageDraw,ImageFont

img=Image.new('RGB',(256,256),(255,0,255))
largeur,hauteur=img.size
draw=ImageDraw.Draw(img)

def cercle(x,y,rayon,couleur):
    draw.ellipse((x-rayon,y-rayon,x+rayon, y+rayon),fill=couleur)

def tracecible(circle):
    img.show(circle)
    tracecible(10,20)
img.show(tracecible)

"""
