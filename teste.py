'''
Created on 19/02/2015

@author: miguel.reginaldo
'''

# import sys
# from PyQt4.QtCore import *
# from PyQt4.QtGui import *
# 
# if __name__ == "__main__":
# 
#     app = QApplication(sys.argv)
#     
#     qt_translator = QTranslator()
#     print qt_translator.load("qt_al",
#                        QLibraryInfo.location(QLibraryInfo.TranslationsPath))
#     app.installTranslator(qt_translator)
#     
#     QMessageBox.aboutQt(None)
#     sys.exit()


# from PyQt4.QtGui import *
# from PyQt4.QtCore import *
# import os
 
# class MyWindow(QWidget):
#     def __init__(self, parent=None):
#         super(QWidget, self).__init__(parent)
#  
#         self.hbox = QHBoxLayout(self)
#         self.myButtons = QDialogButtonBox(self)
#         self.hbox.addWidget(self.myButtons)
#         button = self.myButtons.addButton(QDialogButtonBox.Open)
#         QMessageBox.critical(self, self.tr('Fatiador'),
#                                  self.tr('You must enter the Input and Output Files!'),
#                                  buttons=QMessageBox.Ok,
#                                  defaultButton=QMessageBox.NoButton)
#  
# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     translator = QTranslator()
#     print translator.load("qt_fr", QLibraryInfo.location(QLibraryInfo.TranslationsPath))
#     app.installTranslator(translator)
#     ui = MyWindow()
#     ui.show()
#     sys.exit(app.exec_())
    

# plugin_dir = os.path.dirname(__file__)
# print plugin_dir
# # initialize locale
# #locale = QSettings().value("locale/overrideFlag")[0:2]
# print QSettings().value("locale/userLocale", "")
# print QLocale.system().name(), QLocale.UnitedStates
# print QLocale.system().Portuguese, QLocale.Brazil
# print QLocale.system().language(), QLocale.system().country()
# locale = QLocale.system().Brazil, QLocale.Brazil,QLocale.system().country(), QLocale.countryToString(QLocale.system().country())
# print locale
# localePath = os.path.join(plugin_dir, 'i18n', 'fatiador_{}.qm'.format(locale))
# print localePath
# 
# plugin_dir = os.path.dirname(__file__)
# path = os.path.join(plugin_dir, 'help', 'index_%s.html'%QLocale.system().name())
# if not os.path.exists(path):
#     path = os.path.join(plugin_dir, 'help', 'index.html') 
#     
# url = QUrl()
# url.setUrl(QString('file:///'+path))
# QDesktopServices.openUrl(url)
# 
# 
# 
# slices = [(90,200),(200,250),(250,300),(300,350)]
# 
# listclas = range(1, len(slices)+1)
# print listclas


import numpy as np

rasterArray = np.array([[1,4,2,4,3,-99],
              [4,2,3,2,5,7],
              [3,0,5,6,7,8]])
print rasterArray

array_slice = np.array([[0,0,0,0,0,0],
              [0,0,0,0,0,0],
              [0,0,0,0,0,0]])



noDataValue = -99

slices = [(0,2),(2,5),(5,10)]


for cl, sl in enumerate(slices):
    cri = (rasterArray<=sl[0])|(rasterArray>sl[1])
    array_crit = np.where(cri,0,cl+1)
    array_slice = array_slice + array_crit

array_slice[array_slice==0]=noDataValue
print array_slice


# 
#     cri_0 = (a<=0)|(a>2)
#     
#     
#     cri_1 = (a<=2)|(a>5)
#     
#     
#     cri_2 = (a<=5)|(a>10)
# 
# 
# print np.where(cri_0,0,1) + np.where(cri_1,0,2) + np.where(cri_2,0,3)










