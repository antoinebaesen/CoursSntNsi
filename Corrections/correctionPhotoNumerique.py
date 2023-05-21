## Importation des modules

from PIL import Image
from random import randint

## Déclaration des constantes

baseImage = Image.open('Exercice1.jpg')

## Déclaration des fonctions

def filtreSansRouge(pixel):
    """
    Retourne un pixel avec la composante rouge à 0
    @param pixel: le pixel à modifier
    @return: la valeur du pixel modifié
    """
    return (0, pixel[1], pixel[2])

def filtreSansVert(pixel):
    """
    Retourne un pixel avec la composante verte à 0
    @param pixel: le pixel à modifier
    @return: la valeur du pixel modifié
    """
    return (pixel[0], 0, pixel[2])

def filtreQueRouge(pixel):
    """
    Retourne un pixel avec les composantes verte et bleue à 0
    @param pixel: le pixel à modifier
    @return: la valeur du pixel modifié
    """
    return (pixel[0], 0, 0)

def filtreNB(pixel):
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

def nouvelleImageAleatoire(largeur, hauteur):
    """Retourne une image de la taille spécifiée remplie de pixels aléatoires"""
    image = Image.new('RGB', (largeur, hauteur))
    for x in range(largeur):
        for y in range(hauteur):
            image.putpixel((x,y), (randint(0,255), randint(0,255), randint(0,255)))
    return image

def sauvegarderImage(image, nomFichier):
    """Sauvegarde l'image dans un fichier"""
    image.save(nomFichier)

def appliquerFiltre(image, filtre):
    """Applique un filtre à une image"""
    for x in range(image.width):
        for y in range(image.height):
            image.putpixel((x,y), filtre(image.getpixel((x,y))))

## Fonction principale

def main():
    """Fonction principale"""
    appliquerFiltre(baseImage, filtreNB)
    baseImage.show()
    # sauvegarderImage(baseImage, 'Exercice1_rouge.jpg')
    # nouvelleImage = nouvelleImageAleatoire(100, 100)
    # nouvelleImage.show()

## Programme principal

if __name__ == '__main__':
    main()
