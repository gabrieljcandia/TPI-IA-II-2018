import sys

from PyQt5 import uic, QtWidgets

from clases.Clases import Cluster
from visual.Figura import Figura

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


            ####graficos V1 (Estatico)#######################################################
        #prueba de obtencion de clusters
        ''''Cluster.idProximo = 1
        cluster = self.iguPrinc.miControladora.pruebaClustersStaticos(self.iguPrinc.miControladora) #para probar el dendograma

        graficoSL = Figura(self.ui, self.ui.VLgraficoSL)
        graficoSL.graficar(cluster)
        graficoCL = Figura(self.ui, self.ui.VLgraficoCL)
        graficoCL.graficar(cluster)
        graficoAL = Figura(self.ui, self.ui.VLgraficoAL)
        graficoAL.graficar(cluster)
        self.graficarDendograma(cluster)'''

            ####graficos V2 (Funcional)#######################################################
        #calculo de clusters (logica)

        #while len(self.iguPrinc.miControladora.getClusters()) > 1:
        for i in range(9):
            self.iguPrinc.miControladora.simple2()

        self.clusterSL = self.iguPrinc.miControladora.getClusters()[0]
        #Cluster.idProximo = 1
        #self.clusterSL = self.iguPrinc.miControladora.pruebaClustersStaticos()

        '''self.clusterCL = cluster.obtenerCL()
        self.clusterAL = cluster.obtenerAL()
        '''
        #graficar clusers por metodo

        self.graficoSL = Figura(self.ui, self.ui.VLgraficoSL)
        self.graficoSL.graficarCluster(self.clusterSL, self.ui.spinCantElemPorCluster.value())
        '''graficoCL = Figura(self.ui, self.ui.VLgraficoCL)
        graficoCL.graficar(self.clusterCL)
        graficoAL = Figura(self.ui, self.ui.VLgraficoAL)
        graficoAL.graficar(self.clusterAL)
        self.graficarDendograma(cluster)
        '''
        #luego se grafica el dendograma. Modificar metodo "graficarDendograma" para que pase los clusters adecuados

        self.graficarDendogramas(self.clusterSL)


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

    def controlRbPersonalizarVista(self):
        if self.ui.rbCantClusters.isChecked():
            self.ui.spinCantClusters.setEnabled(True)
            self.ui.spinCantElemPorCluster.setEnabled(False)
        if self.ui.rbElemPorCluster.isChecked():
            self.ui.spinCantClusters.setEnabled(False)
            self.ui.spinCantElemPorCluster.setEnabled(True)
        self.editCantClusters()


    #funciones graficos
    def graficarDendogramas(self, cluster):
        if self.ui.rbCantClusters.isChecked():
            cantClusters = self.iguPrinc.spinCantClusters.value()
            cantElemPorCluster = None
        elif self.ui.rbElemPorCluster.isChecked():
            cantElemPorCluster = self.iguPrinc.spinCantElemPorCluster.value()
            cantClusters = None

        self.dendogramaSL = Figura(self.ui, self.ui.VLgraficoDendogramaSL)
        self.dendogramaSL.graficarDendogramaHastaElementos(cluster, cantClusters, cantElemPorCluster) #se pasa el cluster de mayor jerarquia
        #self.dendogramaCL = Figura(self.ui, self.ui.VLgraficoDendogramaCL)
        #self.dendogramaCL.graficarDendogramaHastaElementos(cluster, cantClusters, cantElemPorCluster) #se pasa el cluster de mayor jerarquia
        #self.dendogramaAL = Figura(self.ui, self.ui.VLgraficoDendogramaAL)
        #self.dendogramaAL.graficarDendogramaHastaElementos(cluster, cantClusters, cantElemPorCluster) #se pasa el cluster de mayor jerarquia


    def editCantClusters(self):
        #Cluster.idProximo = 1
        #cluster = self.iguPrinc.miControladora.pruebaClustersStaticos() #para probar el dendograma

        if self.ui.rbCantClusters.isChecked():
            cantClusters = self.ui.spinCantClusters.value()
            cantElemPorCluster = None
            self.dendogramaSL.graficarDendogramaHastaCluster(self.clusterSL, cantClusters, cantElemPorCluster)
        elif self.ui.rbElemPorCluster.isChecked():
            cantElemPorCluster = self.ui.spinCantElemPorCluster.value()
            cantClusters = None
            self.dendogramaSL.graficarDendogramaHastaElementos(self.clusterSL, cantClusters, cantElemPorCluster)


        #self.dendogramaCL.graficarDendogramaHastaElementos(cluster, cantClusters, cantElemPorCluster)
        #self.dendogramaAL.graficarDendogramaHastaElementos(cluster, cantClusters, cantElemPorCluster)

        self.graficoSL.graficarCluster(self.clusterSL, self.ui.spinCantElemPorCluster.value())
