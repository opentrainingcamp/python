L’objectif de cet exercice est de programmer une recherche dans une liste triée.
1. Il faut d’abord récupérer un fichier texte disponible ici [texte](mot_par_ligne.txt)
. Ce fichier contient un mot par
ligne. Il faut lire ce fichier et construire une liste avec tous ces mots.
2. Construire une fonction qui vérifie que la liste chargée à la question précédente est triée.  
3. Construire une fonction qui recherche un mot X dans la liste et qui retourne sa position ou -1
si ce mot n’y est pas. Cette fonction prend deux paramètres : la liste et le mot à chercher. Elle
retourne un entier. On précise que pour savoir si deux chaînes de caractères sont égales, il faut
utiliser l’opérateur ==.  
4. Quels sont les positions des mots "UN" et "DEUX" ? La réponse doit figurer en commentaire
dans le programme. Il faudra écrire aussi le nombre de comparaisons effectuées pour trouver ces
deux positions.  
5. Lorsqu’une liste est triée, rechercher un élément est beaucoup plus rapide. Si on cherche le mot X
dans la liste, il suffit de le comparer au mot du milieu pour savoir si ce mot est situé dans la partie
basse (X inférieur au mot du milieu), la partie haute (X supérieur au mot du milieu). S’il est égal,
le mot a été trouvé. Si le mot n’a pas été trouvé, on recommence avec la sous-liste inférieure ou
supérieure selon les cas jusqu’à ce qu’on ait trouvé le mot ou qu’on soit sûr que le mot cherché n’y
est pas.
Le résultat de la recherche est la position du mot dans la liste ou -1 si ce mot n’a pas été trouvé.
Cette recherche s’appelle une recherche dichotomique.
Écrire la fonction qui effectue la recherche dichotomique d’un mot dans une liste triée de mots.
Vérifiez que les deux fonctions retournent bien les mêmes résultats. Cette fonction peut être récursive
ou non. Elle prend au moins les deux mêmes paramètres que ceux de la question 3, si elle en a
d’autres, il faudra leur donner une valeur par défaut. On précise que les comparaisons entre chaînes
de caractères utilisent aussi les opérateurs <, ==, >.  
6. Normalement, les positions des mots "UN" et "DEUX" n’ont pas changé mais il faut de nouveau déterminer le nombre d’itérations effectuées pour trouver ces deux positions avec la recherche
dichotomique.  
7. Quel est, au pire
, le coût d’une recherche non dichotomique ? La réponse doit figurer en commentaire dans le programme.
8. Quel est, au pire, le coût d’une recherche dichotomique ? La réponse doit figurer en commentaire
dans le programme. 