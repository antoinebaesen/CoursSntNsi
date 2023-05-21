## Importation des modules

from PIL import Image


## Déclaration des constantes

baseImage = Image.open('Exercice1.jpg')


## Déclaration des fonctions

def sans_rouge():
    pass

def afficherImage(image):
    """Affiche l'image dans une fenêtre"""
    image.show()

def sauvegarderImage(image, nomFichier):
    """Sauvegarde l'image dans un fichier"""
    image.save(nomFichier)

def appliquerFiltre(image, filtre):
    """Applique un filtre à une image"""
    for x in range(image.width):
        for y in range(image.height):
            image.putpixel((x,y), filtre(image.getpixel((x,y))))

def filtreRouge(pixel):
    """
    Retourne un pixel avec la composante rouge à 0
    @param pixel: le pixel à modifier
    @return: la valeur du pixel modifié
    """
    return (0, pixel[1], pixel[2])

def filtreGris(pixel):
    """
    Retourne un pixel avec une moyenne des composantes
    @param pixel: le pixel à modifier
    @return: la valeur du pixel modifié
    """
    moyenne = (pixel[0] + pixel[1] + pixel[2]) // 3
    return (moyenne, moyenne, moyenne)

def filtreNegatif(pixel):
    """
    Retourne un pixel avec les composantes inversées
    @param pixel: le pixel à modifier
    @return: la valeur du pixel modifié
    """
    return (255 - pixel[0], 255 - pixel[1], 255 - pixel[2])

def filtreNoirEtBlanc(pixel):
    """
    Retourne un pixel en noir ou blanc selon sa luminosité
    @param pixel: le pixel à modifier
    @return: la valeur du pixel modifié
    """
    luminosite = (pixel[0] + pixel[1] + pixel[2]) // 3
    if luminosite < 128:
        return (0, 0, 0)
    else:
        return (255, 255, 255)
    
def filtreUniquementRouge(pixel):
    """
    Retourne un pixel avec uniquement la composante rouge
    @param pixel: le pixel à modifier
    @return: la valeur du pixel modifié
    """
    return (pixel[0], 0, 0)

def chercherRouge(pixel):
    """
    Retourne un pixel en noir ou blanc si il n'est pas majoritairement rouge
    @param pixel: le pixel à modifier
    @return: la valeur du pixel modifié
    """
    if pixel[0] > pixel[1] and pixel[0] > pixel[2]:
        return (0, 0, 0)
    else:
        return (255, 255, 255)

## Fonction principale

def main():
    """Fonction principale"""
    #afficherImage(baseImage)
    appliquerFiltre(baseImage, chercherRouge)
    #afficherImage(baseImage)
    sauvegarderImage(baseImage, 'Exercice1_rouge.jpg')

## Programme principal

if __name__ == '__main__':
    main()

