from PyQt5.QtWidgets import QSizePolicy, QWidget, QVBoxLayout

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
import matplotlib

# Ensure using PyQt5 backend
matplotlib.use('QT5Agg')


# Matplotlib canvas class to create figure
class MplCanvas(Canvas):
    def __init__(self):
        self.fig = Figure()
        # gs = self.fig.add_gridspec(2, 2, hspace=0, wspace=0)
        # (self.ax1, self.ax2), (self.ax3, self.ax4) = gs.subplots(sharex='col', sharey='row')
        Canvas.__init__(self, self.fig)
        Canvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        Canvas.updateGeometry(self)


# Matplotlib widget
class MplWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)        # Inherit from QWidget
        self.canvas = MplCanvas()             # Create canvas object
        self.vbl = QVBoxLayout()              # Set box for plotting
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)
