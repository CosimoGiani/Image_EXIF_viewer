import webbrowser
from PyQt5.QtWidgets import QWidget, QPushButton, QFileDialog, QListView, QHBoxLayout, QVBoxLayout, QMessageBox, QSizePolicy
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt
from utils.image_list import ImageList
from utils.image_view import ImageView
from utils.table_data import TableData

class View(QWidget):

    '''
    View class: it represents the application window and it is, obviously, the view of our MVC.

    Attributes:
        - controller    (Controller): the controller, which is needed every time the user interacts with the view.
        - title                (str): title of the application window.
        - left                 (int): distance from the left side of the screen and the window.
        - top                  (int): distance from the top side of the screen and the window.
        - width                (int): starting width of the window.
        - height               (int): starting height of the window.
    '''

    def __init__(self, controller):
        super().__init__()
        self.title = 'Image EXIF Viewer'
        self.left = 500
        self.top = 200
        self.width = 800
        self.height = 600
        self.controller = controller
        self.initUI()

    def initUI(self):
        '''
        Initialize the window interface with all the needed components.
        '''

        # Set the window title, the distance between the window and the border of the screen and the initial size.
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Button for adding an image to the app. Shortcut: "Ctrl+o"
        self.addImageButton = QPushButton('Aggiungi immagine', self)
        self.addImageButton.clicked.connect(self.addImage)
        self.addImageButton.setShortcut('Ctrl+o')

        # Button for deleting an image from the app. Shortcut: "Ctrl+d"
        self.removeImageButton = QPushButton('Rimuovi immagine', self)
        self.removeImageButton.setShortcut('Ctrl+d')

        # Button for clearing the whole image list. Shortcut: "Del"
        self.clearImageListButton = QPushButton('Svuota tutto', self)
        self.clearImageListButton.setShortcut('Del')

        # Instance of the ImageView class, needed for displaying the current selected image.
        self.imageToShow = ImageView(self, self.controller)
        # The following lines are needed for managing the rescaling of the image view.
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageToShow.sizePolicy().hasHeightForWidth())
        self.imageToShow.setSizePolicy(sizePolicy)
        self.imageToShow.setMinimumSize(QSize(256, 256))
        self.imageToShow.setAlignment(Qt.AlignCenter)
        self.imageToShow.setBaseSize(QSize(0, 0))
        self.imageToShow.setLayoutDirection(Qt.LeftToRight)
        self.imageToShow.setScaledContents(False)

        # Instance of the TableData class, needed for displaying the info and the EXIF data of the selected image.
        self.tableData = TableData(view = self, controller = self.controller)
        self.tableData.setMinimumSize(QSize(350, 350))

        # Instance of the ImageList class, needed for displaying the list/queue of images stored in the model.
        self.imageList = ImageList(controller = self.controller, view = self, imageView = self.imageToShow, tableData = self.tableData)
        self.imageList.setFlow(QListView.LeftToRight)
        self.imageList.setMaximumHeight(120)

        # Button for rotating the current selected image to the left, i.e. anti-clockwise. Shortcut: "Down"
        self.leftRotate = QPushButton()
        self.leftRotate.setFixedWidth(50)
        self.leftRotate.setIcon(QIcon('icons/leftrotate.png'))
        self.leftRotate.setIconSize(QSize(25, 25))
        self.leftRotate.clicked.connect(self.imageToShow.rotateToLeft)
        self.leftRotate.setShortcut('Down')

        # Button for switching the current selected image to the previous one if possible. Shortcut: "Left"
        self.leftArrow = QPushButton()
        self.leftArrow.setFixedWidth(50)
        self.leftArrow.setIcon(QIcon('icons/left.png'))
        self.leftArrow.setIconSize(QSize(25, 25))
        self.leftArrow.clicked.connect(self.imageList.goPrevious)
        self.leftArrow.setShortcut('Left')

        # Button for switching the current selected image to the next one if possible. Shortcut: "Right"
        self.rightArrow = QPushButton()
        self.rightArrow.setFixedWidth(50)
        self.rightArrow.setIcon(QIcon('icons/right.png'))
        self.rightArrow.setIconSize(QSize(25, 25))
        self.rightArrow.clicked.connect(self.imageList.goNext)
        self.rightArrow.setShortcut('Right')

        # Button for rotating the current selected image to the right, i.e. clockwise. Shortcut: "Up"
        self.rightRotate = QPushButton()
        self.rightRotate.setFixedWidth(50)
        self.rightRotate.setIcon(QIcon('icons/rightrotate.png'))
        self.rightRotate.setIconSize(QSize(25, 25))
        self.rightRotate.clicked.connect(self.imageToShow.rotateToRight)
        self.rightRotate.setShortcut('Up')

        # Button for the geolocalization. Shortcut: "Ctrl+m"
        self.locationButton = QPushButton()
        self.locationButton.setFixedWidth(150)
        self.locationButton.setIcon(QIcon('icons/map.png'))
        self.locationButton.setIconSize(QSize(25, 25))
        self.locationButton.setText(' Apri mappa')
        self.locationButton.clicked.connect(self.setGeoButton)
        self.locationButton.setShortcut('Ctrl+m')

        # The following lines are dedicated to organize the window layout
        topWindowLayout = QHBoxLayout()
        buttonsLayout = QVBoxLayout()
        buttonsLayout.addWidget(self.addImageButton)
        buttonsLayout.addWidget(self.removeImageButton)
        buttonsLayout.addWidget(self.clearImageListButton)
        topWindowLayout.addLayout(buttonsLayout)
        topWindowLayout.addWidget(self.imageList)

        windowLayout = QVBoxLayout()
        centerWindowLayout = QHBoxLayout()
        imageAndButtonsLayout = QVBoxLayout()
        tableAndPlaceLayout = QVBoxLayout()
        tableLayout = QVBoxLayout()
        placeLayout = QHBoxLayout()
        imageButtonsLayout = QHBoxLayout()
        imageButtonsLayout.addWidget(self.leftRotate)
        imageButtonsLayout.addWidget(self.leftArrow)
        imageButtonsLayout.addWidget(self.rightArrow)
        imageButtonsLayout.addWidget(self.rightRotate)
        imageAndButtonsLayout.addWidget(self.imageToShow)
        imageAndButtonsLayout.addLayout(imageButtonsLayout)
        tableLayout.addWidget(self.tableData)
        placeLayout.addWidget(self.locationButton)
        tableAndPlaceLayout.addLayout(tableLayout)
        tableAndPlaceLayout.addLayout(placeLayout)
        windowLayout.addLayout(topWindowLayout)
        centerWindowLayout.addLayout(imageAndButtonsLayout)
        centerWindowLayout.addLayout(tableAndPlaceLayout)
        windowLayout.addLayout(centerWindowLayout)

        layout = QVBoxLayout()
        layout.addLayout(windowLayout)

        self.setLayout(layout)
        self.show()

    def addImage(self):
        '''
        Add an image to the app. When the add button is pressed, an open file dialog pops up in order to select which
        image you want to add. It is effectively added to the image list if it is not already present.
        '''
        image, _ = QFileDialog.getOpenFileName(
            self,
            "",
            "",
            "All Files (*);;Images (*.jpg, *.jpeg, *.png, *.JPG, *.PNG)",
            )
        if image and not self.controller.checkImageExistance(image):
            self.controller.addImage(image)
            self.imageList.updateList()

    def setGeoButton(self):
        '''
        Set the query for the geolocalization button. First the geo data are retrieved by the controller, then a Google
        Maps query is written using the latitude and longitude stored in the geo data. Once the geolocalization button is
        pressed it is opened a new web browser page accordingly to the Google Maps query. Otherwise, if the controller
        could not retrieve the geo data, an alert box pops up advising the user that the operation failed.
        '''
        if self.imageToShow.selectedImageIndex is not None:
            geoData = self.controller.getGeoData()
            if geoData is not None:
                url = "https://www.google.it/maps?q=" + geoData
                webbrowser.open_new(url)
            else:
                QMessageBox.about(self, "Errore", "Informazioni GPS non presenti")

    def resizeEvent(self, ev):
        '''
        Method necessary to resize the image shown in the ImageView accordingly to the user interaction with the
        window size.
        '''
        self.imageToShow.showImage()
        super().resizeEvent(ev)