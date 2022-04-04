import sqlite3
connection=sqlite3.connect("test.db")
cur=connection.cursor()
from math import*
import time
print('Bienvenue sur la Microfinance des Etudiants ! quelle opération voulez-vous faire ? ')
option=int(input('fêtes votre choix en tapant 1 pour créer un nouveau compte, 2 pour faire un dépôt ou un retrait,8 Pour consulter votre historique.\n'))
#Ouverture d'un nouveau compte pour un étudiant 
if(option<1):
      print('Erreur ! Entrez 1 ou 2\n')
elif(option==1):
      print('Veuillez remplir les champs suivants SVP !')
      Nom=str(input( 'Votre nom\n'))
      pren=str(input('Votre prenom\n'))
      nais=str(input('votre date de naissance\n'))
      mat=str(input('Votre matricule\n'))
      tel=str(input('votre numéro de téléphone\n'))
      cur.execute("INSERT INTO etudiant(nom,prenom,matricule,telephone,date_de_naissance) VALUES(?,?,?,?,?);",(Nom,pren,mat,tel,nais))
      connection.commit()
      print('Votre compte a été créé avec succès! Voulez-vous faire un retrait ou un dépôt?')
      opera=int(input('Si oui,Tapez 3 pour faire un dépôt ou 4 pour un rétrait, Si non, Tapez 5 pour Quitter'))
      if(opera==3):
            mat=str(input('Entrer votre matricule\n'))
            montD=int(input('Entrez le montant SVP !\n'))
            if(montD<=0):
                print('Erreur ! Veuillez entrer un montant superieur à 0\n')
            elif(montD<499):
                montD=int(input('le montant demandé ne peut pas être traité. Veuillez entrer un montant supérieur ou égal à 500,merci!.\n'))
            elif(montD>=499):
                dat=time.strftime("%d/%m/%Y %H:%M")
                cur.execute("INSERT INTO operation(type,matricule_etudiant,montant,date) VALUES(?,?,?,?);",("depot", mat, montD, dat))
                cur.execute("UPDATE etudiant SET solde=solde+? WHERE matricule=?;",(montD, mat))
                connection.commit()
                print('Bravo ! Votre dépot a été effectué avec succès\n')
                print('Vous avez déposé sur votre compte un montant de:')
                print(montD)
                cur.execute("SELECT solde FROM etudiant WHERE matricule=? LIMIT 1;", [mat])
                sold=cur.fetchone()
                print('Votre nouveau solde est:\n')
                print(sold[0])
                print('La Microfinance Etudiant vous remercie et à très bientôt')
      elif(opera==4):
            mat=int(input('Entrer votre matricule\n'))
            montR=int(input('Entrer le montant SVP !\n'))
            cur.execute("SELECT solde FROM etudiant WHERE matricule=? LIMIT 1;", [mat])
            montB=cur.fetchone()
            if(montR>montB[0]):
                print('ERREUR!opération impossible')
            elif(montR<=499):
                print('ERREUR!opération impossible.\n')
            else:
                dat=time.strftime("%d/%m/%Y %H:%M")
                cur.execute("INSERT INTO operation(type,matricule_etudiant,montant,date) VALUES(?,?,?,?);",("retrait", mat, montR, dat))
                cur.execute("UPDATE etudiant SET solde=solde-? WHERE matricule=?;",(montR, mat))
                connection.commit()
                cur.execute("SELECT solde FROM etudiant WHERE matricule=? LIMIT 1;", [mat])
                sold=cur.fetchone()
                print('Bravo ! Votre retrait a été effectué avec succès\n')
                print('Vous avez retiré de votre compte, une somme de:')
                print(montR,"FrCFA")
                print('Votre nouveau solde est de:')
                print(sold[0],"FRCFA")
                print('La Microfinance des Etudiants vous remercie !')
      else:
            print('Au revoir')
elif(option==2):
      print('Taper "3" pour un Dépot ; "4" pour un Retrait')
      op=int(input('Quel est votre choix ?\n'))
      if(op==3):
            mat=str(input('Entrer votre matricule\n'))
            montD=int(input('Entrez le montant SVP !\n'))
            if(montD<=0):
                print('Erreur ! Veuillez entrer un montant superieur à 0\n')
            elif(montD<499):
                montD=int(input('le montant demandé ne peut pas être traité. Veuillez entrer un autre montant.\n'))
            elif(montD>=499):
                dat=time.strftime("%d/%m/%Y %H:%M")
                cur.execute("INSERT INTO operation(type,matricule_etudiant,montant,date) VALUES(?,?,?,?);",("depot", mat, montD, dat))
                cur.execute("UPDATE etudiant SET solde=solde+? WHERE matricule=?;",(montD, mat))
                connection.commit()
                print('Bravo ! Votre dépot a été effectué avec succès\n')
                print('Vous avez déposé sur votre compte un montant de:')
                print(montD,"FrCFA")
                cur.execute("SELECT solde FROM etudiant WHERE matricule=? LIMIT 1;", [mat])
                sold=cur.fetchone()
                print('Votre nouveau solde est:\n')
                print(sold[0],"FrCFA")
                print('La Microfinance Etudiant vous remercie et à très bientôt')

      elif(op==4):
            mat=int(input('Entrer votre matricule\n'))
            montR=int(input('Entrer le montant SVP !\n'))
            cur.execute("SELECT solde FROM etudiant WHERE matricule=? LIMIT 1;", [mat])
            montB=cur.fetchone()
            if(montR>montB[0]):
                print('ERREUR!opération impossible')
            elif(montR<=499):
                print('ERREUR!opération impossible.\n')
            else:
                dat=time.strftime("%d/%m/%Y %H:%M")
                cur.execute("INSERT INTO operation(type,matricule_etudiant,montant,date) VALUES(?,?,?,?);",("retrait", mat, montR, dat))
                cur.execute("UPDATE etudiant SET solde=solde-? WHERE matricule=?;",(montR, mat))
                connection.commit()
                cur.execute("SELECT solde FROM etudiant WHERE matricule=? LIMIT 1;", [mat])
                sold=cur.fetchone()
                print('Bravo ! Votre retrait a été effectué avec succès\n')
                print('Vous avez retiré de votre compte, une somme de:')
                print(montR)
                print('Votre nouveau solde est de:')
                print(sold[0])
                print('La Microfinance des Etudiants vous remercie !')

      else:
            print('Mauvais choix!')
            #Affichage du relevé des opérations
elif(option==8):
      mat=str(input('Entrez votre matricule: \n'))
      cur.execute("SELECT * FROM etudiant WHERE matricule=? LIMIT 1;", [mat])
      res=cur.fetchone()
      if(res == None):
            print("Aucun étudiant n'a ce matricule")
      else:
            print("\n Matricule: "+mat)
            print("Nom: "+res[1])
            #print("\n")
            print('Prenom: '+res[2])
            #print("\n")
            print('Telephone: '+res[4])
            print("\n Solde actuel: ",res[6],"FRCFA")
            cur.execute("SELECT * FROM operation WHERE matricule_etudiant=?;", [mat])
            ops=cur.fetchall()
            if(ops==None):
                  print('Aucune opération pour le moment')
            else:
                  print("N° \t Opération \t Montant \t Date")
                  for row in ops:
                        print(row[0],'\t ',row[1],' \t ',row[3],' \t '+row[4])
#connection.close() mat:123456/456123
