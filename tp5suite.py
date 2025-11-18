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

note_ue1={
    'R101':10,'R102':10,'R103':10,'R104':10,'R105':10,'R106':10,'R107':10,'R108':10,'R109':10,
    'R110':10,'R111':10,'R112':10,'R113':10,'R114':10,'R115':10,'SAE11':10,'SAE12':10,'SAE13':10,
    'SAE14':10,'SAE15':10,'SAE16':10,
}

note_ue2={
    'R101':10,'R102':10,'R103':10,'R104':10,'R105':10,'R106':10,'R107':10,'R108':10,'R109':10,
    'R110':10,'R111':10,'R112':10,'R113':10,'R114':10,'R115':10,'SAE11':10,'SAE12':10,'SAE13':10,
    'SAE14':10,'SAE15':10,'SAE16':10,
}
note_ue3={
    'R101':10,'R102':10,'R103':10,'R104':10,'R105':10,'R106':10,'R107':10,'R108':10,'R109':10,
    'R110':10,'R111':10,'R112':10,'R113':10,'R114':10,'R115':10,'SAE11':10,'SAE12':10,'SAE13':10,
    'SAE14':10,'SAE15':10,'SAE16':10,
}

moyenne_ue1 = calcul_moyenne(coef_ue1, note_ue1)
moyenne_ue2 = calcul_moyenne(coef_ue2, note_ue2)
moyenne_ue3 = calcul_moyenne(coef_ue3, note_ue3)

print('Moyenne pondérée de UE 1 :', round(moyenne_ue1, 2))
print('Moyenne pondérée de UE 2 :', round(moyenne_ue2, 2))
print('Moyenne pondérée de UE 3 :', round(moyenne_ue3, 2))