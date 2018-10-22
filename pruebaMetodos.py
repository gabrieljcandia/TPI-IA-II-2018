from clases.Clases import Cluster
from Controladora import Controladora

con = Controladora()

c1 = Cluster(1, 1, 1)
c2 = Cluster(2.5, 2.5, 2)
c3 = Cluster(3.5, 3.5, 3.5)
c4 = Cluster(4.6, 4.6, 4.6)
c5 = Cluster(5.8, 5.8, 5.8)

con.setClusters([c1, c2, c3, c4, c5])

con.simple()
con.complete()
con.complete()

for x in con.getClusters():
    print ("El id del nodo es: ", x.getId())
    if x.getClusters() is not None:
        for y in x.getClusters():
            if y is not None:
                print ("El nodo ", x.getId(), " contiene a:", y.getId())

#print("Los clústers ", con.getClusters()[5].getId(), " y ", con.getClusters()[6].getId() , "pertenecen al mismo clúster?:", con.perteneceAlMismoCluster(con.getClusters()[5], con.getClusters()[6]))
print ("El superior de ", con.getClusters()[5].getId(), " es: ", con.devolverSuperior(con.getClusters()[5]).getId())

