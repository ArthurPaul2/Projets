from pygame import mixer
mixer.init()

#fichier dans lequel on implémente toute les musiques

son_bon = mixer.Sound("musiques/YOUWIN.mp3")
son_mauv = mixer.Sound("musiques/YOULOSE.mp3")

mus_menu = 'musiques/kart.mp3'
mus_comb = ["musiques/Lisztmazeppa.mp3","musiques/LisztOrage.mp3"] #+2

son_bon2 = mixer.Sound('musiques/MONTAGE.mp3')
son_mauv2= mixer.Sound("musiques/BUZZER.mp3")
mus_cred = "musiques/chopin.mp3"
mus_coul = ['musiques/Mario.mp3','musiques/wii.mp3',"musiques/Star.mp3"]

son_trans = mixer.Sound('musiques/buddy.mp3')

correct = [son_bon,son_bon2] #+2
mauvais = [son_mauv,son_mauv2]#+2