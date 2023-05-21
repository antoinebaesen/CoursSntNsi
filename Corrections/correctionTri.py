## Importation des modules


## Déclaration des constantes

## Déclaration des fonctions
def inverse(liste, pos1, pos2):
    """ inverse la position de 2 éléments dans la liste"""
    tmp = liste[pos1]
    liste[pos1] = liste[pos2]
    liste[pos2] = tmp

    # Autre possibilité
    #(liste[pos1], liste[pos2]) = (liste[pos2], liste[pos1])
    return liste

def plusPetit(liste, pos):
    min = pos
    for i in range(pos+1, len(liste)):
        if liste[min] > liste[i]:
            min = i
    return min

def triParSelection(liste):
    for i in range(len(liste)):
        min = plusPetit(liste, i)
        inverse(liste, i, min)

def triParInsertion(liste):
    # On suppose que le premier élément est trié
    for i in range(1, len(liste)):
        # On insère l'élément i dans la liste triée
        j = i
        # Tant que l'élément i est plus petit que l'élément précédent
        while j > 0 and liste[j-1] > liste[j]:
            # On inverse les 2 éléments
            inverse(liste, j, j-1)
            j -= 1

## Fonction principale

def main():
    liste = [7, 5, 8, 45, 67, 1, 12, 9, 2]
    print(str(liste))
    triParInsertion(liste)
    print(str(liste))
    
## Programme principal

if __name__ == '__main__':
    main()


