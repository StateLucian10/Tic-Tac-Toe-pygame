import functii
import button
import pygame
from pygame.draw import rect


pygame.init()

#Screen
SCREEN_WIDTH = 1050
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Culoarea de fundal si titlu si fontul textului
color = (67, 219, 128)
pygame.display.set_caption('X si 0')
Icon = pygame.image.load('imagini/xsi0.png')
pygame.display.set_icon(Icon)
font = pygame.font.SysFont("Comic Sans MS", 52)

#incarcare imagini
X_img = pygame.image.load("imagini/X_buton.png").convert_alpha()
zero_img = pygame.image.load("imagini/0_buton.png").convert_alpha()
xz_img = pygame.image.load("imagini/xsi0.png").convert_alpha()
x_tabla = pygame.image.load("imagini/x_tabla.png").convert_alpha()
zero_tabla = pygame.image.load("imagini/zero_tabla.png").convert_alpha()
tabla = pygame.image.load("imagini/tabla.png").convert_alpha()
casuta_img = pygame.image.load("imagini/casuta.png").convert_alpha()
resume_img = pygame.image.load("imagini/resume.png").convert_alpha()
menu_img = pygame.image.load("imagini/menu.png").convert_alpha()
quit_img = pygame.image.load("imagini/quit.png").convert_alpha()
restart_img = pygame.image.load("imagini/restart.png").convert_alpha()
math_img = pygame.image.load("imagini/math.png").convert_alpha()
skill_img = pygame.image.load("imagini/skill.png").convert_alpha()
usor_img = pygame.image.load("imagini/usor.png").convert_alpha()
mediu_img = pygame.image.load("imagini/mediu.png").convert_alpha()
imposibil_img = pygame.image.load("imagini/imposibil.png").convert_alpha()
up_img = pygame.image.load("imagini/up.png").convert_alpha()
down_img = pygame.image.load("imagini/down.png").convert_alpha()
iarba_img = pygame.image.load("imagini/iarba.png").convert_alpha()
frunze_img = pygame.image.load("imagini/frunze.png").convert_alpha()
foc_img = pygame.image.load("imagini/foc.png").convert_alpha()
copac_img = pygame.image.load("imagini/copac.png").convert_alpha()
copac_toamna_img = pygame.image.load("imagini/copac_toamna.png").convert_alpha()
copac_mort_img = pygame.image.load("imagini/copac_mort.png").convert_alpha()

#butoane
X_buton= button.Button(330, 155, X_img, 1)
zero_buton= button.Button(330, 260, zero_img, 1)
resume_button = button.Button(380, 125, resume_img, 1)
menu_button = button.Button(850, 20, menu_img, 1)
quit_button = button.Button(380, 355, quit_img, 1)
restart_button = button.Button(380, 235, restart_img, 1)
up_button = button.Button(250, 375, up_img, 1)
down_button = button.Button(330, 375, down_img, 1)

#functie pentru crearea casutelor pentru a putea interactiona cu ele
def creare_casute():
    casuta = []
    x = 385
    y = 180
    for i in range(9):
        casuta.append(casuta_img.get_rect())
        if i!=0:
            if i%3 == 0:
                x -= 435
                y += 140
            x += 145
        casuta[i].center = (x, y)

    return casuta

casuta = creare_casute()
terminat = False 

#functie pentru afisare text
def afisare_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

#functie pentru afisare imagine
def afisare_imagine(imagine, centru):
    screen.blit(imagine, centru)

dificultate = 1
running = True
selectare_pion = True
pauza = False

#Joc
while running:
     
    if dificultate == 1:
        screen.fill(color)
        afisare_imagine(iarba_img, (0, 125))
        afisare_imagine(copac_img, (690, 0))
    elif dificultate == 2:
        screen.fill((255,165,0))
        afisare_imagine(frunze_img, (0, 250))
        afisare_imagine(copac_toamna_img, (690, 0))
    elif dificultate == 3:
        screen.fill((255, 0, 0))
        afisare_imagine(foc_img, (0, 225))
        afisare_imagine(copac_mort_img, (690, -25))

    if selectare_pion :
        afisare_text("Alege cu ce vrei sa joci :", font, (255, 255, 255), 255, 70) #Text afisat in zona de alegere a pionului
        afisare_imagine(xz_img, (5, 10))
        afisare_imagine(math_img, (920, 470))

        if X_buton.draw(screen):
            functii.pion = 'X'
            selectare_pion = False
            
        elif zero_buton.draw(screen):
            functii.pion = 'O'
            selectare_pion = False

        if up_button.draw(screen):
            if dificultate <3:
                dificultate += 1
        elif down_button.draw(screen):
            if dificultate >1:
                dificultate -=1     

        if dificultate == 1:
            afisare_imagine(usor_img, (420, 375))
        elif dificultate == 2:
            afisare_imagine(mediu_img, (420, 375))
        elif dificultate == 3:
            afisare_imagine(imposibil_img, (420, 375))

    
    elif pauza == True:
        if resume_button.draw(screen):  #se revine la joc
            pauza = False

        if restart_button.draw(screen):  #se revine la joc
            pauza = False
            functii.restart()
            dificultate = 1
            terminat = False
            selectare_pion = True
            

        if quit_button.draw(screen): #se iese din joc
            running = False

        
    else:
        afisare_imagine(skill_img, (5, 20))
        afisare_imagine(tabla, (270, 80))
        for cas in casuta:
            screen.blit(casuta_img, cas)

        if menu_button.draw(screen): #daca se apasa butonul menu
            pauza = True

        if functii.castig(functii.joc) == 0 and len(functii.lista_mutari(functii.joc)) >= 1:
            for i in range(9):
                if functii.joc[i] == 'X':
                    afisare_imagine(x_tabla, casuta[i])
                elif functii.joc[i] == 'O':
                    afisare_imagine(zero_tabla, casuta[i])
                else:
                    pass


        elif functii.castig(functii.joc) == 1:
            for i in range(9):
                if functii.joc[i] == 'X':
                    afisare_imagine(x_tabla, casuta[i])
                elif functii.joc[i] == 'O':
                    afisare_imagine(zero_tabla, casuta[i])
                else:
                    pass
            afisare_text("X a câștigat!", font, (255, 255, 255), 400, 20)
            terminat = True
        
        elif functii.castig(functii.joc) == -1:
            for i in range(9):
                if functii.joc[i] == 'X':
                    afisare_imagine(x_tabla, casuta[i])
                elif functii.joc[i] == 'O':
                    afisare_imagine(zero_tabla, casuta[i])
                else:
                    pass
            afisare_text("0 a câștigat!", font, (255, 255, 255), 400, 20)
            terminat = True

        else:
            for i in range(9):
                if functii.joc[i] == 'X':
                    afisare_imagine(x_tabla, casuta[i])
                elif functii.joc[i] == 'O':
                    afisare_imagine(zero_tabla, casuta[i])
                else:
                    pass
            afisare_text("Egal!", font, (255, 255, 255), 480, 20)
            terminat = True
            
        

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False      

        if selectare_pion == False and terminat == False and pauza == False:
            jucator = functii.alegere_jucator(functii.joc)
            
            if jucator == functii.pion:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for i in range(9):
                            if casuta[i].collidepoint(event.pos) and i in functii.lista_mutari(functii.joc):
                                functii.joc = functii.joaca_mutare(functii.joc, i)
                                break
                        
            else:
                if functii.pion == 'O':
                    mutare = -1
                    if dificultate == 1:
                        _, mutare = functii.valMax(functii.joc, -2, 2, adancime = 1)
                    elif dificultate == 2:
                        _, mutare = functii.valMax(functii.joc, -2, 2, adancime = 2)
                    elif dificultate == 3:
                        _, mutare = functii.valMax(functii.joc, -2, 2, adancime = 100)
                    functii.joc = functii.joaca_mutare(functii.joc, mutare)
                else:
                    mutare = -1
                    if dificultate == 1:
                        _, mutare = functii.valMax(functii.joc, -2, 2, adancime = 1)
                    elif dificultate == 2:
                        _, mutare = functii.valMin(functii.joc, -2, 2, adancime = 2)
                    elif dificultate == 3:
                        _, mutare = functii.valMin(functii.joc, -2, 2, adancime = 100)
                    functii.joc = functii.joaca_mutare(functii.joc, mutare)
      
            
                

    pygame.display.flip() #update display


#functii.joaca_contra_IA(functii.joc, functii.pion)