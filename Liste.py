
import random

#liste des etudiants
student_List=["Shinny","Nissi","Ibucap","Yaourt","Motema","Peace"]

mi_list=len(student_List)//2

indices=list(range(len(student_List))) #indices de la student_List

maNouvelleList =[]
#creation de la liste " indices" des indices de la liste student_List


"""
    code originale : 
        for i in range(len(student_List)):
        #generation des valeurs
        j=random.randint(i,len(student_List)-1) // possibilite de repetition dans la liste 

    
    # ce code permet d'eviter les doublant dans la liste :
        for i in range (len(indices)): # 
        #generation des valeurs
        while len(maList) <len(indices):
            j=random.randint(i,len(student_List)-1)
            if j in maList :
                continue
            else:
                maList.append(j)
"""

for i in range (len(indices)): 
    while len(maNouvelleList) <len(indices):
        #generation des valeurs
        j=random.randint(i,len(student_List)-1)
        if j in maNouvelleList :
            continue
        else:
            maNouvelleList.append(j)

""" team1=[student_List[i] for i in indices[:mi_list]]
team2=[student_List[i] for i in indices[mi_list:]] 

"""
team1 =[student_List[i] for i in maNouvelleList[:mi_list]]
team2 =[student_List[i] for i in maNouvelleList[mi_list:]]

print(team1)
print(team2)
