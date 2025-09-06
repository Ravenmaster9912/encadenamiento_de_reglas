from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene, QGraphicsTextItem, QGraphicsEllipseItem, QGraphicsLineItem
from PySide2.QtCore import Slot, Qt, QRectF, QPointF
from ui_mainwindow import Ui_MainWindow
from PySide2.QtGui import *
from queue import PriorityQueue
from pprint import pprint

class MainWindow(QMainWindow):
    def __init__(self): 
        super(MainWindow, self).__init__()

        self.objetos = ['','A','B','C','D','E','F','G','H','I','J','K','L','M']
        self.estado = ['','V','F']

        self.objtDic = {
            'A': '',
            'B': '',
            'C': '',
            'D': '',
            'E': '',
            'F': '',
            'G': '',
            'H': '',
            'J': '',
            'K': '',
            'L': '',
            'M': ''
        }

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.sceneMp = QGraphicsScene()
        self.sceneMt = QGraphicsScene()

        self.ui.mp_graphicsView.setScene(self.sceneMp)
        self.ui.mt_graphicsView.setScene(self.sceneMt)

        self.ui.aceptar_pushButton.clicked.connect(self.mp)
        #self.ui.aceptar_pushButton.clicked.connect(self.mt)
        self.ui.limpiar_pushButton.clicked.connect(self.limpiar)

        self.ui.h1_comboBox.addItems(self.objetos)
        self.ui.h1vf_comboBox.addItems(self.estado)
        self.ui.h2_comboBox.addItems(self.objetos)
        self.ui.h2vf_comboBox.addItems(self.estado)
        self.ui.h3_comboBox.addItems(self.objetos)
        self.ui.h3vf_comboBox.addItems(self.estado)
        self.ui.h4_comboBox.addItems(self.objetos)
        self.ui.h4vf_comboBox.addItems(self.estado)

        self.ui.nodo_comboBox.addItems(self.objetos)

    
    def wheelEvent(self, event):
        #print(event.delta())
        if event.delta() > 0:
            self.ui.mp_graphicsView.scale(1.2, 1.2)
            self.ui.mt_graphicsView.scale(1.2, 1.2)
        else:
            self.ui.mp_graphicsView.scale(0.8, 0.8)
            self.ui.mt_graphicsView.scale(0.8, 0.8)
    
    @Slot( )
    def mp(self):
        self.limpiar()
        # Crear vista y escena
        r1 = self.ui.h1_comboBox.currentText()
        r1Valor = self.ui.h1vf_comboBox.currentText()
        r2 = self.ui.h2_comboBox.currentText()
        r2Valor = self.ui.h2vf_comboBox.currentText()
        r3 = self.ui.h3_comboBox.currentText()
        r3Valor = self.ui.h3vf_comboBox.currentText()
        r4 = self.ui.h4_comboBox.currentText()
        r4Valor = self.ui.h4vf_comboBox.currentText()
        nodo = self.ui.nodo_comboBox.currentText()

        # Pen para dibujar líneas
        self.pen = QPen(Qt.black, 2)
        self.brush = QBrush(Qt.white)
        self.fBrush = QBrush(Qt.gray)

        # Crear nodos
        nodes = {
            "A": (50, 50),
            "B": (50, 120),
            "C": (150, 85),
            "D": (50, 200),
            "E": (50, 270),
            "F": (50, 340),
            "G": (200, 250),
            "H": (50, 420),
            "I": (50, 490),
            "J": (150, 455),
            "K": (300, 150),
            "L": (300, 350),
            "M": (400, 250),
        }

        # Conexiones entre nodos (origen, destino, etiqueta)
        edges = [
            ("A", "C"),
            ("B", "C"),
            ("D", "G"),
            ("E", "G"),
            ("F", "G"),
            ("H", "J"),
            ("I", "J"),
            ("C", "K"),
            ("J", "L"),
            ("G", "K"),
            ("G", "L"),
            ("K", "M"),
            ("L", "M"),
        ]

        #Modus ponens
        for src, dst in edges:
            p1 = nodes[src]
            p2 = nodes[dst]

            line = QGraphicsLineItem(p1[0]+15, p1[1]+12, p2[0]+15, p2[1]+12)
            line.setPen(self.pen)
            self.sceneMp.addItem(line)

        # Dibujar nodos como círculos con texto
        self.node_items = {}
        for label, (x, y) in nodes.items():
            #if (nodes[label] == 'v'):
            circle = QGraphicsEllipseItem(QRectF(x, y, 40, 40))
            circle.setPen(self.pen)
            circle.setBrush(self.brush) 
            text = QGraphicsTextItem(label, circle)
            text.setPos(x + 12, y + 8)
            self.sceneMp.addItem(circle)
            self.node_items[label] = (circle, QPointF(x + 20, y + 20))

        if(nodo != ''):
            selectedNode = QGraphicsEllipseItem(QRectF(nodes[nodo][0]-5,nodes[nodo][1]-5,50,50))
            selectedNode.setPen(self.pen)
            self.sceneMp.addItem(selectedNode)
        
        #Modus tollens

    @Slot( )
    def limpiar(self):
        '''for item in self.objetos:
            self.objetos[item] = '''
            
        self.sceneMp.clear()
        self.sceneMp.clear()
        self.ui.resultadomp_label.setText("")
        self.ui.resultadomt_label.setText("")

    '''@Slot( )
    def mt(self):'''
