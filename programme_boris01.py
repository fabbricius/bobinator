from random import randint
sortir=False
print("\n")
print("     salut à toi nouveau joueur")

while(sortir==False):
    print("\n")
    print("choisis une difficulté:")
    print("   1: de 1 à 10     2: de 1 à 100     3: de 1 à 1000")
    #niveau=int(input())
    nb_a_trouver=0
    nb_choisis=0
    resultat_trouve=False
    nb_de_coups=0
    recommencer=False
    limite=0
    difficulte_choisie=False
    while(difficulte_choisie==False):
        niveau=int(input())
        if(niveau==1):
            print(" niveau facile")
            difficulte_choisie=True
            nb_a_trouver=randint(1,10)
            limite=10
        elif(niveau==2):
            print(" niveau moyen")
            difficulte_choisie=True
            nb_a_trouver=randint(1,100)
            limite=100
        elif(niveau==3):
            print(" niveau difficile")
            difficulte_choisie=True
            nb_a_trouver=randint(1,1000)
            limite=1000
        else:
            print("je ne comprends pas, tu dois choisir une difficulté")
    #print(nb_a_trouver)
    while(resultat_trouve==False):
        print("propose un nombre")
        nb_choisis=int(input())
        nb_de_coups=nb_de_coups+1
        if(nb_choisis==nb_a_trouver):
            print("bravo, tu a trouvé en "+str(nb_de_coups)+ " coup(s)")
            print("\n")
            resultat_trouve=True
        elif(nb_choisis>limite):
            print("tu dois respecter la difficulté !")
        elif(nb_choisis>nb_a_trouver):
            print("c'est moins !")
        elif(nb_choisis<nb_a_trouver):
            print("c'est plus !")
    print("veux-tu recommencer une partie ?")
    print("\n")
    print("    1: oui         2:non")
    oui_non=int(input())
    if(oui_non==2):
        sortir=True
        
