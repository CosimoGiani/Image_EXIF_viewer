class Controller:
    '''
    Controller class: it contains the methods used by the view widgets to communicate with the model.
    It is, obviously, the controller of our MVC.

    Attributes:
        - model    (Model): the model, in order to access to the needed data.
    '''

    def __init__(self, model):
        self.model = model

    def checkImageExistance(self, imageToCheck):
        '''
        Check whether the image passed as argument is present in the model image list.
        If so, it returns 'True'; otherwise it returns 'False'.
        '''
        if self.model.checkImage(imageToCheck):
            return True
        else:
            return False

    def addImage(self, imageToAdd):
        '''
        Add the image received as argument to the model image list.
        '''
        self.model.addImage(imageToAdd)

    def getImageList(self):
        '''
        Getter for the model image list.
        '''
        return self.model.getImageList()

    def removeImageFromIndex(self, imageIndex):
        '''
        Remove the image contained in the model image list at the corresponding index passed as argument.
        '''
        imageToRemove = self.model.getSelectedImageFromIndex(imageIndex)
        self.model.removeImage(imageToRemove)

    def clearImageList(self):
        '''
        Clear the model image list. Remove all the images.
        '''
        self.model.clearImageList()

    def selectImageFromIndex(self, imageIndex):
        '''
        Set the model image to the one selected based on its index.
        '''
        selectedImage = self.model.getSelectedImageFromIndex(imageIndex)
        self.model.setImage(selectedImage)

    def getSelectedImage(self):
        '''
        Getter for the model selected image. It returns the current image selected.
        '''
        return self.model.getSelectedImage()

    def getTabsData(self):
        '''
        Getter for the model data. Particularly it returns the general info and the EXIF data stored in the model.
        '''
        info = self.model.getInfo()
        exifData = self.model.getEXIF()
        return info, exifData

    def getGeoData(self):
        '''
        Getter for the model geo data. It returns the localization info.
        '''
        return self.model.getGeoData()