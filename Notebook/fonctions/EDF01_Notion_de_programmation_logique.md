<a href="https://colab.research.google.com/github/opentrainingcamp/python/blob/main/Notebook/fonctions/EDF01_Notion_de_programmation_logique.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

Ce document est un Notebook autoformant, entre le cours et l’exercice. L’objectif est de vous introduire par l’exemple des fondamentaux du paradigme fonctionnel.

# Les closures (fermeture)

Variable utilisé dans une fonction, ni paramètre, ni locale.

## Variable paramètre


```python
def fp(x):
  '''Ici x est un paramètre'''
  return x+1
```


```python
fp(1)
```




    2




```python
# que donne ceci?
x=10
fp()
```

<font color="red">@TODO1 expliquer pourquoi d'après vous.<font>

## Variable locale


```python
def fl():
  x=0
  return x+1
```


```python
# Que donne ceci cette fois ci
x=10
fl()
```

<font color="red">@TODO2 expliquer pourquoi d'après vous.<font>

## Fermeture (closure)



```python
# Closure
def f():
  'y et z ne sont ni des paramètres ni des variable locale!'
  return z+y

# si vous faire f() que se passe t'il?
f()
```

<font color="red">@TODO3 expliquer pourquoi d'après vous.<font>


```python
# Essayer ceci
z=2
y=3
w=z+y
print(f(),w)
z=10
y=20

#w ne change pas mais le resultat de f() si
print(f(),w)
```

<font color="red">@TODO4 expliquer pourquoi d'après vous.<font>

## Une utilisation des closures


Les closure sont source de bug car ils introduisent un effet qui pourrait être non prévisible. 
Mais cette notion permet de définir des fonctions dynamiquement, par exemple


### Fonction qui définit une autre fonction
Nous y reviendrons en déatil quand nous définirons la notion de lambda fonction


```python
#soit 
def poly(a, b):
  def app(x):
    return a*x+b
  return app
```

<font color="red">@TODO5 Quel est le résultat de ploly(1,1) par exemple<font>


```python
poly(1,1)
```

<font color="red">@TODO6 Une explication?<font>

La fonction poly revoie queqlues chose qui semble être elle même une fonction

En effet elle renvoie une fonction permettant de définir un polynome de premier degré ax+b


```python
# définir le polynome 2x+3
p1 = poly(2,4)
```

<font color="red">@TODO7 Que donne p1(1)?<font>


```python
p1(1)
```

<font color="red">@TODO8 Que donne p1(1) expliquer pourquoi?<font>

<font color="red">@TODO9 Definir dans une cellule le polynome -x+1</font>


```python
# definir polynome -x+1 ici
```

<font color="red">@TODO10 Exercice final</font>
Ecrire la fonction qui génère la fonction pour calculer des polynome de second degré $ax^2+bx+c$


```python
# Code de todo10
```
