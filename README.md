# Neybor One Route Optimizer

Ce script calcule et trace l’itinéraire optimal pour distribuer des bonbons pour d'Halloween dans les maisons Neybor à Bruxelles.
---
##Fonctionnalités

- Calcule les distances entre adresses (formule de Haversine).

- Optimise l’ordre de visite (nearest neighbor + 2-opt).

- Génère une carte PNG du trajet.

### Formule de Haversine
```
La distance \( d \) entre deux points de coordonnées \( (\text{lat}_1, \text{lon}_1) \) et \( (\text{lat}_2, \text{lon}_2) \) est donnée par :

\[
d = 2R \cdot \arcsin\!\left(
    \sqrt{
        \sin^2\!\left(\frac{\text{lat}_2 - \text{lat}_1}{2}\right)
        + \cos(\text{lat}_1) \cdot \cos(\text{lat}_2) \cdot
          \sin^2\!\left(\frac{\text{lon}_2 - \text{lon}_1}{2}\right)
    }
\right)
\]

où :
- \( R \) est le rayon de la Terre (en km, typiquement \( R = 6371 \))
- Les latitudes et longitudes sont exprimées en radians.
```

---

## Algorithme Nearest Neighbor

L’idée : partir d’un point et visiter toujours le point le plus proche non visité.
```
Soit :
- un ensemble de points \( V = \{1, 2, \dots, n\} \)
- \( d(i, j) \) = distance entre les points \( i \) et \( j \)

Le chemin \( P = (p_1, p_2, \dots, p_n) \) est construit itérativement :

\[
p_{k+1} = \underset{j \in V \setminus \{p_1, \dots, p_k\}}{\arg\min} \; d(p_k, j)
\]
```
---

## Algorithme 2-Opt

L’idée : améliorer un trajet existant en échangeant deux arêtes si cela réduit la distance totale.
```
1. Prendre une route initiale \( P = (p_1, p_2, \dots, p_n) \)  
2. Choisir deux indices \( i < k \)  
3. Inverser la sous-séquence entre \( i \) et \( k \) pour créer une nouvelle route \( P' \)  
4. Si :

\[
L(P') < L(P)
\]

alors remplacer \( P \) par \( P' \)  
5. Répéter jusqu’à ce qu’aucune amélioration ne soit possible  
```
### Distance totale
```
\[
L(P) = \sum_{i=1}^{n-1} d(p_i, p_{i+1})
\]

Pour un cycle fermé :

\[
L_{\text{cycle}}(P) = L(P) + d(p_n, p_1)
\]
```
---
##Utilisation
python route_planner.py --out-png carte.png

##Dépendance
```
pip install matplotlib
```
## Output

Liste ordonnée des maisons avec distances totales

Fichier PNG du parcours (si matplotlib est installé)

##Par défaut

Départ / Arrivée : Neybor Office

Zone : Bruxelles
