from PyQt5.QtWidgets import QTabWidget, QWidget, QVBoxLayout, QTreeWidget, QLabel, QTreeWidgetItem, QShortcut, QApplication
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QKeySequence

class TableData(QTabWidget):

    '''
    TableData class: custom widget to display the general information and EXIF data of a selected image. The data are
                     grouped under a Tree widget inside a specific tab.

    Attributes:
        - view                   (View): the view represents the window of the application in which the TableData is placed.
        - controller       (Controller): the controller, in order to retrieve the info and EXIF data from the model.
    '''

    def __init__(self, view, controller):
        super(TableData, self).__init__(view)
        self.view = view
        self.controller = controller
        shortcutTab = QShortcut(QKeySequence(Qt.Key_Tab), self)
        shortcutTab.activated.connect(self.nextTab)
        shortcutBackTab = QShortcut(QKeySequence(Qt.Key_Backtab), self)
        shortcutBackTab.activated.connect(self.previousTab)

    def initializeTabs(self):
        '''
        Initialize the tabs and add them to the widget.
        '''
        self.clear()
        self.infoTab = QWidget()
        self.exifTab = QWidget()
        self.addTab(self.infoTab, 'Info generali')
        self.addTab(self.exifTab, 'EXIF')

    @pyqtSlot()
    def nextTab(self):
        '''
        Switch to the next tab. This method is only used for the keyboard shortcut to switch to the next tab.
        '''
        self.changeTab((self.currentIndex() + 1) % self.count())

    @pyqtSlot()
    def previousTab(self):
        '''
        Switch to the previous tab. This method is only used for the keyboard shortcut to switch to the previous tab.
        '''
        self.changeTab((self.currentIndex() - 1) % self.count())

    def changeTab(self, index):
        '''
        Every time the keyboard shortcut to switch tab is pressed it is invoked this method, which manages the logic
        responsible to change the tab focus once the shortcut is pressed.
        '''
        focusWidget = QApplication.focusWidget()
        tabIndex = focusWidget.property('tab_index') if focusWidget else None
        self.setCurrentIndex(index)
        if tabIndex is not None and self.currentWidget() is not None:
            for widget in self.currentWidget().findChildren(QWidget):
                i = widget.property('tab_index')
                if i == tabIndex:
                    widget.setFocus(True)

    def clearTabsData(self):
        '''
        Clear the data in the tabs. It removes the info and the EXIF data from the tabs once the selected image is removed
        or the whole image list is wiped out.
        '''
        self.clear()

    def updateTabsData(self):
        '''
        Update the data contained in each tab, i.e. the general info and the EXIF data. First it initializes new tabs
        and the it fills them with the appropriate data.
        '''
        self.initializeTabs()
        info, exifData = self.controller.getTabsData()
        self.updateInfo(info)
        self.updateEXIF(exifData)

    def updateInfo(self, info):
        '''
        Update the info tab with the data passed as argument. It is also responsible to organize these data, if available,
        into a TreeWidget and set the layout accordingly.
        '''
        if info is not None:
            layout = QVBoxLayout()
            if len(info):
                infoTree = QTreeWidget()
                self.writeTab(infoTree, info)
                infoTree.setHeaderLabel('Dettagli:')
            else:
                infoTree = QLabel()
                infoTree.setAlignment(Qt.AlignCenter)
                infoTree.setText('Informazioni generali non disponibili')
            layout.addWidget(infoTree)
            self.setTabText(0, 'Info generali')
            self.infoTab.setLayout(layout)

    def updateEXIF(self, exifData):
        '''
        Update the EXIF tab with the data passed as argument. It is also responsible to organize these data, if available,
        into a TreeWidget and set the layout accordingly.
        '''
        if exifData is not None:
            if len(exifData):
                exifTree = QTreeWidget()
                self.writeTab(exifTree, exifData)
                exifTree.setHeaderLabel('Data:')
            else:
                exifTree = QLabel()
                exifTree.setAlignment(Qt.AlignCenter)
                exifTree.setText('Dati EXIF non disponibili')
        else:
            exifTree = QLabel()
            exifTree.setAlignment(Qt.AlignCenter)
            exifTree.setText('Dati EXIF non disponibili')
        layout = QVBoxLayout()
        layout.addWidget(exifTree)
        self.setTabText(1, 'EXIF')
        self.exifTab.setLayout(layout)

    def writeTab(self, widget, data):
        '''
        Associate data to a widget. First it makes sure the widget is "brand new" and then it invokes the appropriate
        method to fill the data into the widget.
        '''
        self.widget = widget
        self.widget.clear()
        self.writeData(self.widget.invisibleRootItem(), data)

    def writeData(self, item, data):
        '''
        Fill the item received as a parameter with the corresponding data. Precisely, it is responsible to populate
        the TreeWidget that composes the tab, accordingly to the received data.
        '''
        item.setExpanded(True)
        if type(data) is dict:
            for key, val in data.items():
                child = QTreeWidgetItem()
                child.setText(0, str(key))
                item.addChild(child)
                self.writeData(child, val)
        elif type(data) is list:
            for val in data:
                child = QTreeWidgetItem()
                item.addChild(child)
                if type(val) is dict:
                    child.setText(0, '[dict]')
                    self.writeData(child, val)
                elif type(val) is list:
                    child.setText(0, '[list]')
                    self.writeData(child, val)
                else:
                    child.setText(0, str(val))
                    child.setExpanded(True)
        else:
            child = QTreeWidgetItem()
            child.setText(0, str(data))
            item.addChild(child)