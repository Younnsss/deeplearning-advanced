# TP5

## 1

### b

(env) user@w-yboutkri:~/projects/deeplearning-advanced$ python TP5/random_agent.py 
Espace d'observation (Capteurs) : Box([ -2.5        -2.5       -10.        -10.         -6.2831855 -10.
  -0.         -0.       ], [ 2.5        2.5       10.        10.         6.2831855 10.
  1.         1.       ], (8,), float32)
Espace d'action (Moteurs) : Discrete(4)

--- RAPPORT DE VOL ---
Issue du vol : CRASH DÉTECTÉ 💥
Récompense totale cumulée : -164.64 points
Allumages moteur principal : 15
Allumages moteurs latéraux : 58
Durée du vol : 105 frames
Vidéo de la télémétrie sauvegardée sous 'random_agent.gif'

---

![alt text](report/random_agent.gif)

On constate que le score de -300 est largement inférieur au score moyen de 200, indiquant que l'agent n'a pas encore atteint une maîtrise satisfaisante de l'environnement.

## 2

### b

![alt text](report/trained_ppo_agent.gif)

L'agent a atteint un score de 200 points, validant ainsi sa maîtrise de l'environnement. Au cours de l'entraînement, on a observé une progression constante de ep_rew_mean, à l'exception de quelques périodes de stagnation. La durée de vol, supérieure à celle du premier cas, ainsi que la fréquence élevée d'allumage des moteurs, illustrent le contrôle précis de l'agent sur les actions en fonction de son état actuel.

## 3

### b

--- RAPPORT DE VOL PPO HACKED ---
Issue du vol : CRASH DÉTECTÉ 💥
Récompense totale cumulée : -130.63 points
Allumages moteur principal : 0
Allumages moteurs latéraux : 51
Durée du vol : 81 frames
Vidéo du nouvel agent sauvegardée sous 'hacked_agent.gif'
(env) user@w-yboutkri:~/projects/deeplearning-advanced$ 

![alt text](report/hacked_agent.gif)


L'allumage du moteur principal entraîne une pénalité de 50 points sur la récompense. Ainsi, l'agent favorise l'évitement total de son utilisation, même si cela implique un crash avant d'atteindre la destination. En suivant cette stratégie, le score serait de -6250.

## 4

### b

--- RAPPORT DE VOL PPO (GRAVITÉ MODIFIÉE) ---
Issue du vol : CRASH DÉTECTÉ 💥
Récompense totale cumulée : -96.45 points
Allumages moteur principal : 27
Allumages moteurs latéraux : 175
Durée du vol : 203 frames
Vidéo de la télémétrie sauvegardée sous 'ood_agent.gif'

![alt text](report/ood_agent.gif)

L'expérience a totalement échoué en raison du changement d'environnement. L'agent, incapable de s'adapter, ne parvient pas à se stabiliser et continue d'utiliser son moteur latéral inutilement.

## 5

- Ajouter une variable aléatoire pour modifier la gravité présente.
- Introduire un taux d'aléatoire influençant la réussite de l'utilisation des moteurs.
