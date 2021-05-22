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
canwidth, canheight = 800, 640
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

""" création des murs """

def genere_murs():
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
genere_murs()

""" création des robots """

# création de robot qui n'apparaitrons pas dans le carré du milieu
def robotrouge():
    global x0, y0, robot1_startX, robot1_startY 
    x0 = 0
    y0 = 200
    cercle1 = canvas.create_oval(x0, y0, x0 + 40, y0 + 40, fill = "red")
    robot1_startX, robot1_startY =  x0, y0
    return cercle1

def robotjaune():
    global x1, y1, robot2_startX, robot2_startY
    x1 = 160
    y1 = 480
    cercle2 = canvas.create_oval(x1, y1, x1 + 40, y1 + 40, fill = "yellow")
    robot2_startX, robot2_startY =  x1, y1
    return cercle2

def robotbleu():
    global x2, y2, robot3_startX, robot3_startY
    x2 = 120
    y2 = 120
    cercle3 = canvas.create_oval(x2, y2, x2 + 40, y2 + 40, fill = "blue")
    robot3_startX, robot3_startY =  x2, y2
    return cercle3


def robotvert():
    global x3, y3, robot4_startX, robot4_startY
    x3 = 440
    y3 = 440
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
        xa, ya = 200, 120
        objet.append(canvas.create_rectangle(xa, ya, xa + 40, ya + 40, fill = "red"))
        return objet
    elif len(objet) == 0:
        xa, ya = 200, 120
        objet.append(canvas.create_rectangle(xa, ya, xa + 40, ya + 40, fill = "red"))
        return objet

def ciblejaune():
    if len(objet) != 0:
        canvas.delete(objet[-1])
        del objet[-1]        
        xb, yb = 40, 360
        objet.append(canvas.create_rectangle(xb, yb, xb + 40, yb + 40, fill = "yellow"))
        return objet
    elif len(objet) == 0:
        xb, yb = 40, 360
        objet.append(canvas.create_rectangle(xb, yb, xb + 40, yb + 40, fill = "yellow"))
        return objet

def ciblebleu():
    if len(objet) != 0:
        canvas.delete(objet[-1])
        del objet[-1]        
        xc, yc = 240, 520
        objet.append(canvas.create_rectangle(xc, yc, xc + 40, yc + 40, fill = "blue"))
        return objet
    elif len(objet) == 0:
        xc, yc = 240, 520
        objet.append(canvas.create_rectangle(xc, yc, xc + 40, yc + 40, fill = "blue"))
        return objet

def ciblevert():
    if len(objet) != 0:
        canvas.delete(objet[-1])
        del objet[-1]        
        xd, yd = 440, 400
        objet.append(canvas.create_rectangle(xd, yd, xd + 40, yd + 40, fill = "green"))
        return objet
    elif len(objet) == 0:
        xd, yd = 440, 400
        objet.append(canvas.create_rectangle(xd, yd, xd + 40, yd + 40, fill = "green"))
        return objet


""" déplacement des robot, je ne vois pas ou est l'erreur"""

affiche_score = canvas.create_text(724.25, 360, fill = "white", text = "0")

def deplacementRobot(event):
    global x0, y0, x1, y1, x2, y2, x3, y3, cpt
    touche = event.keysym
    global X, Y, mouvement
    X = event.x
    Y = event.y
    #assignement de la variable mouvement en fonction des coordonnées des robots
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
    #deplacement du robot rouge 
    if mouvement == 1 and touche == "Up": 
        y0 =- 40
        canvas.move(robot1, 0, -40)
        cpt += 1
        print ("Nombres de coups:",cpt)
    elif mouvement == 1 and touche == "Down":
        canvas.move(robot1, 0, 40)
        y0 =+ 40
        cpt+= 1
        print ("Nombres de coups:",cpt)
    elif mouvement == 1 and touche == "Right":
        x0 =+ 40
        canvas.move(robot1, 40, 0)
        cpt += 1
        print ("Nombres de coups:",cpt)
    elif mouvement == 1 and touche == "Left":
        x0 =-40
        canvas.move(robot1, -40, 0)
        cpt += 1
        print ("Nombres de coups:",cpt)
    #deplacement du robot jaune
    if touche == "Up" and mouvement == 2: 
        y1 =- 40
        canvas.move(robot2, 0,-40)
        cpt += 1 
        print ("Nombres de coups:",cpt)
    elif touche == "Down" and mouvement == 2:
        canvas.move(robot2, 0, 40)
        y1 =+ 40
        cpt += 1
        print ("Nombres de coups:",cpt)
    elif touche == "Right" and mouvement == 2:
        x1 =+ 40
        canvas.move(robot2, 40, 0)
        cpt += 1
        print ("Nombres de coups:",cpt)
    elif touche == "Left" and mouvement == 2:
        x1 =-40
        canvas.move(robot2, -40, 0)
        cpt += 1
        print ("Nombres de coups:",cpt)
    #deplacement du robot bleu
    if touche == "Up" and mouvement == 3: 
        y2 =- 40
        canvas.move(robot3, 0,-40)
        cpt += 1
        print ("Nombres de coups:",cpt)
    elif touche == "Down" and mouvement == 3:
        canvas.move(robot3, 0, 40)
        y2 =+ 40
        cpt += 1
        print ("Nombres de coups:",cpt)
    elif touche == "Right" and mouvement == 3:
        x2 =+ 40
        canvas.move(robot3, 40, 0)
        cpt += 1
        print ("Nombres de coups:",cpt)
    elif touche == "Left" and mouvement == 3:
        x2 =-40
        canvas.move(robot3, -40, 0)
        cpt += 1
        print ("Nombres de coups:",cpt)
    #deplacement du robot vert 
    if touche == "Up" and mouvement == 4: 
        y3 =- 40
        canvas.move(robot4, 0,-40)
        cpt += 1
        print ("Nombres de coups:",cpt)
    elif touche == "Down" and mouvement == 4:
        canvas.move(robot4, 0, 40)
        y3 =+ 40
        cpt += 1
        print ("Nombres de coups:",cpt)
    elif touche == "Right" and mouvement == 4:
        x3 =+ 40
        canvas.move(robot4, 40, 0)
        cpt += 1
        print ("Nombres de coups:",cpt)
    elif touche == "Left" and mouvement == 4:
        x3 =-40
        canvas.move(robot4, -40, 0)
        cpt += 1
        print ("Nombres de coups:",cpt)
    canvas.itemconfigure(affiche_score, text = cpt )

canvas.bind_all("<Button-1>", deplacementRobot)
canvas.bind_all("<Up>", deplacementRobot)
canvas.bind_all("<Down>", deplacementRobot)
canvas.bind_all("<Right>", deplacementRobot)
canvas.bind_all("<Left>", deplacementRobot)

""" la partie revien au début quand on clique sur le bouton du milieu """
def recommencer():
    fen.destroy()
    # principal()


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

def score_et_record():
    canvas.create_rectangle(645, 260, 800, 300, fill = "black", outline = "yellow", width = 5)
    canvas.create_text(685, 280, fill = "white", text = "record :")

    canvas.create_rectangle(645, 340, 800, 380, fill = "black" , outline = "red", width = 5)
    canvas.create_text(685, 360, fill = "white", text = "score :")


""" configuration du curseur et de la fenètre"""

canvas.configure(cursor ='hand2')
fen.resizable(width=False, height=False)

#apparition de la fenètre Tkinter
fen.mainloop()
