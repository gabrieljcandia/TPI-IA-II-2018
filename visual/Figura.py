import matplotlib.pyplot as plt
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

    def graficar(self, clusters): #recibe como parametro un grupo de clusters; ver si no conviene pasar solo el cluster de mayor nivel, y recorrer los demas desde ese
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        for cluster in clusters.getClusters():
            x, y = cluster.getPuntosR2()
            ax.scatter(x, y, s=None, color=[cluster.getRGB()])
            if cluster.clusters is not None:
                self.graficarCirculo(cluster)
        plt.autoscale(enable=True, axis='both', tight=None) #habilita autoscale
        self.canvas.draw()

    def graficarDendograma(self, cluster, maxClusters=None, maxElemPorCluster=None): #recibe como parametro inicial el cluster de mayor nivel
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

            if (maxElemPorCluster is not None) and (cluster.getNivel(cantPuntos) <= nvl):
                self.graficarDendogramaClusterLineas(cluster, cantPuntos)

            for cl in cluster.clusters: #recursividad
                    self.graficarDendogramaCluster(cl, cantPuntos, cantClusters, maxClusters, maxElemPorCluster, nvl)

        if cluster.getId() <= cantPuntos: #grafica puntos, correspondientes a los puntos originales (de nivel 0 en la jerarquia)
                x = cluster.getId()
                self.ax.scatter(x, 0, s=None, color=[cluster.getRGB()])

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
        circle = plt.Circle(centroide, radio, color=cluster.getRGB(), fill=False, lw=3)
        plt.gcf().gca().add_artist(circle)



