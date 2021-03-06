import sys

from PyQt5 import uic, QtWidgets

from clases.Clases import Cluster
from visual.Figura import Figura

#from visual.frame.py import Ui_Frame
qtCreatorFile2 = "visual/frame.ui" #Nombre del archivo .ui
Ui_Frame, QtBaseClass2 = uic.loadUiType(qtCreatorFile2)


class IGU_Graficos():
    def __init__(self, iguPrinc, clusters):
        self.frame = QtWidgets.QFrame()
        self.ui = Ui_Frame()
        self.ui.setupUi(self.frame)
        self.frame.show()
        self.iguPrinc = iguPrinc

        ####Inicializar elementos ventana
        #Spins
        self.ui.spinCantClusters.setValue(self.iguPrinc.spinCantClusters.value())
        self.ui.spinCantElemPorCluster.setValue(self.iguPrinc.spinCantElemPorCluster.value())

        self.ui.spinCantClusters.valueChanged.connect(self.controlSpinCantClusters)
        self.ui.spinCantElemPorCluster.valueChanged.connect(self.controlSpinCantElemPorCluster)

        #radio buttons
        self.agruparRbPersonalizarVista()
        self.inicializarRbPersonalizarVista()
        self.ui.rbCantClusters.clicked.connect(self.controlRbPersonalizarVista)
        self.ui.rbElemPorCluster.clicked.connect(self.controlRbPersonalizarVista)

        self.ui.rbEuclidea.clicked.connect(self.controlRbPersonalizarVista)
        self.ui.rbManhattan.clicked.connect(self.controlRbPersonalizarVista)
        self.ui.rbMinkowski.clicked.connect(self.controlRbPersonalizarVista)


        ###Calculo de clusters por cada algoritmo y distancia
        '''for i in range(self.iguPrinc.miControladora.getClusters().__len__()):
            self.iguPrinc.miControladora.agrupamiento(1, "euclidea", 1)

        self.clusterSL = self.iguPrinc.miControladora.getClusters()[0]
        self.clusterCL = self.iguPrinc.miControladora.getClusters()[0]
        self.clusterAL = self.iguPrinc.miControladora.getClusters()[0]'''

        self.iguPrinc.miControladora.generarClusters(3)
        '''for i in range(self.iguPrinc.miControladora.getClusters().__len__()):
            self.iguPrinc.miControladora.simple()
        self.clusterSL = self.iguPrinc.miControladora.getClusters()[0]'''

        self.clusterSL_Eu = self.iguPrinc.miControladora.getClusterSingleEuclideo()[0]
        self.clusterCL_Eu = self.iguPrinc.miControladora.getClusterCompleteEuclideo()[0]
        self.clusterAL_Eu = self.iguPrinc.miControladora.getClusterAverageEuclideo()[0]

        self.clusterSL_Mi = self.iguPrinc.miControladora.getClusterSingleMinshowski()[0]
        self.clusterCL_Mi = self.iguPrinc.miControladora.getClusterCompleteMinshowski()[0]
        self.clusterAL_Mi = self.iguPrinc.miControladora.getClusterAverageMinshowski()[0]

        self.clusterSL_Ma = self.iguPrinc.miControladora.getClusterSingleManhattan()[0]
        self.clusterCL_Ma = self.iguPrinc.miControladora.getClusterCompleteManhattan()[0]
        self.clusterAL_Ma = self.iguPrinc.miControladora.getClusterAverageManhattan()[0]

        #inicializar figuras donde iran los graficos
        self.graficoSL = Figura(self.ui, self.ui.VLgraficoSL, self.iguPrinc)
        self.graficoCL = Figura(self.ui, self.ui.VLgraficoCL, self.iguPrinc)
        self.graficoAL = Figura(self.ui, self.ui.VLgraficoAL, self.iguPrinc)

        self.graficarClusters()
        self.graficarDendogramas()

    #funciones spins
    def controlSpinCantClusters(self, val): #para CantidadClusters
        if val > self.iguPrinc.spinCantPuntos.value():
            self.ui.spinCantClusters.setValue(self.iguPrinc.spinCantPuntos.value())
        self.editCantClusters()

    def controlSpinCantElemPorCluster(self, val):
        if val > self.iguPrinc.spinCantPuntos.value():
            self.ui.spinCantElemPorCluster.setValue(self.iguPrinc.spinCantPuntos.value())
        self.editCantClusters()

    #funciones radio buttons
    def agruparRbPersonalizarVista(self):
        #crear grupo de radio buttons
        self.rbGroup = QtWidgets.QButtonGroup()
        self.rbGroup.addButton(self.ui.rbCantClusters)
        self.rbGroup.addButton(self.ui.rbElemPorCluster)

    def inicializarRbPersonalizarVista(self):
        if self.iguPrinc.rbCantClusters.isChecked():
            self.ui.rbCantClusters.setChecked(True)
            self.ui.spinCantClusters.setValue(self.iguPrinc.spinCantClusters.value())
        elif self.iguPrinc.rbElemPorCluster.isChecked():
            self.ui.rbElemPorCluster.setChecked(True)
            self.ui.spinCantElemPorCluster.setValue(self.iguPrinc.spinCantElemPorCluster.value())
            self.ui.spinCantElemPorCluster.setEnabled(True)
            self.ui.spinCantClusters.setEnabled(False)

        if self.iguPrinc.rbEuclidea.isChecked():
            self.ui.rbEuclidea.setChecked(True)
            self.ui.rbManhattan.setChecked(False)
            self.ui.rbMinkowski.setChecked(False)
        if self.iguPrinc.rbManhattan.isChecked():
            self.ui.rbEuclidea.setChecked(False)
            self.ui.rbManhattan.setChecked(True)
            self.ui.rbMinkowski.setChecked(False)
        if self.iguPrinc.rbMinkowski.isChecked():
            self.ui.rbEuclidea.setChecked(False)
            self.ui.rbManhattan.setChecked(False)
            self.ui.rbMinkowski.setChecked(True)

    def controlRbPersonalizarVista(self):
        if self.ui.rbCantClusters.isChecked():
            self.ui.spinCantClusters.setEnabled(True)
            self.ui.spinCantElemPorCluster.setEnabled(False)
        if self.ui.rbElemPorCluster.isChecked():
            self.ui.spinCantClusters.setEnabled(False)
            self.ui.spinCantElemPorCluster.setEnabled(True)
        self.editCantClusters()


    #funciones graficos
    def graficarDendogramas(self):
        self.dendogramaSL = Figura(self.ui, self.ui.VLgraficoDendogramaSL, self.iguPrinc)
        self.dendogramaCL = Figura(self.ui, self.ui.VLgraficoDendogramaCL, self.iguPrinc)
        self.dendogramaAL = Figura(self.ui, self.ui.VLgraficoDendogramaAL, self.iguPrinc)

        if self.ui.rbCantClusters.isChecked():
            cantClusters = self.iguPrinc.spinCantClusters.value()
            cantElemPorCluster = None
            self.dendogramaSL.graficarDendogramaHastaCluster(self.clusterSL, cantClusters, cantElemPorCluster)
            self.dendogramaCL.graficarDendogramaHastaCluster(self.clusterCL, cantClusters, cantElemPorCluster)
            self.dendogramaAL.graficarDendogramaHastaCluster(self.clusterAL, cantClusters, cantElemPorCluster)

        elif self.ui.rbElemPorCluster.isChecked():
            cantElemPorCluster = self.iguPrinc.spinCantElemPorCluster.value()
            cantClusters = None
            self.dendogramaSL.graficarDendogramaHastaElementos(self.clusterSL, cantClusters, cantElemPorCluster) #se pasa el cluster de mayor jerarquia
            self.dendogramaCL.graficarDendogramaHastaElementos(self.clusterCL, cantClusters, cantElemPorCluster) #se pasa el cluster de mayor jerarquia
            self.dendogramaAL.graficarDendogramaHastaElementos(self.clusterAL, cantClusters, cantElemPorCluster) #se pasa el cluster de mayor jerarquia

    def editCantClusters(self):
        self.graficarClusters()

        if self.ui.rbCantClusters.isChecked():
            cantClusters = self.ui.spinCantClusters.value()
            cantElemPorCluster = None
            self.dendogramaSL.graficarDendogramaHastaCluster(self.clusterSL, cantClusters, cantElemPorCluster)
            self.dendogramaCL.graficarDendogramaHastaCluster(self.clusterCL, cantClusters, cantElemPorCluster)
            self.dendogramaAL.graficarDendogramaHastaCluster(self.clusterAL, cantClusters, cantElemPorCluster)
        elif self.ui.rbElemPorCluster.isChecked():
            cantElemPorCluster = self.ui.spinCantElemPorCluster.value()
            cantClusters = None
            self.dendogramaSL.graficarDendogramaHastaElementos(self.clusterSL, cantClusters, cantElemPorCluster)
            self.dendogramaCL.graficarDendogramaHastaElementos(self.clusterCL, cantClusters, cantElemPorCluster)
            self.dendogramaAL.graficarDendogramaHastaElementos(self.clusterAL, cantClusters, cantElemPorCluster)

    def graficarClusters(self):
        if self.ui.rbCantClusters.isChecked():
            cantClusters = self.ui.spinCantClusters.value()
            cantElemPorCluster = None
        elif self.ui.rbElemPorCluster.isChecked():
            cantElemPorCluster = self.ui.spinCantElemPorCluster.value()
            cantClusters = None

        if self.ui.rbEuclidea.isChecked():
            self.clusterSL = self.clusterSL_Eu
            self.clusterCL = self.clusterCL_Eu
            self.clusterAL = self.clusterAL_Eu
        if self.ui.rbManhattan.isChecked():
            self.clusterSL = self.clusterSL_Ma
            self.clusterCL = self.clusterCL_Ma
            self.clusterAL = self.clusterAL_Ma
        if self.ui.rbMinkowski.isChecked():
            self.clusterSL = self.clusterSL_Mi
            self.clusterCL = self.clusterCL_Mi
            self.clusterAL = self.clusterAL_Mi

        self.graficoSL.graficarCluster(self.clusterSL, cantElemPorCluster, cantClusters)
        self.graficoCL.graficarCluster(self.clusterCL, cantElemPorCluster, cantClusters)
        self.graficoAL.graficarCluster(self.clusterAL, cantElemPorCluster, cantClusters)
