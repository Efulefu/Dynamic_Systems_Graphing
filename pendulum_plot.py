import matplotlib.pyplot as plt
import numpy as np

w = 10
Y, X = np.mgrid[-w:w:25j, -w:w:25j]

# X est l'angle, donc -sin(X) donne une action du poids
# Y est la vitesse angulaire, donc -0.2 * Y donne une force de frottement qui
# agit toujours contre le mouvement
# et donc V est la composante vitesse angulaire du vecteur de trajectoire du système
V = -np.sin(X) - 0.2 * Y # composante du vecteur résultant sur l'axe vertical
# et U la composante position du vecteur de trajectoire
U = Y # composante du vecteur résultant sur l'axe horizontal
speed = np.sqrt(U**2 + V**2)

fig, axs = plt.subplots(1, 2, figsize=(15, 8))

# Système pendule avec frottements
strm = axs[0].streamplot(X, Y, U, V, density=3, color=speed)
fig.colorbar(strm.lines)

# deuxième système pour s'amuser à faire des comparaisons
_V = -np.sin(X) - np.sin(2.5*X)
_U = Y

_speed = np.sqrt(U**2 + _V**2)

strm = axs[1].streamplot(X, Y, _U, _V, density=3, color=_speed)
fig.colorbar(strm.lines)

plt.tight_layout()
plt.show()