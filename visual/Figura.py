from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import copy
import numpy as np
from PyQt5.QtWidgets import QDialog, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import math


class Figura(QDialog):
    def __init__(self, parent, layout, iguPrinc):
        super(Figura, self).__init__(parent=None)
        self.iguPrinc = iguPrinc

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

    def graficarCluster(self, cluster, maxElemPorCluster=None, maxClusters=None):
        self.figure.clear()
        if self.iguPrinc.miControladora.dimensiones == 2:
            self.ax = self.figure.add_subplot(111)
        else:
            self.ax = self.figure.add_subplot(111, projection='3d')

        clustersOrdenados = cluster.getClustersOrdenados()

        # recorrer clustersOrdenados y tomar maximo cluster con cant elementos menor al maximo
        # tomar los clusters de mayor nivel que agrupen a los clusters menores o iguales al maximo
        if maxElemPorCluster is not None:
            max = 0
            clusters = []
            for cluster in clustersOrdenados:
                if cluster.cantPuntos() <= maxElemPorCluster:
                    max = cluster.getId()
                    clusters.insert(0, cluster) #inserta "cluster" al inicio de "clusters"

            clustersImpresos = [] #ID de los clusters de nivel 0 que ya se han impreso
            for cluster in clusters:
                # si puntos del cluster no se han imprimido previamente, imprimirlos
                if not self.clusterImpreso(cluster, clustersImpresos): # cluster no esta en clustersImpresos:
                    self.graficarPuntosCluster(cluster)
                    clustersImpresos.append(cluster)

        if maxClusters is not None:
            if maxClusters == 1:
                self.graficarPuntosCluster(cluster) #grafica cluster de nivel mas alto
            else:
                self.graficarPuntosCluster(cluster) #grafica cluster de nivel mas alto
                for cl in clustersOrdenados:
                    if (cl.getId() < cluster.getId()) and (cl.getId() <= (cluster.getId() - maxClusters + 1)):
                        self.graficarPuntosCluster(cl)

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
        if self.iguPrinc.miControladora.dimensiones == 2:
            x, y = cluster.getPuntosR2()
            self.ax.scatter(x, y, s=None, color=[cluster.getRGB()])
        else:
            x, y, z = cluster.getPuntosR3()
            self.ax.scatter(x, y, z, color=[cluster.getRGB()])


    def graficarDendogramaHastaElementos(self, cluster, maxClusters=None, maxElemPorCluster=None): #recibe como parametro inicial el cluster de mayor nivel
        self.cluster = cluster #para usar al final del metodo, porque en el camino se modifica su contenido
        self.figure.clear()
        self.ax = self.figure.add_subplot(111)

        cantPuntos = cluster.cantPuntos() #devuelve cantidad de puntos original

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
        for cl in reversed(clustersContenidos): #imprime los puntos del dendograma, correspondientes a los puntos originales (de nivel 0 en la jerarquia)
            if cl.getId() <= cantPuntos:
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

    def graficarDendogramaCluster(self, cluster, cantPuntos, cantClusters, maxClusters=None, maxElemPorCluster=None, nvl=None):
        if cluster.clusters is not None:
            if (maxClusters is not None) and (cluster.getId() <= cantClusters - maxClusters + 1): #control limite cantidad clusters
                self.graficarDendogramaClusterLineas(cluster, cantPuntos)

            if maxElemPorCluster is not None:
                self.graficarDendogramaClusterLineas(cluster, cantPuntos)

            for cl in cluster.clusters: #recursividad
                self.graficarDendogramaCluster(cl, cantPuntos, cantClusters, maxClusters, maxElemPorCluster, nvl)

        if cluster.getId() <= cantPuntos: #grafica puntos, correspondientes a los puntos originales (de nivel 0 en la jerarquia)
            self.graficarPuntoDendograma(cluster)

    def graficarDendogramaClusterLineas(self, cluster, cantPuntos):
        modificarAltura = False
        nivel = cluster.getNivel(cantPuntos)
        clIzq = cluster.getClusterIzq()
        clDer = cluster.getClusterDer()

        if clIzq is clDer:
            clIzq = cluster.getClusterIzqIguales()
            clDer = cluster.getClusterDerIguales()

            xIzq = clIzq.getLinkIguales()
            xDer = clDer.getLinkIguales()

            modificarAltura = True

        hIzq = clIzq.getNivel(cantPuntos)
        hDer = clDer.getNivel(cantPuntos)

        if modificarAltura is False:
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




