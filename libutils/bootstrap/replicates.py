'''
Ensemble de fonctions pour générer des bootstrap

Simuler des échantillons aléatoires à partir d'un échantillon

En Statistiques, les techniques de bootstrap sont des méthodes d'Inférence statistique modernes, 
datant de la fin des années 70, et requérant des calculs informatiques intensifs. L'objectif est de 
connaître certaines indications sur une statistique : son estimation bien sûr, mais aussi la dispersion 
(variance, écart-type), des intervalles de confiance voire un Test d'hypothèse. Cette méthode est basée sur 
des simulations, comme les méthodes de Monte-Carlo, les méthodes numériques bayésiennes (échantillonneur de 
Gibbs (en), l'algorithme de Metropolis-Hastings (en)), à la différence près que le bootstrap ne nécessite pas 
d'information supplémentaire que celle disponible dans l'échantillon. En général, il est basé sur 
de « nouveaux échantillons » obtenus par tirage avec remise à partir de l'échantillon initial 
(on parle de ré-échantillonnage).

L'aspect autocentré et itératif de la méthode a inspiré sa désignation anglaise : 
en effet, le bootstrap désigne le fait de « se hisser en tirant sur ses propres lacets ou 
plus précisément sur ses « bootstraps » qui désignent en anglais les anneaux de cuir ou tissu cousus 
au rebord des bottes pour y passer les doigts afin de les enfiler plus facilement ».
'''

def bootstrap_replicate_1d(data, func):
    """Générez une réplication bootstrap des données 1D.
    
    Params:

    data : l’échantillon d'origine
    func : la fonction (propriété) à appliquer par exemple moyenne, ecart-type etc...
    
    Return:
            function appliqué à un échantillon aléatoire avec remise issue de data
    """
    bs_sample = np.random.choice(data, len(data))
    return func(bs_sample)

def draw_bs_reps(data, func, size=1):
    """Tirages de size replications bootstrap."""

    # Initialize array of replicates: bs_replicates
    bs_replicates = np.empty(size)

    # Generate replicates
    for i in range(size):
        bs_replicates[i] = bootstrap_replicate_1d(data, func)

    return bs_replicates
