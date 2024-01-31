# Installation

Il y a deux façons d'installer les dépendances pour le script:

1. La façon plus longue mais correcte:
- Vérifier qu'on a [pip](https://pypi.org/project/pip/) installé correctement
- Installer [pipenv](https://pipenv.pypa.io/en/latest/)
- Lancer la commande suivante pour installer les dépendances:
`pipenv install`
- Lancer la commande suivante (depuis le dossier du script) pour lancer le graphe:
`pipenv run python pendulum_plot.py`

2. La façon plus rapide mais moins perenne:
- Installez [numpy](https://numpy.org/) dans le `PATH` de votre installation Python
- Installez [matplotlib](https://matplotlib.org/) dans le `PATH` de votre installation Python
- Lancez `python pendulum_plot.py` normalement

# Utilisation
Pour l'instant, faut aller modifier le fichier `pendulum_plot.py` pour modifier ce qu'on graphe. Les commentaires indiquent à peu près ce qu'il faut modifier et où.