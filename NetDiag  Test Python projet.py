import subprocess
oeil_mot = r"""
                     W A T C H I N G
                  WATCHING WATCHING WATCHING
             WATCHING                 WATCHING
         WATCHING                         WATCHING
      WATCHING                               WATCHING
    WATCHING          .---------.              WATCHING
  WATCHING          .'           '.              WATCHING
 WATCHING         .'               '.              WATCHING
WATCHING         /   .-----------.   \              WATCHING
WATCHING        |   /             \   |             WATCHING
WATCHING        |  |  .-------.    |  |             WATCHING
WATCHING        |  |  |       |    |  |             WATCHING
WATCHING        |  |  |       |    |  |             WATCHING
WATCHING        |  |  |       |    |  |             WATCHING
WATCHING        |  |  '-------'    |  |             WATCHING
WATCHING        |   \             /   |             WATCHING
WATCHING         \   '-----------'   /              WATCHING
 WATCHING         '.               .'              WATCHING
  WATCHING          '.           .'              WATCHING
    WATCHING          '---------'              WATCHING
      WATCHING                               WATCHING
         WATCHING                         WATCHING
             WATCHING                 WATCHING
                  WATCHING WATCHING WATCHING
                     W A T C H I N G

             [ NETDIAG // THE EYE IS WATCHING ]
"""

print("\033[92m" + oeil_mot + "\033[0m")
print("   NET DIAG V1.2")


while True:

    print("1. TESTER LA CONNEXION")
    print("2. AFFICHER L'IP")
    print("3. QUIT")

    choix = input("Fais ton choix : ")

    if choix == "1":
        print("Lancement du test de connexion...")
    
        resultat = subprocess.run(
            ["ping", "-n", "5", "1.1.1.1"],
            capture_output=True,
            text=True,
            encoding="oem",
            errors="replace",   
            )

        
        print("Terminé 👍👍.")
        print(resultat.stdout)
        if resultat.returncode == 0:
         print("Ok Test Réussi!👍👍")
        else: 
            print("Test Echoué")
        print(resultat.stderr)
        print("Code de retour :", resultat.returncode)

    elif choix == "2":
        resultat = subprocess.run (["ipconfig"],
                                   capture_output=True,
                                   text=True,
                                   encoding="oem",
                                   errors="remplace",
                                   )

        if resultat.returncode == 0:

            lignes = resultat.stdout.splitlines()

            for ligne in lignes:

                if "IPv4" in ligne:

                    adresse = ligne.split(":", 1)[1].strip()

                    print("Adresse IPv4 :", adresse)
                elif "Masque" in ligne:
                    masque = ligne.split(":", 1)[1].strip()
                    print ("Masque:", masque)
                elif "Passerelle" in ligne:
                    passerelle = ligne.split(":", 1)[1].strip()
                    print ("Passerelle", passerelle)

            print("Terminé !")

        else:
            print("Erreur lors de la récupération réseau")

    elif choix == "3":

        reponse = input("Quitter ? O/N : ")

        if reponse.strip().upper() == "O":
            print("Fermeture de NetDiag...")
            break

        else:
            print("Retour au menu...")

    else:
        print("Choix invalide")