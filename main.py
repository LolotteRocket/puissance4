import random

joueurs = ["axo", "lolotte", "adel", "anouk"]
print("bienvenue mon g")
while True:
    
    random.shuffle(joueurs)
    equipe1= joueurs[:len(joueurs)//2]
    print("Capitaine de l'équipe 1 : " + random.choice(equipe1))
    print("Equipe 1:")
    for joueur in equipe1 :
        print(joueur)
    equipe2 = joueurs[len(joueurs)// 2:]
    print("\nCapitaine de l'équipe 2 : " + random.choice(equipe2))
    print("Equipe 2 :")
    for joueur in equipe2 :
        print(joueur)

    reponse = input("Choisir de nouvelle équipes?\
                    saissisez o ou n: ")
    if reponse == "n":
        break