# TP1

## 1

### c

le lien du dépot : https://github.com/Younnnsss
endroit d'exécution : slurm


└── TP1
    ├── data
    │   └── images
    ├── outputs
    │   ├── logs
    │   └── overlays
    ├── README.md
    ├── report
    │   └── report.md
    ├── requirements.txt
    └── src
        ├── app.py
        ├── geom_utils.py
        ├── sam_utils.py
        └── viz_utils.py

### e

Résultat de la commande : 
torch 2.10.0+cu128
cuda_available True
device_count 1

### g

yboutkrida@arcadia-slurm-node-1:~$ python -c "import streamlit, cv2, numpy; print('ok'); import segment_anything; print('sam_ok')"
ok
sam_ok

### i

port choisi : 8888

![alt text](image-1.png)

UI accessible via SSH tunnel : oui

## 2

### b

im1.jpeg — Objet unique bien visible sur fond simple (cas simple, segmentation facile).
im2.jpeg — Objet principal complexe mais isolé (PC), bon contraste global.
im4.jpeg — Scène de rue avec plusieurs objets et arrière-plan chargé (cas complexe).
im6.jpeg — Cuisine avec de nombreux éléments et plans visuels (cas chargé).
im7.jpeg — Grillage fin et répétitif, contours difficiles à segmenter (cas difficile).

## 3

Model : sam_vit_h_4b8939.pth

yboutkrida@arcadia-slurm-node-1:~/deeplearning-advanced$ python TP1/src/quick_test_sam.py 
img (189, 267, 3) mask (189, 267) score 0.8512305021286011 mask_sum 9058

L'inférence s'exécute correctement : le modèle `sam_vit_h_4b8939.pth` se charge sur GPU et génère un masque binaire avec une résolution identique à celle de l'image d'entrée.
Avec ce modèle ViT-H, le temps d'exécution est suffisamment rapide pour une utilisation interactive via l'interface Streamlit.
La précision du masque dépend considérablement de la qualité de la bounding box fournie : une box imprécise peut inclure des zones non pertinentes.
Le mode multimask est particulièrement utile dans des cas ambigus, bien qu'une fonctionnalité pour sélectionner automatiquement le meilleur masque reste nécessaire.
