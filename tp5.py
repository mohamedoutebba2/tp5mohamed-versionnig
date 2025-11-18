# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 09:40:02 2025

@author: outebmoh
"""

import matplotlib.pyplot as plt
import numpy as np

def calcul_moyenne(coefficients, notes):
    moyenne = np.average(list(notes.values()), weights=list(coefficients.values()))
    return moyenne

coef_ue1={
    'R101':10,'R102':10,'R103':12,'R104':10,'R105':0,'R106':5,'R107':0,'R108':6,'R109':0,
    'R110':5,'R111':4,'R112':2,'R113':5,'R114':5,'R115':0,'SAE11':20,'SAE12':20,'SAE13':0,
    'SAE14':0,'SAE15':0,'SAE16':7,
}
coef_ue2={
    'R101':4,'R102':0,'R103':2,'R104':8,'R105':6,'R106':0,'R107':0,'R108':0,'R109':0,
    'R110':5,'R111':5,'R112':2,'R113':9,'R114':9,'R115':3,'SAE11':0,'SAE12':0,'SAE13':29,
    'SAE14':0,'SAE15':0,'SAE16':7,
}
coef_ue3={
    'R101':4,'R102':0,'R103':2,'R104':0,'R105':0,'R106':5,'R107':15,'R108':6,'R109':4,
    'R110':5,'R111':5,'R112':2,'R113':0,'R114':0,'R115':3,'SAE11':0,'SAE12':0,'SAE13':0,
    'SAE14':20,'SAE15':20,'SAE16':7,
}