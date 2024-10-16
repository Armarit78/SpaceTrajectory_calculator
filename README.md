# Calculateur de Trajectoire Spatiale

Ce programme Python est conçu pour résoudre des exercices complexes relatifs aux trajectoires de satellites dans l'espace. Il permet de calculer divers paramètres orbitaux et les instants de passage par des points spécifiques de l'orbite. Cette version est optimisée pour être embarquée et compacte, afin de pouvoir être exécutée sur des calculatrices programmables.

## Capacités

Le programme offre des solutions détaillées pour les problématiques suivantes :

- **Demi-grand axe (a)** : Calculé à partir des altitudes de l'apogée et du périgée du satellite.
- **Rayon au périgée (rP)** : Calcul du point le plus proche de la Terre dans l'orbite du satellite.
- **Rayon à l'apogée (rA)** : Calcul du point le plus éloigné de la Terre dans l'orbite du satellite.
- **Période orbitale (T)** : Temps total pour un satellite de compléter une orbite complète autour de la Terre.
- **Vitesse au périgée (Vp)** : Vitesse orbitale du satellite lorsqu'il est le plus proche de la Terre.
- **Vitesse à l'apogée (Va)** : Vitesse orbitale du satellite à son point le plus éloigné de la Terre.
- **Temps de passage au périgée (tp)** : Calcul de l'instant exact où le satellite passe par son point le plus proche de la Terre, par rapport à un temps de référence fixé.
- **Calculs des anomalies et des longitudes vraies** : Le programme peut déterminer les anomalies vraies et les longitudes lors de l'orbite du satellite basées sur différentes anomalies vraies données (v).

Ces calculs sont basés sur les paramètres fournis pour l'exercice :

- Altitudes du périgée et de l'apogée
- Excentricité de l'orbite
- Inclinaison du plan orbital
- Divers paramètres angulaires incluant la longitude et la latitude du nœud ascendant, ainsi que l'argument du périgée

## Contributeurs

Ce programme a été développé grâce à la collaboration entre PORET Guillaume et Ludovic Cure-Moog.
