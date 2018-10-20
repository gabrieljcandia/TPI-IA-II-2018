import sys

from PyQt5 import uic, QtWidgets

from clases.Clases import Cluster
from visual.Figura import Figura

qtCreatorFile2 = "visual/frame.ui" #Nombre del archivo .ui
Ui_Frame, QtBaseClass2 = uic.loadUiType(qtCreatorFile2)


class IGU_Graficos():
    def __init__(self, iguPrinc):
        self.frame = QtWidgets.QFrame()
        self.ui = Ui_Frame()
        self.ui.setupUi(self.frame)
        self.frame.show()
        self.iguPrinc = iguPrinc

        #inicializar elementos ventana
        self.ui.spinCantClusters.setValue(self.iguPrinc.spinCantClusters.value())
        self.ui.spinCantElemPorCluster.setValue(self.iguPrinc.spinCantElemPorCluster.value())

        self.ui.spinCantClusters.valueChanged.connect(self.controlSpinCantClusters)
        self.ui.spinCantElemPorCluster.valueChanged.connect(self.controlSpinCantElemPorCluster)

        #prueba de obtencion de clusters
        Cluster.idProximo = 1
        cluster = self.iguPrinc.miControladora.pruebaClustersStaticos(self.iguPrinc.miControladora) #para probar el dendograma

        #graficos
        graficoSL = Figura(self.ui, self.ui.VLgraficoSL)
        graficoSL.graficar(cluster)
        graficoCL = Figura(self.ui, self.ui.VLgraficoCL)
        graficoCL.graficar(cluster)
        graficoAL = Figura(self.ui, self.ui.VLgraficoAL)
        graficoAL.graficar(cluster)
        self.graficarDendograma(cluster)
        #figura2 = Figura(self.ui, self.ui.VLgraficoCL)
        #figura2.graficar(clusters)
        #figura3 = Figura(self.ui, self.ui.VLgraficoAL)
        #figura3.graficar(clusters)



    #funciones spins
    def controlSpinCantClusters(self, val): #para CantidadClusters
        if val < self.iguPrinc.spinCantPuntos.value() and self.iguPrinc.spinCantPuntos.isEnabled():
            self.ui.spinCantClusters.setValue(self.iguPrinc.spinCantPuntos.value())
        elif (val > self.iguPrinc.spinCantPuntos.value() + self.iguPrinc.spinCantPuntos.value() - 1) and (self.iguPrinc.spinCantPuntos.isEnabled()):
            self.ui.spinCantClusters.setValue(self.iguPrinc.spinCantPuntos.value() + self.iguPrinc.spinCantPuntos.value() - 1)
        self.editCantClusters()

    def controlSpinCantElemPorCluster(self, val):
        if val > self.iguPrinc.spinCantPuntos.value() and self.iguPrinc.spinCantPuntos.isEnabled():
            self.ui.spinCantElemPorCluster.setValue(self.iguPrinc.spinCantPuntos.value())

    #funciones graficos
    def graficarDendograma(self, cluster):
        self.dendogramaSL = Figura(self.ui, self.ui.VLgraficoDendogramaSL)
        self.dendogramaSL.graficarDendograma(cluster, self.iguPrinc.spinCantClusters.value()) #se pasa el cluster de mayor jerarquia
        self.dendogramaCL = Figura(self.ui, self.ui.VLgraficoDendogramaCL)
        self.dendogramaCL.graficarDendograma(cluster, self.iguPrinc.spinCantClusters.value()) #se pasa el cluster de mayor jerarquia
        self.dendogramaAL = Figura(self.ui, self.ui.VLgraficoDendogramaAL)
        self.dendogramaAL.graficarDendograma(cluster, self.iguPrinc.spinCantClusters.value()) #se pasa el cluster de mayor jerarquia

    def editCantClusters(self):
        Cluster.idProximo = 1
        cluster = self.iguPrinc.miControladora.pruebaClustersStaticos(self.iguPrinc.miControladora) #para probar el dendograma
        self.dendogramaSL.graficarDendograma(cluster, self.ui.spinCantClusters.value())
        self.dendogramaCL.graficarDendograma(cluster, self.ui.spinCantClusters.value())
        self.dendogramaAL.graficarDendograma(cluster, self.ui.spinCantClusters.value())
