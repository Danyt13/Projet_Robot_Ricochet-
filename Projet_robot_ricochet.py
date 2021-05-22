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

""" création de la fenètre """

fen = tk.Tk()
fen.title("Robot Ricochet")
canwidth, canheight = 640, 640
canvas = tk.Canvas(fen, width = canwidth, height = canheight, bg = "white")
canvas.grid(column = 5, row = 5, rowspan = 5)
position = [0, 40, 80, 120, 160, 200, 240, 280, 320, 360, 400, 440, 480, 520, 560, 600]
position1 = [0, 40, 80, 120, 160, 200, 240, 400, 440, 480, 520, 560, 600]
objet = []

"""initialisation des variables """

robot1_startX, robot1_startY = 0, 0
robot2_startX, robot2_startY = 0, 0
robot3_startX, robot3_startY = 0, 0
robot4_startX, robot4_startY = 0, 0
cpt = 0

""" création de la gille de jeu """
def grille():
    for i in range(16):
     canvas.create_line(0, 40 * i, canheight, 40 * i, fill = "grey")
    for i in range(16):
     canvas.create_line(40 * i, 0, 40 * i, canwidth, fill = "grey")
    
    canvas.create_rectangle(280 ,280, 360, 360, fill = "black")
    canvas.create_line(640, 0, 640, 640, fill = "black", width= 4)
    canvas.create_line(0, 0, 0, 640, fill = "black", width= 10)
    canvas.create_line(0, 0, 640, 0, fill = "black", width= 10)
    canvas.create_line(0, 640, 640, 640, fill = "black", width= 4)
grille()

""" création des murs extérieurs """ 

liste1 = [80, 120, 160, 200, 240, 280, 320]
liste2 = [360, 400, 440,480, 520, 560, 600]

def mursexterieur(): 
     x = liste1[random.randint(0, 6)]
     x1 = liste2[random.randint(0, 6)]
     x3 = 0
     x4 = 640
     y2 = liste1[random.randint(0, 6)]
     y3 = liste2[random.randint(0, 6)]
     y = 0
     y1 = 640
     canvas.create_line(x, y, x, y + 40, fill = "black", width= 5)
     canvas.create_line(x1, y, x1, y + 40, fill = "black", width= 5)
     canvas.create_line(x, y1, x, y1 - 40, fill = "black", width= 5)
     canvas.create_line(x1, y1, x1, y1 - 40, fill = "black", width= 5)
     canvas.create_line(x3, y2, x3 + 40, y2, fill = "black", width= 5)
     canvas.create_line(x3, y3, x3 + 40, y3, fill = "black", width= 5)
     canvas.create_line(x4, y2, x4 - 40, y2, fill = "black", width= 5)
     canvas.create_line(x4, y3, x4 - 40, y3, fill = "black", width= 5)
mursexterieur()

""" création des murs intérieurs """
def mur1():
    x = position[random.randint(1, 15)]
    y = position[random.randint(1, 15)]
    canvas.create_line(x, y, x, y + 40, fill = "black", width= 5)
    canvas.create_line(x, y, x + 40, y, fill = "black", width= 5)

def mur2():
    x = position[random.randint(1, 15)]
    y = position[random.randint(1, 15)]
    canvas.create_line(x, y, x, y - 40, fill = "black", width= 5)
    canvas.create_line(x, y, x + 40, y, fill = "black", width= 5)

def mur3():
    x = position[random.randint(1, 15)]
    y = position[random.randint(1, 15)]
    canvas.create_line(x, y, x, y - 40, fill = "black", width= 5)
    canvas.create_line(x, y, x - 40, y, fill = "black", width= 5)

def mur4():
    x = position[random.randint(1, 15)]
    y = position[random.randint(1, 15)]
    canvas.create_line(x, y, x, y + 40, fill = "black", width= 5)
    canvas.create_line(x, y, x - 40, y, fill = "black", width= 5)

"""apparition aléatoire des murs intérieurs """

for i in range(25):
    x = random.randint(0, 3)
    if x == 0:
        mur1()
    elif x == 1:
        mur2()
    elif x == 2:
        mur3()
    elif x == 3:
        mur4()

""" création des robots """

# création de robot qui n'apparaitrons pas dans le carré du milieu
def robotrouge():
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

robot1, robot2, robot3, robot4 = robotrouge(), robotjaune(),robotbleu(), robotvert()

listeDeRobot = [robot1, robot2, robot3, robot4]

""" création des cibles """

def ciblerouge():
    if len(objet) != 0:
        canvas.delete(objet[-1])
        del objet[-1]        
        xa, ya = position[random.randint(0, 15)], position[random.randint(0, 15)]
        objet.append(canvas.create_rectangle(xa, ya, xa + 40, ya + 40, fill = "red"))
        return objet
    elif len(objet) == 0:
        xa, ya = position[random.randint(0, 15)], position[random.randint(0, 15)]
        objet.append(canvas.create_rectangle(xa, ya, xa + 40, ya + 40, fill = "red"))
        return objet

def ciblejaune():
    if len(objet) != 0:
        canvas.delete(objet[-1])
        del objet[-1]        
        xb, yb = position[random.randint(0, 15)], position[random.randint(0, 15)]
        objet.append(canvas.create_rectangle(xb, yb, xb + 40, yb + 40, fill = "yellow"))
        return objet
    elif len(objet) == 0:
        xb, yb = position[random.randint(0, 15)], position[random.randint(0, 15)]
        objet.append(canvas.create_rectangle(xb, yb, xb + 40, yb + 40, fill = "yellow"))
        return objet

def ciblebleu():
    if len(objet) != 0:
        canvas.delete(objet[-1])
        del objet[-1]        
        xc, yc = position[random.randint(0, 15)], position[random.randint(0, 15)]
        objet.append(canvas.create_rectangle(xc, yc, xc + 40, yc + 40, fill = "blue"))
        return objet
    elif len(objet) == 0:
        xc, yc = position[random.randint(0, 15)], position[random.randint(0, 15)]
        objet.append(canvas.create_rectangle(xc, yc, xc + 40, yc + 40, fill = "blue"))
        return objet

def ciblevert():
    if len(objet) != 0:
        canvas.delete(objet[-1])
        del objet[-1]        
        xd, yd = position[random.randint(0, 15)], position[random.randint(0, 15)]
        objet.append(canvas.create_rectangle(xd, yd, xd + 40, yd + 40, fill = "green"))
        return objet
    elif len(objet) == 0:
        xd, yd = position[random.randint(0, 15)], position[random.randint(0, 15)]
        objet.append(canvas.create_rectangle(xd, yd, xd + 40, yd + 40, fill = "green"))
        return objet


""" déplacement des robot, je ne vois pas ou est l'erreur"""

def deplacementRobot(event):
    global x0, y0, x1, y1, x2, y2, x3, y3, cpt
    touche = event.keysym
    global X, Y
    X = event.x
    Y = event.y 
    if x0 <= X <= x0+40 and y0 <= Y <= y0+40:
        print("robot rouge")
        if touche == "<Up>": 
            print("up")
            y0 =- 40
            canvas.move(robot1, 0,-40)
            cpt += 1
        elif touche == "Down":
            canvas.move(robot1, 0, 40)
            y0 =+ 40
            cpt += 1
        elif touche == "Right":
            x0 =+ 40
            canvas.move(robot1, 40, 0)
            cpt += 1
        elif touche == "Left":
            x0 =-40
            canvas.move(robot1, -40, 0)
            cpt += 1
    if x1 <= X <= x1+40 and y1 <= Y <= y1+40:
        print("robot jaune")
        if touche == "<Up>": 
            y1 =- 40
            canvas.move(robot2, 0,-40)
            cpt += 1 
        elif touche == "Down":
            canvas.move(robot2, 0, 40)
            y1 =+ 40
            cpt += 1
        elif touche == "Right":
            x1 =+ 40
            canvas.move(robot2, 40, 0)
        elif touche == "Left":
            x1 =-40
            canvas.move(robot2, -40, 0)
            cpt += 1
    if x2 <= X <= x2+40 and y2 <= Y <= y2+40:
        print("robot bleu")
        if touche == "<Up>": 
            y2 =- 40
            canvas.move(robot3, 0,-40)
            cpt += 1
        elif touche == "Down":
            canvas.move(robot3, 0, 40)
            y2 =+ 40
            cpt += 1
        elif touche == "Right":
            x2 =+ 40
            canvas.move(robot3, 40, 0)
            cpt += 1
        elif touche == "Left":
            x2 =-40
            canvas.move(robot3, -40, 0)
            cpt += 1
    if x3 <= X <= x3+40 and y3 <= Y <= y3+40:
        print("robot vert") 
        if touche == "<Up>": 
            y3 =- 40
            canvas.move(robot4, 0,-40)
            cpt += 1
        elif touche == "Down":
            canvas.move(robot4, 0, 40)
            y3 =+ 40
            cpt += 1
        elif touche == "Right":
            x3 =+ 40
            canvas.move(robot4, 40, 0)
            cpt += 1
        elif touche == "Left":
            x3 =-40
            canvas.move(robot4, -40, 0)
            cpt += 1

canvas.bind("<Button-1>", deplacementRobot)
canvas.bind("<Up>", deplacementRobot)
canvas.bind("<Down>", deplacementRobot)
canvas.bind("<Right>", deplacementRobot)
canvas.bind("<Left>", deplacementRobot)

""" la partie revien au début quand on clique sur le bouton du milieu """
def recommencer():
    print("reset")
    global robot1_startX, robot1_startY, robot2_startX, robot2_startY, robot3_startX, robot3_startY, robot4_startX, robot4_startY
    global x0, y0, x1, y1, x2, y2, x3, y3, cpt 

    x0, y0 = robot1_startX, robot1_startY
    x1, y1 = robot2_startX, robot2_startY
    x2, y2 = robot3_startX, robot3_startY
    x3, y3 = robot4_startX, robot4_startY
    cpt = 0
    return  x0, y0, x1, y1, x2, y2, x3, y3, cpt 


""" bouton pour l'apparition des cibles """

bouton = tk.Button(fen, bg = "black",width = 8, height = 4, command= recommencer)
bouton.grid(column = 5, row = 5, rowspan = 5)
boutonvert = tk.Button(fen, bg = "green",width = 8, height = 2, command= ciblevert, text = "cible", borderwidth = 10, relief = "groove")
boutonvert.grid(column = 1, row = 2, rowspan = 5)
boutonrouge = tk.Button(fen, bg = "red",width = 8, height = 2, command= ciblerouge, text = "cible", borderwidth = 10, relief = "groove")
boutonrouge.grid(column = 1, row = 3, rowspan = 5)
boutonjaune = tk.Button(fen, bg = "yellow",width =8, height = 2, command= ciblejaune, text = "cible", borderwidth = 10, relief = "groove")
boutonjaune.grid(column = 1, row = 4, rowspan = 5)
boutonbleu = tk.Button(fen, bg = "blue",width = 8, height = 2, command= ciblebleu, text = "cible", borderwidth = 10, relief = "groove")
boutonbleu.grid(column = 1, row = 5, rowspan = 5)


""" widgets pour score et nombres de coups """

nombredecoup = tk.Button(fen,text = "Nombre de coup: " + str(cpt))
nombredecoup.grid(column = 1, row = 0, rowspan = 1)

score = tk.Button(fen,text = "score" )
score.grid(column = 0, row = 0, rowspan = 1)


def miseajourscore(event):
    global var_score 
    pass

""" configuration du curseur et de la fenètre"""

canvas.configure(cursor ='hand2')
fen.resizable(width=False, height=False)

#apparition de la fenètre Tkinter
fen.mainloop()
