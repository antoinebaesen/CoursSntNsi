## Importation des modules


## Déclaration des constantes


## Déclaration des fonctions

def rechercheNaive(motCherche, texte):
    for i in range(len(texte)):
        #if texte[i:i+len(motCherche)] == motCherche:
        #    return i

        for j in range(len(motCherche)):
            if texte[i+j] != motCherche[j]:
                break
            if j == len(motCherche)-1:
                return i
    return -1

def tableCorrespondance(mot):
    """Renvoi un dictionnaire représentant la table de correspondance associée au mot.
    
    @Args :
        mot : le mot dont on veut la table de correspondance
    @Return :
        dict : la table de correspondance associée au mot
    """

    table = {}
    for i in range(len(mot)):
        table[mot[i]] = len(mot) - i - 1
    return table

def chercheDansTable(table, char):
    """Renvoi la valeur associée à la clé char dans la table de correspondance table.
    
    @Args :
        table : dict, la table de correspondance
        char : str, le charactère dont on veut la valeur associée
    @Return :
        int, la valeur associée à la clé char dans la table de correspondance table
    """

    if char in table:
        return table[char]
    else:
        return len(table)

def avancer(texte, mot, indice):
    """
    Renvoi l'indice à partir duquel on doit rechercher le mot suivant.
    @Args
        texte: str, le texte dans lequel on recherche le mot
        mot: str, le mot à rechercher
        indice: int, l'indice du dernier charactère du mot à partir duquel on va tester
    @Return:
        int, l'indice à partir duquel on doit rechercher le mot suivant
    """

    if indice < 0:
        return 0
    else:
        return indice + chercheDansTable(tableCorrespondance(mot), texte[indice])
    
def memeMot(texte, mot, indice):
    """
    Verifie à partir de l'indice de dernier charactère "indice" si le mot "mot" correspond à celui dans le texte.
    Renvoi l'indice du premier charactère différent ou -1 si le mot correspond.
    """

    for i in range(len(mot)):
        if texte[indice-i] != mot[len(mot)-1-i]:
            return indice-i
    return -1

def rechercheBoyerMoore(motCherche, texte):
    """
    Recherche le mot "motCherche" dans le texte "texte" et renvoi l'indice du premier charactère du mot ou -1 si le mot n'est pas présent.
    
    @Args :
        motCherche : str, le mot à rechercher
        texte : str, le texte dans lequel on recherche le mot
    @Return :
        int, l'indice du premier charactère du mot ou -1 si le mot n'est pas présent
    """

    indice = len(motCherche) - 1
    while indice < len(texte):
        # Si le dernier charactère du mot est le même que celui du texte, on vérifie si le mot est présent
        if texte[indice] == motCherche[-1]:
            # On vérifie si le mot est présent à partir de l'indice indice
            comparaison = memeMot(texte, motCherche, indice)
            if comparaison == -1:
                return indice
        indice = avancer(texte, motCherche, indice)
    return -1

## Fonction principale

def main():
    motCherche = "chat"
    texte = "les chats sont des felidés"
    texte2 = "croustichat"

    print(rechercheNaive(motCherche, texte))

    print(tableCorrespondance(motCherche))
    print(rechercheBoyerMoore(motCherche, texte))
    print(rechercheBoyerMoore(motCherche, texte2))
    
## Programme principal

if __name__ == '__main__':
    main()




