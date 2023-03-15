# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 15:21:45 2023

@author: migue
"""

# Brainflow documentation: https://brainflow.readthedocs.io/en/stable/UserAPI.html

# cd C:\Users\migue\OneDrive\Ambiente de Trabalho\EEG comparison
# python acquisition_comparison.py --eeg cyton --serial-port COM6

import argparse
import logging
import numpy as np

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtWidgets

from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds
from brainflow.data_filter import DataFilter, FilterTypes, DetrendOperations

def eeg_systemId(_id):
    
    # Maps the EEG system name to the brainflow Id parameter of the corresponding system
    
    if(_id == "cyton"):
        board_id = BoardIds.CYTON_BOARD
        isCyton = True 
    elif(_id == "crown"):
        # https://console.neurosity.co/settings
        board_id = BoardIds.CROWN_BOARD
        isCyton = False
    elif(_id == "muse"):
        # How to use: https://bio-medical.com/media/support/muse-brain-sensing-headband-user-guide.pdf
        # python acquisition_comparison.py --eeg muse --mac-address 00:55:da:b3:af:39 --serial-number 2041-C4VH-AF39 --ip-port 5000 --ip-address 192.168.1.1
        board_id = BoardIds.MUSE_2016_BOARD.value
        isCyton = False
    elif(_id == "muse2"):
        board_id = BoardIds.MUSE_2_BOARD
        isCyton = False
    elif(_id == "test"):
        board_id = BoardIds.SYNTHETIC_BOARD
        isCyton = False
    return board_id, isCyton

def cyton_channels_sep(channel_string):

    individual_chs = channel_string.split(',')
    return individual_chs

class Graph:
    
    # Live graph class
    
    def __init__(self, board_shim, cyton_channels):
        
        # The constructor method initializes various instance variables
        
        self.board_id = board_shim.get_board_id()
        self.board_shim = board_shim
        self.eeg_channels = BoardShim.get_eeg_channels(self.board_id) 
        self.sampling_rate = BoardShim.get_sampling_rate(self.board_id)
        if(len(cyton_channels) > 1):
            self.channel_labels = cyton_channels
            self.eeg_channels = self.eeg_channels[0:len(self.channel_labels)]
        else:
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
        self.colors = ['#A54E4E', '#A473B6', '#5B45A4', '#2079D2', '#32B798', '#2FA537', '#9DA52F', '#A57E2F', '#A53B2F'] # Hex
        self.col_sz = len(self.colors)
        for i in range(len(self.colors)):
            pen = pg.mkPen({'color': self.colors[i], 'width': 2}) # mkPen refers to the outline of a shape object. mkBrush is to fill the shapes (e.g., histograms)
            self.pens.append(pen)

    def _init_timeseries(self):
        
        # Sets up the plots and curves for the live graph
        # It initializes empty lists for plots and curves, and creates a plot for each EEG channel. 
        # It then creates a curve for each plot and adds it to the curves list.
    
        self.plots = list()
        self.curves = list()
        self.sz = len(self.channel_labels)
        for i in range(self.sz):
            p = self.win.addPlot(row=i, col=0) # Object of each plot
            p.showAxis('left', False)
            p.setMenuEnabled('left', False)
            p.setYRange(-100,100)
            p.setMouseEnabled(x = False, y = False)
            if i < self.sz-1:
                p.showAxis('bottom', False)
            else:
                p.showAxis('bottom', True)
                p.setLabel('bottom','Time (ms)')
            p.setMenuEnabled('bottom', False)
            p.setTitle(self.channel_labels[i], color = self.colors[i % self.col_sz], size = "12pt")
            self.plots.append(p)
            curve = p.plot(pen = self.pens[i % self.col_sz])
            self.curves.append(curve)
                    
    def update(self):
        
        # This method is called at regular intervals by the QTimer created in the constructor
        # Finally, it updates the curves with the filtered data and processes any pending events in the application event loop using app.processEvents()
        
        data = self.board_shim.get_current_board_data(self.num_points) # Gets data from the board

        for count, channel in enumerate(self.eeg_channels):
            
            DataFilter.detrend(data[channel], DetrendOperations.CONSTANT.value)
            DataFilter.perform_bandpass(data[channel], self.sampling_rate, 3.0, 45.0, 2,
                                     FilterTypes.BUTTERWORTH.value, 0)
            DataFilter.perform_bandstop(data[channel], self.sampling_rate, 48.0, 52.0, 2,
                                     FilterTypes.BUTTERWORTH.value, 0)
            DataFilter.perform_bandstop(data[channel], self.sampling_rate, 58.0, 62.0, 2,
                                     FilterTypes.BUTTERWORTH.value, 0)
            self.curves[count].setData(data[channel].tolist()) # setData is the method that updates the graph from the initial plot object reference
        
        self.app.processEvents()

def main():
    BoardShim.enable_dev_board_logger()
    logging.basicConfig(level=logging.DEBUG) # Sets the logging level to debug, which means that debug messages will be printed to the console.

    parser = argparse.ArgumentParser()
    
    # For the Cyton board, only the board_id (0) and serial port must be passed to the script
    #Parser for command-line options, arguments and sub-commands: https://docs.python.org/3/library/argparse.html
    
    parser.add_argument('--eeg', type=str, 
                        help='EEG headband, check docs to get a list of supported boards: https://brainflow.readthedocs.io/en/stable/SupportedBoards.html#supported-boards-label',
                        required=True, default='')
    parser.add_argument('--channels', type=cyton_channels_sep,
                        help='Headbad channels that will be used. For example, write in order and seperated by a comma from pins NP1 to NP8: [Fp1, Fp2,...]',
                        required=False, default='')
    parser.add_argument('--timeout', type=int, help='Timeout for device discovery or connection', required=False,
                        default=0)
    parser.add_argument('--ip-port', type=int, help='IP port', required=False, default=0)
    parser.add_argument('--ip-protocol', type=int, help='IP protocol, check IpProtocolType enum', required=False,
                        default=0)
    parser.add_argument('--ip-address', type=str, help='IP address', required=False, default='')
    parser.add_argument('--serial-port', type=str, help='Serial port', required=False, default='')
    parser.add_argument('--mac-address', type=str, help='Mac address', required=False, default='')
    parser.add_argument('--other-info', type=str, help='Other info', required=False, default='')
    parser.add_argument('--streamer-params', type=str, help='Streamer params', required=False, default='')
    parser.add_argument('--serial-number', type=str, help='Serial number', required=False, default='')
    parser.add_argument('--file', type=str, help='File', required=False, default='')
    parser.add_argument('--master-board', type=int, help='Master board id for streaming and playback boards',
                        required=False, default=BoardIds.NO_BOARD)
    args = parser.parse_args()

    params = BrainFlowInputParams()
    params.ip_port = args.ip_port
    params.serial_port = args.serial_port
    params.mac_address = args.mac_address
    params.other_info = args.other_info
    params.serial_number = args.serial_number
    params.ip_address = args.ip_address
    params.ip_protocol = args.ip_protocol
    params.timeout = args.timeout
    params.file = args.file
    params.master_board = args.master_board

    try:
        
        # https://brainflow.readthedocs.io/en/stable/UserAPI.html
        
        board_id, isCyton = eeg_systemId(args.eeg)
        if (isCyton):
            cyton_ch = args.channels
        else:
            cyton_ch = ""
        print("\nBoard description: \n")
        print(BoardShim.get_board_descr(board_id,0)) # 0 is the default preset
        print("\n")
        board = BoardShim(board_id, params)
        board.prepare_session()
        board.start_stream(450000, args.streamer_params)
        Graph(board, cyton_ch)
    except BaseException:
        print("--------------------------------------------------------------------------------------------------------------------------")
        logging.warning('Exception', exc_info=True)
        print("--------------------------------------------------------------------------------------------------------------------------")
    finally:
        logging.info('End')
        if board.is_prepared():
            logging.info('Releasing session')
            board.release_session()


if __name__ == '__main__':
    main()