# TP2 

## 1 

![alt text](../outputs/smoke.png)

Tout a fonctionné parfaitement du premier coup ! 

## 2

CONFIG: {'model_id': 'stable-diffusion-v1-5/stable-diffusion-v1-5', 'scheduler': 'EulerA', 'seed': 42, 'steps': 30, 'guidance': 7.5}

![alt text](../outputs/baseline.png)

## 3

| Expérience | Image | Paramètre Clé |
| :--- | :---: | :--- |
| **01. Baseline** | ![Baseline](../outputs/t2i_run01_baseline.png) | EulerA, 30 steps, G=7.5 |
| **02. Steps Bas** | ![Steps 15](../outputs/t2i_run02_steps15.png) | 15 steps (Rapide) |
| **03. Steps Haut** | ![Steps 50](../outputs/t2i_run03_steps50.png) | 50 steps (Précis) |
| **04. Guidance Bas** | ![Guid 4](../outputs/t2i_run04_guid4.png) | G=4.0 (Libre) |
| **05. Guidance Haut** | ![Guid 12](../outputs/t2i_run05_guid12.png) | G=12.0 (Strict) |
| **06. Scheduler** | ![DDIM](../outputs/t2i_run06_ddim.png) | DDIM (Différent) |

La variation du nombre d'étapes révèle une différence notable dans la qualité des images générées. À 15 steps, les couleurs et lumières sont imparfaites, les jantes manquent de netteté et les logos sont peu détaillés. En augmentant à 50 steps, ces éléments deviennent bien définis, mais les phares présentent un effet de tourbillon. Avec une guidance de 4, l'image est réaliste avec des détails maîtrisés. En revanche, une guidance élevée (12) donne un rendu moins naturel, avec un style plus cartoonesque. Le scheduler DDIM entraîne une inversion de la position de la voiture, une texture trop lisse et une perte de réalisme dans les détails, notamment avec un fond modifié par rapport à la baseline.


## 4 

Image source (avant) :

![](../outputs/i2i_source.png)

Résultats :

- strength = 0.35  
![](../outputs/i2i_run07_strength035.png)

- strength = 0.60  
![](../outputs/i2i_run08_strength060.png)

- strength = 0.85  
![](../outputs/i2i_run09_strength085.png)


Les structures et formes globales demeurent constantes entre strength 035 et 085, avec des couleurs retranscrites dans le même thème que l'image initiale. Cependant, la guitare est progressivement remplacée par les caractéristiques dominantes de la tour Eiffel, avec son manche prenant l'apparence de ses structures distinctives. Une inscription évoquant "Paris" semble également être ajoutée.

Ces transformations illustrent le potentiel créatif pour la génération d'images commerciales, permettant des ajustements visuels tels que des effets spéciaux, des modifications de fonds ou la correction directe d'anomalies sans recours à un montage complexe.


## 5