import random
import math

from clases.Clases import Cluster


class Controladora:
    clusters = []  # Contiene los ids de todos los clusters existentes.

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

    # Agrega el nuevo clúster a la lista de clústers del dominio
    def agregarClusterSuperior(self, nc):
        agregar = self.clusters
        agregar.append(nc)
        self.setClusters(agregar)

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
                # Verificación de que los clusters evaluados no pertenecen al mismo cluster superior
                if (not self.perteneceAlMismoCluster(self.getClusters()[i], self.getClusters()[j])):
                    # dist = self.getClusters()[i].distanciaEuclidea(self.getClusters()[j].getX(), self.getClusters()[j].getY())
                    dist = self.distanciaEuclideaClusters(self.getClusters()[i], self.getClusters()[j])
                    if (dist < min):
                        #print("Nueva distancia mínima: ", dist)
                        #print("Entre los clústers: ", self.getClusters()[i].getCoordenadasR2(), ", y ",
                              #self.getClusters()[j].getCoordenadasR2())
                        min = dist
                        cn1 = self.getClusters()[i]
                        cn2 = self.getClusters()[j]
                j = j + 1
            i = i + 1
            j = i + 1
        if ((cn1 is not None) & (cn2 is not None)):
            #print("El valor del cluster a unir, en la posición 0 es: ", cn1.getCoordenadasR2())
            #print("El valor del cluster a unir, en la posición 1 es: ", cn2.getCoordenadasR2())
            cs1 = self.devolverSuperior(cn1)
            #print("El valor de cs1, 1, es: ", cs1)
            cs2 = self.devolverSuperior(cn2)
            nuevoCluster.setClusters([cs1, cs2])

            self.agregarClusterSuperior(nuevoCluster)

    def devolverSuperior(self, c):
        retornar = c
        #longitud = c.getClustersContenidos()
        for x in self.getClusters():
            if (c in x.getClustersContenidos()):
                #min = len(x.getClustersContenidos())
                retornar = x
        return retornar

    def perteneceAlMismoCluster(self, c1, c2):
        retorno = False
        for x in self.getClusters():  # Recorro los clusters que contiene el dominio
            if x.hasClusters():
                cAux = x.getClustersContenidosId()  # Traigo todos los elementos que posee x

                if ((c1.getId() in cAux) & (c2.getId() in cAux)):
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

# -----------------ESPACIO DE TRABAJO DE FABIÁ-----------------
    def distanciaEuclideaClusters(self, c1, c2): #distancia entre 2 puntos
        dist = 1000000000000000000000000
        if (c1.getX() is not None) & (c2.getX() is not None):
            dist = math.sqrt((c1.getX() - c2.getX())**2 + (c1.getY() - c2.getY())**2)
        return dist
