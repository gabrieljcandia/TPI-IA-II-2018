from clases.Clases import Cluster
from Controladora import Controladora

con = Controladora()

c1 = Cluster(0.4, 0.53, 0)
c2 = Cluster(0.22, 0.38, 0)
c3 = Cluster(0.35, 0.32, 0)
c4 = Cluster(0.26, 0.19, 0)
c5 = Cluster(0.08, 0.41, 0)
c6 = Cluster(0.45, 0.30, 0)

con.setClusters([c1, c2, c3, c4, c5, c6])

#con.average()

x = con.distanciaEuclideaClustersSimple(c1, c2)
print ("El valor de x es ", x)
y = con.distanciaManhattanSingle(c1, c2)
print ("El valor de y es ", y)
print ("hasta acá")
a = con.distanciaMinkowski(c1, c2, 1)
print ("El valor de a es: ", a)
b = con.distanciaMinkowski(c1, c2, 2)
print ("El valor de b es ", b)
c = con.distanciaMinkowski(c1, c2, 3)
print ("El valor de c es ", c)
#print("Los clústers ", con.getClusters()[5].getId(), " y ", con.getClusters()[6].getId() , "pertenecen al mismo clúster?:", con.perteneceAlMismoCluster(con.getClusters()[5], con.getClusters()[6]))
#print ("El superior de ", con.getClusters()[5].getId(), " es: ", con.devolverSuperior(con.getClusters()[5]).getId())

