import sys 
import bpy
from importlib import reload

from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtCore
from PyQt5 import QtWidgets

from StoneEdgeGeneration import utils, UI
from StoneEdgeGeneration.UI import BaseWindow
reload(utils)
reload(UI)
reload(BaseWindow)

class AssetWindow(BaseWindow.BaseWindow):
    def __init__(self):
        super(AssetWindow, self).__init__()
        self.setWindowTitle("Asset Generation")
