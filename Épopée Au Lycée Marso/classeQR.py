from random import randint,choice

#implémentation des questions

class Question:
    def __init__(self,nom,réponses):
        self.nom = nom                  # intitulé de la question (str)
        self.réponses = réponses        # liste de 4 objets de classe Réponse

    def répondre(self,rep):
        """
            méthode qui permet de vérifier si la
            réponse donnée est bonne ou fausse
        """
        if rep > 3:
            pass
        else:
            return self.réponses[rep].bonne
        
         


class Reponse :
    def __init__(self,nom,bonne):
        self.nom = nom                      # intitulé de la Reponse
        self.bonne = bonne                  # booléen qui définit si une Reponse est bonne ou fausse
        




def QuestionRandom(): 
    '''renvoie une question aléatoire parmis une matière aléatoire'''
    l = ['MATHS','NSI','SPORT','SVT','HISTOIRE',"MUSIQUE"]
    a = choice(l)
    return choice(liste_des_matieres[a])
    
def QuestionMat(matiere):
    '''renvoie une question aléatoire parmis une matière donnée'''
    a = choice(liste_des_matieres[matiere])
    return a


def CreerQ(tq,tr,id_rep):
    """fonction qui permet de créer une fontion plus facilement (créée trop tard malheureusement)"""
    r = [(tr[0],0),(tr[1],1),(tr[2],2),(tr[3],3)]
    L = []
    for elt in r:
        if elt[1] in id_rep:
            L.append(Reponse(elt[0],True))
        else:
            L.append(Reponse(elt[0],False))
    return Question(tq,L)


### NSI ###
#réponses
r1 = Reponse("7", False)
r2 = Reponse("9", False)
r3 = Reponse("33", False)
r4 = Reponse("11", True)
r5 = Reponse("10", True)
r6 = Reponse("5", False)
r7 = Reponse("0", False)
r8 = Reponse("A", False)
r9 = Reponse("1000", True)
r10 = Reponse("1024", False)
r11 = Reponse("1048", False)
r12 = Reponse("2048", False)
r13 = Reponse("1.000.000", True)
r14 = Reponse("1.048.576.000", False)
r15 = Reponse("1.073.741.824", False)
r16 = Reponse("1.024.024.024", False)
r17 = Reponse("AZERTY", True)
r18 = Reponse("QWERTY", False)
r19 = Reponse("Type 12", False)
r20 = Reponse("Type 02", False)
r21 = Reponse("Une mise à jour", True)
r22 = Reponse("Le chargement d’un fichier informatique vers un autre ordinateur", False)
r23 = Reponse("Un diplôme d’informaticien", False)
r24 = Reponse("Un système d’exploitation", False)
r25 = Reponse("Le fichier autoexec.bat", False)
r26 = Reponse("Le fichier win.ini", True)
r27 = Reponse("La base de registre", False)
r28 = Reponse("La base de composants de windows", False)
r29 = Reponse("d’images", True)
r30 = Reponse("de base de données", False)
r31 = Reponse("de Tervminal Informatique de type FF", False)
r32 = Reponse("de protocole internet", False)
r33 = Reponse("le client", True)
r34 = Reponse("le prestataire", False)
r35 = Reponse("la société chargée de l’accompagnement", False)
r36 = Reponse("les utilisateurs", False)
r37 = Reponse("La partie données de la méthode MERISE", False)
r38 = Reponse("un standard de communication", False)
r39 = Reponse("un type de port", False)
r40 = Reponse("un langage de modélisation", True)

#questions
q10 = Question("Le nombre binaire 1011 vaut en décimal :", [r1, r2, r3, r4])
q11 = Question("Le nombre qui suit le nombre 4 en base 5 est :", [r5, r6, r7, r8])
q12 = Question("Combien y a t-il d’octets dans un ko (kilo-octet) ?", [r9, r10, r11, r12])
q13 = Question("Combien de bytes y-a-t-il dans un Giga-Octet ?",  [r13, r14, r15, r16])
q14 = Question("Un clavier français est un clavier ?", [r17, r18, r19, r20])
q15 = Question("Qu’est-ce qu’un upgrade ?", [r21, r22, r23, r24])
q16 = Question("Sous Windows XP, la configuration est enregistré dans ?", [r25, r26, r27, r28])
q17 = Question("TIFF est un format:", [r29, r30, r31, r32])
q18 = Question("En gestion de projet qui appelle-t-on le maître d’ouvrage ?", [r33, r34, r35, r36])
q19 = Question("UML est :", [r37, r38, r39, r40])
q110 = CreerQ("Le protocole RIP privilégie quel paramètre pour relier deux routeurs ?",["Le débit","La distance","La valeur numérique de l'adresse IP","Le nombre de routeurs sur le chemin"],[3])
q111 = CreerQ("Une fonction récursive est une fonction qui:",["a une condition d'arrêt","s'appelle elle même","renvoie une liste triée","existe uniquement en python"],[1])
q112 = CreerQ("La clé primaire d'une table de données doit être:",["un nombre entier","une clé d'une autre table","unique à chaque entrée","le premier attribut de la table"],[2])
q113 = CreerQ("L'algorithme de Dijkstra :",["est imprononçable","sert à déterminer la compléxité d'un algorithme","sert à déterminer le plus court chemin dans un graphe","se développe sous forme de pyramide"],[0,2])
q114 = CreerQ("Avec le protocole OSPF, le coût est calculé par:",["la bande passante + le debit de la liaison","la bande passante / le debit de la liaison","la bande passante * le debit de la liaison","la bande passante - le debit de la liaison"],[1])
q115 = CreerQ("Dans un ABR, quel parcours utiliser pour récupérer les valeurs des feuilles dans l'ordre croissant",["Le parcours en largeur","le parcours postfixe","le parcours infixe","le parcours préfixe"],[2])
q116 = CreerQ("Si a vaut False et b vaut True, que vaut l’expression booléenne NOT(a AND b) ?",["0","False","True","None"],[2])
q117 = CreerQ("Quelle est l'expression qui a pour valeur la liste [1, 4, 9, 16, 25, 36]:",["{n**n for n in range(1,7)}","[n**n for n in range(1,7)]","[n**n for n in range(6)]","{n**n for n in range(6)}"],[1])
q118 = CreerQ("Parmi les quatre nombres suivants lequel est le seul à pouvoir être représenté de façon exacte en machine ?",["7.25","4.2","5.24","3.1"],[0])
q119 = CreerQ("Quel est le nombre minimum de bits pour encoder les 7 couleurs de l’arc en ciel ?",["2","7","3","8"],[2])
q120 = CreerQ("Lequel de ces périphériques n'est pas un périphérique d'entrée ?",["l’écran","la souris","le clavier","les enceintes"],[3])
q121 = CreerQ("Sous Unix, quelle commande permet de créer un nouveau répertoire?",["mkdir","echo","ls","rm"],[0])
q122 = CreerQ("Quelle est la profondeur d'une image encodée en nuances de gris ?",["2","8","16","24"],[2])
q123 = CreerQ("Combien y a t'il de couches dans le protocole TCp-IP?",["7","3","6","1"],[0])
q124 = CreerQ("Quelle est la dernière couche du protocole TCP-IP ?",["Reseau","Transport","Application","Physique"],[3])
### MATHS ###

#réponses
r41 = Reponse("v’u+u’v", True)
r42 = Reponse("u’v+v’u", True)
r43 = Reponse("uv-vu", False)
r44 = Reponse("afrique", True)
r45 = Reponse("2", False)
r46 = Reponse("16", True)
r47 = Reponse("8", False)
r48 = Reponse("la réponse d", False)
r49 = Reponse("Comprise entre -1 et 1", True)
r50 = Reponse("Comprise entre 0 et 1 (aussi haut que ma moyenne", False)
r51 = Reponse("Une fonction provenant de Marseille, la capitale de Paris.", False)
r52 = Reponse("strictement croissante", False)
r53 = Reponse("(a+b)^2 = a^2 + 2ab + b^2", False)
r54 = Reponse("AB^2 = AC^2 + BC^2", True)
r55 = Reponse("AB = AC + AD", False)
r56 = Reponse("AB^2 = AC + AD", False)
r57 = Reponse("d’une addition", False)
r58 = Reponse("d’une soustraction", False)
r59 = Reponse("d’une multiplication", True)
r60 = Reponse("d’une division", False)
r61 = Reponse("160 deg", False)
r62 = Reponse("180 deg", True)
r63 = Reponse("190 deg", False)
r64 = Reponse("2 (ça doit être la bonne réponse)", False)          
r65 = Reponse("160 deg", False)
r66 = Reponse("90cm", False)
r67 = Reponse("j’aime beaucoup les tartes au citron meringué", False)
r68 = Reponse("360 deg", True)
r69 = Reponse("1, je ne réfléchis pas", False)
r70 = Reponse("1.5, je suis super intelligent", False)
r71 = Reponse("0.5, je suis le couteau le plus aiguisé du tiroir", True)
r72 = Reponse("je corromp le prof avec une tarte au citron meringuée", True)
r73 = Reponse("elle est ou la Question?", False)
r74 = Reponse("dans le doute je vais répondre 2", False)
r75 = Reponse("La Question me met en effet en difficulté", True)
r76 = Reponse("c’est de la triche je vais rater ce test", True)
r77 = Reponse("17 demi-vies de carbone 14", False)
r78 = Reponse("je ne peux pas lire l’énoncé", True)
r79 = Reponse("il faudrait revoir le code de ce jeu", True)
r80 = Reponse("quelques instants", False)

#questions
q20 = Question("Quelle est la dérivée de la fonction u*v?", [r41, r42, r43, r44])
q21 = Question("4^2?", [r45, r46, r47, r48])
q22 = Question("La fonction sinus est:", [r49, r50, r51, r52])
q23 = Question("Quel est le théorème de Pythagore?", [r53, r54, r55, r56])
q24 = Question("Le produit est le résultat:", [r57, r58, r59, r60])
q25 = Question("La somme des angles d’un triangle est:", [r61, r62, r63, r64])
q26 = Question("Combien mesure une tarte au citron meringuée ronde?", [r65, r66, r67, r68])
q27 = Question("1*0.5 est égal à:", [r69, r70, r71, r72])
q28 = Question("Une Question qui vous mettra en difficulté:", [r73, r74, r75, r76])
q29 = Question("Problème: Un train de type Locomotive française électrique Alstom Prima II à une alimentation thermique de 1,5 kV continu, 25 kV et 50 Hz ; 4200 kW. Combien de temps mettra une baignoire de 1578 litres à se vider d’essence sachant qu’elle est trouée d’un trou de 120cm de diamètre causé par l’énergie thermique que dégage la Locomotive française électrique Alstom Prima II ?", [r77, r78, r79, r80])
q210 = CreerQ("0^0=",["0","1","undefined","4/3"],[2])
q211 = CreerQ("Une fonction impaire:",["n'a que des solutions impaires","admet f(x)=f(-x)","admet f(x) = -f(x)","est toujours concave"],[2])
q212 = CreerQ('Dans un champ, il y a des coqs et des chevaux. On compte 20 pattes. Combien y a-t-il de coqs au maximum ?',["10","20","8","13"],[2])
q213 = CreerQ('Comment appelle-t-on un triangle qui a un angle droit ?',["Triangle linéaire","Triangle rectangle","Triangle orthogonal","Triangle raciste"],[1])
q214 = CreerQ('Quel était le nom du système de mesure avant que nous passions au système métrique ?',["système impérial","système royal","système communiste","system error"],[0])
q215 = CreerQ('Qui a inventé le calcul infinitésimal indépendamment de Newton et créé le système binaire ?',["Gottfried Leibniz","Hermann Grassmann","Johannes Kepler","Isaac Newton"],[0])
q216 = CreerQ('Quel mathématicien est à l’origine du théorème de Gauss sur la divisibilité ?',["Leonhart Euler","Bernhart Riemann","Carl Friedrich Gauss","Isaac Newton"],[2])
q217 = CreerQ('La série alternée des harmoniques:',["diverge","je sais pas chef","converge vers 2**(1/2)","converge vers ln(2)"],[2,3])
q218 = CreerQ('Quel est le nom de la fonction la plus célèbre de Bernhart Riemann?',["Eta","Sigma","Gamma","Zeta"],[3])
q219 = CreerQ('(a+b)**2 =?',["a**2 + b**2 ","(ab)**2","a**2 + 2ab + b**2","a**2 + ab + b**2"],[2])
q220 = CreerQ('La valeur de l’intégrale de exp(-x**2) sur son domaine de définition vaut:',["3","je passe","pi**(1/2)","pi"],[1,2])
q221 = CreerQ("Quelle est la dérivée de la fonction exp(-x**2) ?",["-2exp(-x**2)","-2xexp(x)","-2xexp(-x**2)","-2exp(-x**2)"],[2])
q222 = CreerQ("9/3(12/4)",["1","6","3","9"],[3])
q223 = CreerQ("Quelle est la valeur de cos(pi/4) ?",["2**(1/2)/2","3**(1/2)/2","rond","1"],[0])
q224 = CreerQ("Quel est le nom de l'oeuvre qui définit les fondements des mathémaiques ?",["Axiomes","Principia Mathematica","Elements d'algèbres","Introduction à l’analyse infinitésimale"],[1])

### SPORT ###

#réponses
r301 = Reponse("42.195 kilomètres", True) 
r302 = Reponse("43.195 kilomètres", False)
r303 = Reponse("41.195 kilomètres", False)
r304 = Reponse("2.195 kilomètres", False)
r311 = Reponse("5 joueurs", False)
r312 = Reponse("9 joueurs", True)
r313 = Reponse("7 joueurs", False)
r314 = Reponse("3 joueurs", False)
r321 = Reponse("La France", False)
r322 = Reponse("Le Brésil", False)
r323 = Reponse("L’Allemagne", True)
r324 = Reponse("L’Argentine", False)
r331 = Reponse("Le basketball", False)
r332 = Reponse("Le rugby", False)
r333 = Reponse("Le handball", False)
r334 = Reponse("Le football", True)
r341 = Reponse("La crosse et le football américain", False)
r342 = Reponse("La crosse et le hockey sur glace", True)
r343 = Reponse("Le hockey sur glace et le basketball", False)
r344 = Reponse("Le cricket et la bataille de boule de neige", False)
r351 = Reponse("Les Knicks", True)
r352 = Reponse("Les Lakers", False)
r353 = Reponse("Les Boston Celtics", False)
r354 = Reponse("Les Chicago Bulls", False)
r361 = Reponse("La boxe anglaise", False)
r362 = Reponse("Le karaté", False)
r363 = Reponse("Le rugby", False)
r364 = Reponse("Le football américain", True)
r371 = Reponse("La plongée sous-marine", True)
r372 = Reponse("La plongée sur-marine", False)
r373 = Reponse("Le waterpolo", False)
r374 = Reponse("Le 50m en crawl", False)
r381 = Reponse("Lebron James", True)
r382 = Reponse("La chaise", False)
r383 = Reponse("Les pompes", True)
r384 = Reponse("Les squats", False)
r391 = Reponse("Jeet kune do", False)
r392 = Reponse("Boxing", False)
r393 = Reponse("Escrime", False)
r394 = Reponse("Wushu", True)

#questions
q30 = Question("Quelle est la longueur d'un un marathon ?",[r301,r302,r303,r304])
q31 = Question("Combien y a-t-il de joueurs dans une équipe de baseball ?",[r311,r312,r313,r314])
q32 = Question("Quel pays a remporté la Coupe du monde de foot en 2014 ?",[r321,r322,r323,r324])
q33 = Question("Quel sport est considéré comme le  roi des sports  ?",[r331,r332,r333,r334])
q34 = Question("Quels sont les deux sports nationaux du Canada ?",[r341,r342,r343,r344])
q35 = Question("Quelle équipe a remporté le premier match NBA en 1946 ?",[r351,r352,r353,r354])
q36 = Question("Dans quel sport auriez-vous un touchdown ?",[r361,r362,r363,r364])
q37 = Question("Quel est le sport nautique le plus ancien jamais enregistré ?",[r371,r372,r373,r374])
q38 = Question("Quel est le meilleur exercice pour muscler ses bras?",[r381,r382,r383,r384])
q39 = Question("Quel sport n'a pas été pratiqué par Bruce Lee ?",[r391,r392,r393,r394])
q310 = CreerQ("Combien y avait il de pilotes de F1 lors de la saison 2022 ?",["18","24","20","21"],[2])
q311 = CreerQ("Où ont eu lieu les JO de 1936 ?",["Londres","Berlin","Rome","Madrid"],[1])
q312 = CreerQ("Lors du Tour de France, que signifie maillot blanc à pois rouges ?",["Le meilleur jeune coureur","le meilleur sprinteur","le premier de la compétition","le meilleur grimpeur"],[3])
q313 = CreerQ("Le handball est un sport d'origine:",["Suédoise","Danoise","Portugais","Allemand"],[3])
q314 = CreerQ("Qui a gagné la coupe du monde de rugby à 15 en 2007 ?",["Afrique du Sud","Nouvelle Zélande","France","Iles Fidji"],[0])
q315 = CreerQ("Dans quel sport collectif tire-t-on des lancers francs ?",["Handball","Volleyball","Basketball","Badminiton"],[2])
q316 = CreerQ("Quel pilote français de Formule 1 est décédé des suites d’un accident survenu au Grand Prix du Japon 2014 ?",["Sébastien Bourdais","Jules Bianchi","Pierre Gasly","Romain Grosjean"],[1])
q317 = CreerQ("Quel est le sport le plus populaire en Inde ?",["Demandez à Arthur Paul","Le kabaddi","Le football","Le cricket"],[0,3])
q318 = CreerQ("Quel pays est le champion du monde en titre de lancer de nains ?",["Inde","Angleterre","Corée Du Nord","Allemagne"],[1])
q319 = CreerQ("Qui est Lebron James ?",["un footballeur","un basketteur","le joueur préféré de Mbappé","Lebron James"],[1,2,3])
q320 = CreerQ("Dans le sport de la Pétanque, si le cochonnet est à une distance élévée, il faut :",["Pointer","Piquer","Porter Plainte","Prendre un ricard"],[0,3])
q321 = CreerQ("De combien de joueur sont constituées les équipes d'Ultimate ?",["5","4","6","3"],[0])
q322 = CreerQ("Quand a été joué le premier combat de ChessBoxing ?",["1845","19970","1974","2003"],[3])
q323 = CreerQ("Au judo, quel est le grade le plus élevé parmi ces ceinturesÂ ?",["Bleu","Orange","Jaune","Verte"], [0])
q324 = CreerQ("Quel est la plus haute ceinture parmi celles-ci au karaté ?",["Marron","Verte","Blanche","Bleue"], [0])
### SVT ###


#réponses
r401 = Reponse("Le liquide dans une cellule",True)
r402 = Reponse("Un pokemon",False)
r403 = Reponse("Un insecte",False)
r404 = Reponse("Une partie d'une graine",False)
r411 = Reponse("La présence d'une bouche",False)
r412 = Reponse("La cellule",True)
r413 = Reponse("La présence d'os",False)
r414 = Reponse("La vie",False)
r421 = Reponse("46 chromosomes",True)
r422 = Reponse("48 chromosomes",False)
r423 = Reponse("23 paires de chromosomes + 1",False)
r424 = Reponse("22 paire de chromosomes",False)
r431 = Reponse("D'engrais",False)
r432 = Reponse("Uniquement d'eau",False)
r433 = Reponse("De sel minéraux et d'eau",True)
r434 = Reponse("De coca",False)
r441 = Reponse("Le panda",False)
r442 = Reponse("L'ornithorynque",True)
r443 = Reponse("Le capybara",False)
r444 = Reponse("Le damon medius",False)
r451 = Reponse("Bouche, oesophage, estomac, intestin grêle et gros intestin",True)
r452 = Reponse("Pancréas, foie, côlon, appendice",False)
r453 = Reponse("Y a que 4 réponses à la réponse 2",False)
r454 = Reponse("Pharynx, larynx, trachée, bronche, bronchioles et alvéoles",False)
r461 = Reponse("Le diaphragme",False)
r462 = Reponse("L'endocarde",True)
r463 = Reponse("Le péricarde",False)
r464 = Reponse("La MasterCard",False)
r471 = Reponse("Le système nerveux",True)
r472 = Reponse("Les organes de sens",False)
r473 = Reponse("L'appareil circulatoire",False)
r474 = Reponse("Le système d'exploitation",False)
r481 = Reponse("Inerte",False)
r482 = Reponse("Mort",False)
r483 = Reponse("Endormi",False)
r484 = Reponse("Vivant",True)
r491 = Reponse("23 chromosomes sexuels",False)
r492 = Reponse("23 chromosomes",True)
r493 = Reponse("6 chromosomes sexuels",False)
r494 = Reponse("6 chromosomes",False)

#questions
q40 = Question("Le cytoplasme c'est :",[r401,r402,r403,r404])
q41 = Question("Le caractère commun à tous les êtres vivants est :",[r411,r412,r413,r414])
q42 = Question("L'Homme possède :",[r421,r422,r423,r424])
q43 = Question("Les plantes se nourrissent :",[r431,r432,r433,r434])
q44 = Question("Quel animal vient d'Australie ?",[r441,r442,r443,r444])
q45 = Question("Quels sont les cinq organes qui constituent l'appareil digestif ?",[r451,r452,r453,r454])
q46 = Question("L'intérieur du coeur est tapissé par une membrane :",[r461,r462,r463,r464])
q47 = Question("Les fonctions de relation sont assurées par :",[r471,r472,r473,r474])
q48 = Question("L'os est un tissu :",[r481,r482,r483,r484])
q49 = Question("Les cellules sexuelles contiennent :",[r491,r492,r493,r494])
q410 = CreerQ('Le système nerveux comprend :',['Le diaphragme','L’estomac','Le cerveau','Les pieds'], [2])
q411 = CreerQ('Les neurones :',['Sont plusieurs milliards dans le cerveau','Ne sont pas reliés entre eux','Sont aux nombres de 2 chez Arthur Paul','Sont permanents'], [0])
q412 = CreerQ('Un écosystème est constitué :',['D’êtres vivants et d’Arthur Paul','Des végétaux et des végétariens','D’animaux et de smartphones','Des végétaux et d’animaux'], [3])
q413 = CreerQ('Une des causes de la destruction de la biodiversité est :',['La surpoire','La surpêche','La surbanane','Le surabricot'], [1])
q414 = CreerQ('Comment s’étudie la météorologie ?',['En faisant des relevés fréquents','En regardant le ciel','En respirant',"En regardant à l'horizon"], [0])
q415 = CreerQ('Qu’est-ce qui caractérise l’activité interne de la Terre ?',['Les séismes et les volcans','Les séismes et les inondations','Les inondations et les volcans','Les tornades'], [0])
q416 = CreerQ('La biodiversité :',['est un écosystème','influence la chaîne alimentaire',"est une catégorie d'aliments",'est un truc'], [1])
q417 = CreerQ("La pollution de l'environnement",["est due à l'activité animale","n'a aucune conséquences","est due à l'activité végétale","est due à l'activité humaine"], [3])
q418 = CreerQ('Les végétaux sont :',['les derniers maillons de la chaîne alimentaire','les deuxièmes maillons de la chaîne alimentaire','pas dans la chaîne alimentaire','les premiers maillons de la chaîne alimentaire'], [3])
q419 = CreerQ('Quel élément permet-il les échanges gazeux entre la plante et l’atmosphère ?',['La fleur','La racine','Le stomate','La tige'], [2])
q420 = CreerQ("Lequel de ces animaux est un mammifère ?",["Le pigeon","La tarentule","Le chat","Le crocodile"], [2])
q421 = CreerQ("L'ornithorynque est un :",["Un félin","Un mammifère","Un reptile","Un oiseau"], [1,2,3])
q422 = CreerQ("Qu'est ce qu'un animal qui pond des oeufs ?",["Un vivipare","Un poisson","Un ovipare","Un oiseau"], [2])
q423 = CreerQ("La baleine est :",["Un félin","Un mammifère","Un oiseau","Un ovipare"], [1])
q424 = CreerQ("Combien y a-t-il d'espÃ¨ces de requins ?",["2","1500","300","500"], [3])
### HISTOIRE ###


#réponses
r501 = Reponse("10 millions d’années av. J.-C.", False)
r502 = Reponse("5 millions d’années av. J.-C.", False)
r503 = Reponse("11 septembre 2001", False)
r504 = Reponse("3 millions d’années av. J.-C.", True)
r511 = Reponse("à l’invention de l’écriture", False)
r512 = Reponse("à l’apparition de l’homme", True)
r513 = Reponse("à l’âge de fer", False)
r514 = Reponse("à la révélation du Coran", False)        
r521 = Reponse("1500 av. J.-C.", False)
r522 = Reponse("Capitale du Botswana", False)
r523 = Reponse("300 apr. J.-C.", False)
r524 = Reponse("700 av. J.-C.", True)
r531 = Reponse("En embrayant", False)
r532 = Reponse("En 10 000 av. J.-C.", False)
r533 = Reponse("En 3 000 av. J.-C.", True)
r534 = Reponse("En 476", False)
r541 = Reponse("Osiris", False)
r542 = Reponse("Rê", True)
r543 = Reponse("Anubis", False)
r544 = Reponse("Horus", False)
r551 = Reponse("Marseille", False)
r552 = Reponse("Tunis", False)
r553 = Reponse("Bogota", False)
r554 = Reponse("Ajaccio", True)
r561 = Reponse("le 2 décembre 1804", True)
r562 = Reponse("le 24 décembre 1804",False)
r563 = Reponse("le 8 décembre 2006", False)
r564 = Reponse("le 24 décembre 1805", False)
r571 = Reponse("Héphaïstos", False)
r572 = Reponse("Hadès", True)
r573 = Reponse("Hermès", False)
r574 = Reponse("Héra", False)
r581 = Reponse("Ouranos", False)
r582 = Reponse("Héphaïstos", False)
r583 = Reponse("M. Dureuil", False)
r584 = Reponse("Kratos", True)
r591 = Reponse("Barack Obama", False)
r592 = Reponse("John Fitzgerald Kennedy", True)
r593 = Reponse("George W. Bush", False)
r594 = Reponse("Joe Biden", False)

#questions
q50 = Question("On situe l'apparition de l'homme à :",[r501,r502,r503,r504])
q51 = Question("La préhistoire débute :",[r511,r512,r513,r514])
q52 = Question("On situe l'âge de fer à :",[r521,r522,r523,r524])
q53 = Question("L'Antiquité démarre :",[r531,r532,r533,r534])
q54 = Question("Qui est le dieu du soleil de la mythologie égyptienne :",[r541,r542,r543,r544])
q55 = Question("Dans quelle ville est né Napoléon Bonaparte",[r551,r552,r553,r554])
q56 = Question("Quelle est la date du couronnement de Napoléon :",[r561,r562,r563,r564])
q57 = Question("Lequel de ces dieux ne siège pas au mont Olympe :",[r571,r572,r573,r574])
q58 = Question("Qui est le dieu de la puissance, du pouvoir, de la vigueur et/ou de la solidité :",[r581,r582,r583,r584])
q59 = Question("Quel président des États-Unis d’Amérique a été élu le plus jeune :",[r591,r592,r593,r594])
q510 = CreerQ("Vercingétorix est vaincu à Alésia en -52 par:",["Charlemagne","Les Vikings","Jules César","Dark Vador"],[2])
q511 = CreerQ("Clovis Ier est le fondateur de la dynastie :",['carolingienne',"mérovingienne","capétienne","bourbonne"],[1])
q512 = CreerQ("Charlemagne signifie :",["Charles le Prompt","Charles le Grand","Charles le Magnifique","Charles le Manche"],[1])
q513 = CreerQ("Louis le Pieux était en réalité:",["Louis X", "Louis LI","Louis XI","Louis IX"],[1])
q514 = CreerQ("Combien y a t-il eu de croisades ?",["12","14","9","11"],[2])
q515 = CreerQ("Quelles lois ont rendu l’enseignement laïque en France ?",["les lois Ferry","Les lois Bonapartes","les lois laïques","les lois communardes"],[0])
q516 = CreerQ("Quand l'esclavage a t-il été abolit en France ?",["1802","1874","1848","1948"],[2])
q517 = CreerQ("Quel était le nom de code du débarquement en Normandie ?",["Overingé","Gameover","Ovehead","Overlord"],[3])
q518 = CreerQ("Qu'est il arrivé au parachutiste américain John Steele lors du Débarquement ?",["Il est resté accroché au clocher d'une église","il est tombé dans un puit","il a atterit sur un bataillon allemand","il a été le premier soldat tué"],[0])
q519 = CreerQ('Quel commandant français est considéré comme "le héros de Verdun" ?',["Robert Nivelle","Ferdinand Foch","Philippe Pétain","Joseph Gallieni"],[2])
q520 = CreerQ("Quelle célèbre phrase a prononcé César en franchissant le fleuve Rubicon ?",["Flucuat nec mergitur","Ave Caesar, morituri te salutant","Veni Vidi Vici","Alea jacta est"],[3])
q521 = CreerQ("Quel est le nom de code désignant l’invasion de l’URSS par la Wehrmacht ?",["Overlord","Barbarossa","Gelb","Stalingrad"],[1])
q522 = CreerQ('Qu’étaient les "Einsatzgruppen" ',["Des troupes de police militarisées","Des troupes d'assaut","Des groupes de sabotage","Des groupes de membres étrangers servant la Gestapo"],[0])
q523 = CreerQ('Quelle est la date de la signature des actes de capitulation du Japon ?',["2 septembre 1944","6 août 1945","6 août 1944","2 septembre 1945"],[3]) 
q524 = CreerQ("Louis XV est le ___ de Louis XVI",["père","grand-père","arrière grabd-père","trisaïeul"],[1])  
    ### MUSIQUE ###

#réponses
r601 = Reponse("Or noir",True)
r602 = Reponse("Or blanc",False)
r603 = Reponse("Argent blanc",False)
r604 = Reponse("Argent noir",False)           
r611 = Reponse("Le romantisme",False)
r612 = Reponse("L’impressionnisme",True)
r613 = Reponse("le kaarisme",False)
r614 = Reponse("le franquisme",False)
r621 = Reponse("Aiguë",True)
r622 = Reponse("Grave",False)
r623 = Reponse("Son crâne luisant",False)
r624 = Reponse("De ton moyen",False)
r631 = Reponse("C’est Joe Biden",False)
r632 = Reponse("C’est les condés",False)
r633 = Reponse("C’est la Gestapo",True)
r634 = Reponse("C’est Kaaris",False)
r641 = Reponse("Il faudrait payer ses impôts",False)
r642 = Reponse("Il faudrait faire de l’évasion fiscale",False)
r643 = Reponse("Il faudrait 5 ouvriers",False)
r644 = Reponse("Il faudrait tout oublier",True)
r651 = Reponse("Le Ré",True)
r652 = Reponse("Le Sol",False)
r653 = Reponse("Le Fa",False)
r654 = Reponse("Le Si",False)
r661 = Reponse("Ré",False)
r662 = Reponse("Mii",False)
r663 = Reponse("Fa",True)
r664 = Reponse("Do",False)
r671 = Reponse("Oui",True)
r672 = Reponse("Je me sens forcé de répondre oui",True)
r673 = Reponse("Je pense que oui",True)
r674 = Reponse("Bien entendu",True)
r681 = Reponse("Inutile",True)
r682 = Reponse("Un couvert de table",False)
r683 = Reponse("Une paille à boire",False)
r684 = Reponse("Un instrument à vent",True)
r691 = Reponse("Il est musclé et séduisant",True)
r692 = Reponse("Il a beaucoup de respect pour les femmes",True)
r693 = Reponse("Il est devant moi",False)
r694 = Reponse("Il respire la joie de vivre",True)

#questions
q60 = Question("Quel est le célèbre album de Kaaris ?",[r601,r602,r603,r604])
q61 = Question("Quelle est le mouvement principal du pianiste Franz Lizst ?",[r611,r612,r613,r614])
q62 = Question("Comment est le type de voix Soprano ?",[r621,r622,r623,r624])
q63 = Question("On casse la porte... (Maître Gims).",[r631,r632,r633,r634])
q64 = Question("Mais pour y croire... (Angèle)",[r641,r642,r643,r644])
q65 = Question("Quelle note de musique suis le Do ?",[r651,r652,r653,r654])
q66 = Question("Il y a en musique la clé de sol et la clé de...",[r661,r662,r663,r664])
q67 = Question("Kaaris est-t-il le meilleur artiste à ce jour ?",[r671,r672,r673,r674])
q68 = Question("La flûte est :",[r681,r682,r683,r684])
q69 = Question("Kaaris se démarque des autres dans son domaine car :",[r691,r692,r693,r694])
q610 = CreerQ("Combien de membres étaient dans le groupe des Beatles au début?",["5","4","6","3"],[1])
q611 = CreerQ("Quel Artiste/Groupe est l’auteur du titre 'Smoke on the Water’?",["Deep Purple","Inoxtag","Kaaris","The Beatles"],[0])
q612 = CreerQ("Qui est auteur de la chanson 'Mili Mili ?",["Michou","Mr Dureuil","Jeanfils","Inoxtag"],[3])
q613 = CreerQ("Quel était le genre de la musique performée par le groupe Nirvana ?",["le type acier","le rock","la Kpop (squid games)","le blues"],[1])
q614 = CreerQ("On écrit sur les murs le nom de...",["Kaaris","Ceux qu'on aime","L'acteur de Squid Game","Lee Jung-jae"],[1])
q615 = CreerQ("Que signifie le M de M-Pokora ?",["Matthieu","Bing Chiling","Michael","Michou"],[0])
q616 = CreerQ('Dans "Dès que le vent soufflera", quand la mer prend elle Renaud ?',["Tous les soirs","Le 30 janvier 1933","Un mardi","C'est Renaud qui prend la mer"],[2])
q617 = CreerQ('Qui a composé la "sonate au clair de Lune" ?',["Patrick Sebastien","Mozart","Beethoven","Kaaris"],[2])
q618 = CreerQ("Dans le conte du joueur de flûte de Hamelin, de quel animal le musicien débarrasse-t-il la ville?",["Les serpents","Les mouches","Les rats","Les autres..."],[2,3])
q619 = CreerQ("Dans quel groupe jouaient David Gilmour et Roger Waters?",["Pink Floyd","Radiohead","Genesis","Kaaris"],[0])
q620 = CreerQ("Combien y a t'il de membres dans le boys-band BTS ?",["5","7","1 et Kaaris","je m'en fiche"],[1,3])
q621 = CreerQ("Qui est le rappeur américain ayant eu le plus d'album certifié disque de diamant de son vivant ?",["Eminem","Michou","2pac","Drake"], [0])
q622 = CreerQ("Lequel de ces artistes n'a pas pratiqué de la musique classique ?",["Liszt","Chopin","Bach","Mozart"], [1])
q623 = CreerQ("Quel style de musique est apparu en premier ?",["Classique","Opéra","Baroque","Blues"], [2])







liste_des_matieres = {'NSI':[q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q110,q111,q112,q113,q114,q115,q116,q117,q118,q119,q120,q121,q122,q123,q124],
                      'MATHS':[q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,q210,q211,q212,q213,q214,q215,q216,q217,q218,q219,q220,q221,q222,q223,q224],
                      'SPORT':[q30,q31,q32,q33,q34,q35,q36,q37,q38,q39,q310,q311,q312,q313,q314,q315,q316,q317,q318,q319,q320,q321,q322,q323,q324],
                      'SVT':[q40,q41,q42,q43,q44,q45,q46,q47,q48,q49,q410,q411,q412,q413,q414,q415,q416,q417,q418,q419,q420,q421,q422,q423,q424],
                      'HISTOIRE':[q50,q51,q52,q53,q54,q55,q56,q57,q58,q59,q510,q511,q512,q513,q514,q515,q516,q517,q518,q519,q520,q521,q522,q523,q524],
                      'MUSIQUE':[q60,q61,q62,q63,q64,q65,q66,q67,q68,q69,q610,q611,q612,q613,q614,q615,q616,q617,q618,q619,q620,q621,q622,q623]}

#149
