import os

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from qgis.core import QgsProject
from qgis.PyQt.QtWidgets import QFileDialog

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'StylePalapa_dialog_base2.ui'))

class StylePalapaDialog(QtWidgets.QDialog, FORM_CLASS):
    
    def __init__(self, parent=None):
        """Constructor."""
        super(StylePalapaDialog, self).__init__(parent)
        self.setupUi(self)
        self.upload.clicked.connect(self.import_layer)
        self.browser.clicked.connect(self.import_meteadata)
      
    def import_layer(self):
        layerName = self.select_layer.currentText()
        print(layerName)
        layer = QgsProject().instance().mapLayersByName(layerName)[0]
        layer.saveSldStyle(f'D:/{layerName}.sld')
        os.remove(f'D:/{layerName}.sld')

    def import_meteadata(self):
        filename1, text = QFileDialog.getOpenFileName()
        self.select_layer.setText(filename1)
        print(filename1)
