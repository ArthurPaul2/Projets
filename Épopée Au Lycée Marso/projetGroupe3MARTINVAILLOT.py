import pygame
from random import choice
pygame.init()

#implémentation de la classe professeur
class Prof:

    def __init__(self,nom,catchphrases,liste_images,matière,):
        '''nom: string
           liste_image: list, les images du prof, liste de longueur 3
           les images sont des variables qui contiennent le chemin vers l'image dans le dossier
           matière: clé de la liste matières,valeur associée: type list, liste des questions
           pv: int
        '''

        self.nom = nom
        self.images = liste_images    #attribut qui stocke toutes les images
        self.im_aff = liste_images[0] #attribut qui stocke l'image associée au prof 
        self.mat = matière
        self.etat = 0
        self.pv = 8
        self.lines = catchphrases
    def resetprof(self):
        self.pv = 8
        self.etat = 0
    def baisser_pv(self):
        self.pv -= 1

    def changer_etat(self,id_n_etat):
        '''id_n_etat: int, l'indice du nouvel etat dans la liste liste_images'''
        self.etat = id_n_etat

    def changer_image(self):
        self.im_aff = self.images[self.etat]#selection de l'image associée à l'état du prof



police = pygame.font.Font('font/FFFFORWA.TTF', 13) #police d'écriture de la fenetre graphique
police_gros = pygame.font.Font('font/FFFFORWA.TTF', 30) #police d'écriture pour bonne/mauvaise rep
police_trans = pygame.font.Font('font/FFFFORWA.TTF', 20)


#fonctions


def SeparerSTR(phrase,endroit):
    '''fonction qui sépare un str au bout d'un certain nombre de caractères'''
    while phrase[endroit] != ' ':
        endroit -= 1
    b = phrase[:endroit]
    c = phrase[endroit:]
    d = b + ';' + c
    p_new = d.split(';')
    return p_new


def Afficher(phrase,surf,taille):
    '''fonction qui affiche un texte sur une surface en sautant une ligne au bout d'un certain nombre de caractères'''
    if len(phrase) > taille:
        a = SeparerSTR(phrase,taille) #phrase séparée en deux
        s = 0
        for elt in a:
            elt = police.render(elt,True,(1,0,0))
            surf.blit(elt,(surf.get_width()//2-elt.get_width()//2,surf.get_height()//2-elt.get_height()//2+s))
            s += 20
    else:
        texte = police.render(phrase,True,(1,0,0))
        surf.blit(texte,(surf.get_width()//2-texte.get_width()//2,surf.get_height()//2-texte.get_height()//2))



def AfficherQuestion(q,surfQ,surfsR,couleur):
    '''fonction qui affiche une question et ses réponses sur des surfaces données
    
        q: type question,
        surfQ: type display, surface d'affichage de la question
        surfsR: type list, les des surfaces d'affichage des réponses
        couleur: type tuple, un tuple RGB de la couleur'''
    num = 1 #numéro de la réponse


    
    if len(q.nom) > 35:
        qText_temp = SeparerSTR(q.nom,35) 
        s = 0 #variable pour afficher les lignes les unes sous les autres
        for elt in qText_temp:
            elt = police.render(elt, True,couleur)
            surfQ.blit(elt,((surfQ.get_width()/2)-(elt.get_width()/2),(surfQ.get_height()/2)-(elt.get_height()/2)+s))
            s += 20
    else:
        qText = police.render(q.nom, True, couleur) #texte de la question
        surfQ.blit(qText,((surfQ.get_width()/2)-(qText.get_width()/2),(surfQ.get_height()/2)-(qText.get_height()/2)))


    for i in range(4): #chaque réponse est affichée séparément
        surf = surfsR[i]
        if len(q.réponses[i].nom) > 35:
            rText_temp = SeparerSTR(q.réponses[i].nom,35) 
            p = -5 #variable pour afficher les lignes les unes sous les autres
            for elt in rText_temp:
                if elt == rText_temp[0]:
                    elt = police.render("{}. {}".format(num,elt), True, (1,0,0))
                else:
                    elt = police.render(elt, True, (1,0,0))
                surf.blit(elt,((78,(surf.get_height()/2)-(elt.get_height()/2)+p)))
                p += 20
        else:
            rText = police.render("{}. {}".format(num,q.réponses[i].nom), True, (1,0,0)) #texte de la réponse
            if i > 0:  
                surf.blit(rText,((78,(surf.get_height()/2)-(rText.get_height()/2-8))))#on affiche la réponse un tout petit peu plus haut si c'est pas la premiere
            else:
                surf.blit(rText,((78,(surf.get_height()/2)-(rText.get_height()/2))))#on affiche la réponse   
        num += 1                       
        
    


def ResultatQuestion(res,res_surf):
    """fonction qui affiche bonne ou mauvaise réponse en fonction de la réponse du joueur"""
    if res == 'y':
        restext = police_gros.render('Bonne Réponse !', True, (107,142,35))
    elif res == 'n':
        restext = police_gros.render('Mauvaise Réponse !', True, (139,0,0))
    res_surf.blit(restext,((res_surf.get_width()/2)-(restext.get_width()/2),(res_surf.get_height()/2)-(restext.get_height()/2)))


def ResetSurf(list_surf):
    '''
        fontion qui réinitialise les surfaces entrées en paramètre (par exemple pour supprimer du texte)
        list_surf: type list, liste des surfaces à reset
    '''
    for surf in list_surf:
        surf.fill((0,0,0))
        surf = pygame.Surface((surf.get_width(),surf.get_height()))

   
def credits(screen,i,nom):
    '''fonction qui affiche les crédits du jeu et les fait remonter grâce au fait que i soit décroissant'''
    surf = pygame.Surface((1000,2060))
    saut = 80 #saut entre chaque ligne
    L = []
    texte = ["Merci d'avoir joué à L'épopée au lycée Marso !",
             "Ce jeu vous a été présenté par le groupe 3",
             "Bilal OUYOUSSEF, Arthur PAUL, Martin VAILLOT",
             "Graphisme: Bilal OUYOUSSEF",
             "Sélection des musiques: Arthur PAUL",
             "Classe Question/Réponses: Bilal OUYOUSSEF",         
             "Classe Joueur: Arthur PAUL",
             "Classe Professeurs: Martin VAILLOT",
             "Hotel ? Trivago",
             "Implémentation des questions: Bilal OUYOUSSEF, Arthur PAUL",
             "Implémentation des professeurs: Martin VAILLOT",
             "Interface graphique: Martin VAILLOT",
             "Professeur de mathématiques: Clément DUREUIL ",
             "Un grand merci à lui",
             "Musiques:",
             "Menu : Mario Kart Wii Pause Theme - Nintendo",
             "Couloirs:",
             "Star Road Super Mario World, Starman remix  - Nintendo;David Bowie",
             "          Wii Shop Channel - Nintendo",
             "          Mario Strikers Charged Pause Menu - Nintendo",
             "Combats: Mazeppa - Frank Liszt",
             "         Orage - Frank Liszt",
             "Transition : Buddy Holly but just the riff- Bubbsterr",
             "Crédits : Nocturne op.9 No.2 - Frédéric Chopin",
            "Merci beaucoup d'avoir joué {}!".format(nom)
             ]
    for elt in texte:
        a = police_trans.render(elt,True,(255,255,255))
        L.append(a)
    for elt in L:
        surf.blit(elt,(500-elt.get_width()//2,saut))
        saut += 80
    screen.blit(surf,(0,600+i))


def rond_def(screen,rayon):
    """fonction qui créé le rond de la défaite qui remplit l'écran petit à petit"""
    pygame.draw.circle(screen,(0,0,0),(500,300),750,rayon)
