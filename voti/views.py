from django.shortcuts import render

voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}

def viewA(request):
   materie = ["Matematica","Italiano","Inglese","Storia","Geografia"]
   context={'materie':materie}
   return render(request,"viewA.html",context)

def viewB(request):
   context={'voti':voti}
   return render(request,"viewB.html",context)

def viewC(request):
   media1=0.0
   media2=0.0
   media3=0.0
   cont=0
   studenti=[]
   for studente, materie in voti.items():
      studenti.append(studente)
      somma_voti = 0
      numero_voti = 0
      for materia in materie:
         voto = materia[1]
         somma_voti += voto
         numero_voti += 1
      if cont==0:
         media1 = somma_voti / numero_voti
      elif cont==1:
         media2 = somma_voti / numero_voti
      else:
         media3 = somma_voti / numero_voti
      cont+=1
   context={
      'media1':media1,
      'media2':media2,
      'media3':media3,
      'studenti':studenti
   }
   return render(request,"viewC.html",context)

def viewD(request):
   maxVoto=0
   minVoto=15
   materieMax=[]
   studenteMax=[]
   materieMin=[]
   studenteMin=[]
   for studente, materie in voti.items():
      for materia in materie:
         if materia[1]>maxVoto:
            maxVoto=materia[1]
         if materia[1]<minVoto:
            minVoto=materia[1]

   for studente, materie in voti.items():
      for materia in materie:
         if materia[1]==maxVoto:
            materieMax.append(materia[0])
            studenteMax.append(studente)
         if materia[1]==minVoto:
            materieMin.append(materia[0])
            studenteMin.append(studente)
   
   context={
      'maxVoto':maxVoto,
      'minVoto':minVoto,
      'materieMax':materieMax,
      'materieMin':materieMin,
      'studenteMax':studenteMax,
      'studenteMin':studenteMin
   }
   return render(request,"viewD.html",context)

   


