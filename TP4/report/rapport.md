# Exercice1

## A 

(env) user@w-yboutkri:~/projects/deeplearning-advanced$ tree -L 3 TP4
TP4
├── config
│   ├── baseline_mlp.yaml
│   ├── gcn.yaml
│   └── sage_sampling.yaml
├── rapport.md
└── src
    ├── smoke_test.py
    └── utils.py

3 directories, 6 files

## E

![alt text](img/image-1.png)


# Exercice2

## G

Les métriques des 3 datasets sont calculées séparément afin de s'assurer qu'il n'y ait pas de fuite de données, comme un entraînement du modèle sur les données de test. Cela permet également d'évaluer si le modèle généralise bien ou s'il sur-apprend les données de validation.

## H

![alt text](img/image-2.png)

# Exercice3

## E 

![alt text](img/image-3.png)

## F

Le GCN surpasse nettement le MLP sur le dataset Cora, présentant une amélioration de 23 %, car il intègre la structure du graphe plutôt que d'analyser chaque document isolément. Ce dataset présente une forte homophilie, indiquant que les articles reliés par des citations traitent fréquemment du même sujet. Le GCN exploite les informations des voisins pour affiner et compléter les caractéristiques textuelles parfois partielles. Il s'appuie sur le contexte relationnel du graphe pour pallier les insuffisances lorsque les mots clés d'un document ne suffisent pas pour une classification précise.


# Exercice4

## E 

![alt text](img/image-4.png)

## F

Le neighbor sampling est principalement utilisé pour limiter l'explosion combinatoire en restreignant le nombre de voisins explorés grâce au fanout. Cela permet d'effectuer l'entraînement sur des mini-batchs de taille fixe au lieu de charger l'intégralité du graphe en mémoire, ce qui rend le processus d'entraînement plus rapide. Cependant, il est essentiel de surveiller l'impact sur le CPU lors de la génération des sous-graphes.

En revanche, le tirage aléatoire des voisins introduit inévitablement du bruit dans l'estimation du gradient, augmentant la variance de l'apprentissage. Cela affecte particulièrement les noeuds hubs, car une grande partie de leurs connexions est ignorée. En définitive, il s'agit d'un compromis entre la scalabilité sur des datasets volumineux et la précision optimale que fournirait un GCN complet.

# Exercice5

