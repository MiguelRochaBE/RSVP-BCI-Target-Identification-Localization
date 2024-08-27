#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.3),
    on março 26, 2024, at 01:20
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from code
import pandas as pd
import random

# ------------------------------------------- .xlsx file path -------------------------------------------

file_path = 'C:/Users/migue/OneDrive/Ambiente de Trabalho/Tese/AcquisitionProtocols/FEUP_droneImages.xlsx'



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.3'
expName = 'FeupDroneImages_Protocol'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\migue\\OneDrive\\Ambiente de Trabalho\\Tese\\AcquisitionProtocols\\RealDroneImg_Protocol\\FeupDroneImages_Protocol_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1280, 720], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "Welcome_Screen" ---
text = visual.TextStim(win=win, name='text',
    text='Welcome!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Instructions_Screen" ---
instructions_text = visual.TextStim(win=win, name='instructions_text',
    text='Images captured by a Drone at FEUP will be shown in rapid succession. \nPay attention to the images with minimal head movements if possible.\n\nMentally count each instance of an image of a human laying down (red seater), which can show up in every possible position of the image.\n\nPress the SPACEBAR key when you are ready to start the Experiment.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instructions_space = keyboard.Keyboard()

# --- Initialize components for Routine "EOG_Screen" ---
EOG_text = visual.TextStim(win=win, name='EOG_text',
    text='Blink you eyes every 1 to 2 seconds.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
stim_square_EOG = visual.Rect(
    win=win, name='stim_square_EOG',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(-0.9, -0.5), anchor='bottom-left',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "EMG_Screen" ---
EMG_text = visual.TextStim(win=win, name='EMG_text',
    text='Clench your jaw every 1 to 2 seconds.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
stim_square_EMG = visual.Rect(
    win=win, name='stim_square_EMG',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(-0.9, -0.5), anchor='bottom-left',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "Coding_Trials" ---
# Run 'Begin Experiment' code from code
imgs_file = pd.read_excel(file_path)

permutation = np.random.permutation(imgs_file.index)
shuffled_df = imgs_file.loc[permutation]

img = shuffled_df['Image'].values

# --- Initialize components for Routine "fixation_cross" ---
fix_cross = visual.ShapeStim(
    win=win, name='fix_cross', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=0.5,     colorSpace='rgb',  lineColor='white', fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "trial" ---
trialImage = visual.ImageStim(
    win=win,
    name='trialImage', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.593, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=256.0, interpolate=True, depth=0.0)
stim_square = visual.Rect(
    win=win, name='stim_square',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(-0.9, -0.5), anchor='bottom-left',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "trial_BlockScreen" ---
trial_Blocktext = visual.TextStim(win=win, name='trial_Blocktext',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
trial_space = keyboard.Keyboard()

# --- Initialize components for Routine "GoodBye_Screen" ---
goddbye_text = visual.TextStim(win=win, name='goddbye_text',
    text='Thank you for participating!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Welcome_Screen" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Welcome_ScreenComponents = [text]
for thisComponent in Welcome_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Welcome_Screen" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 2.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    
    # if text is starting this frame...
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text.started')
        # update status
        text.status = STARTED
        text.setAutoDraw(True)
    
    # if text is active this frame...
    if text.status == STARTED:
        # update params
        pass
    
    # if text is stopping this frame...
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.stopped')
            # update status
            text.status = FINISHED
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Welcome_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Welcome_Screen" ---
for thisComponent in Welcome_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-2.000000)

# --- Prepare to start Routine "Instructions_Screen" ---
continueRoutine = True
# update component parameters for each repeat
instructions_space.keys = []
instructions_space.rt = []
_instructions_space_allKeys = []
# keep track of which components have finished
Instructions_ScreenComponents = [instructions_text, instructions_space]
for thisComponent in Instructions_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Instructions_Screen" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_text* updates
    
    # if instructions_text is starting this frame...
    if instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_text.frameNStart = frameN  # exact frame index
        instructions_text.tStart = t  # local t and not account for scr refresh
        instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instructions_text.started')
        # update status
        instructions_text.status = STARTED
        instructions_text.setAutoDraw(True)
    
    # if instructions_text is active this frame...
    if instructions_text.status == STARTED:
        # update params
        pass
    
    # *instructions_space* updates
    waitOnFlip = False
    
    # if instructions_space is starting this frame...
    if instructions_space.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_space.frameNStart = frameN  # exact frame index
        instructions_space.tStart = t  # local t and not account for scr refresh
        instructions_space.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_space, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instructions_space.started')
        # update status
        instructions_space.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructions_space.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructions_space.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructions_space.status == STARTED and not waitOnFlip:
        theseKeys = instructions_space.getKeys(keyList=['space'], waitRelease=False)
        _instructions_space_allKeys.extend(theseKeys)
        if len(_instructions_space_allKeys):
            instructions_space.keys = _instructions_space_allKeys[-1].name  # just the last key pressed
            instructions_space.rt = _instructions_space_allKeys[-1].rt
            instructions_space.duration = _instructions_space_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instructions_Screen" ---
for thisComponent in Instructions_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if instructions_space.keys in ['', [], None]:  # No response was made
    instructions_space.keys = None
thisExp.addData('instructions_space.keys',instructions_space.keys)
if instructions_space.keys != None:  # we had a response
    thisExp.addData('instructions_space.rt', instructions_space.rt)
    thisExp.addData('instructions_space.duration', instructions_space.duration)
thisExp.nextEntry()
# the Routine "Instructions_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "EOG_Screen" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
EOG_ScreenComponents = [EOG_text, stim_square_EOG]
for thisComponent in EOG_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "EOG_Screen" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 16.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *EOG_text* updates
    
    # if EOG_text is starting this frame...
    if EOG_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EOG_text.frameNStart = frameN  # exact frame index
        EOG_text.tStart = t  # local t and not account for scr refresh
        EOG_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EOG_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'EOG_text.started')
        # update status
        EOG_text.status = STARTED
        EOG_text.setAutoDraw(True)
    
    # if EOG_text is active this frame...
    if EOG_text.status == STARTED:
        # update params
        pass
    
    # if EOG_text is stopping this frame...
    if EOG_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > EOG_text.tStartRefresh + 16-frameTolerance:
            # keep track of stop time/frame for later
            EOG_text.tStop = t  # not accounting for scr refresh
            EOG_text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'EOG_text.stopped')
            # update status
            EOG_text.status = FINISHED
            EOG_text.setAutoDraw(False)
    
    # *stim_square_EOG* updates
    
    # if stim_square_EOG is starting this frame...
    if stim_square_EOG.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        stim_square_EOG.frameNStart = frameN  # exact frame index
        stim_square_EOG.tStart = t  # local t and not account for scr refresh
        stim_square_EOG.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(stim_square_EOG, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'stim_square_EOG.started')
        # update status
        stim_square_EOG.status = STARTED
        stim_square_EOG.setAutoDraw(True)
    
    # if stim_square_EOG is active this frame...
    if stim_square_EOG.status == STARTED:
        # update params
        pass
    
    # if stim_square_EOG is stopping this frame...
    if stim_square_EOG.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > stim_square_EOG.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            stim_square_EOG.tStop = t  # not accounting for scr refresh
            stim_square_EOG.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'stim_square_EOG.stopped')
            # update status
            stim_square_EOG.status = FINISHED
            stim_square_EOG.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EOG_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "EOG_Screen" ---
for thisComponent in EOG_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-16.000000)

# --- Prepare to start Routine "EMG_Screen" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
EMG_ScreenComponents = [EMG_text, stim_square_EMG]
for thisComponent in EMG_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "EMG_Screen" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 16.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *EMG_text* updates
    
    # if EMG_text is starting this frame...
    if EMG_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        EMG_text.frameNStart = frameN  # exact frame index
        EMG_text.tStart = t  # local t and not account for scr refresh
        EMG_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EMG_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'EMG_text.started')
        # update status
        EMG_text.status = STARTED
        EMG_text.setAutoDraw(True)
    
    # if EMG_text is active this frame...
    if EMG_text.status == STARTED:
        # update params
        pass
    
    # if EMG_text is stopping this frame...
    if EMG_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > EMG_text.tStartRefresh + 16-frameTolerance:
            # keep track of stop time/frame for later
            EMG_text.tStop = t  # not accounting for scr refresh
            EMG_text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'EMG_text.stopped')
            # update status
            EMG_text.status = FINISHED
            EMG_text.setAutoDraw(False)
    
    # *stim_square_EMG* updates
    
    # if stim_square_EMG is starting this frame...
    if stim_square_EMG.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        stim_square_EMG.frameNStart = frameN  # exact frame index
        stim_square_EMG.tStart = t  # local t and not account for scr refresh
        stim_square_EMG.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(stim_square_EMG, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'stim_square_EMG.started')
        # update status
        stim_square_EMG.status = STARTED
        stim_square_EMG.setAutoDraw(True)
    
    # if stim_square_EMG is active this frame...
    if stim_square_EMG.status == STARTED:
        # update params
        pass
    
    # if stim_square_EMG is stopping this frame...
    if stim_square_EMG.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > stim_square_EMG.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            stim_square_EMG.tStop = t  # not accounting for scr refresh
            stim_square_EMG.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'stim_square_EMG.stopped')
            # update status
            stim_square_EMG.status = FINISHED
            stim_square_EMG.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EMG_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "EMG_Screen" ---
for thisComponent in EMG_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-16.000000)

# --- Prepare to start Routine "Coding_Trials" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Coding_TrialsComponents = []
for thisComponent in Coding_TrialsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Coding_Trials" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Coding_TrialsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Coding_Trials" ---
for thisComponent in Coding_TrialsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Coding_Trials" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trial_block = data.TrialHandler(nReps=12.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trial_block')
thisExp.addLoop(trial_block)  # add the loop to the experiment
thisTrial_block = trial_block.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_block.rgb)
if thisTrial_block != None:
    for paramName in thisTrial_block:
        exec('{} = thisTrial_block[paramName]'.format(paramName))

for thisTrial_block in trial_block:
    currentLoop = trial_block
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_block.rgb)
    if thisTrial_block != None:
        for paramName in thisTrial_block:
            exec('{} = thisTrial_block[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "fixation_cross" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    fixation_crossComponents = [fix_cross]
    for thisComponent in fixation_crossComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "fixation_cross" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix_cross* updates
        
        # if fix_cross is starting this frame...
        if fix_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_cross.frameNStart = frameN  # exact frame index
            fix_cross.tStart = t  # local t and not account for scr refresh
            fix_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_cross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fix_cross.started')
            # update status
            fix_cross.status = STARTED
            fix_cross.setAutoDraw(True)
        
        # if fix_cross is active this frame...
        if fix_cross.status == STARTED:
            # update params
            pass
        
        # if fix_cross is stopping this frame...
        if fix_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_cross.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                fix_cross.tStop = t  # not accounting for scr refresh
                fix_cross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fix_cross.stopped')
                # update status
                fix_cross.status = FINISHED
                fix_cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixation_crossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "fixation_cross" ---
    for thisComponent in fixation_crossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('C:/Users/migue/OneDrive/Ambiente de Trabalho/Tese/AcquisitionProtocols/FEUP_droneImages.xlsx'),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "trial" ---
        continueRoutine = True
        # update component parameters for each repeat
        trialImage.setImage(Image)
        # keep track of which components have finished
        trialComponents = [trialImage, stim_square]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.2:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *trialImage* updates
            
            # if trialImage is starting this frame...
            if trialImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialImage.frameNStart = frameN  # exact frame index
                trialImage.tStart = t  # local t and not account for scr refresh
                trialImage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialImage, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trialImage.started')
                # update status
                trialImage.status = STARTED
                trialImage.setAutoDraw(True)
            
            # if trialImage is active this frame...
            if trialImage.status == STARTED:
                # update params
                pass
            
            # if trialImage is stopping this frame...
            if trialImage.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > trialImage.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    trialImage.tStop = t  # not accounting for scr refresh
                    trialImage.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'trialImage.stopped')
                    # update status
                    trialImage.status = FINISHED
                    trialImage.setAutoDraw(False)
            
            # *stim_square* updates
            
            # if stim_square is starting this frame...
            if stim_square.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stim_square.frameNStart = frameN  # exact frame index
                stim_square.tStart = t  # local t and not account for scr refresh
                stim_square.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim_square, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stim_square.started')
                # update status
                stim_square.status = STARTED
                stim_square.setAutoDraw(True)
            
            # if stim_square is active this frame...
            if stim_square.status == STARTED:
                # update params
                pass
            
            # if stim_square is stopping this frame...
            if stim_square.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stim_square.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    stim_square.tStop = t  # not accounting for scr refresh
                    stim_square.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'stim_square.stopped')
                    # update status
                    stim_square.status = FINISHED
                    stim_square.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial" ---
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.200000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials'
    
    
    # --- Prepare to start Routine "trial_BlockScreen" ---
    continueRoutine = True
    # update component parameters for each repeat
    trial_Blocktext.setText('When you are ready to start a trial number, press the SPACEBAR!')
    trial_space.keys = []
    trial_space.rt = []
    _trial_space_allKeys = []
    # keep track of which components have finished
    trial_BlockScreenComponents = [trial_Blocktext, trial_space]
    for thisComponent in trial_BlockScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial_BlockScreen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trial_Blocktext* updates
        
        # if trial_Blocktext is starting this frame...
        if trial_Blocktext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_Blocktext.frameNStart = frameN  # exact frame index
            trial_Blocktext.tStart = t  # local t and not account for scr refresh
            trial_Blocktext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_Blocktext, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_Blocktext.started')
            # update status
            trial_Blocktext.status = STARTED
            trial_Blocktext.setAutoDraw(True)
        
        # if trial_Blocktext is active this frame...
        if trial_Blocktext.status == STARTED:
            # update params
            pass
        
        # *trial_space* updates
        waitOnFlip = False
        
        # if trial_space is starting this frame...
        if trial_space.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_space.frameNStart = frameN  # exact frame index
            trial_space.tStart = t  # local t and not account for scr refresh
            trial_space.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_space, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_space.started')
            # update status
            trial_space.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(trial_space.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(trial_space.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if trial_space.status == STARTED and not waitOnFlip:
            theseKeys = trial_space.getKeys(keyList=['space'], waitRelease=False)
            _trial_space_allKeys.extend(theseKeys)
            if len(_trial_space_allKeys):
                trial_space.keys = _trial_space_allKeys[-1].name  # just the last key pressed
                trial_space.rt = _trial_space_allKeys[-1].rt
                trial_space.duration = _trial_space_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_BlockScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial_BlockScreen" ---
    for thisComponent in trial_BlockScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if trial_space.keys in ['', [], None]:  # No response was made
        trial_space.keys = None
    trial_block.addData('trial_space.keys',trial_space.keys)
    if trial_space.keys != None:  # we had a response
        trial_block.addData('trial_space.rt', trial_space.rt)
        trial_block.addData('trial_space.duration', trial_space.duration)
    # the Routine "trial_BlockScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 12.0 repeats of 'trial_block'


# --- Prepare to start Routine "GoodBye_Screen" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
GoodBye_ScreenComponents = [goddbye_text]
for thisComponent in GoodBye_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "GoodBye_Screen" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 4.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *goddbye_text* updates
    
    # if goddbye_text is starting this frame...
    if goddbye_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        goddbye_text.frameNStart = frameN  # exact frame index
        goddbye_text.tStart = t  # local t and not account for scr refresh
        goddbye_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(goddbye_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'goddbye_text.started')
        # update status
        goddbye_text.status = STARTED
        goddbye_text.setAutoDraw(True)
    
    # if goddbye_text is active this frame...
    if goddbye_text.status == STARTED:
        # update params
        pass
    
    # if goddbye_text is stopping this frame...
    if goddbye_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > goddbye_text.tStartRefresh + 4-frameTolerance:
            # keep track of stop time/frame for later
            goddbye_text.tStop = t  # not accounting for scr refresh
            goddbye_text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'goddbye_text.stopped')
            # update status
            goddbye_text.status = FINISHED
            goddbye_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GoodBye_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "GoodBye_Screen" ---
for thisComponent in GoodBye_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-4.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
