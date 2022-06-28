### Taux de guérison suite à un nouveau traitement

Considérons ce premier cas, qu’on peut qualifier de **discret** :

Un laboratoire cherche à savoir si la nouvelle composition du médicament (contre une maladie bénigne) qu’il compte commercialiser améliore le taux de guérison par rapport à un médicament déjà sur le marché.

Des tests cliniques ont été effectués sur $\\(n = 216\\)$ individus sur lesquels on a observé la guérison (notée 1 ) ou la non-guérison (notée 0) :

$$ \left\{ x_1,\ldots,x_{216} \right\} = \left\{ 1,0,1,1,\ldots,1,0\right\}$$

$x_i$ désigne l’observation de la guérison ou non pour l’individu $i$ .

Le laboratoire observe au total 167 guérisons, soit environ 77,3% de guérisons.

Le laboratoire s’adresse à un data analyst pour répondre à plusieurs de ses interrogations :

1.  Il aimerait connaître le _taux de guérison_ (théorique) $p$ suite à la prise de son  
    médicament.
    
2.  Le laboratoire étant conscient que le taux de guérison théorique sera délicat à  
    appréhender parfaitement, il souhaiterait disposer d’une _fourchette_ de ce taux  
    de guérison.
    
3.  Enfin, il aimerait vérifier que son nouveau médicament est (significativement) _meilleur_  
    que celui actuellement sur la marché dont le taux de guérison avéré est $p_0 = 0.75$  
    (75%).
    

Notons que l’éventuelle autorisation de mise sur le marché de ce médicament repose sur une procédure plus complexe. Si cela vous intéresse, voyez : [http://ansm.sante.fr/Activites/](http://ansm.sante.fr/Activites/%20Autorisations-de-Mise-sur-le-Marche-AMM/L-AMM-et-le-parcours-du-medicament/)  
[Autorisations-de-Mise-sur-le-Marche-AMM/L-AMM-et-le-parcours-du-medicament/](http://ansm.sante.fr/Activites/%20Autorisations-de-Mise-sur-le-Marche-AMM/L-AMM-et-le-parcours-du-medicament/)

L'échantillon dont vous aurez besoin pour tester les lignes de codes est à télécharger ici : [guerison.txt](https://s3-eu-west-1.amazonaws.com/course.oc-static.com/courses/4525306/guerison.txt)


### Consommation d’essence de cars

Considérons ce second cas, qu’on peut qualifier de **continu, par opposition à "discret"**.

Un constructeur de cars souhaite appréhender la consommation d’essence de son dernier modèle. Pour cela, il lance un protocole d’essais sur 128 cars et recueille leur consommation d’essence en litres après avoir parcouru 100 km (appelée _nombre de litres aux 100_) :

$\left\{x_1,\ldots,x_{128}\right\}=\left\{26.23,26.40,26.85,\ldots,35.50,35.50,36.07\right\}$

Pour information, la consommation moyenne observée est égale à 31.45 litres aux 100.

Le constructeur s’adresse à un data analyst pour répondre à plusieurs de ses interrogations :

1.  Il aimerait connaître la consommation (théorique) d’essence $\mu$ de son modèle de car.
    
2.  De manière plus modeste, il souhaiterait également disposer d’un intervalle autour de cette consommation, il l’aura en effet évalué sur un nombre limité de véhicules et de trajets.
    
3.  Enfin, il souhaiterait communiquer auprès de ses clients sur un chiffre ambitieux :  
    une consommation égale à $\mu_0 = 31$ litres aux 100.
    

L'échantillon dont vous aurez besoin pour tester les lignes de codes est à télécharger ici : [essence.txt](https://s3-eu-west-1.amazonaws.com/course.oc-static.com/courses/4525306/essence.txt)
