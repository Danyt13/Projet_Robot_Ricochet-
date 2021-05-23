# Projet_Robot_Ricochet-
Programmation du Jeu Robot Ricochet dans le cadre d'un projet universitaire 

Touches de contrôles: 

- Cliquez sur un des boutons cible. ( Génére une cible de la couleur du bouton, aléatoirement sur la grille.)
- Cliquez sur le pion que vous voulez utiliser.
- Puis utilisez les flèches directionnelles :  - flèche vers haut pour monter. 
                                               - flèche vers bas pour descendre. 
                                               - flèche vers la gauche pour aller vers la gauche. 
                                               - flèceh vers la droite pour aller vers la droite.
- Si vous voulez reset la partie, cliquez sur le bouton au centre de la grille.

Règle du jeu :

Amener le Robot de la même couleur que la cible sur la cible, avec le moins de coups possible. 

Problème rencontré : 

Difficultés à faire bouger les robots avec les flèches directionnelles, on arrive pas a faire en sorte que les pions s'arrêtent d'avancer quand ils rencontrent un mur sur la grille. Donc notre programme ne permet pas de finir le jeu pour l'instant et la fonction déplacement est encore trop longue. 

# séparement du reste ça fonctionne trés bien mais imposible de mettre une condition en plus 

"""
def deplacementRobotRouge(event):
    global x0, y0
    touche = event.keysym
    global X, Y
    X = event.x
    Y = event.y
    if touche == "Up": 
                y0 =- 40
                canvas.move(robot1, 0, -40)
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

les robots se déplacent une case par une case pour le moment.
quand on change de robot une fois on ne peut plus cliquer sur un nouveau robot
 
les robots ne se superpose plus entres eux ou avec le centre et ils ne peuvent plus sortir du terrain mais quand plusieur robots sont alignés 
il arrive que certain traverse le centre ou un autre robot
 
si un robot touche une cible le nombre de coups est afficher aux mauvaise endroit 
les robots traversent toujours les murs 
"""

Difficultés à faire bouger les robots avec les flèches directionnelles, on arrive pas a faire en sorte que les pions s'arrêtent d'avancer quand ils rencontrent un mur sur la grille et on a encore quelque problème de priorité quand les robots sont alignés parfois un robot se superpose à un autre. 
La fonction déplacement est encore trop longue.

