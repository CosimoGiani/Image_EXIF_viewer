from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtCore import QSize, Qt

class ImageView(QLabel):
    '''
    ImageView class: it contains the logic for displaying the selected model image and for rotating it clockwise and anti-clockwise.

    Attributes:
        - view                     (View): the view represents the window of the application in which the ImageView is placed.
        - controller         (Controller): the controller, in order to retrieve the image to show in the ImageView.
        - rotation                  (int): integer to keep track of the image rotation.
        - selectedImageIndex        (int): the index of the selected image in the image list. It is necessary to let the class understand whether
                                           an image is selected or not to enable the rotation buttons' logic.
    '''

    def __init__(self, view, controller):
        QLabel.__init__(self, view)
        self.view = view
        self.controller = controller
        self.setAlignment(Qt.AlignCenter)
        self.rotation = 0
        self.selectedImageIndex = None

    def showImage(self):
        '''
        Display the image. After having retrieved the current selected image in the list,
        it takes care of displaying the image accordingly to the rotation.
        '''
        imageToShow = self.controller.getSelectedImage()
        if self.rotation == 0:
            self.qpix = QPixmap(imageToShow)
            self.setPixmap(self.qpix.scaled(QSize(min(self.size().width(), 512), min(self.size().height(), 512)),
                                            Qt.KeepAspectRatio, Qt.FastTransformation))
        else: self.setPixmap(self.qpix.scaled(QSize(min(self.size().width(), 512), min(self.size().height(), 512)),
                                        Qt.KeepAspectRatio, Qt.FastTransformation))
        self.rotation = 0

    def resetImageView(self):
        '''
        Remove the image from the view. In other words, it clears the widget from the previous shown image.
        '''
        self.qpix = QPixmap()
        self.setPixmap(self.qpix)

    def setSelectedImageIndex(self, index):
        '''
        Setter for the index of the selected image.
        '''
        self.selectedImageIndex = index

    def rotateToLeft(self):
        '''
        Rotate the displayed image anti-clockwise, i.e. to the left of 90 degrees.
        '''
        if self.selectedImageIndex is not None:
            self.rotation -= 90
            transform = QTransform().rotate(self.rotation)
            self.qpix = self.qpix.transformed(transform, Qt.SmoothTransformation)
            self.showImage()

    def rotateToRight(self):
        '''
        Rotate the displayed image clockwise, i.e. to the right of 90 degrees.
        '''
        if self.selectedImageIndex is not None:
            self.rotation += 90
            transform = QTransform().rotate(self.rotation)
            self.qpix = self.qpix.transformed(transform, Qt.SmoothTransformation)
            self.showImage()