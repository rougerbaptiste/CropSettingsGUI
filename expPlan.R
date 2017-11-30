rm(list=ls())
library(planor)
K=5 # nombre de paramètres
m=3 # nombre de niveau

binf = 1+K*(m-1)+K*(K-1)/2*(m-1)^2 # calcul de la borne inférieure, ie nb minimum de simulations

print(binf)

i = 0
nbMin = m^(i) # on cherche une puissance de m t.q. m^x > borne inférieure
while(nbMin < binf){
    i = i + 1
    nbMin = m^(i)
}

print(i)
print(nbMin)

plankey = planor.designkey(factors=LETTERS[1:K],nlevels = 3,resolution = 5,nunits = nbMin) # creation du plan
plan=planor.design(plankey)
MyData = plan@design # affichage du plan

MyData = as.matrix(MyData)

write.table(MyData, sep=',', file = "MyData.csv",row.names = FALSE, col.names=FALSE)
