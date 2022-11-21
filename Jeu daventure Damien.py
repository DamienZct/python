#Programme réalisé par Zuchetto, Damien, 1G3
import pygame

pygame.init()
fenetre = pygame.display.set_mode((1000,650))
pygame.display.set_caption("jeu d'aventure")
font = pygame.font.SysFont ("Impact", 30)
image1=pygame.image.load("vestiaire france.jpg")   #Tu dois remplir avec les noms des images et leurs types (PNG/JPG/JPEG)(entre les guillemets)
image2=pygame.image.load("vestiaire england.jpg")    #Il faut donc que tu trouves des images de taille : 1000 * 650 pixels
image3=pygame.image.load("vestiaire qatar.jpg")
image4=pygame.image.load("vestiaire portugal.jpg")
image5=pygame.image.load("vestiaire argentine.jpg")    #Plan (chaque numéro correspond à une salle) :
image6=pygame.image.load("vestiaire paysbas.jpg")    # 3|6|9         Nord
image7=pygame.image.load("vestiaire bresil.jpg")    # 2|5|8      Ouest Est       Salle 9 : salle secrète donc il faut la clé
image8=pygame.image.load("vestiaire espagne.jpg")    # 1|4|7         Sud          Salle 5: salle ou on obtient la clé
image9=pygame.image.load("Salle trophee.jpg")

text1 = font.render("Equipe de France", True, (0, 0, 0)) # Tu dois remplir avec le nom de la salle (celui qui s'affichera)(entre les guillemets)
text2 = font.render("Equipe d'angleterre", True, (0, 0, 0))
text3 = font.render("Equipe du Qatar", True, (0, 0, 0))
text4 = font.render("Equipe du Portugal", True, (0, 0, 0))
text5 = font.render("Equipe de l'Argentine", True, (0, 0, 0))
text6 = font.render("Equipe des Pays Bas", True, (0, 0, 0))
text7 = font.render("Equipe du Bresil", True, (0, 0, 0))
text8 = font.render("Equipe de l'Espagne", True, (0, 0, 0))
text9 = font.render("Salle du trophée", True, (0, 0, 0))

def secret(cleff,piece):
    if piece==5:
        cleff=1
        print("")
    return cleff

def descriptionpiece(piece,cleff):
    if piece==1:
        fenetre.blit(image1,(0,0))
        fenetre.blit(text1,(25,600))
    elif piece==2:
        fenetre.blit(image2,(0,0))
        fenetre.blit(text2,(25,600))
    elif piece==3:
        fenetre.blit(image3,(0,0))
        fenetre.blit(text3,(25,600))
    elif piece==4:
        fenetre.blit(image4,(0,0))
        fenetre.blit(text4,(25,600))
    elif piece==5:
        fenetre.blit(image5,(0,0))
        fenetre.blit(text5,(25,600))
    elif piece==6:
        fenetre.blit(image6,(0,0))
        fenetre.blit(text6,(25,600))
    elif piece==7:
        fenetre.blit(image7,(0,0))
        fenetre.blit(text7,(25,600))
    elif piece==8:
        fenetre.blit(image8,(0,0))
        fenetre.blit(text8,(25,600))
    elif piece==9:
        fenetre.blit(image9,(0,0))
        fenetre.blit(text9,(25,600))


def decision(direction,piece,cleff):
    print("Vous désirez allez au",direction)
    memopiece=piece
    if direction=='n':
        if piece==1:
            piece=2
        elif piece==2:
            piece=3
        elif piece==4:
            piece=5
        elif piece==5:
            piece=6
        elif piece==7:
            piece=8
        elif piece==8:
            if cleff==1:
                print("")
                piece=9
    elif direction=='s':
        if piece==2:
            piece=1
        elif piece==3:
            piece=2
        elif piece==5:
            piece=4
        elif piece==6:
            piece=5
        elif piece==8:
            piece=7
        elif piece==9:
            piece=8
    elif direction=='e':
        if piece==1:
            piece=4
        elif piece==4:
            piece=7
        elif piece==2:
            piece=5
        elif piece==3:
            piece=6
        elif piece==6:
            if cleff==1:
                print("")
                piece=9
        elif piece==5:
            piece=8
    elif direction=='o':
        if piece==4:
            piece=1
        elif piece==7:
            piece=4
        elif piece==8:
            piece=5
        elif piece==5:
            piece=2
        elif piece==6:
            piece=3
        elif piece==9:
            piece=6
    elif memopiece==piece:
        print("Déplacement impossible")
    return piece

pieceactuelle=4
clef=0
loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        elif event.type == pygame.KEYDOWN:
            pieceactuelle=decision(event.unicode,pieceactuelle,clef)
            clef=secret(clef,pieceactuelle)
            if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                loop = False
    descriptionpiece(pieceactuelle,clef)
    pygame.display.flip()
pygame.quit()
