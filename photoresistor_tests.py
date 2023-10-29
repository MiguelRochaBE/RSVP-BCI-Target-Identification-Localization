# Documentação do Brainflow: https://brainflow.readthedocs.io/en/stable/UserAPI.html

'''
Este scrip é executado a partir do terminal de forma a definir os elétrodos onde se quer adquirir o EEG

Para correr o script é preciso primeiro definir o diretório onde ele está:
- cd path

De seguida:
- python acquisition_brainflow.py --subject 1 --age 25 --gender Male

'''

# Setup importante da cyton/cyton+daisy: https://docs.openbci.com/Troubleshooting/FTDI_Fix_Windows/
# https://brainflow.readthedocs.io/en/stable/UserAPI.html

import keyboard
import logging

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtWidgets

from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds

channel_labels = ['C3','CP3','P3','PO3','P7','PO7','Fz','Cz','CPz','Pz','C4','CP4','P4','PO4','P8','PO8']

class Graph:
    
    # Live graph class
    
    def __init__(self, board_shim):
        
        # The constructor method initializes various instance variables
        
        self.board_id = board_shim.get_board_id()
        self.board_shim = board_shim
        self.eeg_channels = BoardShim.get_eeg_channels(self.board_id) 
        self.sampling_rate = BoardShim.get_sampling_rate(self.board_id)
        self.channel_labels = BoardShim.get_eeg_names(self.board_id)
        self.update_speed_ms = 50
        self.window_size = 4
        self.num_points = self.window_size * self.sampling_rate
        
        self.app = QtWidgets.QApplication([])
        self.app.setAttribute(QtCore.Qt.AA_Use96Dpi)
        self.win = pg.GraphicsLayoutWidget(title='EEG data', show=True, size=(1280, 720)) # Convenience class consisting of a GraphicsView with a single GraphicsLayout as its central item.

        self._init_pens()
        self._init_timeseries()

        timer = QtCore.QTimer()
        timer.timeout.connect(self.update)
        timer.start(self.update_speed_ms)
        QtWidgets.QApplication.instance().exec_()

    def _init_pens(self):

        # Graph customization

        self.pens = list()
        self.colors = '#A54E4E' # Hex color
        pen = pg.mkPen({'color': self.colors, 'width': 2}) # mkPen refers to the outline of a shape object. mkBrush is to fill the shapes (e.g., histograms)
        self.pens.append(pen)

    def _init_timeseries(self):
        
        # Sets up the plots and curves for the live graph
        # It initializes empty lists for plots and curves, and creates a plot for each EEG channel. 
        # It then creates a curve for each plot and adds it to the curves list.
    
        self.plots = list()
        self.curves = list()

        p = self.win.addPlot(row=1, col=0) # Object of each plot
        p.showAxis('left', False)
        p.setMenuEnabled('left', False)
        p.setYRange(0,300)
        p.setMouseEnabled(x = False, y = False)
        p.showAxis('bottom', False)
        p.showAxis('bottom', True)
        p.setLabel('bottom','Time (ms)')
        p.setMenuEnabled('bottom', False)
        p.setTitle('Photoresistor', color = self.colors, size = "12pt")
        self.plots.append(p)
        curve = p.plot(pen = self.pens)
        self.curves.append(curve)
                    
    def update(self):

        # This method is called at regular intervals by the QTimer created in the constructor
        # Finally, it updates the curves with the filtered data and processes any pending events in the application event loop using app.processEvents()
        
        data = self.board_shim.get_current_board_data(self.num_points) # Gets data from the board
        ldr = data[24] # Analog pin D12.
        self.curves.setData(ldr.tolist()) # setData is the method that updates the graph from the initial plot object reference
        self.app.processEvents()
        #print(data[self.eeg_channels])

def main():
    BoardShim.enable_dev_board_logger()
    logging.basicConfig(level=logging.DEBUG) # Ativa as mensagens log do brainflow para fazer debug
    board_id = BoardIds.CYTON_DAISY_BOARD.value
    params = BrainFlowInputParams()
    params.serial_port = 'COM7' # Porta COM do BT dongle no PC

    try:
    
        print("\nBoard description: \n")
        print(BoardShim.get_board_descr(board_id,0)) # 0 is the default preset
        print("\n")

        board = BoardShim(board_id, params)
        board.prepare_session()
        board.start_stream(450000)

        if keyboard.is_pressed('esc'): # Clicar no esc para parar o stream.
            stopStream(board)

        Graph(board)

    except BaseException:
        print("--------------------------------------------------------------------------------------------------------------------------")
        logging.warning('Exception', exc_info=True)
        print("--------------------------------------------------------------------------------------------------------------------------")
    finally:
        stopStream(board)

def stopStream(board): # Termina a sessão corretamente
    logging.info('End')
    if board.is_prepared():
        logging.info('Releasing session')
        board.release_session()  


if __name__ == '__main__':
    main()