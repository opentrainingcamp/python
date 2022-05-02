<a href="https://colab.research.google.com/github/opentrainingcamp/python/blob/main/Notebook/fonctions/00_UnPeuPlus.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# Allons un peu plus loin, spécificités de Python

Préparation des notions qui noujs permettrons d'introduire 
le paradigme fonctionnel dans le contexte Python

* Closure
* and-or et booléen
* docstring
* paramètres par défaut
* signature de fonction (surcharge? polymorphisme?)
* ‘expression if’ vs ‘instruction if’
* iterable / générateur
* Les modules: Avec le chapitre sur les objets
* Les lambda, fonction de première classes : prochain chapitres
* Quelques exemples préparant la suite


# Closure


```
# Closure
def f():
  'x et y ne sont ni des paramètres ni des variable locale!'
  return x+y

# si vous faire f() il y aura une erreure car ni x, ni y sont défini
f()
```

Si vous définissez x et y, ça marche! x et y on été pris depuis le contexte... c'est la closure (la fermeture)


```
x=2
y=3
z=x+y
print(f(),z)
x=10
y=20

#z ne change pas mais le resultat de f() si
print(f(),z)
```

Remarque : La closure est un anti-pattern dans le paradigme fonctionnel, c'est même une réelle sourtce de bugs en paradigme impératif

## Expression Booléenne et Les expressions and et or : pythonique

En Python, `and` et `or` appliquent la logique booléenne comme vous pouvez l’attendre, mais ils ne retournent pas de valeurs booléennes, ils retournent une des valeurs comparées.

>Lorsqu’on utilise `and` ou `or` les valeurs sont évaluées dans un contexte booléen de gauche à droite. `0, '', [], (), {} et None` valent faux dans ce contexte, tout le reste vaut vrai.  
* Si toutes les valeurs valent vrai dans un contexte booléen, and retourne la dernière valeur, sinon rerourne la première valeure fausse
* or rtourne la première vraie, ou la drenière si toutes sont fausse. 





```
'a' and 'b'
```


```
0 and 'a'
```


```
if (0 and 'a'):
  print('T')
else:
  print('F')
```


```
if ('b'and 'a'):
  print('T')
else:
  print('F')
```


```
x = 'a' and 'b' and 'c'
```


```
x
```


```
y = 'a' and '' and 'c'
```


```
y
```


```
xo = 'a' or 'b' or 'c'
```


```
xo
```


```
def f():
  print('x')
  return 1
```


```
calcul = f() and f() and '' and f()
```


```
calcul
```


```
calculor = f() or f() or '' or f()
```


```
'a' or 'b'
```


```
0 and 'a'
```

## cas condition and e1 or e2
equivalent à si condition alor e1 sinon e2

Supposons que e1 et e2 ne soit pas interprété False.

Quand condition True:  True and e1 donne e1

Quand condition False: True and e1 est False on continue avec or et la réponse est e2


```
e1,e2 = 'string1', 'string2'
```


```
True and e1 or e2
```


```
False and e1 or e2
```


```
# ATTENTION
True and '' or e2
```


```
def uneCond(cond, exp1, exp2):
  ''' Nous utilisons return car c and e1 or e2 est une expression
  Return ne peut pas être utilisé avec une enstruction
  '''
  return cond and exp1 or exp2
```


```
print("Avec True", uneCond(True, e1, e2), "avec False", uneCond(False, e1, e2))
```

# Operateurs spalt * et **


```
x = ['A', 'B']
y = ('C', 'D')
z = [*x, *y]
print (z)


d1={0: 'A', 1: 'B', 'c': 'C', 'd': 'D'}
d2={'v1':'Data v1', 'v2':2, 1.0:'pourquoi pas'}
print(*d1)
print([*d1,*d2])
print({**d1,**d2})
```

## Unpacking dans le détail, l'opérateur * un peu étrange

* \* pour la multiplication des nombres,
* mais \* avec les listes ça donne quoi?


```
# soit la liste lst
lst = [1, 2, 3]
```

## lst * nombre ?

créer nouvelle liste en répétant `nombre` fois la liste `lst`


```
# exemple
lst * 3
```

lst contient 3 élément que se passe t'il si on fait


```
a, b, c = lst
```

Python intègre une fonctionnalité, l’unpacking, qui permet de prendre chaque élément d’un itérable et de les attribuer à des variables distinctes, d’un seul coup. C’est un raccourci très pratique :


```
print(a, b, c)
```


```
# moins de varibales
ma, mb = lst
```


```
#plus de variables
pa, pb, pc, pd = lst
```

### utilisation de * pour capturer le reste de la liste


```
#mais
tete, *reste = lst
```


```
print("tete=", tete, "reste=", reste)
```

# utilisation de * pour forcer le unpacking



```
# Soit l1, l2
l1 = [1, 2]
l2 = [3, 4]
```


```
# si on fait
l = [l1, l2]

# On obtient une liste l de 2 éléments composés de la liste l1 et la liste l2
l
```


```
# Par contre si on utilise 
lunpack = [*l1, *l2]

#On a 4 éléments l1 et l2 éyant été "unpacked" 
lunpack
```

## Le unpack de dictionnaire le double * (**)


```
d1 = { 'a': 'vala', 2: 'val2', 'trois': 3, 10:100}
d2 = { 'b': 'valb', 20: 'val20', 'trois': 3, 100:1000}


d= {**d1, **d2}
d
```

## Utilisation utile avec les fonctions

### paramétres par défaut


```
# dans cet exemple
def f(x, y=10):
  return x+y

```

si on appel la fonction f avec un seul paramétre y prendra a valeur 10 par défaut 

***(attention dans la définition des paramétres ou l'appel l'opérateur `=` n'est pas une affectation!)***


```
f(1)
```


```
f(1,100)
```

#### plusieurs paramétres par défauts


```
def plusf(x=1, y=2, z=3):
  print(x, y, z)
  return x+y+z
```


```
print(plusf(), plusf(10), plusf(10, 20), plusf(z=30))
```

### paramétres variables

La syntaxe *params (remplacez “params” par ce que vous voulez) permet d’indiquer lors de la définition d’une fonction que notre fonction peut accepter un nombre variable d’arguments. Ces arguments sont intégrés dans un tuple. On va pouvoir préciser 0, 1 ou plusieurs paramètres classiques dans la définition de la fonction avant la partie variable.


```
# exemple
def somme(*params):
  print(params)
  s = 0
  for e in params:
    s += e
  return s
```


```
print(somme(1), somme(1,2,3,4), somme())
```

De façon alternative, la syntaxe **kwargs (remplacez “kwargs” par ce que vous voulez) permet également d’indiquer que notre fonction peut recevoir un nombre variable d’arguments mais cette fois-ci les arguments devront être passés sous la forme d’un dictionnaire Python.


```
def kf(**kargs):
  print(kargs)

kf(a=1, b=3, c=4)
```

kargs est un dictionnaire!


```
# plus généralement
def vkf(*p, **ps):
  print("varibale", p, "nommés", ps)

vkf(1,2,3,4,5,x=1,y=2,z=3)
```

### nous utiliserons tout ceci bientôt dans le paradigme fonctionnel pure.... en particulier pour définir des décorateurs... 

# expression if vs instruction if


```
# l'intruction if
def est_paire_ou_impaire(x):
  res = ''
  if x%2:
    res = 'impaire'
  else:
    res = 'paire'
  return res
```


```
print(est_paire_ou_impaire(11))
print(est_paire_ou_impaire(12))
```


```
# l'expression if
def paire_ou_impaire(x):
  return 'impaire' if x%2 else 'paire'
```


```
print(paire_ou_impaire(11))
print(paire_ou_impaire(12))
```


```
# comme c'est une expression on peut l'utiliser comme tel
x=11
(1 if x%2 else 0) + x
```


```
x=12
(1 if x%2 else 0) + x
```

# List comprehention


Un bon développeur cherchera toujours à augmenter sa productivité avec le temps. Il existe des astuces python qui permettent d'optimiser le code .

Une de ces astuces est la compréhension de liste (ou liste en compréhension ou list comprehension ).

Pour le moment l'idée est simple: simplifier le code pour le rendre plus lisible et donc plus rapide à écrire et plus simple à maintenir.

nous verrons que la liste comprehention est un filter, map, nous y reviendrons 

### syntaxe

```python
new_list = [function(item) for item in list if condition(item)]
```

### Un premier exemple : filter une liste


```
l = [1, 10, 50, 3, 10, 20, 2, 8, 11, 101]
```

recuperer une liste avec les valeurs > 10

On aurait


```
def plusque(l,n):
  res = []
  for e in l:
    if (e > n):
      res.append(e)
  return res

```


```
plusque(l,10)
```


```
# avec liste comprehention
[e for e in l if e>10]
```


```
def plusque_c(l, n):
  return [e for e in l if e>n]
```

## Un deuxième exemple : Exécuter une fonction sur chaque item d'une liste
Prenons l'exemple d'une conversion de string en integer de plusieurs items:


```
lstr = ["10", "20", "30"]
[int(s) for s in lstr]
```

### Que donne ces 'comprehention liste's?


```
[(x,y) for x in range(3) for y in range(3)]
```


```
[(x,x**2) for x in range(10+1)]

[x for x in range(10+1) if x%2 == 0]

[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]


[num for elem in [[1,2,3], [4,5,6], [7,8,9]] for num in elem]

[num for elem in [[1,2,3], 4, [5,6,7]] if isinstance(elem,list) for num in elem ]

((x,x**3) for x in range(10+1))

(x for x in range(10+1) if x%2 == 1)

{x for x in 'abracadabra' if x not in 'abc'}

{x:'paire' for x in range(10+1) if x%2 == 0}
```
