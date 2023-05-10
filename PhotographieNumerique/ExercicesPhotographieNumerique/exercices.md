
# Exercices : Photographie numérique

## Exercice 1

> Pour utiliser une image dans un programme python on peut utiliser la bibliothèque PIL (Python Imaging Library). Cette bibliothèque permet de lire et d'écrire des images dans de nombreux formats.

Pour installer la bibliothèque PIL, il faut taper la commande suivante dans un terminal :

```bash
pip install pillow
```

Voici un exemple d'utilisation de la bibliothèque PIL pour lire une image :

```python
from PIL import Image

# Charger l'image à partir du fichier
image = Image.open('Exercice1.jpg')

# Afficher les dimensions de l'image
print(image.size)

# Afficher le premier pixel de l'image
print(image.getpixel((0, 0)))

# Modifier le premier pixel de l'image
image.putpixel((0, 0), (255, 0, 0))

# Sauvegarder l'image modifiée dans un nouveau fichier
image.save('Exercice1_resultat.jpg')
```

> Ce programme est disponible dans le fichier [ExempleUtilisationPil.py](ExempleUtilisationPil.py)

Ecrire un programme pour récupérer la couleur du pixel en position (2, 2) de l'image `Exercice1.jpg`

---

## Exercice 2

Pour convertir une image en noir et blanc, il faut remplacer la valeur de chaque pixel par la moyenne des valeurs RVB du pixel.

Par exemple, le pixel (255, 0, 0) devient (85, 85, 85) car (255 + 0 + 0) / 3 = 85

Ecrire un programme pour convertir l'image `Exercice1.jpg` en noir et blanc et sauvegarder le résultat dans un nouveau fichier `Exercice2.jpg`

---

### Exercice 3

```python
# Pour créer une nouvelle image :
image2 = Image.new('RGB', (100, 100), (255, 255, 255))

image2.save('Exercice3.jpg')
```

Ecrire un programme pour créer une image de 100x100 pixels que vous remplirez avec des pixels de couleur aléatoire.

---
