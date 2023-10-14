
import random

#liste des etudiants
student_List=["Shinny","Nissi","Ibucap","Yaourt","Motema","Peace"]
mi_list=len(student_List)//2


#creation de la liste " indices" des indices de la liste student_List
 
indices=list(range(len(student_List)))

for i in range(len(student_List)):
    #generation des valeurs
    j=random.randint(i,len(student_List)-1)

    #permutation des valeurs liées aux indices de la liste "indices"
    indices[i],indices[j]=indices[j],indices[i]

""" affectation des valeurs aléatoires aux differentes équipes selon 
          notre liste consacrée aux indices """

team1=[student_List[i] for i in indices[:mi_list]]
team2=[student_List[i] for i in indices[mi_list:]]

print(team1)
print(team2)