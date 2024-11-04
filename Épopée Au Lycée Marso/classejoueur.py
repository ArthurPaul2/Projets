
#fichier où on crée le joueur
class Joueur:

    def __init__(self,nom, pv = 3, nb_reponses = 0): #constructeur
        
        self.pv = pv #de type integer 
        self.nb_reponses = nb_reponses #de type integer
        self.nom = nom #de type string

    def __str__(self): # permettra de savoir le nom du joueur ses points de vies et les bonnes réponses qu'on afifchera en bas a gauche de l'écran
        return (f"Nom: {self.nom}\n"
                f"Point(s) de vie: {self.pv}\n"
                f"Nombre de bonnes réponses: {self.nb_reponses}")
    

    
    def retirervie(self):
        
        """méthode qui sera appelée pour retirer un point de vie au joueur"""
        self.pv = self.pv -1
        

    def bonnereponse(self):
        
        """méthode qui sera appelée pour ajouter 1 au nombre de bonnes réponses"""
        self.nb_reponses += 1

    def Reset(self):

        """méthode qui sera appelée pour reset le joueur quand il aura atteint 5 bonnes réponses ou que le boss n'aura plus de points de vie"""
        self.pv = 3
        self.nb_reponses = 0
        
        
        
    
