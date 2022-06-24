from main import JeuDeCartes

joueurA = JeuDeCartes()
joueurB = JeuDeCartes()
joueurA.battre()
joueurB.battre()
pointA, pointB = 0, 0
for _ in range(52):
    ca, cb = joueurA.tirer(), joueurB.tirer()
    va, vb = ca[0], cb[0]
    if va > vb:
        pointA += 1
    elif vb > va:
        pointB += 1

    print(f"{joueurA.nom_carte(ca)}, {joueurB.nom_carte(cb)}, {pointA}, {pointB}")

print(f"\nLe joeur A obtient {pointA} points, le joeur B obtient {pointB} points")