class JeuDeCartes:
    couleur = ('pique', 'tréfle', 'carreau', 'coeur')
    valeur = (0, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'valet', 'dame', 'roi', 'as')

    def __init__(self):
        self.carte = []
        for coul in range(4):
            for val in range(13):
                self.carte.append((val + 2, coul))

    def nom_carte(self, c):
        return f"{self.valeur[c[0]]} {self.couleur[c[1]]}"

    def battre(self):
        random.shuffle(self.carte)

    def tirer(self):
        t = len(self.carte)
        if t > 0:
            carte = self.carte[0]
            del (self.carte[0])
            return carte
        return None


if __name__ == "__main__":
    euA.battre()
    for n in range(53):
        c = jeuA.tirer()
        if c == None:
            print("Terminé !")
        else:
            print(jeuA.nom_carte(c))
