import pygame
from random import randint
from random import choice
from sys import exit
import projetGroupe3MARTINVAILLOT as MV
import classeQR as QR
import img
import classejoueur as j
import musiques as mu
from professeurs import liste_profs

#autofocus entrée du nom
#faire si len(texte) > 0 couleur = couleurA


print('nécessite pygame 2.0+ \
cmd : 1.python -m pip uninstall pygame  2.pip install pygame')


pygame.init()
pygame.mixer.init()
pygame.display.set_icon(pygame.image.load(img.lycée_nom))

#screen setup
larg = 1000 #largeur fenetre
haut = 600  #hauteur fenetre
screen = pygame.display.set_mode((larg,haut))
pygame.display.set_caption("L'épopée au Lycée Marso")

#création des clocks
clock = pygame.time.Clock()
clocktemp = pygame.time.Clock()

#création des surfaces
catchphrases_surf       = pygame.image.load(img.bubble)
bg_surf                 = pygame.Surface((larg,haut))
anim_surf               = pygame.Surface((larg,haut))
prof_surf               = pygame.Surface((larg/2,(haut/2)-50))
q_surf                  = pygame.Surface((larg,60))
rep1_surf               = pygame.Surface((650,70))
rep2_surf               = pygame.Surface((650,70))
rep3_surf               = pygame.Surface((650,70))
rep4_surf               = pygame.Surface((650,70))
resultat_surf           = pygame.Surface((400,70))
fond_noir               = pygame.Surface((1000,600))
rep_bg_surf             = pygame.image.load(img.papier)
filtre_gris             = pygame.Surface((1000,600)) #filtre gris sur la phase de transition
filtre_rouge            = pygame.Surface((1000,600))
trans_text_surf         = pygame.Surface ((1000,600))
erreur_surf             = pygame.Surface((650,30)) #affichage du message d'erreur si nom bizarre
t_aide_bg               = pygame.Surface((200,25))



#coloration des couleurs
filtre_rouge.fill((150,0,0))
filtre_gris.fill((54, 69, 79))
t_aide_bg.fill((255,255,255))


#transparence des surfaces
erreur_surf.set_alpha(175)
filtre_rouge.set_alpha(100)
filtre_gris.set_alpha(200)
filtre_gris.set_colorkey((0,0,0))
erreur_surf.set_colorkey((0,0,0))
q_surf.set_colorkey((0,0,0))
rep1_surf.set_colorkey((0,0,0))
rep2_surf.set_colorkey((0,0,0))
rep3_surf.set_colorkey((0,0,0))
rep4_surf.set_colorkey((0,0,0))
prof_surf.set_colorkey((0,0,0))
resultat_surf.set_colorkey((0,0,0))
trans_text_surf.set_colorkey((0,0,0))

#création du texte d'info nom
t_aide = MV.police.render("veuillez entrer un nom",True,(0,0,0))
t_aide_bg.set_alpha(175)
t_aide_bg.blit(t_aide,(t_aide_bg.get_width()//2-t_aide.get_width()//2,t_aide_bg.get_height()//2-t_aide.get_height()//2))


#partie "entrée du nom du joueur" 
inputnom = pygame.Rect(larg/2-50,haut/2,100,30)#input du nom
couleurA = pygame.Color('lightskyblue3')
couleurP = (255,255,255)
texte = ''
active = False
nomdonné = False
ok_surf = pygame.Rect(larg/2-20,haut/2+35,40,25) #bouton "OK"



#initialisation des variables

debut_surf = pygame.image.load(img.lycée_deb) #surface de l'accueil du jeu
partie_jeu = 'deb'
timer = -60 #on met un timer qui se déclenchera toutes les 20s et qui commence à -5 secondes pour laisser le temps au joueur de se familiariser à l'UI
rep = 4
lp = liste_profs
k = 50 #saut de départ pour les crédits
i_joueur = 0 #indice de l'image du joueur
i_coul = 0 #indice de l'image des couloirs
larg_cercle = 1
repondu = False #on indique au jeu que le joueur n'a pas répondu à la question
boucle = True
clique = False
couloir_mus = True
combat_mus = True
menu_mus = True
trans_mus = True
jeu = True
pause = False
mute = False
vol_mus = 0.1
vol_son = 0.2

while True:#boucle dans laquelle tout le jeu se déroule

    while boucle: #boucle de départ, comprend le début du jeu jusqu'à ce que le joueur clique sur le bouton ok avec un nom acceptée par la machine

        if partie_jeu == "deb":
            if menu_mus: #lancement de la musique
                pygame.mixer.music.unload()
                pygame.mixer.music.load(mu.mus_menu)
                pygame.mixer.music.set_volume(vol_mus)
                pygame.mixer.music.play(-1)
                menu_mus = False
            screen.blit(debut_surf,(0,0))

        if active: #changement de la couleur de la zone d'input
            couleur = couleurA
        else:
            couleur = couleurP
                
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.KEYDOWN: #on détecte le texte ecrit dans la case d'input
                if event.key == pygame.K_RETURN and not clique:#si c'est entrée on vérifie que le joueur n'a pas encore cliqué sur le bouton jouer et on l'envoie dans le jeu
                    clique = True
                if active:
                    if event.key == pygame.K_BACKSPACE:#on supprime le dernier élément du texte
                         texte = texte[:-1]
                         
                    elif event.key == pygame.K_RETURN and len(texte)>0:
                        for elt in texte:
                            if 65<ord(elt)<90 or 97<ord(elt)<122: #on regarde si tous les caractères sont bien des lettres
                                bon = True
                            else:
                                bon = False
                            if bon:
                                nomdonné = True
                                mu.son_bon2.set_volume(vol_son)
                                pygame.mixer.Sound.play(mu.son_bon2)
                                
                                
                    else:
                        if len(texte)<=12: #on empêche les noms de plus de 12 caractères
                                texte += event.unicode
                        
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if inputnom.collidepoint(event.pos): 
                    active = True
                if ok_surf.collidepoint(event.pos) and len(texte)>0: #on detecte le clic sur le bouton ok
                    for elt in texte:
                        if 65<ord(elt)<90 or 97<ord(elt)<122: #on regarde si tous les caractères sont bien des lettres
                            bon = True
                        else:
                            bon = False
                    if bon:
                        nomdonné = True
                        pygame.mixer.Sound.play(mu.son_bon2)
                        
                    else: #si le texte comprend des caracteres non-acceptés on envoie un message d'erreur pour que le joueur sache qu'il doit réinsérer un nom
                        texte = ''
                        MV.ResetSurf([t_aide])
                        erreur_surf.fill((255,255,255))
                        MV.Afficher("Erreur: Le nom doit être composé uniquement de caractères dans a-z,A-Z",erreur_surf,1000)
                        mu.mauvais[1].set_volume(vol_son)
                        pygame.mixer.Sound.play(mu.mauvais[1])
                        active = False
                elif larg/2-200 <= pygame.mouse.get_pos()[0] <= larg/2+200 and haut/2+120 <= pygame.mouse.get_pos()[1] <= haut/2+250 and partie_jeu == 'deb': #bouton "jouer"
                    clique = True

        if clique: #on affiche tout

            if not nomdonné: #affichage de la zone d'input et du bouton ok
                screen.blit(pygame.image.load(img.lycée_nom),(0,0))
                pygame.draw.rect(screen, couleur, inputnom)
                texte_surf = MV.police.render(texte,True,(0,0,0))
                screen.blit(texte_surf,(inputnom.x+5,inputnom.y+5))
                inputnom.w = max(100, texte_surf.get_width()+10)           
                ok_txt = MV.police.render("OK",True,(0,0,0)) 
                screen.blit(t_aide_bg,(larg//2-t_aide.get_width()//2,270))
                screen.blit(erreur_surf,(larg//2-erreur_surf.get_width()//2,haut//2-65))

                if len(texte) > 0:#si il y a un nom d'inscrit le bouton s'affiche
                    pygame.draw.rect(screen,(128,128,128),ok_surf)
                    screen.blit(ok_txt,(ok_surf.x+10,ok_surf.y+5)) 
                

            else: #on crée le joueur et on termine la boucle pour passer au reste du jeu
                joueur = j.Joueur(texte)
                boucle = False
                jeu = True
                partie_jeu = "couloir"                
                MV.ResetSurf([erreur_surf])

        pygame.display.update()
        clocktemp.tick(60)


    

    while jeu: #jeu principal

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN: 

                if event.key == pygame.K_v and joueur.nom == "BOAPMV":#on passe directement à un combat (avec qq bugs car variables pas aux bonnes valeurs) si le joueur a le nom secret
                    partie_jeu = 'combat'
                    timer = -140

                if event.key == pygame.K_w and joueur.nom == "BOAPMV":#on passe directement aux crédits (avec qq bugs car variables pas aux bonnes valeurs) si le joueur a le nom secret
                    partie_jeu = "credits"
                    k = 50
                if event.key == pygame.K_p and not partie_jeu == "credits":#bouton de pause
                    if pause:
                        filtre_gris.set_alpha(200)
                        pause = False
                        MV.ResetSurf([pause_surf])#on retire le bouton
                    else:#on met en pause et on affiche le bouton
                        filtre_gris.set_alpha(225)
                        pause = True
                        pause_surf = pygame.image.load(img.pause)
                        pause_surf.set_alpha(150)

                if event.key == pygame.K_m:#bouton de mute
                    

                    if mute:#on retire le mute
                        vol_mus = 0.1 #on remet le son au bon volume
                        vol_son = 0.2
                        pygame.mixer.music.unpause()
                        mute = False
                    

                    else:#on met mute en true et on coupe tout les sons
                        pygame.mixer.music.pause()
                        vol_son,vol_mus = 0,0
                        mute = True
                    


            if event.type == pygame.MOUSEBUTTONDOWN:#on regarde si le joueur clique sur une réponse
                if 0 < timer < 900:
                    if (larg/2-50 < event.pos[0] < larg) and (haut/2+20 < event.pos[1] < haut/2+90):#rep1
                        rep = 0
                        repondu = True #on indique au jeu que le joueur à répondu pour changer de question
                    elif (larg/2-50 < event.pos[0] < larg) and (haut/2+90 < event.pos[1] < haut/2+160): #rep2
                        rep = 1
                        repondu = True
                    elif (larg/2-50 < event.pos[0] < larg) and (haut/2+160 < event.pos[1] < haut/2+230): #rep3
                        rep = 2
                        repondu = True
                    elif (larg/2-50 < event.pos[0] < larg) and (haut/2+230 < event.pos[1] < haut): #rep4
                        rep = 3
                        repondu = True 
                if partie_jeu == 'fin':#si on est dans l'écran de fin
                    if (400 < event.pos[0] < 600) and (330 < event.pos[1] < 380):#si on clique sur le bouton 'quitter'
                        pygame.quit()
                        exit()
                    if (400 < event.pos[0] < 600) and (220 < event.pos[1] < 270):#si on clique sur le bouton 'rejouer'
                        repondu = False #on réinitialise tout les paramètres
                        boucle = True
                        clique = False
                        couloir_mus = True
                        combat_mus = True
                        menu_mus = True
                        trans_mus = True
                        jeu = False
                        active = False
                        nomdonné = False   
                        pause = False 
                        texte = ''
                        timer = -60
                        rep = 4
                        lp = liste_profs
                        k = 50 
                        i_joueur = 0
                        i_coul = 0
                        larg_cercle = 1
                        partie_jeu = 'deb'
                        for elt in liste_profs:
                            elt.resetprof()
                        MV.ResetSurf([q_surf,rep1_surf,rep2_surf,rep3_surf,rep4_surf,resultat_surf])



        if partie_jeu == 'couloir':

            if couloir_mus: #on lance une musique aléatoire parmis les musiques du couloir
                pygame.mixer.music.unload()
                pygame.mixer.music.load(choice(mu.mus_coul))
                pygame.mixer.music.set_volume(vol_mus)
                pygame.mixer.music.play(-1) #musique jouée en boucle jusqu'à changement
                couloir_mus = False

            joueur_surf = pygame.image.load(img.im_joueur[i_joueur]) #changement de l'image du joueur pour animation
            barre_de_bonne_rep_surf = pygame.image.load(img.barre_rep[joueur.nb_reponses]) #on affiche toutes les surfaces
            bg_surf.blit(pygame.image.load(img.bg_couloirs[i_coul]),(0,0))
            screen.blit(bg_surf,(0,0))    
            screen.blit(joueur_surf,(50,150))
            screen.blit(q_surf,(0,10))
            screen.blit(rep_bg_surf,((larg/2)-25,(haut/2)+15))
            screen.blit(rep1_surf,((larg/2)-50,(haut/2)+20))
            screen.blit(rep2_surf,((larg/2)-50,(haut/2)+90))
            screen.blit(rep3_surf,((larg/2)-50,(haut/2)+160))
            screen.blit(rep4_surf,((larg/2)-50,(haut/2)+230))
            screen.blit(barre_de_bonne_rep_surf,(23,haut-20))



            if timer < 0: 

                if repondu: #si le joueur a cliqué sur une réponse

                    bonnerep= question.répondre(rep)# on regarde si la réponse est bonne
                    if bonnerep:

                        MV.ResetSurf([q_surf,rep1_surf,rep2_surf,rep3_surf,rep4_surf,resultat_surf])
                        MV.ResultatQuestion('y',resultat_surf)#on affiche 'bonne réponse' sur l'écran
                        screen.blit(resultat_surf,((larg/2)-(resultat_surf.get_width()/2),(haut/2)-(resultat_surf.get_height()/2)-5))
                        if timer == -99:
                            if not joueur.nb_reponses == 7: #si ce n'est pas la dernière réponse nécessaire on joue le son
                                son = choice(mu.correct)
                                son.set_volume(vol_son)
                                pygame.mixer.Sound.play(son)#on joue un son de bonne réponse
                            joueur.bonnereponse()#on ajoute 1 au compteur
                    else:

                        MV.ResetSurf([q_surf,rep1_surf,rep2_surf,rep3_surf,rep4_surf,resultat_surf])
                        MV.ResultatQuestion('n',resultat_surf)#on affiche 'mauvaise réponse' sur l'écran
                        screen.blit(resultat_surf,((larg/2)-(resultat_surf.get_width()/2),(haut/2)-(resultat_surf.get_height()/2)-5))
                        if timer == -99:
                                son = choice(mu.mauvais)
                                son.set_volume(vol_son)
                                pygame.mixer.Sound.play(son)#on joue un son de mauvaise réponse

            if timer == 0:  #affichage des nouvelles questions

                question = QR.QuestionRandom()
                repondu = False #on indique au jeu que le joueur n'a pas répondu à la question
                MV.ResetSurf([q_surf,rep1_surf,rep2_surf,rep3_surf,rep4_surf,resultat_surf])
                MV.AfficherQuestion(question,q_surf,[rep1_surf,rep2_surf,rep3_surf,rep4_surf],(1,0,0))   #affichage de la question 



            if 0 < timer < 800:
                if repondu:
                    timer = -100



            if timer >= 800:     #changement de la question                

                timer = -100
                MV.ResetSurf([q_surf,rep1_surf,rep2_surf,rep3_surf,rep4_surf])

            

            if joueur.nb_reponses == 8: #quand le nombre de bonnes réponses est atteint

                joueur.Reset()
                partie_jeu = 'combat' #on lance le combat
                combat_mus = True
                repondu = False
                timer = -140
                rep = 4
                MV.ResetSurf([q_surf,rep1_surf,rep2_surf,rep3_surf,rep4_surf,resultat_surf])
                pygame.mixer.music.fadeout(139)
            


        if partie_jeu == 'combat':#lancement du combat

            
            if timer == -140:#sélection du professeur
                prof = choice(lp)
                joueur.Reset()
            
            if combat_mus:#lancement de la musique du combat
                pygame.mixer.music.unload()
                pygame.mixer.music.load(choice(mu.mus_comb))
                pygame.mixer.music.set_volume(vol_mus)
                pygame.mixer.music.play(-1)
                combat_mus = False

            joueur_surf = pygame.image.load(img.im_joueur_combat)#chargement des images
            prof_surf = pygame.image.load(prof.im_aff)
            barre_de_vie_surf = pygame.image.load(img.barre_vie[prof.pv])
            bg_surf = pygame.image.load(img.combat_bg)
            barre_vie_j = pygame.image.load(img.vie_joueur[joueur.pv])

            screen.blit(bg_surf,(0,0))#affichage des images et des surfaces
            screen.blit(prof_surf,(larg/2-prof_surf.get_width()//2,0))
            screen.blit(joueur_surf,(150,(haut/2)+20))
            
            screen.blit(barre_de_vie_surf,(larg/2-barre_de_bonne_rep_surf.get_width()//2,prof_surf.get_height()-10))
            screen.blit(q_surf,(0,(haut/2)-40))
            screen.blit(barre_vie_j,(300,580))
            screen.blit(rep_bg_surf,((larg/2)-25,(haut/2)+15))
            screen.blit(rep1_surf,((larg/2)-50,(haut/2)+20))
            screen.blit(rep2_surf,((larg/2)-50,(haut/2)+90))
            screen.blit(rep3_surf,((larg/2)-50,(haut/2)+160))
            screen.blit(rep4_surf,((larg/2)-50,(haut/2)+230))



            if -120 < timer < -20:

                if repondu: #même chose que pendant les couloirs mais on mets à jour la vie des deux personnages à chaque réponse
                    bonnerep = question.répondre(rep)

                    if bonnerep:
                            
                        if timer == -119:
                            if not prof.pv == 1:#si on est pas sur le dernier point de vie du professeur
                                son = choice(mu.correct)
                                son.set_volume(vol_son)
                                pygame.mixer.Sound.play(son)#on joue un son de bonne réponse
                            joueur.bonnereponse()
                            prof.baisser_pv()
                            prof.changer_etat(2) 
                            prof.changer_image()
                            phrase = choice(prof.lines)#sélection de la phrase que le prof dira      

                        MV.ResetSurf([q_surf,rep1_surf,rep2_surf,rep3_surf,rep4_surf,resultat_surf,catchphrases_surf])
                        catchphrases_surf= pygame.image.load(img.bubble)
                        MV.ResultatQuestion('y',resultat_surf)      
                        screen.blit(resultat_surf,((larg/4)-resultat_surf.get_width()/2-55,(haut/4)))
                        MV.Afficher(phrase,catchphrases_surf,25)
                        screen.blit(catchphrases_surf,(larg//2+120,70))
                        
                    elif not bonnerep:
                            
                        if timer == -119:

                            son = choice(mu.mauvais)
                            son.set_volume(vol_son)
                            pygame.mixer.Sound.play(son)#on joue un son de bonne réponse
                            joueur.retirervie()
                            prof.changer_etat(1)
                            prof.changer_image()
                            phrase = choice(prof.lines)#sélection de la phrase que le prof dira   

                        MV.ResetSurf([q_surf,rep1_surf,rep2_surf,rep3_surf,rep4_surf,resultat_surf,catchphrases_surf])
                        catchphrases_surf= pygame.image.load(img.bubble)
                        MV.ResultatQuestion('n',resultat_surf)
                        screen.blit(resultat_surf,((larg/4)-resultat_surf.get_width()/2-55,(haut/4)))                 
                        MV.Afficher(phrase,catchphrases_surf,25)
                        screen.blit(catchphrases_surf,(larg//2+120,70))
            
            
            if timer == -19: #réinitialisation de la bulle et de l'image du prof
                MV.ResetSurf([catchphrases_surf])
                prof.changer_etat(0)
                prof.changer_image()          


            if timer == 0:  #affichage des nouvelles questions
                    question = QR.QuestionMat(prof.mat)
                    repondu = False 
                    MV.ResetSurf([q_surf,rep1_surf,rep2_surf,rep3_surf,rep4_surf,resultat_surf])
                    MV.AfficherQuestion(question,q_surf,[rep1_surf,rep2_surf,rep3_surf,rep4_surf],(255,255,255))   #affichage de la question


            if 0 < timer < 800:
                if repondu:
                    timer = -120        


            if timer >= 800:     #changement de la question                  
                timer = -120
                MV.ResetSurf([q_surf,rep1_surf,rep2_surf,rep3_surf,rep4_surf])
            
            
            if joueur.pv == 0:#on prépare l'animation de la défaite si on perd
                MV.ResetSurf([q_surf,rep1_surf,rep2_surf,rep3_surf,rep4_surf,resultat_surf,trans_text_surf])
                partie_jeu = 'défaite'
                timer = 0

            if prof.pv == 0:#si on bat le professeur on le supprime de la liste et on retourne aux couloirs
                joueur.Reset()
                MV.ResetSurf([q_surf,rep1_surf,rep2_surf,rep3_surf,rep4_surf,resultat_surf,trans_text_surf])
                partie_jeu = 'transition'
                couloir_mus = True
                trans_mus = True
                repondu = False
                rep = 4
                timer = -200
                pygame.mixer.stop()
                lp.remove(prof)
                


        if partie_jeu == 'transition':#transition entre les combats et les couloirs

            if len(lp) == 0:

                partie_jeu = "credits"

            else:

                if timer < 0:

                    bg_surf.blit(pygame.image.load(img.combat_bg),(0,0))#affichage du fond et d'un filtre gris
                    screen.blit(bg_surf,(0,0))
                    screen.blit(filtre_gris,(0,0))               
                    t1 = 'Félicitation {}! Vous avez vaincu {} !'.format(joueur.nom,prof.nom)    #texte de la transition
                    t2 = 'Veuillez répondre à 8 questions pour combattre un autre professeur !'
                    t1Pret = MV.police_trans.render(t1,True,(255,255,255))
                    t2Pret = MV.police_trans.render(t2,True,(255,255,255))
                    trans_text_surf.blit(t1Pret,(trans_text_surf.get_width()//2-t1Pret.get_width()//2,trans_text_surf.get_height()//2-35))#affichage du texte
                    trans_text_surf.blit(t2Pret,(trans_text_surf.get_width()//2-t2Pret.get_width()//2,trans_text_surf.get_height()//2+35))
                    screen.blit(trans_text_surf,(larg/2-trans_text_surf.get_width()//2,haut/2-trans_text_surf.get_height()//2))

                    if trans_mus:#lancement du son de la transition
                        mu.son_trans.set_volume(vol_son)
                        pygame.mixer.Sound.play(mu.son_trans)
                        trans_mus = False

                else:#retour aux couloirs
                    partie_jeu = 'couloir'
                    timer = -60



        if partie_jeu == 'défaite':

            if timer == 0:#affichage de tout les trucs
                joueur_surf = pygame.image.load(img.im_joueur_combat)#chargement des images
                prof_surf = pygame.image.load(prof.im_aff)
                barre_de_vie_surf = pygame.image.load(img.barre_vie[prof.pv])
                bg_surf = pygame.image.load(img.combat_bg)
                barre_vie_j = pygame.image.load(img.vie_joueur[joueur.pv])

                screen.blit(bg_surf,(0,0))#affichage des images
                screen.blit(prof_surf,(larg/2-prof_surf.get_width()//2,0))
                screen.blit(joueur_surf,(150,(haut/2)+20))
                
                screen.blit(barre_de_vie_surf,(larg/2-barre_de_bonne_rep_surf.get_width()//2,prof_surf.get_height()-10))
                screen.blit(q_surf,(0,(haut/2)-40))
                screen.blit(barre_vie_j,(300,580))
                screen.blit(rep_bg_surf,((larg/2)-25,(haut/2)+15))
            
            MV.rond_def(screen,larg_cercle)#animation de la défaite avec un rond qui se referme
            
            if timer > 175:#affichage du texte
                def_surf = pygame.Surface((380,70))
                def_surf.fill((255,255,255))
                MV.Afficher("Vous avez été vaincu par {} !".format(prof.nom),def_surf,50)
                def_surf.set_alpha(200)
                screen.blit(def_surf,(310,265))

            if timer == 375:
                MV.ResetSurf([def_surf])
                partie_jeu = 'fin'

            larg_cercle += 5


        if partie_jeu =='credits':#si tous les profs ont été battus
            if k == 50:#on lance la musique des crédits
                pygame.mixer.music.stop()
                pygame.mixer.music.unload()
                pygame.mixer.music.load(mu.mus_cred)
                pygame.mixer.music.set_volume(vol_mus)
                pygame.mixer.music.play(-1)  

            screen.fill((0,0,0))#on remplit l'écran de noir
            MV.credits(screen,k,joueur.nom)#on fait passer les crédits
            k -= 1#on fait monter les crédits petit à petit

            if k == -2760: #toute la surface des crédits a été déroulée
                partie_jeu ="fin"



        if partie_jeu == 'fin':#écran de fin
            bg_surf = pygame.image.load(img.lycée_nom)#fond
            rejouer_surf = pygame.image.load(img.rejouer)#bouton pour rejouer
            quitter_surf = pygame.image.load(img.quitter)#bouton pour quitter le jeu
            screen.blit(bg_surf,(0,0))#affichage des surfaces
            screen.blit(filtre_rouge,(0,0))
            screen.blit(rejouer_surf,(500-rejouer_surf.get_width()//2,230))
            screen.blit(quitter_surf,(500-quitter_surf.get_width()//2,330))



        if timer%12 == 0 and not pause:#on change l'image du joueur lorsque timer = 12k, avec k un entier, deuxième condition car si on pause avec la premiere True alors joueur devient fou
            i_joueur += 1    
            if i_joueur >= 3:
                i_joueur = 0
        if timer%30 == 0 and not pause:
            i_coul += 1
            if i_coul >= 161:
                i_coul = 0

        if not pause:#pas de pause 
            timer += 1#incrémentation du timer
        else:#si on est en pause
            
            screen.blit(filtre_gris,(0,0))
            screen.blit(pause_surf,(50,50))


        if mute:#si on est en mute on affiche l'icone
            mute_surf = pygame.image.load(img.mute)
            screen.blit(mute_surf,(900,20))


        pygame.display.update()
        clock.tick(60)

#Probleme: récupérer la réponse selectionnée par le joueur. solution: changer la surface de réponse en 4 surfaces de réponses
#Probleme: la réponse du joueur n'est pas définie avant qu'il ne clique dessus. solution : on initialise la variable à 4, qui est impossible à avoir en temps normal et on ajoute une condition pass dans la méthode répondre si la réponse est 4
#Probleme: les questions/réponses ne s'effacent pas après chaque question. solution: création d'une fonction ResetSurf() qui remet les surfaces à 0
#Probleme: le joueur est créé durant la boucle et est donc reset à chaque boucle. solution : nouvelle boucle while ainsi que nouvelle clock qui s'occupe uniquement de la partie avant le jeu, aucun retour sur la boucle après 
#Problème : pour le bouton rejouer on ne peut pas retourner dans le jeu puisque les boucles while sont fini. solution: on crée une nouvelle boucle dans laquelle on met tout le reste
#Problème: pour afficher certaines phrases, le texte sortait de la surface. solution : création d'une fonction qui sépare un str en deux moins longs et d'une qui les affiche l'un sous l'autre
#Problème: il faut afficher les questions en noir dans les couloirs et en blanc dans les combats. solution : ajout du paramètre "couleur" dans la fonction afficherquestion pour pouvoir la choisir
