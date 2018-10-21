import math
import random


class Cluster:
    idProximo = 1
    R = []
    G = []
    B = []

    def __init__(self, x=None, y=None, z=None): #si "x", "y" o "z" es vacio, les asigna "None"
        self.id = self.obtenerNuevaId()
        self.clusters = None #cluster de menor jerarquia
        self.R = self.obtenerColor(self.R)
        self.G = self.obtenerColor(self.G)
        self.B = self.obtenerColor(self.B)
        self.x = x
        self.y = y
        self.z = z
        if x is not None and y is not None:
            self.tieneComponentes = True
        else:
            self.tieneComponentes = False

    def obtenerColor(self, col):
        salir = False
        #random.seed(1234124) #para repetir misma secuencia de colores en cada ejecucion, no funciona en Python 3
        while not salir:
            nuevoCol = random.random()
            if nuevoCol not in col:
                salir = True
                col.append(nuevoCol)
        return nuevoCol

    def obtenerNuevaId(self):
        nuevaId = Cluster.idProximo
        Cluster.idProximo = self.idProximo + 1
        return nuevaId

    def setX (self, x):
        self.x = x

    def getX(self):
        return self.x

    def setY(self, y):
        self.y = y

    def getY(self):
        return self.y

    def setZ(self, z):
        self.z = z

    def getZ(self):
        return self.z

    def getId(self):
        return self.id

    def getR(self):
        return self.R

    def getG(self):
        return self.G

    def getB(self):
        return self.B

    def getRGB(self):
        rgb = [self.getR(), self.getG(), self.getB()]
        return rgb

    def addCluster(self, cluster):
        if self.clusters is None:
            self.clusters = []
        self.clusters.append(cluster)

    def cantPuntos(self): #devuelve el numero de puntos de nivel 0, ingresado por usuario (o autogenerado)
        cant = 0
        if self.clusters is not None:
            for cluster in self.clusters:
                cant = cant + cluster.cantPuntos()
        else:
            cant = cant + 1
        return cant

    def hasComponentes(self):
        return self.tieneComponentes

    def getPuntosR2(self): #modificar para que contemple que clusters sea un array de dos clusters (terminado)
        x, y = [], []
        if self.hasComponentes() is True:
            x.append(self.getX())
            y.append(self.getY())

        if self.clusters is not None:
            for cluster in self.clusters:
                xClusters, yClusters = cluster.getPuntosR2()
                for xi in xClusters:
                    x.append(xi)
                for yi in yClusters:
                    y.append(yi)
                #x.append(xClusters)
                #y.append(yClusters)

        return x, y

    def getCoordenadasR2(self):
        retornar = [self.x, self.y]
        return retornar

    def getCoordenadasR3(self):
        retornar = [self.x, self.y, self.z]
        return retornar

    def getClusters(self):
        return self.clusters

    def setClusters(self, c):
        self.clusters = c

    def hasClusters(self): #devuelve True si el cluster agrupa a otros
        if self.clusters is not None:
            retornar = True
        else:
            retornar = False
        return retornar

    # Método que devuelve los clústers contenidos en los clústers superiores
    def getClustersContenidos(self):
        retorno = []
        if self.clusters is not None:
            for x in self.clusters:
                result = x.getClustersContenidos()
                if type(result) is list:
                    for i in result:
                        retorno.append(i)
                else:
                    retorno.append(result)
        else:
            retorno.append(self)
        return retorno

    def getClustersContenidosId(self):
        retorno = []
        if self.clusters is not None:
            for x in self.clusters:
                result = x.getClustersContenidosId()
                if type(result) is list:
                    for i in result:
                        retorno.append(i)
                else:
                    retorno.append(result)
        else:
            retorno.append(self.getId())
        return retorno

    def obtenerCentroide(self):
        x, y = self.getPuntosR2()
        sumX, sumY = 0, 0
        for xi in x: sumX = sumX + xi
        for yi in y: sumY = sumY + yi
        cX = sumX/x.__len__()
        cY = sumY/x.__len__()
        return cX, cY

    def obtenerMayorDistante(self, punto): #devuelve el punto mas distante entre uno dado y los del cluster
        maxDistancia = 0
        ptoDistante = [0, 0]
        puntosClX, puntosClY = self.getPuntosR2()
        pX, pY = punto[0], punto[1]
        for i in range(puntosClX.__len__()):
                dist = self.distanciaEuclidea([pX, puntosClX[i]], [pY, puntosClY[i]])
                if dist > maxDistancia:
                    maxDistancia = dist
                    ptoDistante = [puntosClX[i], puntosClY[i]]
        return ptoDistante

    def distanciaEuclidea(self, x, y): #distancia entre 2 puntos
        dist = math.sqrt((x[0]-x[1])**2 + (y[0]-y[1])**2)
        #dist = ((self.getX() - x)**2 + (self.getY() - y)**2)
        return dist

    ########### metodos graficar dendograma #####################

    def getNivel(self, cantPuntos): #devuelve el nivel jerarquico del cluster
        if self.getId() <= cantPuntos:
            nivel = 0
        else:
            nivel = self.getId() - cantPuntos
        return nivel

    def getClusterIzq(self): #devuelve el cluster de nivel inmediatamente inferior que posea, de entre todos sus clusters hijos, la menor ID
        ClIzq = None
        if self.clusters is not None:
            for cl in self.clusters:
                if ClIzq is None or cl.getMenorId() < ClIzq.getMenorId():
                    ClIzq = cl
        else:
            ClIzq = self
        return ClIzq

    def getClusterDer(self): #devuelve el cluster de nivel inmediatamente inferior que posea, de entre todos sus clusters hijos, la mayor ID
        ClDer = None
        if self.clusters is not None:
            for cl in self.clusters:
                if ClDer is None or cl.getMayorId() > ClDer.getMayorId():
                    ClDer = cl
        else:
            ClDer = self
        return ClDer

    def getMenorId(self): #devuelve la menor ID, de entre las IDs de todos los clusters inferiores
        menor = 999999999
        if self.clusters is not None:
            for cl in self.clusters:
                if cl.getMenorId() < menor:
                    menor = cl.getMenorId()
        else:
            menor = self.getId()
        return menor

    def getMayorId(self): #devuelve la mayor ID, de entre las IDs de todos los clusters inferiores
        mayor = 0
        if self.clusters is not None:
            for cl in self.clusters:
                if cl.getMayorId() > mayor:
                    mayor = cl.getMayorId()
        else:
            mayor = self.getId()
        return mayor

    def getLink(self): #devuelve la consecucion de medias entre los puntos de nivel 0 de cada cluster (devuelve la posicion en X, interseccion horizontal-vertical entre nuevo cluster y uno anterior)
        if self.clusters is not None:
            clIzq = self.getClusterIzq()
            clDer = self.getClusterDer()

            linkIzq = clIzq.getLink()
            linkDer = clDer.getLink()

            link = (linkIzq + linkDer) / 2
        else:
            link = self.id
        return link

    def obtenerNivelDeXelementos(self, maxElemPorCluster, cantPuntos): #devuelve el maximo nivel en la jerarquia que mantenga la cantidad de puntos maxima recibida
        nivel = 0
        ptos = self.cantPuntos()
        if ptos == maxElemPorCluster:
            nivel = self.getNivel(cantPuntos)
        elif ptos > maxElemPorCluster:
            if self.clusters is not None:
                nvl1 = self.clusters[0].obtenerNivelDeXelementos(maxElemPorCluster, cantPuntos)
                nvl2 = self.clusters[1].obtenerNivelDeXelementos(maxElemPorCluster, cantPuntos)
                if nvl1 is not 0:
                    if nvl2 is not 0:
                        if nvl1 > nvl2:
                            nivel = nvl1
                        else:
                            nivel = nvl2
                    else:
                        nivel = nvl1
                else:
                    nivel = nvl2
        elif ptos < maxElemPorCluster:
            nivel = self.getNivel(cantPuntos)
        return nivel

    '''
    tiene 3 puntos?
    si entonces retorno
    no entonces, si
        mayor entonces
            pregunto a los de adentro
        menor entonces
            retorno 0
    
    '''

    #############################################################





    ################----ESPACIO DE TRABAJO DE FABIÁN----##################################







