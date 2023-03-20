# https://pypi.org/project/thu-rsvp-dataset/
# https://www.physionet.org/content/ltrsvp/1.0.0/

import mne
import sys, os, re
import numpy as np
import matplotlib as plt

fname = "eeg-signals-from-an-rsvp-task-1.0.0"

# Loading the dataset files

def run_fast_scandir(dir, ext):    
    subfolders, datafiles = [], []

    for f in os.scandir(dir):
        if f.is_dir():
            subfolders.append(f.path)
        if f.is_file():
            if os.path.splitext(f.name)[1].lower() in ext:
                datafiles.append(f.path)

    for dir in list(subfolders):
        sf, f = run_fast_scandir(dir, ext)
        subfolders.extend(sf)
        datafiles.extend(f)
    return subfolders, datafiles

dt_folder = 'C:/Users/migue/OneDrive/Ambiente de Trabalho/EEG comparison/eeg-signals-from-an-rsvp-task-1.0.0/5-Hz'
subfolders, datafiles = run_fast_scandir(dt_folder, [".edf"])
datafiles.sort();

# Reading data

# Disable prints
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore prints
def enablePrint():
    sys.stdout = sys.__stdout__

blockPrint()

# MNE does not load the data into memory by default, just links to the file in the directory.
# preload = True enables the loading of the data into memory for processing
data = mne.io.read_raw_edf(datafiles[6], preload = True)
annotations = data.annotations
annotations.description = [re.sub(r"T=0.*", "T0",d) for d in annotations.description] # Renames the classes of the annotations object removing the section related to the position of the image on the x axis
annotations.description = [re.sub(r"T=1.*", "T1",d) for d in annotations.description]
data.set_annotations(annotations) 
enablePrint()

print("Data info: \n")
print(data.info)

# Returns 3 columns: [Sample Index, Trigger value's Channel, Label of the event] with just the bocks of data from the labels T0 and T1
events = mne.events_from_annotations(data, event_id = {'T0': 1, 'T1': 2}) 
#mne.viz.plot_events(events[0])

#data.plot(block=True) 

# Epoching

event_ids = {"standard/stimulus": 1, "target/stimulus": 2}
epochs = mne.Epochs(data, events[0], event_id = event_ids, preload = True)
print("Epochs info: \n")
print(epochs.info)
#epochs.plot(block=True)

epochs["target"].plot_image(picks=[1])


