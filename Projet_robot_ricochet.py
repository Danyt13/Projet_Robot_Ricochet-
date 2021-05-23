#########################################
# groupe MPCI 5
# Riyad KENZI
# Yanis MOHELLIBI
# Dany TANG
#Florian GONDRY
#https://github.com/Danyt13/Projet_Robot_Ricochet-
########################################

import tkinter as tk 
import random
from tkinter.constants import CENTER, TRUE

#  création fenêtre 

fen = tk.Tk()
fen.title("Robot Ricochet")
canwidth, canheight = 800, 640
canvas = tk.Canvas(fen, width = canwidth, height = canheight, bg = "white")

# variables

position = [0, 40, 80, 120, 160, 200, 240, 280, 320, 360, 400, 440, 480, 520, 560, 600]
position1 = [0, 40, 80, 120, 160, 200, 240, 400, 440, 480, 520, 560, 600]
objet = []
cpt = 0
record = 0
points = 0
mouvement = 0
ciblerougecliquer,ciblejaunecliquer, ciblebleucliquer, ciblevertcliquer = 0, 0, 0, 0

#  définition 

def grille():
    """ création de la gille de jeu """
    for i in range(16):
     canvas.create_line(0, 40 * i, canheight, 40 * i, fill = "grey")
    for i in range(16):
     canvas.create_line(40 * i, 0, 40 * i, canwidth, fill = "grey")
    
    canvas.create_rectangle(280 ,280, 360, 360, fill = "black")
    canvas.create_line(640, 0, 640, 640, fill = "black", width= 4)
    canvas.create_line(0, 0, 0, 640, fill = "black", width= 10)
    canvas.create_line(0, 0, 640, 0, fill = "black", width= 10)
    canvas.create_line(0, 640, 640, 640, fill = "black", width= 4)


def genere_murs():
    """ création des murs """
    mursverticale = ((0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0),(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0), (0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0), (0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1), (0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),(0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0), (0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0), (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0))
    murshorizontale = ((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0), (0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0), (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0), (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0), (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
    for i in range(len(mursverticale)):
        for j in range(len(mursverticale[i])):
            if mursverticale[i][j] == 1 :
                canvas.create_line((j*40,i*40),(j*40,(i+1)*40),fill = "black", width = 5)
    for i in range(len(murshorizontale)):
        for j in range(len(murshorizontale[i])):
            if murshorizontale[i][j] == 1 :
                canvas.create_line((j*40,i*40),((j+1)*40,i*40),fill = "black", width = 5)


def robotrouge():
    """ création du robot rouge avec positionnement aléatoire dans la grille """
    global x0, y0, robot1_startX, robot1_startY 
    x0 = position[random.randint(0, 15)]
    y0 = position[random.randint(0, 15)]
    if x0 == 280 or x0 == 320:
        y0 = position1[random.randint(0, 12)]
    else:
        y0 = position[random.randint(0, 15)]
    if y0 == 280 or y0 == 320:
        x0 = position1[random.randint(0, 12)]
    else:
        x0 = position[random.randint(0, 15)]
    cercle1 = canvas.create_oval(x0, y0, x0 + 40, y0 + 40, fill = "red")
    robot1_startX, robot1_startY =  x0, y0
    return cercle1


def robotjaune():
    """ création du robot jaune avec positionnement aléatoire dans la grille """
    global x1, y1, robot2_startX, robot2_startY
    x1 = position[random.randint(0, 15)]
    y1 = position[random.randint(0, 15)]
    if x1 == 280 or x1 == 320:
        y1 = position1[random.randint(0, 12)]
    else:
        y1 = position[random.randint(0, 15)]
    if y1 == 280 or y1 == 320:
        x1 = position1[random.randint(0, 12)]
    else:
        x1 = position[random.randint(0, 15)]
    cercle2 = canvas.create_oval(x1, y1, x1 + 40, y1 + 40, fill = "yellow")
    robot2_startX, robot2_startY =  x1, y1
    return cercle2


def robotbleu():
    """ création du robot bleu avec positionnement aléatoire dans la grille """
    global x2, y2, robot3_startX, robot3_startY
    x2 = position[random.randint(0, 15)]
    y2 = position[random.randint(0, 15)]
    if x2 == 280 or x2 == 320:
        y2 = position1[random.randint(0, 12)]
    else:
        y2 = position[random.randint(0, 15)]
    if y2 == 280 or y2 == 320:
        x2 = position1[random.randint(0, 12)]
    else:
        x2 = position[random.randint(0, 15)]
    cercle3 = canvas.create_oval(x2, y2, x2 + 40, y2 + 40, fill = "blue")
    robot3_startX, robot3_startY =  x2, y2
    return cercle3


def robotvert():
    """ création du robot vert avec positionnement aléatoire dans la grille """
    global x3, y3, robot4_startX, robot4_startY
    x3 = position[random.randint(0, 15)]
    y3 = position[random.randint(0, 15)]
    if x3 == 280 or x3 == 320:
        y3 = position1[random.randint(0, 12)]
    else:
        y3 = position[random.randint(0, 15)]
    if y3 == 280 or y3 == 320:
        x3 = position1[random.randint(0, 12)]
    else:
        x3 = position[random.randint(0, 15)]
    cercle4 = canvas.create_oval(x3, y3, x3 + 40, y3 + 40, fill = "green")
    robot4_startX, robot4_startY =  x3, y3
    return cercle4


def ciblerouge():
    """ création d'une cible (carré) de couleur rouge sur la grille """
    global ciblerougecliquer,ciblejaunecliquer, ciblebleucliquer, ciblevertcliquer, cercle1
    ciblerougecliquer = 1
    ciblejaunecliquer = 0
    ciblebleucliquer = 0
    ciblevertcliquer = 0
    cercle1 = canvas.create_rectangle(200, 120, 240, 160, fill = "red")
    if len(objet) != 0:
        canvas.delete(objet[-1])
        del objet[-1]        
        objet.append(cercle1)
        return objet
    elif len(objet) == 0:
        objet.append(cercle1)
        return objet


def ciblejaune():
    """ création d'une cible (carré) de couleur jaune sur la grille """
    global ciblerougecliquer,ciblejaunecliquer, ciblebleucliquer, ciblevertcliquer, cercle2
    ciblerougecliquer = 0
    ciblejaunecliquer = 1
    ciblebleucliquer = 0
    ciblevertcliquer = 0
    cercle2 = canvas.create_rectangle(40, 360, 80, 400, fill = "yellow")
    if len(objet) != 0:
        canvas.delete(objet[-1])
        del objet[-1]        
        objet.append(cercle2)
        return objet
    elif len(objet) == 0:
        objet.append(cercle2)
        return objet
        

def ciblebleu():
    """ création d'une cible (carré) de couleur bleu sur la grille """
    global ciblerougecliquer,ciblejaunecliquer, ciblebleucliquer, ciblevertcliquer, cercle3
    ciblerougecliquer = 0
    ciblejaunecliquer = 0
    ciblebleucliquer = 1
    ciblevertcliquer = 0
    cercle3 = canvas.create_rectangle(440, 400, 480, 440, fill = "blue")
    if len(objet) != 0:
        canvas.delete(objet[-1])
        del objet[-1]        
        objet.append(cercle3)
        return objet
    elif len(objet) == 0:
        objet.append(cercle3)
        return objet


def ciblevert():
    """ création d'une cible (carré) de couleur vert sur la grille """
    global ciblerougecliquer,ciblejaunecliquer, ciblebleucliquer, ciblevertcliquer, cercle4
    ciblerougecliquer = 0
    ciblejaunecliquer = 0
    ciblebleucliquer = 0
    ciblevertcliquer = 1
    cercle4 = canvas.create_rectangle(240, 520, 280, 560, fill = "green")
    if len(objet) != 0:
        canvas.delete(objet[-1])
        del objet[-1]        
        objet.append(cercle4)
        return objet
    elif len(objet) == 0:
        objet.append(cercle4)
        return objet

robot1, robot2, robot3, robot4 = robotrouge(), robotjaune(),robotbleu(), robotvert()

def move_et_record(): 
    canvas.create_rectangle(645, 260, 800, 300, fill = "black", outline = "yellow", width = 5)
    canvas.create_text(685, 280, fill = "white", text = "record :")

    canvas.create_rectangle(645, 340, 800, 380, fill = "black" , outline = "red", width = 5)
    canvas.create_text(685, 360, fill = "white", text = "move :")
move_et_record()

affiche_move = canvas.create_text(724.25, 360, fill = "white", text = "0")
affiche_record = canvas.create_text(724.25, 280, fill = "white", text = "0")

def deplacementRobot(event):
    """ permet de faire bouger les pions en leurs cliquants dessus, puis les diriger avec les flèches directionnelles du clavier """
    global x0, y0, x1, y1, x2, y2, x3, y3, cpt
    touche = event.keysym
    global X, Y, mouvement, record, cercle1, cercle2, cercle3, cercle4
    X = event.x
    Y = event.y

    """ assignement de la variable mouvement en fonction des coordonnées des robots """
    if x0 <= X <= x0+40 and y0 <= Y <= y0+40:
        mouvement = 1
        print("robot rouge")
    elif x1 <= X <= x1+40 and y1 <= Y <= y1+40:
        mouvement = 2
        print("robot jaune")
    elif x2 <= X <= x2+40 and y2 <= Y <= y2+40:  
        mouvement = 3
        print("robot bleu")
    elif x3 <= X <= x3+40 and y3 <= Y <= y3+40:
        mouvement = 4
        print("robot vert") 

    """ detection des cibles de chaque couleur et gain de points """
    if x0 == 200 and y0 == 120 and ciblerougecliquer == 1:
        canvas.destroy(robot1)
        robotrouge()
        canvas.destroy(cercle1)
        record = cpt
        canvas.itemconfigure(affiche_record, text = record)
        cpt = 0
        print ("c'est gagnée !!")
    elif x1 == 40 and y1 == 360 and ciblejaunecliquer == 1:
        canvas.destroy(robot2)
        robotjaune()
        canvas.destroy(cercle2)
        record = cpt
        canvas.itemconfigure(affiche_record, text = record)
        cpt = 0
        print ("c'est gagnée !!")
    elif x2 == 200 and y2 == 120 and ciblebleucliquer == 1:
        canvas.destroy(robot3)
        robotvert()
        canvas.destroy(cercle3)
        record = cpt
        canvas.itemconfigure(affiche_record, text = record)
        cpt = 0
        print ("c'est gagnée !!")
    elif x3 == 200 and y3 == 120 and ciblevertcliquer == 1:
        canvas.destroy(robot4)
        robotbleu()
        canvas.destroy(cercle4)
        record = cpt
        canvas.itemconfigure(affiche_record, text = record)
        cpt = 0
        print ("c'est gagnée !!")

    """ deplacement du robot rouge """ 
    if mouvement == 1 and touche == "Up":
        if x0 == x1 and y0 > y1:
            canvas.move(robot1, 0, -y0+y1+40)
            y0 = y1 + 40
        elif x0 == x2 and y0 > y2:
            canvas.move(robot1, 0, -y0+y2+40)
            y0 = y2 + 40
        elif x0 == x3 and y0 > y3:
            canvas.move(robot1, 0, -y0+y3+40)
            y0 = y3 + 40
        elif (x0 == 280 or x0 == 320) and y0 >= 360:
            canvas.move(robot1, 0, -y0+360)   
            y0 = 360
        else:
            canvas.move(robot1, 0, -y0)
            y0 =0
        cpt += 1
        print ("Nombres de coups:",cpt)
    elif mouvement == 1 and touche == "Down":
        if x1 == x0 and y0 < y1 :
            canvas.move(robot1, 0, y1-y0-40)
            y0 = y1 - 40
        elif x0 == x2 and y0 < y2 :
            canvas.move(robot1, 0, y2-y0-40)
            y0 = y2 - 40
        elif x3 == x0 and y0 < y3 :
            canvas.move(robot1, 0, y3-y0-40)
            y0 = y3 - 40
        elif (x0 == 280 or x0 == 320) and y0 <= 240:
            canvas.move(robot1, 0, -y0+240)
            y0 = 240
        else:
            canvas.move(robot1, 0, 600-y0)
            y0 = 600
        cpt += 1
        print ("Nombres de coups:",cpt)
    elif mouvement == 1 and touche == "Right":
        if x0 < x1 and y0 == y1:
            canvas.move(robot1, x1-x0-40, 0)
            x0 = x1 - 40
        elif x0 < x2 and y0 == y2:
            canvas.move(robot1, x2-x0-40, 0)
            x0 = x2 - 40
        elif x0 < x3 and y0 == y3:
            canvas.move(robot1, x3-x0-40, 0)
            x0 = x3 - 40
        elif (y0 == 280 or y0 == 320) and x0 <= 240:
            canvas.move(robot1, 240-x0, 0)
            x0 = 240
        else: 
             canvas.move(robot1, 600-x0, 0)
             x0 = 600
        cpt += 1
        print ("Nombres de coups:",cpt)
    elif mouvement == 1 and touche == "Left":
        if x0 > x1 and y0 == y1:
            canvas.move(robot1, -x0+x1+40, 0)
            x0 = x1 + 40 
        elif x0 > x2 and y0 == y2:
            canvas.move(robot1, -x0+x2+40, 0)
            x0 = x2 + 40 
        elif x0 > x3 and y0 == y3:
            canvas.move(robot1, -x0+x3+40, 0)
            x0 = x3 + 40 
        elif (y0 == 280 or y0 == 320) and x0 >= 360:
            canvas.move(robot1, 360-x0, 0)
            x0 = 360
        else:
            canvas.move(robot1,-x0, 0)
            x0 = 0
        cpt += 1
        print ("Nombres de coups:",cpt)
   
    """ deplacement du robot jaune """
    if touche == "Up" and mouvement == 2: 
        if x1 == x0 and y1 > y0:
            canvas.move(robot2, 0, -y1+y0+40)
            y1 = y0 + 40
        elif x1 == x2 and y1 > y2:
            canvas.move(robot2, 0, -y1+y2+40)
            y1 = y2 + 40
        elif x1 == x3 and y1 > y3:
            canvas.move(robot2, 0, -y1+y3+40)
            y1 = y3 + 40
        elif (x1 == 280 or x1 == 320) and y1 >= 360:
            canvas.move(robot2, 0, -y1+360)   
            y1 = 360
        else:
            canvas.move(robot2, 0, -y1)
            y1 =0
        cpt += 1
        print ("Nombres de coups:",cpt)
    elif touche == "Down" and mouvement == 2:
        if x1 == x0 and y1 < y0 :
            canvas.move(robot2, 0, y0-y1-40)
            y1 = y0 - 40
        elif x1 == x2 and y1 < y2 :
            canvas.move(robot2, 0, y2-y1-40)
            y1 = y2 - 40
        elif x3 == x1 and y1 < y3 :
            canvas.move(robot2, 0, y3-y1-40)
            y1 = y3 - 40
        elif (x1 == 280 or x1 == 320) and y1 <= 240:
            canvas.move(robot2, 0, -y1+240)
            y1 = 240
        else:
            canvas.move(robot2, 0, 600-y1)
            y1 = 600
    elif touche == "Right" and mouvement == 2:
        if x1 < x0 and y1 == y0:
            canvas.move(robot2, x0-x1-40, 0)
            x1 = x0 - 40
        elif x1 < x2 and y1 == y2:
            canvas.move(robot2, x2-x1-40, 0)
            x1 = x2 - 40
        elif x1 < x3 and y1 == y3:
            canvas.move(robot2, x3-x1-40, 0)
            x1 = x3 - 40
        elif (y1 == 280 or y1 == 320) and x1 <= 240:
            canvas.move(robot2, 240-x1, 0)
            x1 = 240
        else:
            canvas.move(robot2, 600-x1, 0)
            x1 = 600
        cpt += 1
        print ("Nombres de coups:",cpt)
    elif touche == "Left" and mouvement == 2:
        if x1 > x0 and y1 == y0:
            canvas.move(robot2, -x1+x0+40, 0)
            x1 = x0 + 40 
        elif x1 > x2 and y1 == y2:
            canvas.move(robot2, -x1+x2+40, 0)
            x1 = x2 + 40 
        elif x1 > x3 and y1 == y3:
            canvas.move(robot2, -x1+x3+40, 0)
            x1 = x3 + 40 
        elif (y1 == 280 or y1 == 320) and x1 >= 360:
            canvas.move(robot2, 360-x1 , 0)
            x1 = 360
        else:
            canvas.move(robot2,-x1, 0)
            x1 = 0
        cpt += 1
        print ("Nombres de coups:",cpt)

    """ deplacement du robot bleu """
    if touche == "Up" and mouvement == 3:
        if x2 == x0 and y2 > y0:
            canvas.move(robot3, 0, -y2+y0+40)
            y2 = y0 + 40
        elif x1 == x2 and y2 > y1:
            canvas.move(robot3, 0, -y2+y1+40)
            y2 = y1 + 40
        elif x2 == x3 and y2 > y3:
            canvas.move(robot3, 0, -y2+y3+40)
            y2 = y3 + 40
        elif (x2 == 280 or x2 == 320) and y2 >= 360:
            canvas.move(robot3, 0, -y2+360)   
            y2 = 360
        else:
            canvas.move(robot3, 0, -y2)
            y2 =0
        cpt += 1
        print ("Nombres de coups:",cpt)
    elif touche == "Down" and mouvement == 3:
        if x2 == x0 and y2 < y0 :
            canvas.move(robot3, 0, y0-y2-40)
            y2 = y0 - 40
        elif x2 == x1 and y2 < y1 :
            canvas.move(robot3, 0, y1-y2-40)
            y2 = y1 - 40
        elif x2 == x3 and y2 < y3 :
            canvas.move(robot3, 0, y3-y2-40)
            y2 = y3 - 40
        elif (x2 == 280 or x2 == 320) and y2 <= 240:
            canvas.move(robot3, 0, -y2+240)
            y2 = 240
        else:
            canvas.move(robot3, 0, 600-y2)
            y2 = 600
        cpt += 1
        print ("Nombres de coups:",cpt)
    elif touche == "Right" and mouvement == 3:
        if x2 < x0 and y2 == y0:
            canvas.move(robot3, x0-x2-40, 0)
            x2 = x0 - 40
        elif x2 < x1 and y2 == y1:
            canvas.move(robot3, x1-x2-40, 0)
            x2 = x1- 40
        elif x2 < x3 and y2 == y3:
            canvas.move(robot3, x3-x2-40, 0)
            x2 = x3 - 40
        elif (y2 == 280 or y2 == 320) and x2 <= 240:
            canvas.move(robot3, 240-x2, 0)
            x2 = 240
        else:
            canvas.move(robot3, 600-x2, 0)
            x2 = 600
        cpt += 1
        print ("Nombres de coups:",cpt)
    elif touche == "Left" and mouvement == 3:
        if x2 > x0 and y2 == y0:
            canvas.move(robot3, -x2+x0+40, 0)
            x2 = x0 + 40 
        elif x2 > x1 and y2 == y1:
            canvas.move(robot3, -x2+x1+40, 0)
            x2 = x1 + 40 
        elif x2 > x3 and y2 == y3:
            canvas.move(robot3, -x2+x3+40, 0)
            x2 = x3 + 40 
        elif (y2 == 280 or y2 == 320) and x2 >= 360:
            canvas.move(robot3, 360-x2 , 0)
            x2 = 360
        else:
            canvas.move(robot3,-x2, 0)
            x2 = 0
        cpt += 1
        print ("Nombres de coups:",cpt)
    
    """ deplacement du robot vert """  
    if touche == "Up" and mouvement == 4:
        if x3 == x0 and y3 > y0:
            canvas.move(robot4, 0, -y3+y0+40)
            y3 = y0 + 40
        elif x1 == x3 and y3 > y1:
            canvas.move(robot4, 0, -y3+y1+40)
            y3 = y1 + 40
        elif x2 == x3 and y3 > y2:
            canvas.move(robot4, 0, -y3+y2+40)
            y3 = y2 + 40
        elif (x3 == 280 or x3 == 320) and y3 >= 360:
            canvas.move(robot4, 0, -y3+360)   
            y3 = 360
        else:
            canvas.move(robot4, 0, -y3)
            y3 =0
        cpt += 1
        print ("Nombres de coups:",cpt)
    elif touche == "Down" and mouvement == 4:
        if x3 == x0 and y3 < y0 :
            canvas.move(robot4, 0, y0-y3-40)
            y3 = y0 - 40
        elif x3 == x1 and y3 < y1 :
            canvas.move(robot4, 0, y1-y3-40)
            y3 = y1 - 40
        elif x2 == x3 and y3 < y2 :
            canvas.move(robot4, 0, y2-y3-40)
            y3 = y2 - 40
        elif (x3 == 280 or x3 == 320) and y3 <= 240:
            canvas.move(robot4, 0, -y3+240)
            y3 = 240
        else:
            canvas.move(robot4, 0, 600-y3)
            y3 = 600
        cpt += 1
        print ("Nombres de coups:",cpt)
    elif touche == "Right" and mouvement == 4:
        if x3 < x0 and y3 == y0:
            canvas.move(robot4, x0-x3-40, 0)
            x3 = x0 - 40
        elif x3 < x1 and y3 == y1:
            canvas.move(robot4, x1-x3-40, 0)
            x3 = x1- 40
        elif x3 < x2 and y3 == y2:
            canvas.move(robot4, x2-x3-40, 0)
            x3 = x2 - 40
        elif (y3 == 280 or y3 == 320) and x3 <= 240:
            canvas.move(robot4, 240-x3, 0)
            x3 = 240
        else:
            canvas.move(robot4, 600-x3, 0)
            x3 = 600
        cpt += 1
        print ("Nombres de coups:",cpt)
    elif touche == "Left" and mouvement == 4:
        if x3 > x0 and y3 == y0:
            canvas.move(robot4, -x3+x0+40, 0)
            x3 = x0 + 40 
        elif x3 > x1 and y3 == y1:
            canvas.move(robot4, -x3+x1+40, 0)
            x3 = x1 + 40 
        elif x3 > x2 and y3 == y2:
            canvas.move(robot4, -x3+x2+40, 0)
            x3 = x2 + 40 
        elif  x3 >= 360 and  y3 == 280:
            canvas.move(robot4, 360-x3 , 0)
            x3 = 360
        elif  x3 >= 360 and  y3 == 320:
            canvas.move(robot4, 360-x3 , 0)
            x3 = 360
        else:
            canvas.move(robot4,-x3, 0)
            x3 = 0
        cpt += 1
        print ("Nombres de coups:",cpt)
    canvas.itemconfigure(affiche_move, text = cpt )


def recommencer():
    """ permet de relancer la grille quand on appuye sur le carré noir du milieu de la grille """ 
    pass
    # principal()


#  Boutons 

boutonvert = tk.Button(fen, bg = "green",width = 8, height = 2, command= ciblevert, text = "cible", borderwidth = 10, relief = "groove")
boutonvert.grid(column = 1, row = 2, rowspan = 5)
boutonrouge = tk.Button(fen, bg = "red",width = 8, height = 2, command= ciblerouge, text = "cible", borderwidth = 10, relief = "groove")
boutonrouge.grid(column = 1, row = 3, rowspan = 5)
boutonjaune = tk.Button(fen, bg = "yellow",width =8, height = 2, command= ciblejaune, text = "cible", borderwidth = 10, relief = "groove")
boutonjaune.grid(column = 1, row = 4, rowspan = 5)
boutonbleu = tk.Button(fen, bg = "blue",width = 8, height = 2, command= ciblebleu, text = "cible", borderwidth = 10, relief = "groove")
boutonbleu.grid(column = 1, row = 5, rowspan = 5)


#  widgets 

canvas.grid(column = 5, row = 5, rowspan = 5,)
canvas.bind_all("<Button-1>", deplacementRobot)
canvas.bind_all("<Up>", deplacementRobot)
canvas.bind_all("<Down>", deplacementRobot)
canvas.bind_all("<Right>", deplacementRobot)
canvas.bind_all("<Left>", deplacementRobot)


#  appel de fonction

grille()
genere_murs()


#  configuration du curseur et de la fenètre

canvas.configure(cursor ='hand2')
fen.resizable(width=False, height=False)


#  apparition de la fenètre Tkinter

fen.mainloop()




# On a mis ces fonctions en commentaire, car on a décider d'au lieu de définir l'emplacement des pions (robots) à chaque fois au même endroit,
# On va les générer aléatoirement sur la grille, pour varier les parties.

# fonction qui créer des robots avec placement définie sur la grille 

# def robotrouge():
#     global x0, y0, robot1_startX, robot1_startY 
#     x0 = 0
#     y0 = 200
#     cercle1 = canvas.create_oval(x0, y0, x0 + 40, y0 + 40, fill = "red")
#     robot1_startX, robot1_startY =  x0, y0
#     return cercle1


# def robotjaune():
#     global x1, y1, robot2_startX, robot2_startY
#     x1 = 160
#     y1 = 480
#     cercle2 = canvas.create_oval(x1, y1, x1 + 40, y1 + 40, fill = "yellow")
#     robot2_startX, robot2_startY =  x1, y1
#     return cercle2


# def robotbleu():
#     global x2, y2, robot3_startX, robot3_startY
#     x2 = 120
#     y2 = 120
#     cercle3 = canvas.create_oval(x2, y2, x2 + 40, y2 + 40, fill = "blue")
#     robot3_startX, robot3_startY =  x2, y2
#     return cercle3


# def robotvert():
#     global x3, y3, robot4_startX, robot4_startY
#     x3 = 440
#     y3 = 440
#     cercle4 = canvas.create_oval(x3, y3, x3 + 40, y3 + 40, fill = "green")
#     robot4_startX, robot4_startY =  x3, y3
#     return cercle4


# Au début on était parti sur des cibles aléatoires mais si on fait ça, il y a un risque que le jeu soit impossible a finir. 
# et on a donc décidé de garder l'emplacement des cibles fixes, identiques à l'exemple qu'on à pris sur le site http://www.robotreboot.com/challenge,
# Ce site est donner dans le sujet comme inspiration pour créer l'interface graphique pour le projet robot ricochet. 
# On a donc décidé de garder une trace des définitions pour les cibles aléatoires.

# fonction qui permet de généré une cible aléatoirement sur le grille 

# def ciblerouge():
#     if len(objet) != 0:
#         canvas.delete(objet[-1])
#         del objet[-1]        
#         xa, ya = position[random.randint(0, 15)], position[random.randint(0, 15)]
#         objet.append(canvas.create_rectangle(xa, ya, xa + 40, ya + 40, fill = "red"))
#         return objet
#     elif len(objet) == 0:
#         xa, ya = position[random.randint(0, 15)], position[random.randint(0, 15)]
#         objet.append(canvas.create_rectangle(xa, ya, xa + 40, ya + 40, fill = "red"))
#         return objet

# def ciblejaune():
#     if len(objet) != 0:
#         canvas.delete(objet[-1])
#         del objet[-1]        
#         xb, yb = position[random.randint(0, 15)], position[random.randint(0, 15)]
#         objet.append(canvas.create_rectangle(xb, yb, xb + 40, yb + 40, fill = "yellow"))
#         return objet
#     elif len(objet) == 0:
#         xb, yb = position[random.randint(0, 15)], position[random.randint(0, 15)]
#         objet.append(canvas.create_rectangle(xb, yb, xb + 40, yb + 40, fill = "yellow"))
#         return objet

# def ciblebleu():
#     if len(objet) != 0:
#         canvas.delete(objet[-1])
#         del objet[-1]        
#         xc, yc = position[random.randint(0, 15)], position[random.randint(0, 15)]
#         objet.append(canvas.create_rectangle(xc, yc, xc + 40, yc + 40, fill = "blue"))
#         return objet
#     elif len(objet) == 0:
#         xc, yc = position[random.randint(0, 15)], position[random.randint(0, 15)]
#         objet.append(canvas.create_rectangle(xc, yc, xc + 40, yc + 40, fill = "blue"))
#         return objet

# def ciblevert():
#     if len(objet) != 0:
#         canvas.delete(objet[-1])
#         del objet[-1]        
#         xd, yd = position[random.randint(0, 15)], position[random.randint(0, 15)]
#         objet.append(canvas.create_rectangle(xd, yd, xd + 40, yd + 40, fill = "green"))
#         return objet
#     elif len(objet) == 0:
#         xd, yd = position[random.randint(0, 15)], position[random.randint(0, 15)]
#         objet.append(canvas.create_rectangle(xd, yd, xd + 40, yd + 40, fill = "green"))
#         return objet