import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QIcon

from xml.dom import minidom
xmldoc = minidom.parse('config.xml')
itemlist = xmldoc.getElementsByTagName('item') 

app = QApplication(sys.argv)
 
wv = QWebEngineView()
wv.setWindowTitle('App queue')
wv.setWindowIcon(QIcon('favicon.ico'))
 
if itemlist[1].attributes['mode'].value=='fullscreen' :
    wv.showFullScreen()
else:
    wv.showMaximized() 
 
wv.load(QUrl(itemlist[0].attributes['url'].value))
wv.show()

app.exec_()
