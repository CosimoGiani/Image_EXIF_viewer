import os
import time
from PIL import Image
from PIL.ExifTags import TAGS

class Model:

    '''
    Model class: it holds the data needed by the application and it is, obviously, the model of our MVC.

    Attributes:
        - selectedImage   (str): specifies the image selected in the list (precisely an image is represented by its path).
        - imageList      (list): list of the images added in the app.
        - info           (dict): general info of the selected image.
        - exifData       (dict): EXIF data of the selected image.
        - geoData        (str): geo data (latitude and longitude) of the selected image.
    '''

    def __init__(self):
        self.selectedImage = None
        self.imageList = []
        self.info = {}
        self.exifData = {}
        self.geoData = None

    def checkImage(self, imageToCheck):
        '''
        Check whether the image passed as argument is present in the list.
        If so, it returns 'True'; otherwise it returns 'False'.
        '''
        if imageToCheck in self.imageList:
            return True
        else:
            return False

    def addImage(self, imageToAdd):
        '''
        Add the image received as argument to the image list.
        '''
        self.imageList.append(imageToAdd)

    def getImageList(self):
        '''
        Getter for the image list. It returns the image list in its entirety.
        '''
        return self.imageList

    def getSelectedImageFromIndex(self, imageIndex):
        '''
        Getter for the image selected in the list.
        It returns the image collocated at the passed index.
        '''
        return self.imageList[imageIndex]

    def removeImage(self, imageToRemove):
        '''
        Remove the image received as argument from the image list.
        '''
        self.imageList.remove(imageToRemove)

    def clearImageList(self):
        '''
        Clear the list. Remove all the images.
        '''
        self.imageList.clear()

    def setImage(self, selectedImage):
        '''
        Set the current image to the selected one.
        It is also responsible to extract the info and the EXIF data which will be displayed.
        '''
        self.selectedImage = selectedImage
        self.retrieveInfo()
        self.retrieveEXIF()

    def getSelectedImage(self):
        '''
        Getter for the selected image. It returns the current image selected.
        '''
        return self.selectedImage

    def retrieveInfo(self):
        '''
        Retrieve the general info for the image selected in the list.
        It sets the relative info dict appropriately.
        '''
        self.info = {}
        if self.selectedImage is not None:
            image = Image.open(self.selectedImage)
            self.info['Nome file'] = os.path.basename(image.filename)
            self.info['Formato'] = image.format
            self.info['Dimensione immagine'] = image.size
            self.info['Data creazione'] = time.ctime(os.path.getctime(image.filename))
            self.info['Ultima modifica'] = time.ctime(os.path.getmtime(image.filename))

    def retrieveEXIF(self):
        '''
        Retrieve the EXIF data for the image selected in the list. It also sets the geo location data accordingly to the GPS info.
        If something goes wrong during the data extraction, an exception is caught and the EXIF data will not be displayed.
        '''
        self.geoData = None
        try:
            if self.selectedImage is not None:
                img = Image.open(self.selectedImage)
                if img.format == 'PNG':
                    for tag, value in img.info.items():
                        decoded = TAGS.get(tag, tag)
                        self.exifData[decoded] = value
                else:
                    self.exifData = {TAGS[k]: v
                                     for k, v in img._getexif().items()
                                     if k in TAGS}
                if 'GPSInfo' in self.exifData.keys():
                    latitude = str(self.convertCoordinates(self.exifData['GPSInfo'][2], self.exifData['GPSInfo'][1]))
                    longitude = str(self.convertCoordinates(self.exifData['GPSInfo'][4], self.exifData['GPSInfo'][3]))
                    self.exifData['GPSInfo'] = latitude + ", " + longitude
                    self.geoData = latitude + "," + longitude
        except Exception:
            self.exifData = None

    def convertCoordinates(self, value, cardinalPoint):
        '''
        Convert the GPS latitude and longitude into appropriate values which will be displayed and used in the Google Maps query.
        '''
        d, m, s = value
        if cardinalPoint in ['S', 'W']:
            d = -d
            m = -m
            s = -s
        return d + m / 60.0 + s / 3600.0

    def getInfo(self):
        '''
        Getter for the info dict. If an image is selected from the image list it returns the corresponding general info, otherwise it returns 'None'.
        '''
        if self.selectedImage:
            return self.info
        return None

    def getEXIF(self):
        '''
        Getter for the EXIF data. If an image is selected from the image list it returns the corresponding EXIF data, otherwise it returns 'None'.
        '''
        if self.selectedImage:
            return self.exifData
        return None

    def getGeoData(self):
        '''
        Getter for the geo localization data. It returns the geo data for the selected image.
        '''
        return self.geoData