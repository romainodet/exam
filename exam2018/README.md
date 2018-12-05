# LE JEU

Ce projet est un mini jeu de PACMAN en mode texte.
PACMAN se déplace dans un niveau 2D, son but étant de manger toutes les pac-gommes sans se faire manger.
Quand PACMAN a mangé toutes les pac-gomme le joueur a gagné.

Le niveau est composé des éléments suivants :

- 'C' Le joueur (PACMAN !)
- 'X' Ennemi(s)
- '#' mur (PACMAN et les ennemis ne peuvent pas passer a travers !)
- '.' pac-gomme (miam !)
- 'o' super-gomme, PACMAN devient invincible et il peut manger les ennemis

Le joueur utilise les touches suivantes pour se déplacer :

- 'L' ou 'l' pour aller à gauche
- 'R' ou 'r' pour aller à droite
- 'U' ou 'u' pour aller en haut
- 'D' ou 'D' pour aller en bas

Au départ, PACMAN se trouve à la position (1,1).

La position de PACMAN est stockée dans une liste à 2 éléments représentant l'abscisse et l'ordonnée.
L'origine est situé en haut à gauche, les coordonnées sont donc toujours positives.

Le jeu se termine 
 - quand PACMAN rencontre un ennemi => le joueur perd
 - quand PACMAN a mangé toutes les pac-gommes => le joueur gagne

Le jeu est en rafraîchissement lent, c'est à dire qu'après chaque déplacement de PACMAN, le programme affiche
le niveau avec tous les personnages.

Je vous fourni un code de base (presque) fonctionnel, à vous de jouer maintenant !

# VOTRE TRAVAIL

Créer un projet dans PyCharm, avec ce README et le code de base en python.
**Vous devrez uniquement modifier ces 2 fichiers.**

Vous allez devoir implémenter un maximum de fonctionnalités.
Quand vous avez terminé une fonctionnalité (c'est à dire que vous l'avez **testée** !),
marquez là dans ce fichier README avec deux tildes (~) en début de ligne et deux tildes en fin (sans espace) :
~~- E0. Lire le code~~

En fin d'examen, déposez sur moodle une archive zip portant votre nom, avec votre programme python et votre fichier README.md.
Vous pouvez proposer une fonctionnalité par niveau de difficulté.

Pour valider le module, vous devez amasser au minimum **18 points**.
Avant de commencer les fonctionnalités modérées et avancés, vous **devez** implémenter toutes les fonctionnalités faciles.

## Fonctionnalités facile (2 pt)

- ~~E1. Afficher un message en **vert** au début de votre programme.~~
- ~~E2. Changer le niveau (ne mettez pas trop de gommes pour que vos tests ne soient pas trop longs !).~~
- ~~E3. Demander son age au joueur, si il a moins de 12 ans quitter, sinon continuer.~~
- ~~E4. L'utilisateur peut quitter le jeu en tapant 'q' ou 'Q' comme déplacement.~~
- ~~E5. Vérifier, dans la fonction 'get_case_content' que la position donnée ne sort pas du niveau, si cela sort, retourner `None`.~~
- ~~E6. Compléter la fonction `move_pacman` de sorte que PACMAN se déplace vraiment.
  * INDICE => Cette fonction est très similaire à la fonction  `remove_gum_from_map`~~
- E7. Afficher le nombre de pac-gomme mangées en fin de jeu.
- E8. Implémenter la fin "PACMAN gagne" 
  * INDICE => Compter le nomb~~~~re de '.' dans le niveau, si PACMAN a mangé ce nombre de pac-gomme il a gagné !
- E9. Quand PACMAN mange une super-gomme, il devient invincible et il peut manger les ennemis.
  * INDICE => C'est très similaire à quand PACMAN mange les pac-gommes !
- E10. Afficher le nombre d'ennemi mangés en fin de partie.
- E11. _votre fonctionnalité ici_

## Fonctionnalités modérés (4 pt)

- M1. Quand PACMAN mange une super-gomme il devient bleu et les ennemis deviennent rose
- M2. Gérer un nouveau type de case `B`, quand PACMAN passe dessus, il peut manger les murs (et donc passer à travers !)
  * INDICE => Attention cela ne concerne que PACMAN, pas les ennemis
- M3. Après chaque déplacement de PACMAN, l'ennemi se déplace aléatoirement (sans passer a travers les murs!)
  * INDICES => L'ennemi se déplace dans une des directions principales (haut, bas, gauche ou droite).
  * INDICES => Dans un premier temps, l'ennemi va manger aussi les gommes, super-gommes et autre bonus, tant pis !
  * INDICES => L'ennemi peut, bien entendu, manger PACMAN et alors le joueur perd !
  * INDICES => Attention à ne plus faire bouger l'ennemi quand PACMAN l'a mangé !
- M4. _votre fonctionnalité ici_

## Fonctionnalités avancées (6 pt)

- A1. _valable uniquement si M3 fait_ Gérer le déplacement des ennemis sans qu'ils mangent les gommes, super-gommes et autres bonus 
  * INDICE => Vous pouvez par exemple utiliser 2 représentations du niveau, une sans les personnages mobiles et une avec.
- A2. _valable uniquement si M3 et A1 fait_ Gérer plusieurs ennemis (paramétrable)
  * INDICE => la position de l'ennemi va devenir une liste de positions des différents ennemis
- A3. Le(s) ennemi(s) se rapproche de PACMAN quand il(s) se déplace(nt) (laisser la fonction de M3 en commentaire dans votre code)
  * INDICE => Pour chaque ennemi prenez la direction qui minimize la distance avec PACMAN !
- A4. _votre fonctionnalité ici_

# CONSEILS

- Lisez d'abord le code de base en entier pour bien le comprendre
- Prenez en particulier le temps de lire les commentaires !
- Si vous avez trop d'erreur, n'hésitez pas à retélécharger le code original et recommencer !
- Attention le niveau n'est pas stocké de la meme manière que dans le projet labyrinthe !
- Je vous conseil (sans vous l'imposer) d'implémenter les fonctionnalités dans l'ordre, meme si il y a peu de dépendances
- Prenez soin de l'interface utilisateur (messages, gestion des erreurs, etc.)
- Si vous voulez afficher des messages de debug, utiliser la fonction `debug_text`
