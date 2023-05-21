def tableCorrespondance(mot):
    """
    Renvoi un dictionnaire représentant la table de correspondance associée au mot.
    @Args: mot: str
        le mot dont on veut la table de correspondance
    @Returns: dict
        la table de correspondance associée au mot
    """

    # à compléter ...

def memeMot(texte, mot, indice):
    """
    Verifie à partir de l'indice de dernier charactère si le mot est le même.

    @Args: texte: str
        le texte dans lequel on effectue la recherche
    @Args: mot: str
        le mot recherché
    @Args: indice: int
        l'indice du dernier charactère du mot dans le texte
    @Returns: bool
        renvoie True si le mot est le même
    """

    # à compléter ...

def recherche_mot_boyer(texte, mot):
    """
    Recherche un mot dans un texte avec l'algo de boyer-moore

    @Args: texte: str
        le texte dans lequel on effectue la recherche
    @Args: mot: str
        le mot recherché
    @Returns: bool
        renvoie True si le mot est trouvé
    """
    
    N = len(texte)
    n = len(mot)
    
    # création de notre dictionnaire de décalages
    décalages = tableCorrespondance(mot)
    
    # on commence à la fin du mot
    i = n - 1
    # et on avance jusqu'à la fin du texte
    while i < N:
        # on récupère le caractère actuel sur lequel on est
        lettre = texte[i]
        if lettre == mot[-1]:
            # On vérifie que le mot est là avec un slice sur texte
            # On pourrait faire un while
            if texte[i-n+1:i+1] == mot:
                return True
            if memeMot(texte[i-n+1:i+1], mot):
                return True
            
        # on décale selon la table de correspondance
        if lettre in décalages.keys():
            i += décalages[lettre]
        else:
            i += n
        
    return False