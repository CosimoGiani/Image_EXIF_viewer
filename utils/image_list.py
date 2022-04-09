from PyQt5.QtWidgets import QListWidget, QListWidgetItem
from PyQt5.QtGui import QPixmap, QIcon, QImage
from PyQt5.QtCore import QSize
from PIL import Image

class ImageList(QListWidget):

    '''
    ImageList class: it represents the list of the images inserted in the model. Particularly it holds the logic of the list and
                     it is also responsible of the arrow buttons' behaviour (i.e. left and right buttons).

    Attributes:
        - view                      (View): the view represents the window of the application in which the ImageList is placed.
        - controller          (Controller): the controller, in order to retrieve the model image list.
        - imageView            (ImageView): reference to the ImageView, in order to display correctly the current selected image.
        - tableData            (TableData): reference to the TableData, in order to update correctly the data in the info and EXIF tabs.
        - selectedImageIndex         (int): integer to keep track of the selected image's index.
    '''

    def __init__(self, controller, view, imageView, tableData):
        QListWidget.__init__(self, view)
        self.controller = controller
        self.view = view
        self.imageView = imageView
        self.tableData = tableData
        self.itemClicked.connect(self.setImage)
        self.setIconSize(QSize(100, 100))
        self.selectedImageIndex = None
        self.view.removeImageButton.clicked.connect(self.removeImage)
        self.view.clearImageListButton.clicked.connect(self.clearImageList)

    def updateList(self):
        '''
        Update the list. Every time this method is called, first it wipes out the present images and then it retrieves
        the current updated image list. Finally for each image it places a representative icon/thumbnail in the list.
        '''
        self.clear()
        list = self.controller.getImageList()
        for img in list:
            image = Image.open(img)
            icon = QIcon(QPixmap.fromImage(QImage(image.filename)))
            item = QListWidgetItem(self)
            item.setIcon(icon)

    def setImage(self):
        '''
        Once an icon in the list is clicked (or is already selected), the corresponding image is displayed and
        the relative data tabs are updated.
        '''
        self.selectedImageIndex = self.currentRow()
        self.controller.selectImageFromIndex(self.selectedImageIndex)
        self.imageView.showImage()
        self.imageView.setSelectedImageIndex(self.selectedImageIndex)
        self.tableData.updateTabsData()

    def removeImage(self):
        '''
        Remove an image. When the remove button in the view is clicked it is invoked this method, which delegates the controller
        to remove the image from the model. Then the list is updated and the image view is cleared as well as the data tabs.
        '''
        if self.selectedImageIndex is not None:
            self.controller.removeImageFromIndex(self.selectedImageIndex)
            self.selectedImageIndex = None
            self.updateList()
            self.imageView.resetImageView()
            self.imageView.setSelectedImageIndex(None)
            self.tableData.clearTabsData()

    def clearImageList(self):
        '''
        Clear the entire list. When the clear button in the view is clicked this method is invoked, which delegates the controller to
        wipe out the whole image list from the model. Then the list is updated and the image view is cleared as well as the data tabs.
        '''
        self.controller.clearImageList()
        self.updateList()
        self.selectedImageIndex = None
        self.imageView.resetImageView()
        self.imageView.setSelectedImageIndex(None)
        self.tableData.clearTabsData()

    def goPrevious(self):
        '''
        Go to the previous image. If an image is selected and it is not the first in the list in order of appearance,
        it is possible to navigate to the previous image.
        '''
        if self.imageView.selectedImageIndex is not None:
            if self.selectedImageIndex > 0:
                self.selectedImageIndex -= 1
                self.setCurrentRow(self.selectedImageIndex)
                self.setImage()

    def goNext(self):
        '''
        Go to the next image. If an image is selected and it is not the last in the list in order of appearance,
        it is possible to navigate to the next image.
        '''
        if self.imageView.selectedImageIndex is not None:
            if self.selectedImageIndex < len(self.controller.getImageList()) - 1:
                self.selectedImageIndex += 1
                self.setCurrentRow(self.selectedImageIndex)
                self.setImage()