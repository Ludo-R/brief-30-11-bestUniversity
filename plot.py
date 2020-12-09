#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:42:46 2020

@author: randon
"""
import pandas as pd
import numpy as np
from sklearn import decomposition
from sklearn import preprocessing
import matplotlib.pyplot as plt
from functionns import *


df = pd.read_csv("timesData.csv")
# choix du nombre de composantes à calculer
df2016 = df[df.year == 2016]
df2016.num_students  = [str(each).replace(',', '') for each in df2016.num_students]

y = df2016["university_name"]  

dfnums = df2016[['teaching', 'international', 'research', 'citations', 'income', 'total_score', 'num_students',  'student_staff_ratio','international_students' ]]
numeric_cols = ['teaching', 'international', 'research', 'citations', 'income', 'total_score', 'num_students', 'student_staff_ratio','international_students']
for col in numeric_cols:
    dfnums[col] = pd.to_numeric(dfnums[col], errors='coerce')
    
data_pca = dfnums.fillna(0)
print(dfnums)

# choix du nombre de composantes à calculer
n_comp = 2

# import de l'échantillon

# selection des colonnes à prendre en compte dans l'ACP
# préparation des données pour l'ACP
data_pca = data_pca.fillna(data_pca.mean()) # Il est fréquent de remplacer les valeurs inconnues par la moyenne de la variable
X = data_pca.values
names = y# ou data.index pour avoir les intitulés
features = dfnums.columns

# Centrage et Réduction
std_scale = preprocessing.StandardScaler().fit(X)
X_scaled = std_scale.transform(X)

# Calcul des composantes principales
pca = decomposition.PCA(n_components=n_comp)
pca.fit(X_scaled)

# Eboulis des valeurs propres
display_scree_plot(pca)

# Cercle des corrélations
pcs = pca.components_
display_circles(pcs, n_comp, pca, [(0,1),(2,3),(4,5)], labels = np.array(features))

# Projection des individus
X_projected = pca.transform(X_scaled)
display_factorial_planes(X_projected, n_comp, pca, [(0,1),(2,3),(4,5)], labels = np.array(names))
