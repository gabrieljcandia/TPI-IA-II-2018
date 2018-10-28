import random
import math

from clases.Clases import Cluster


class Controladora:
    clusters = []  # Contiene los ids de todos los clusters existentes.
    clusterSingleEuclideo = []
    clusterCompleteEuclideo = []
    clusterAverageEuclideo = []
    clusterSingleManhattan = []
    clusterCompleteManhattan = []
    clusterAverageManhattan = []
    clusterSingleMinchowski = []
    clusterCompleteMinchowski = []
    clusterAverageMinchowski = []

    def __init__(self):
        self.a = "3"  # borrar esta liena

    def pruebaClustersStaticos(
            self):  # crea una jerarquia de clusters, como si fuera el resultado de uno de los metodos
        # creacion clusters puntos
        cl1 = Cluster(1, 4, 0)
        cl2 = Cluster(2, 5, 0)
        cl3 = Cluster(2, 4, 0)
        cl4 = Cluster(3, 4, 0)

        cl5 = Cluster(5, 6, 0)
        cl6 = Cluster(6, 6, 0)
        cl7 = Cluster(6, 5, 0)

        cl8 = Cluster(6, 3, 0)
        cl9 = Cluster(5, 2, 0)
        cl10 = Cluster(6, 2, 0)

        # creacion clusters agrupadores
        cl11 = Cluster()
        cl12 = Cluster()
        cl13 = Cluster()
        cl14 = Cluster()
        cl15 = Cluster()
        cl16 = Cluster()
        cl17 = Cluster()
        cl18 = Cluster()
        cl19 = Cluster()

        # agrupamiento clusters
        cl11.addCluster(cl5)
        cl11.addCluster(cl6)

        cl12.addCluster(cl9)
        cl12.addCluster(cl10)

        cl13.addCluster(cl3)
        cl13.addCluster(cl4)

        cl14.addCluster(cl2)
        cl14.addCluster(cl13)

        cl15.addCluster(cl8)
        cl15.addCluster(cl12)

        cl16.addCluster(cl7)
        cl16.addCluster(cl11)

        cl17.addCluster(cl1)
        cl17.addCluster(cl14)

        cl18.addCluster(cl15)
        cl18.addCluster(cl16)

        cl19.addCluster(cl17)
        cl19.addCluster(cl18)

        return cl19

    def leerDatosArch(self, dir):
        x = []
        y = []
        z = []

        with open(dir, "r") as file:
            lines = []
            for line in file:
                line.strip()  # quita espacios si hubieran
                lines.append(line)  # agrega linea en lineas

        # si son 2 dimensiones
        try:
            for line in lines:
                a, b, c = line.split("\t")
                b.rstrip()  # quita el \n del final
                x.append(float(a))
                y.append(float(b))
                z.append(float(c))
            datos = (x, y, z)

        # si son 3 dimensiones
        except Exception as inst:
            # x, y, z = []
            for line in lines:
                a, b = line.split("\t")
                b.rstrip()  # quita el \n del final
                x.append(float(a))
                y.append(float(b))
            # datos = (x, y)

            clusters = []
            for i in range(x.__len__()):
                print(i)
                miCluster = Cluster(x[i], y[i], 0)
                clusters.append(miCluster)
            print(clusters)

            '''# prueba relacionar clusters
            nuevoCluster1 = Cluster(1, 2, 0)
            nuevoCluster2 = Cluster(1, 3, 0)
            nuevoCluster3 = Cluster(1, 4, 0)
            nuevoCluster4 = Cluster(1, 5, 0)
            nuevoCluster1.addCluster(nuevoCluster2)
            nuevoCluster2.addCluster(nuevoCluster3)
            nuevoCluster3.addCluster(nuevoCluster4)
            clusters[0].addCluster(nuevoCluster1)

            # otra prueba similar
            nuevoCluster1 = Cluster(4, 5, 0)
            nuevoCluster2 = Cluster(4, 4, 0)
            nuevoCluster3 = Cluster(3, 3, 0)
            nuevoCluster4 = Cluster(3, 4, 0)
            nuevoCluster1.addCluster(nuevoCluster2)
            nuevoCluster2.addCluster(nuevoCluster3)
            nuevoCluster3.addCluster(nuevoCluster4)
            clusters[1].addCluster(nuevoCluster1)'''
        return clusters

    def generarPuntosAleatorios2D(self, cant, Xmin, Xmax, Ymin, Ymax):
        clusters = []
        for i in range(cant):
            miCluster = Cluster(random.uniform(Xmin, Xmax), random.uniform(Ymin, Ymax), 0)
            clusters.append(miCluster)
        print(clusters)

        ''''# prueba relacionar clusters
        nuevoCluster1 = Cluster(1, 2, 0)
        nuevoCluster2 = Cluster(1, 3, 0)
        nuevoCluster3 = Cluster(1, 4, 0)
        nuevoCluster4 = Cluster(1, 5, 0)
        nuevoCluster1.addCluster(nuevoCluster2)
        nuevoCluster2.addCluster(nuevoCluster3)
        nuevoCluster3.addCluster(nuevoCluster4)
        clusters[0].addCluster(nuevoCluster1)

        # otra prueba similar
        nuevoCluster1 = Cluster(4, 5, 0)
        nuevoCluster2 = Cluster(4, 4, 0)
        nuevoCluster3 = Cluster(3, 3, 0)
        nuevoCluster4 = Cluster(3, 4, 0)
        nuevoCluster1.addCluster(nuevoCluster2)
        nuevoCluster2.addCluster(nuevoCluster3)
        nuevoCluster3.addCluster(nuevoCluster4)
        clusters[1].addCluster(nuevoCluster1)'''

        return clusters

    def setClusters(self, clustersAgregar):
        self.clusters = clustersAgregar

    def getClusterSingleEuclideo(self):
        return self.clusterSingleEuclideo

    def getClusterCompleteEuclideo(self):
        return self.clusterCompleteEuclideo

    def getClusterAverageEuclideo(self):
        return self.clusterAverageEuclideo

    def getClusterSingleManhattan(self):
        return self.clusterSingleManhattan

    def getClusterCompleteManhattan(self):
        return self.clusterCompleteManhattan

    def getClusterAverageManhattan(self):
        return self.clusterAverageManhattan

    def getClusterSingleMinshowski(self):
        return self.clusterSingleMinchowski

    def getClusterCompleteMinshowski(self):
        return self.clusterCompleteMinchowski

    def getClusterAverageMinshowski(self):
        return self.clusterAverageMinchowski

    # Agrega el nuevo clúster a la lista de clústers del dominio
    def agregarClusterSuperior(self, nc):
        agregar = self.clusters
        agregar.append(nc)
        self.setClusters(agregar)

    def devolverSuperior(self, c):
        retornar = c
        for x in self.getClusters():
            if (x.hasClusters()):
                if (c in x.getClusters()):
                    retornar = x
        return retornar

    def perteneceAlMismoCluster(self, c1, c2):
        retorno = False
        for x in self.getClusters():  # Recorro los clusters que contiene el dominio
            if x.hasClusters():
                cAux = x.getClustersContenidosId()  # Traigo todos los elementos que posee x

                if ((c1.getId() in cAux) & (c2.getId() in cAux) & (not self.esSuperior(c1, c2) & (not self.esSuperior(c2, c1))) & (c1 != c2)):
                    return True
        # end for
        return retorno

    def distanciaClusters(self, cluster1, cluster2):
        # dist = cluster1.distanciaEuclidea(cluster2.getX(), cluster2.getY())
        retorno = 10000000
        c1 = cluster1.getClustersContenidos()
        c2 = cluster2.getClustersContenidos()

        for x in c1:
            for y in c2:
                dist = self.distanciaEuclideaClusters(x, y)
                if dist < retorno:
                    retorno = dist

        return retorno

    def generarPuntosAleatorios3D(self, cant, Xmin, Xmax, Ymin, Ymax, Zmin, Zmax):
        clusters = []
        for i in range(cant):
            miCluster = Cluster(random.uniform(Xmin, Xmax), random.uniform(Ymin, Ymax), random.uniform(Zmin, Zmax))
            clusters.append(miCluster)
        print(clusters)

        return clusters


    def getClusters(self):
        return self.clusters


    #Retorna la distancia de 2 clústers, sean superiores o inferiores. NECESARIO ARREGLAR PARA QUE TRABAJEN USANDO LOS IDS DE LOS CLÚSTERS
    def distanciaClusters(self, c1, c2):
        min = 1000000000000000000000000  # el valor que representa a la mínima distancia entre los clusters

        if c1.hasClusters():
            dist = self.distanciaClusters(c1.getClusters(), c2)
        else:
            if c2.hasClusters():
                dist = self.distanciaClusters(c1, c2.getClusters())
            else:
                dist = c1.distanciaEuclidea(c2.getX(), c2.getY())
        if dist < min:
            min = dist
            dist = 1000000000000000000000000


# miControladora = Controladora()
# miControladora.Visual.iniciarVentana()
# miControladora.leerDatos("C:/Users/mejor/Desktop/Libro1.txt")

# ----------------- ESPACIO DE TRABAJO DE FABIÁN -----------------
    def distanciaEuclideaClusters(self, c1, c2): #distancia entre 2 puntos
        dist = 1000000000000000000000000
        if (c1.getX() is not None) & (c2.getX() is not None):
            dist = math.sqrt((c1.getX() - c2.getX())**2 + (c1.getY() - c2.getY())**2)
        return dist

#Borrar función
    def distanciaEuclideaClustersSimple(self, c1, c2): #distancia entre 2 puntos
        dist = 0
        min = 1000000000000000000000000
        cn1 = c1.getClustersContenidos()
        cn2 = c2.getClustersContenidos()

        for x in cn1:
            for y in cn2:
                dist = math.sqrt((x.getX() - y.getX())**2 + (x.getY() - y.getY())**2)
                if dist < min:
                    min = dist

        return min

#Borrar función
    def distanciaEuclideaClustersComplete(self, c1, c2): #distancia entre 2 puntos
        dist = 0
        max = 0
        cn1 = c1.getClustersContenidos()
        cn2 = c2.getClustersContenidos()

        for x in cn1:
            for y in cn2:
                dist = math.sqrt((x.getX() - y.getX())**2 + (x.getY() - y.getY())**2)
                print ("La distancia entre", x.getId(), "(", x.getCoordenadasR2(), ")", " y ", y.getId(), "(", y.getCoordenadasR2(), ")... es ", dist)
                if dist > max:
                    max = dist
        return max

#Borrar función
    def distanciaEuclideaClustersAverage(self, c1, c2): #distancia entre 2 puntos
        dist = 0
        min = 1000000000000000000000000
        cantidad = 0
        cn1 = c1.getClustersContenidos()
        cn2 = c2.getClustersContenidos()

        for x in cn1:
            dist = 0
            for y in cn2:
                dist = dist + math.sqrt((x.getX() - y.getX())**2 + (x.getY() - y.getY())**2)
                cantidad = cantidad + 1
            dist = dist/cantidad
            print ("La distancia entre", x.getId(), "(", x.getCoordenadasR2(), ")", " y ", y.getId(), "(", y.getCoordenadasR2(), ")... es ", dist)
            if dist < min:
                min = dist
        return min

    #Devuelve verdadero si csup es el clúster superior de c
    #   c es el clúster inferior
    #   csup es el clúster superior a evaluar
    def esSuperior(self, c, csup):
        retornar = False
        cAux = self.devolverSuperior(c)
        if cAux == csup:
            retornar = True
        return retornar

#Borrar función
    def average(self):
        min = 1000000000000000000000000
        clustersUnirse = []  # va a tener los ids de los clusters a fusionarse
        nuevoCluster = Cluster(None, None, None)  # es el nuevo cluster superior que se creará con el algoritmo
        cn1 = None
        cn2 = None
        dist = 0
        i = 0
        j = 1

        while i < len(self.getClusters()):
            while j < len(self.getClusters()):
                dist = self.distanciaEuclideaClustersAverage(self.getClusters()[i], self.getClusters()[j])
                if (dist < min):
                    min = dist
                    cn1 = self.getClusters()[i]
                    cn2 = self.getClusters()[j]
                j = j + 1
            i = i + 1
            j = i + 1
        if ((cn1 is not None) & (cn2 is not None)):
            print ("La distancia mínima es: ", min, " entre ", cn1.getId(), " y ", cn2.getId())
            nuevoCluster.setClusters([cn1, cn2])
            self.quitarCluster(cn1)
            self.quitarCluster(cn2)
            self.agregarClusterSuperior(nuevoCluster)

#Borrar función
    def simple(self):
        min = 1000000000000000000000000
        clustersUnirse = []  # va a tener los ids de los clusters a fusionarse
        nuevoCluster = Cluster(None, None, None)  # es el nuevo cluster superior que se creará con el algoritmo
        cn1 = None
        cn2 = None
        dist = 0
        i = 0
        j = 1
        while i < len(self.getClusters()):
            while j < len(self.getClusters()):
                dist = self.distanciaEuclideaClustersSimple(self.getClusters()[i], self.getClusters()[j])
                if (dist < min):
                    min = dist
                    cn1 = self.getClusters()[i]
                    cn2 = self.getClusters()[j]
                j = j + 1
            i = i + 1
            j = i + 1
        if ((cn1 is not None) & (cn2 is not None)):
            nuevoCluster.setClusters([cn1, cn2])
            self.quitarCluster(cn1)
            self.quitarCluster(cn2)

            self.agregarClusterSuperior(nuevoCluster)
#Borrar función
    def complete(self):
        min = 1000000000000000000000000
        clustersUnirse = []  # va a tener los ids de los clusters a fusionarse
        nuevoCluster = Cluster(None, None, None)  # es el nuevo cluster superior que se creará con el algoritmo
        cn1 = None
        cn2 = None
        dist = 0
        i = 0
        j = 1

        while i < len(self.getClusters()):
            while j < len(self.getClusters()):
                dist = self.distanciaEuclideaClustersComplete(self.getClusters()[i], self.getClusters()[j])
                if (dist < min):
                    min = dist
                    cn1 = self.getClusters()[i]
                    cn2 = self.getClusters()[j]
                j = j + 1
            i = i + 1
            j = i + 1
        if ((cn1 is not None) & (cn2 is not None)):
            print ("La distancia mínima es: ", min, " entre ", cn1.getId(), " y ", cn2.getId())
            nuevoCluster.setClusters([cn1, cn2])
            self.quitarCluster(cn1)
            self.quitarCluster(cn2)
            self.agregarClusterSuperior(nuevoCluster)

    def quitarCluster(self, c):
        self.getClusters().remove(c)
    #Borrar función
    def distanciaManhattanSingle(self, c1, c2):
        dist = 0
        min = 1000000000000000000000000
        cn1 = c1.getClustersContenidos()
        cn2 = c2.getClustersContenidos()

        for x in cn1:
            for y in cn2:
                dist = math.fabs(x.getX() - y.getX()) + math.fabs(x.getY() - y.getY())
                if dist < min:
                    min = dist

        return min

    #Borrar función
    def distanciaMinkowski(self, c1, c2, p):
        dist = 0
        min = 1000000000000000000000000
        cn1 = c1.getClustersContenidos()
        cn2 = c2.getClustersContenidos()

        for x in cn1:
            for y in cn2:
                dist = ((x.getX() - y.getX())**p + (x.getY() - y.getY())**p)**(1/p)
                if dist < min:
                    min = dist

        return min

    def imprimir(self, c):
        if c is not None:
            for x in c:
                print ("El cluster ", x.getId())
                if x.hasClusters():
                    for y in x.getClusters():
                        print ("\t contiene a:", y.getId())
                    self.imprimir(x.getClusters())

    '''
    El método recibe el tipo de algoritmo por el cual hacer el agrupamiento en formato string, el tipo de Distancia que utilizará, también en string y el valor de p en caso de que el tipo de Distancia sea Minchowski
        El argumento 'algoritmo' puede ser: "single", "complete" o "average"
        el argumento 'tipoDistancia' puede ser: "euclidea", "manhattan" o "minchowski"
    '''
    def agrupamiento(self, algoritmo, tipoDistancia, p):
        min = 1000000000000000000000000
        clustersUnirse = []  # va a tener los ids de los clusters a fusionarse
        nuevoCluster = Cluster(None, None, None)  # es el nuevo cluster superior que se creará con el algoritmo
        cn1 = None
        cn2 = None
        dist = 0
        i = 0
        j = 1

        while i < len(self.getClusters()):
            while j < len(self.getClusters()):

                #Borrar línea: dist = self.distanciaEuclideaClustersAverage(self.getClusters()[i], self.getClusters()[j])
                if algoritmo is 1: #Single
                    dist = self.distanciaSingle(self.getClusters()[i], self.getClusters()[j], tipoDistancia, p)
                if algoritmo is 2: #Complete
                    dist = self.distanciaComplete(self.getClusters()[i], self.getClusters()[j], tipoDistancia, p)
                if algoritmo is 3: #Average
                    dist = self.distanciaAverage(self.getClusters()[i], self.getClusters()[j], tipoDistancia, p)

                if (dist < min):
                    min = dist
                    cn1 = self.getClusters()[i]
                    cn2 = self.getClusters()[j]
                j = j + 1
            i = i + 1
            j = i + 1
        if ((cn1 is not None) & (cn2 is not None)):
            self.agregarCluster(nuevoCluster, algoritmo, tipoDistancia)

    def agregarCluster(self, nuevoCluster, algoritmo, tipoDistancia):
        if algoritmo is 1: #Single
            if tipoDistancia is "euclidea":
                self.clusterSingleEuclideo.remove(nuevoCluster[0])
                self.clusterSingleEuclideo.remove(nuevoCluster[1])
                self.clusterSingleEuclideo.append(nuevoCluster)
            if tipoDistancia is "manhattan":
                self.clusterSingleManhattan.remove(nuevoCluster[0])
                self.clusterSingleManhattan.remove(nuevoCluster[1])
                self.clusterSingleManhattan.append(nuevoCluster)
            if tipoDistancia is "minchowski":
                self.clusterSingleMinchowski.remove(nuevoCluster[0])
                self.clusterSingleMinchowski.remove(nuevoCluster[1])
                self.clusterSingleMinchowski.append(nuevoCluster)

        if algoritmo is 2: #Complete
            if tipoDistancia is "euclidea":
                self.clusterCompleteEuclideo.remove(nuevoCluster[0])
                self.clusterCompleteEuclideo.remove(nuevoCluster[1])
                self.clusterCompleteEuclideo.append(nuevoCluster)
            if tipoDistancia is "manhattan":
                self.clusterCompleteManhattan.remove(nuevoCluster[0])
                self.clusterCompleteManhattan.remove(nuevoCluster[1])
                self.clusterCompleteManhattan.append(nuevoCluster)
            if tipoDistancia is "minchowski":
                self.clusterCompleteMinchowski.remove(nuevoCluster[0])
                self.clusterCompleteMinchowski.remove(nuevoCluster[1])
                self.clusterCompleteMinchowski.append(nuevoCluster)

        if algoritmo is 3: #Average
            if tipoDistancia is "euclidea":
                self.clusterAverageEuclideo.remove(nuevoCluster[0])
                self.clusterAverageEuclideo.remove(nuevoCluster[1])
                self.clusterAverageEuclideo.append(nuevoCluster)
            if tipoDistancia is "manhattan":
                self.clusterAverageManhattan.remove(nuevoCluster[0])
                self.clusterAverageManhattan.remove(nuevoCluster[1])
                self.clusterAverageManhattan.append(nuevoCluster)
            if tipoDistancia is "minchowski":
                self.clusterAverageMinshowski.remove(nuevoCluster[0])
                self.clusterAverageMinshowski.remove(nuevoCluster[1])
                self.clusterAverageMinshowski.append(nuevoCluster)


    def distanciaSingle(self, c1, c2, tipoDistancia, p): #distancia entre 2 puntos
        dist = 0
        min = 1000000000000000000000000
        cn1 = c1.getClustersContenidos()
        cn2 = c2.getClustersContenidos()

        for x in cn1:
            for y in cn2:
                if (c1.getZ() is None) | (c2.getZ() is None):
                    if tipoDistancia is "euclidea":
                        dist = math.sqrt((x.getX() - y.getX())**2 + (x.getY() - y.getY())**2)
                    if tipoDistancia is "manhattan":
                        dist = math.fabs(x.getX() - y.getX()) + math.fabs(x.getY() - y.getY())
                    if tipoDistancia is "minchowski":
                        dist = ((x.getX() - y.getX())**p + (x.getY() - y.getY())**p)**(1/p)
                else: #Para R3
                    if tipoDistancia is "euclidea":
                        dist = math.sqrt((x.getX() - y.getX())**2 + (x.getY() - y.getY())**2 + (x.getZ() - y.getZ())**2)
                    if tipoDistancia is "manhattan":
                        dist = math.fabs(x.getX() - y.getX()) + math.fabs(x.getY() - y.getY()) + math.fabs(x.getZ() - y.getZ())
                    if tipoDistancia is "minchowski":
                        dist = ((x.getX() - y.getX())**p + (x.getY() - y.getY())**p + (x.getZ() - y.getZ())**p)**(1/p)

                if dist < min:
                    min = dist
        return min

    def ditanciaComplete (self, c1, c2, tipoDistancia, p): #distancia entre 2 puntos
        dist = 0
        max = 0
        cn1 = c1.getClustersContenidos()
        cn2 = c2.getClustersContenidos()

        for x in cn1:
            for y in cn2:
                if (c1.getZ() is None) | (c2.getZ() is None):
                    if tipoDistancia is "euclidea":
                        dist = math.sqrt((x.getX() - y.getX())**2 + (x.getY() - y.getY())**2)
                    if tipoDistancia is "manhattan":
                        dist = math.fabs(x.getX() - y.getX()) + math.fabs(x.getY() - y.getY())
                    if tipoDistancia is "minchowski":
                        dist = ((x.getX() - y.getX())**p + (x.getY() - y.getY())**p)**(1/p)
                else: #Para R3
                    if tipoDistancia is "euclidea":
                        dist = math.sqrt((x.getX() - y.getX())**2 + (x.getY() - y.getY())**2 + (x.getZ() - y.getZ())**2)
                    if tipoDistancia is "manhattan":
                        dist = math.fabs(x.getX() - y.getX()) + math.fabs(x.getY() - y.getY()) + math.fabs(x.getZ() - y.getZ())
                    if tipoDistancia is "minchowski":
                        dist = ((x.getX() - y.getX())**p + (x.getY() - y.getY())**p + (x.getZ() - y.getZ())**p)**(1/p)

                if dist > max:
                    max = dist
        return max

    def distanciaAverage(self, c1, c2, tipoDistancia, p): #distancia entre 2 puntos
        dist = 0
        min = 1000000000000000000000000
        cantidad = 0
        cn1 = c1.getClustersContenidos()
        cn2 = c2.getClustersContenidos()

        for x in cn1:
            dist = 0
            for y in cn2:
                if (c1.getZ() is None) | (c2.getZ() is None):
                    if tipoDistancia is "euclidea":
                        dist = math.sqrt((x.getX() - y.getX())**2 + (x.getY() - y.getY())**2)
                    if tipoDistancia is "manhattan":
                        dist = math.fabs(x.getX() - y.getX()) + math.fabs(x.getY() - y.getY())
                    if tipoDistancia is "minchowski":
                        dist = ((x.getX() - y.getX())**p + (x.getY() - y.getY())**p)**(1/p)

                else: #Para R3
                    if tipoDistancia is "euclidea":
                        dist = math.sqrt((x.getX() - y.getX())**2 + (x.getY() - y.getY())**2 + (x.getZ() - y.getZ())**2)
                    if tipoDistancia is "manhattan":
                        dist = math.fabs(x.getX() - y.getX()) + math.fabs(x.getY() - y.getY()) + math.fabs(x.getZ() - y.getZ())
                    if tipoDistancia is "minchowski":
                        dist = ((x.getX() - y.getX())**p + (x.getY() - y.getY())**p + (x.getZ() - y.getZ())**p)**(1/p)
                cantidad = cantidad + 1
            dist = dist/cantidad
            print ("La distancia entre", x.getId(), "(", x.getCoordenadasR2(), ")", " y ", y.getId(), "(", y.getCoordenadasR2(), ")... es ", dist)
            if dist < min:
                min = dist
        return min


    def generarClusters(self, p):
        self.clusterSingleEuclideo = self.getClusters()
        self.clusterSingleManhattan = self.getClusters()
        self.clusterSingleMinshowski = self.getClusters()
        self.clusterCompleteEuclideo = self.getClusters()
        self.clusterCompleteManhattan = self.getClusters()
        self.clusterCompleteMinshowski = self.getClusters()
        self.clusterAverageEuclideo = self.getClusters()
        self.clusterAverageManhattan = self.getClusters()
        self.clusterAverageMinshowski = self.getClusters()

        for i in range(self.getClusterSingleEuclideo()._len_()):
            self.agrupamiento(1, "euclidea", None)

        for i in range(self.getClusterSingleManhattan()._len_()):
            self.agrupamiento(1, "manhattan", None)

        for i in range(self.getClusterSingleMinshowski()._len_()):
            self.agrupamiento(1, "minchowski", p)

        for i in range(self.getClusterCompleteEuclideo()._len_()):
            self.agrupamiento(2, "euclidea", None)

        for i in range(self.getClusterCompleteManhattan()._len_()):
            self.agrupamiento(2, "manhattan", None)

        for i in range(self.getClusterCompleteMinshowski()._len_()):
            self.agrupamiento(2, "minchowski", p)

        for i in range(self.getClusterAverageEuclideo()._len_()):
            self.agrupamiento(3, "euclidea", None)

        for i in range(self.getClusterAverageManhattan()._len_()):
            self.agrupamiento(3, "manhattan", None)

        for i in range(self.getClusterAverageMinshowski()._len_()):
            self.agrupamiento(3, "minchowski", p)
