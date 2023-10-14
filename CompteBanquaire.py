class CompteBancaire:
    def __init__(self, numeroCompte, nom, solde):
        self.numeroCompte = numeroCompte
        self.nom = nom
        self.solde = solde


    def Versement(self, valeurVerse):
        try:
            if valeurVerse >= 0:
                self.solde = self.solde + valeurVerse
            else:
                print("Valeur Invalide")
        except:
            print("ERREUR D'ENTREE")

    def Retrait(self, valeurRetrait):
        try:
            if self.solde >= valeurRetrait:
                self.solde = self.solde - valeurRetrait
            else:
                print("Solde invalide")
        except:
            print("ERREUR D'ENTREE")

    def Agios(self):
        self.solde = self.solde - (self.solde * 5/100)

    def Affichage(self):
        print(f"Informations du client : ")
        print(f"Nom: {self.nom}")
        print(f"Numéro de compte: {self.numeroCompte}")
        print(f"Solde: {self.solde}")

#Enregistrement du client
numero_compte = int(input("Entrez le numéro de compte : \n"))
nom_client = input("Entrez le nom du client : \n")

# Création d'un compte
compte1 = CompteBancaire(numeroCompte=numero_compte, nom=nom_client, solde=0)

# Versement dans le compte
montant_versement = float(input("Entrez le montant à verser : "))
compte1.Versement(montant_versement)

# Retrait du compte
montant_retrait = float(input("Entrez le montant à retirer : "))
compte1.Retrait(montant_retrait)

# Affichage des informations du client
compte1.Affichage()
