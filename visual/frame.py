# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frame.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(818, 463)
        Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.HLresultados = QtWidgets.QHBoxLayout()
        self.HLresultados.setObjectName("HLresultados")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox_4 = QtWidgets.QGroupBox(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(39)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setMinimumSize(QtCore.QSize(278, 84))
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 82))
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.groupBox_4)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 20, 261, 24))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.rbCantClusters = QtWidgets.QRadioButton(self.horizontalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbCantClusters.sizePolicy().hasHeightForWidth())
        self.rbCantClusters.setSizePolicy(sizePolicy)
        self.rbCantClusters.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.rbCantClusters.setObjectName("rbCantClusters")
        self.horizontalLayout_16.addWidget(self.rbCantClusters)
        self.spinCantClusters = QtWidgets.QSpinBox(self.horizontalLayoutWidget_5)
        self.spinCantClusters.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spinCantClusters.setMinimum(1)
        self.spinCantClusters.setMaximum(100000)
        self.spinCantClusters.setObjectName("spinCantClusters")
        self.horizontalLayout_16.addWidget(self.spinCantClusters)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.groupBox_4)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(10, 50, 266, 24))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.rbElemPorCluster = QtWidgets.QRadioButton(self.horizontalLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbElemPorCluster.sizePolicy().hasHeightForWidth())
        self.rbElemPorCluster.setSizePolicy(sizePolicy)
        self.rbElemPorCluster.setObjectName("rbElemPorCluster")
        self.horizontalLayout_17.addWidget(self.rbElemPorCluster)
        self.spinCantElemPorCluster = QtWidgets.QSpinBox(self.horizontalLayoutWidget_6)
        self.spinCantElemPorCluster.setEnabled(False)
        self.spinCantElemPorCluster.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spinCantElemPorCluster.setMinimum(1)
        self.spinCantElemPorCluster.setMaximum(100000)
        self.spinCantElemPorCluster.setObjectName("spinCantElemPorCluster")
        self.horizontalLayout_17.addWidget(self.spinCantElemPorCluster)
        self.horizontalLayout_3.addWidget(self.groupBox_4)
        self.verticalLayout_11.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_11.addLayout(self.horizontalLayout_5)
        self.frame = QtWidgets.QFrame(Frame)
        self.frame.setMinimumSize(QtCore.QSize(0, 266))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalGroupBox_4 = QtWidgets.QGroupBox(self.frame)
        self.verticalGroupBox_4.setGeometry(QtCore.QRect(0, 0, 281, 111))
        self.verticalGroupBox_4.setObjectName("verticalGroupBox_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalGroupBox_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.VLcalculoDistancia = QtWidgets.QVBoxLayout()
        self.VLcalculoDistancia.setContentsMargins(12, -1, -1, -1)
        self.VLcalculoDistancia.setObjectName("VLcalculoDistancia")
        self.rbEuclidea = QtWidgets.QRadioButton(self.verticalGroupBox_4)
        self.rbEuclidea.setObjectName("rbEuclidea")
        self.VLcalculoDistancia.addWidget(self.rbEuclidea)
        self.rbManhattan = QtWidgets.QRadioButton(self.verticalGroupBox_4)
        self.rbManhattan.setObjectName("rbManhattan")
        self.VLcalculoDistancia.addWidget(self.rbManhattan)
        self.rbMinkowski = QtWidgets.QRadioButton(self.verticalGroupBox_4)
        self.rbMinkowski.setObjectName("rbMinkowski")
        self.VLcalculoDistancia.addWidget(self.rbMinkowski)
        self.verticalLayout_3.addLayout(self.VLcalculoDistancia)
        self.verticalLayout_11.addWidget(self.frame)
        spacerItem = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem)
        self.HLresultados.addLayout(self.verticalLayout_11)
        self.VLayoutArbol = QtWidgets.QVBoxLayout()
        self.VLayoutArbol.setObjectName("VLayoutArbol")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.SL = QtWidgets.QVBoxLayout()
        self.SL.setObjectName("SL")
        self.txtSL = QtWidgets.QLabel(Frame)
        self.txtSL.setAlignment(QtCore.Qt.AlignCenter)
        self.txtSL.setObjectName("txtSL")
        self.SL.addWidget(self.txtSL)
        self.SL2 = QtWidgets.QHBoxLayout()
        self.SL2.setObjectName("SL2")
        self.VLgraficoDendogramaSL = QtWidgets.QVBoxLayout()
        self.VLgraficoDendogramaSL.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.VLgraficoDendogramaSL.setObjectName("VLgraficoDendogramaSL")
        self.SL2.addLayout(self.VLgraficoDendogramaSL)
        self.VLgraficoSL = QtWidgets.QVBoxLayout()
        self.VLgraficoSL.setObjectName("VLgraficoSL")
        self.SL2.addLayout(self.VLgraficoSL)
        self.SL.addLayout(self.SL2)
        self.verticalLayout.addLayout(self.SL)
        self.CL = QtWidgets.QVBoxLayout()
        self.CL.setObjectName("CL")
        self.txtCL = QtWidgets.QLabel(Frame)
        self.txtCL.setAlignment(QtCore.Qt.AlignCenter)
        self.txtCL.setObjectName("txtCL")
        self.CL.addWidget(self.txtCL)
        self.CL2 = QtWidgets.QHBoxLayout()
        self.CL2.setObjectName("CL2")
        self.VLgraficoDendogramaCL = QtWidgets.QVBoxLayout()
        self.VLgraficoDendogramaCL.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.VLgraficoDendogramaCL.setObjectName("VLgraficoDendogramaCL")
        self.CL2.addLayout(self.VLgraficoDendogramaCL)
        self.VLgraficoCL = QtWidgets.QVBoxLayout()
        self.VLgraficoCL.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.VLgraficoCL.setObjectName("VLgraficoCL")
        self.CL2.addLayout(self.VLgraficoCL)
        self.CL.addLayout(self.CL2)
        self.verticalLayout.addLayout(self.CL)
        self.AL = QtWidgets.QVBoxLayout()
        self.AL.setObjectName("AL")
        self.txtAL = QtWidgets.QLabel(Frame)
        self.txtAL.setAlignment(QtCore.Qt.AlignCenter)
        self.txtAL.setObjectName("txtAL")
        self.AL.addWidget(self.txtAL)
        self.AL2 = QtWidgets.QHBoxLayout()
        self.AL2.setObjectName("AL2")
        self.VLgraficoDendogramaAL = QtWidgets.QVBoxLayout()
        self.VLgraficoDendogramaAL.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.VLgraficoDendogramaAL.setObjectName("VLgraficoDendogramaAL")
        self.AL2.addLayout(self.VLgraficoDendogramaAL)
        self.VLgraficoAL = QtWidgets.QVBoxLayout()
        self.VLgraficoAL.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.VLgraficoAL.setObjectName("VLgraficoAL")
        self.AL2.addLayout(self.VLgraficoAL)
        self.AL.addLayout(self.AL2)
        self.verticalLayout.addLayout(self.AL)
        self.VLayoutArbol.addLayout(self.verticalLayout)
        self.HLresultados.addLayout(self.VLayoutArbol)
        self.HLresultados.setStretch(1, 1)
        self.horizontalLayout.addLayout(self.HLresultados)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.groupBox_4.setTitle(_translate("Frame", "Personalizar vista"))
        self.rbCantClusters.setText(_translate("Frame", "Cantidad Clusters"))
        self.rbElemPorCluster.setText(_translate("Frame", "Cantidad Elementos por Cluster"))
        self.verticalGroupBox_4.setTitle(_translate("Frame", "Distancia"))
        self.rbEuclidea.setText(_translate("Frame", "Euclídea"))
        self.rbManhattan.setText(_translate("Frame", "Manhattan"))
        self.rbMinkowski.setText(_translate("Frame", "Minkowski"))
        self.txtSL.setText(_translate("Frame", "Single-Link"))
        self.txtCL.setText(_translate("Frame", "Complete-Link"))
        self.txtAL.setText(_translate("Frame", "Average-Link"))

