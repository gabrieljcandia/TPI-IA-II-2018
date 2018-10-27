import matplotlib.pyplot as plt
import copy
import numpy as np
from PyQt5.QtWidgets import QDialog, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import math


class Figura(QDialog):
    def __init__(self, parent, layout):
        super(Figura, self).__init__(parent=None)


        # a figure instance to plot on
        self.figure = plt.figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Just some button connected to `plot` method
        self.button = QPushButton('Plot')
        #self.button.clicked.connect(self.plot)

        # set the layout
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        #layout.addWidget(self.button)
        self.setLayout(layout)

    '''def graficar(self, clusters): #recibe como parametro un grupo de clusters; ver si no conviene pasar solo el cluster de mayor nivel, y recorrer los demas desde ese
        #self.figure.clear()
        ax = self.figure.add_subplot(111)
        for cluster in clusters.getClusters():
            x, y = cluster.getPuntosR2()
            ax.scatter(x, y, s=None, color=[cluster.getRGB()])
            if cluster.clusters is not None:
                self.graficarCirculo(cluster)
        plt.autoscale(enable=True, axis='both', tight=None) #habilita autoscale
        self.canvas.draw()'''

    '''def graficar(self, clusters, maxClusters=None, nvl=None):
        cantPuntos = clusters.cantPuntos()
        nivel = clusters.getNivel()
        if maxClusters is not None and nivel < :
            
        if nivel == nvl:
        
        #self.figure.clear()
        ax = self.figure.add_subplot(111)
        for cluster in clusters.getClusters():
            x, y = cluster.getPuntosR2()
            ax.scatter(x, y, s=None, color=[cluster.getRGB()])
            if cluster.clusters is not None:
                self.graficarCirculo(cluster)
        plt.autoscale(enable=True, axis='both', tight=None) #habilita autoscale
        self.canvas.draw()'''

    '''def graficarCluster(self, cluster, maxElemPorCluster=None):
        self.figure.clear()
        self.ax = self.figure.add_subplot(111)
        clustersOrdenados = cluster.getClustersOrdenados()

        if maxElemPorCluster is not None:
            cantPuntos = cluster.cantPuntos() #devuelve la cantidad de puntos original
            nvl = cluster.obtenerNivelDeXelementos(maxElemPorCluster, cantPuntos)

            for cl in clustersOrdenados:
                a = cl.getNivel(cantPuntos)
                b = cl.getPadre(clustersOrdenados, cantPuntos)
                #c = cl.getPadre(clustersOrdenados, cantPuntos).getNivel(cantPuntos)
                if (maxElemPorCluster is not None) and (cl.getNivel(cantPuntos) <= nvl) and\
                        (cl.getPadre(clustersOrdenados, cantPuntos)) is not None and (cl.getPadre(clustersOrdenados, cantPuntos).getNivel(cantPuntos) > nvl):
                    self.graficarPuntosCluster(cl)
                    self.graficarCirculo(cl)
        else:
            nvl = None

        plt.autoscale(enable=True, axis='both', tight=None) #habilita autoscale
        self.canvas.draw()'''

    def graficarCluster(self, cluster, maxElemPorCluster=None):
        self.figure.clear()
        self.ax = self.figure.add_subplot(111)
        clustersOrdenados = cluster.getClustersOrdenados()

        # recorrer clustersOrdenados y tomar maximo cluster con cant elementos menor al maximo
        # tomar los clusters de mayor nivel que agrupen a los clusters menores o iguales al maximo

        max = 0
        clusters = []
        for cluster in clustersOrdenados:
            if cluster.cantPuntos() <= maxElemPorCluster:
                max = cluster.getId()
                clusters.insert(0, cluster) #inserta "cluster" al inicio de "clusters"

        clustersImpresos = [] #ID de los clusters de nivel 0 que ya se han imprimido
        for cluster in clusters:
            # si puntos del cluster no se han imprimido previamente, imprimirlos

            # inicializar lista
            # si puntos del cluster no se encuentran en lista, imprimir puntos y guardarlos en lista
            if not self.clusterImpreso(cluster, clustersImpresos): # cluster no esta en clustersImpresos:
                self.graficarPuntosCluster(cluster)
                clustersImpresos.append(cluster)

        plt.autoscale(enable=True, axis='both', tight=None) #habilita autoscale
        self.canvas.draw()

    def clusterImpreso(self, cluster, clustersImpresos): # retorna true si cluster se encuentra dentro de clustersImpresos
        impreso = False
        if clustersImpresos is not None:
            for cli in clustersImpresos:
                cls = cli.getClustersContenidosBruto()
                if cls is not None:
                    for cl in cls:
                        if cl.getId() == cluster.getId():
                            impreso = True
        return impreso

    def graficarPuntosCluster(self, cluster):
        x, y = cluster.getPuntosR2()
        #y = np.full((x.__len__(), 1), 0, dtype=int)
        self.ax.scatter(x, y, s=None, color=[cluster.getRGB()])

    def graficarDendogramaHastaElementos(self, cluster, maxClusters=None, maxElemPorCluster=None): #recibe como parametro inicial el cluster de mayor nivel
        self.cluster = cluster
        self.figure.clear()
        self.ax = self.figure.add_subplot(111)

        cantPuntos = cluster.cantPuntos() #devuelve cantidad de puntos original
        cantClusters = cluster.getId() #devuelve ID del cluster de mayor jerarquia, que se corresponde a la cantidad total de clusters

        if maxElemPorCluster is not None:
            nvl = cluster.obtenerNivelDeXelementos(maxElemPorCluster, cantPuntos)
            clustersOrdenados = cluster.getClustersOrdenados()
            # recorrer clustersOrdenados y tomar maximo cluster con cant elementos menor al maximo
            # tomar los clusters de mayor nivel que agrupen a los clusters menores o iguales al maximo

            max = 0
            clusters = []
            for cluster in clustersOrdenados:
                if cluster.cantPuntos() <= maxElemPorCluster and cluster.getNivel(cantPuntos) <= nvl:
                    max = cluster.getId()
                    clusters.insert(0, copy.deepcopy(cluster)) #inserta "cluster" al inicio de "clusters"

            clustersImpresos = [] #ID de los clusters de nivel 0 que ya se han imprimido
            for cluster in clusters:
                # si puntos del cluster no se han imprimido previamente, imprimirlos
                self.graficarDendogramaClusterLineas(cluster, cantPuntos)
                clustersImpresos.append(copy.deepcopy(cluster))

        clustersContenidos = self.cluster.getClustersContenidosBruto()
        for cl in clustersContenidos:
            if cl.getId() <= cantPuntos: #grafica puntos, correspondientes a los puntos originales (de nivel 0 en la jerarquia)
                self.graficarPuntoDendograma(cl)

        plt.autoscale(enable=True, axis='both', tight=None) #habilita autoscale
        self.canvas.draw()

    def graficarDendogramaHastaCluster(self, cluster, maxClusters=None, maxElemPorCluster=None): #recibe como parametro inicial el cluster de mayor nivel
        self.cluster = cluster
        self.figure.clear()
        self.ax = self.figure.add_subplot(111)

        cantPuntos = cluster.cantPuntos() #devuelve cantidad de puntos original
        cantClusters = cluster.getId() #devuelve ID del cluster de mayor jerarquia, que se corresponde a la cantidad total de clusters

        if maxElemPorCluster is not None:
            nvl = cluster.obtenerNivelDeXelementos(maxElemPorCluster, cantPuntos)
        else:
            nvl = None

        if cantPuntos < cluster.getId() and cantPuntos >= 2: #control de entrada
            self.graficarDendogramaCluster(cluster, cantPuntos, cantClusters, maxClusters, maxElemPorCluster, nvl)

        plt.autoscale(enable=True, axis='both', tight=None) #habilita autoscale
        self.canvas.draw()

    '''def graficarDendograma(self, cluster, maxClusters=None, maxElemPorCluster=None): #recibe como parametro inicial el cluster de mayor nivel
        self.cluster = cluster
        self.figure.clear()
        self.ax = self.figure.add_subplot(111)

        cantPuntos = cluster.cantPuntos() #devuelve cantidad de puntos original
        cantClusters = cluster.getId() #devuelve ID del cluster de mayor jerarquia, que se corresponde a la cantidad total de clusters

        if maxElemPorCluster is not None:
            nvl = cluster.obtenerNivelDeXelementos(maxElemPorCluster, cantPuntos)
        else:
            nvl = None

        if cantPuntos < cluster.getId() and cantPuntos >= 2: #control de entrada
            self.graficarDendogramaCluster(cluster, cantPuntos, cantClusters, maxClusters, maxElemPorCluster, nvl)

        plt.autoscale(enable=True, axis='both', tight=None) #habilita autoscale
        self.canvas.draw()'''

    def graficarDendogramaCluster(self, cluster, cantPuntos, cantClusters, maxClusters=None, maxElemPorCluster=None, nvl=None):
        if cluster.clusters is not None:
            if (maxClusters is not None) and (cluster.getId() <= cantClusters - maxClusters + 1): #control limite cantidad clusters
                self.graficarDendogramaClusterLineas(cluster, cantPuntos)
                #if cluster.getId() == cantClusters - maxClusters + 1:
                    #print("a")
                    #self.graficarCluster(cluster)

            if maxElemPorCluster is not None:
                self.graficarDendogramaClusterLineas(cluster, cantPuntos)

            for cl in cluster.clusters: #recursividad
                self.graficarDendogramaCluster(cl, cantPuntos, cantClusters, maxClusters, maxElemPorCluster, nvl)

        if cluster.getId() <= cantPuntos: #grafica puntos, correspondientes a los puntos originales (de nivel 0 en la jerarquia)
            self.graficarPuntoDendograma(cluster)

    def graficarDendogramaClusterLineas(self, cluster, cantPuntos):
        nivel = cluster.getNivel(cantPuntos)
        clIzq = cluster.getClusterIzq()
        clDer = cluster.getClusterDer()
        hIzq = clIzq.getNivel(cantPuntos)
        hDer = clDer.getNivel(cantPuntos)
        xIzq = clIzq.getLink()
        xDer = clDer.getLink()
        self.ax.plot([xIzq, xIzq, xDer, xDer],[hIzq, nivel, nivel, hDer], color=cluster.getRGB())

    def graficarCirculo(self, cluster):
        centroide = cluster.obtenerCentroide()
        ptoDistante = cluster.obtenerMayorDistante(centroide)
        radio = cluster.distanciaEuclidea([ptoDistante[0], centroide[0]], [ptoDistante[1], centroide[1]])
        circle = plt.Circle(centroide, radio, color=cluster.getRGB())
        plt.gcf().gca().add_artist(circle)

    def graficarPuntoDendograma(self, cluster):
        x = cluster.getId()
        self.ax.scatter(x, 0, s=None, color=[cluster.getRGB()])




