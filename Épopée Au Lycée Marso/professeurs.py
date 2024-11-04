import projetGroupe3MARTINVAILLOT as MV
import img

#fichier dans lequel on implémente tout les professeurs

prof_sport = MV.Prof('Lebron James',["Lebron James !","Lebron James ?","Lebron James...","LEBRON JAMES !!!","Lebron James."],[img.sport_n,img.sport_h,img.sport_t],'SPORT')

prof_svt = MV.Prof('Le Chien',["Woufe!","Woufe?","Woufe...", "Squid Games", "WOUFE !!!"],[img.svt_n,img.svt_h,img.svt_t],'SVT')

prof_histoire = MV.Prof('Joe Biden',["SODA !", "JOE BIDEN JOE BIDEN JOE BIDEN JOE BIDEN","J'AIME QUE LES ENFANTS SAUTENT SUR MES GENOUX","Où est Jackie?", "America is muphmuphmuph"],[img.histoire_n,img.histoire_h,img.histoire_t],'HISTOIRE')

prof_info = MV.Prof('Mark',["Bip boup", "I'm the terminator", "Roger Roger","I'll be back !"],[img.info_n,img.info_h,img.info_t],'NSI')

prof_musique = MV.Prof('Kaaris',["Le rap français fait goleri, il ressemble à Booder","Strass, chat, miaou !","Ouais exactement ouais ouais ouais !","T'es bien renseigné toi !","C’est pas parce que tu ne joues plus que le jeu s’arrête ","Putain... les bâtards..."],[img.mus_n,img.mus_h,img.mus_t],'MUSIQUE')

prof_maths = MV.Prof("Mr.Dureuil",["Est-ce que vous avez des questions ?","Envie d'une tarte au citron meringuée.","Messieurs au fond s'il vous plaît.","C'était plutôt facile, nan ?","Je devrais me remettre à Zelda"], [img.maths_n,img.maths_h,img.maths_t], 'MATHS' )
liste_profs = [prof_sport , prof_svt , prof_histoire , prof_info, prof_maths , prof_musique ]

