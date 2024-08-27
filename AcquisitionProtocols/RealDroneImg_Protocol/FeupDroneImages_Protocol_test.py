#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.3),
    on fevereiro 15, 2024, at 23:17
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import gui, visual, core, data, logging
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

''' Important protocol variables '''

N_TrialBlocks = 8.0
ITI = 0.2 # Inter-Trial Interval (s)

### Changes made to the original PsychoPy code

''' 
The objects that handle the saved data with digital timestamps and the order of the stimuli were removed to 
improve efficiency. In addition to not providing useful information, the algorithm that handles target separation
requirements happens after the list of the ordered stimuli is already formed, which by default PsychoPy 
automatically saves on an Excel sheet. Meaning there is a mismatch between the list and the actual order of the 
stimuli that appear onscreen. Instead, each new stimuli order defined right before a trial block will be saved 
in an Excel file at the end of each trial block to track the instance each defined target centroid appeared during
the experiment. 
'''

'''
win size is set to (800,600) but because fullscreen is enabled, it overwrites the size information
and creates the screen with its original size (e.g., 1920 x 1080). This helps us to regularize and 
set the right position of the square stim (for the LDR) for every screen resolution. This is set by
the simple equation on the square_stim.pos that correlates the horizontal position for 1080p with the
offset -0.9 for the stim in PsychoPy.
'''

'''
An algorithm that handles the target separation was made impossibilitating that a target stimuli appears 
in the first second of a trial block and that two targets appear with less than 600 ms from each 
other. It also random shuffles the order with each new trial block.
'''

# ------------------------------------------- .xlsx file path -------------------------------------------

file_path = 'C:/Users/migue/OneDrive/Ambiente de Trabalho/Tese/rsvp-target-localization-bci/AcquisitionProtocols/FEUP_droneImages.xlsx'
stim_order_files_path = "C:/Users/migue/OneDrive/Ambiente de Trabalho/Tese/rsvp-target-localization-bci/AcquisitionProtocols/RealDroneImg_Protocol/Stim_Order_Files_Test"

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

# An ExperimentHandler isn't essential but helps with data saving
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[800, 600], fullscr=False, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='Monitor', color=[-1,-1,-1], colorSpace='rgb',
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
    text='Aerial Images captured by a Drone at FEUP will be shown in rapid succession. \nPay attention to the images with minimal ocular and head movements if possible.\n\nMentally count each instance of an image where a human is lying down (red seater), which can show up in every possible position of the image. Mantain the gaze at the center of the fixation during the whole trial block, that will appear right before each image burst.\n\nYou will be asked to execute ocular and jaw movements first, right after this message. Press the SPACEBAR key when you are ready to start the Experiment.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instructions_space = keyboard.Keyboard()

# --- Initialize components for Routine "Coding_Trials" ---
# Run 'Begin Experiment' code from code
imgs_file = pd.read_excel(file_path)

permutation = np.random.permutation(imgs_file.index)
shuffled_df = imgs_file.loc[permutation]

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
    ori=0.0, pos=((win.size[1]*(-0.9))/1080+0.025, 0.46), anchor='top-left',
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
    instructions_space.keys = Non10
# the Routine "Instructions_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
trial_block = data.TrialHandler(nReps=N_TrialBlocks, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trial_block')
thisTrial_block = trial_block.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_block.rgb)
if thisTrial_block != None:
    for paramName in thisTrial_block:
        exec('{} = thisTrial_block[paramName]'.format(paramName))

trial_block_count = 0
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
        trialList=data.importConditions(file_path),
        seed=None, name='trials')
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    '''================================== Custom code =================================='''
    '''================================================================================='''
    '''================================================================================='''

    # Perform random shuffles on the data
    permutation = np.random.permutation(imgs_file.index)
    shuffled_df = imgs_file.loc[permutation]

    '''
    This portion of code evaluates if there is space at the end of the stimuli array
    to fit all the target stimuli with the specified TARGET_SEPERATION distance
    In case there is not enough space, the target stimuli at the end of the array
    will be moved directly to the begining of the array where the second part
    of the algorithm will distribute them according to the valid distance between
    target stimuli.
    '''

    FIRST_N_NONTARGET_TRIALS = 5 # 1s
    TARGET_SEPERATION = 3 # 1s target separation

    invalid = True

    df_size = len(shuffled_df) - 1
    shuffled_df = shuffled_df.to_numpy()

    # Loop will run until invalid target positions are removed
    while invalid:
        invalid = False
        target_count = 0
        for it, (_, label, _) in enumerate(shuffled_df[::-1, :]):
            if label == "Target":
                target_count += 1
                if (it + 1 - target_count) / TARGET_SEPERATION < 2.0:
                    # Second target element (the invalid one) on the reversed array
                    row_to_move = shuffled_df[df_size - it].copy()

                    # Remove the row from its current position
                    shuffled_df = np.delete(shuffled_df, df_size - it, axis=0)

                    # Insert the row at the beginning
                    shuffled_df = np.vstack([row_to_move, shuffled_df])

                    invalid = True
                    break
        print("Looping...")

    '''
    This second part is where the consecutive target stimuli will be redistributed according
    to the valid target seperation distance. Furthermore, no target stimuli must be presented
    in the first second of the trial
    '''

    non_target_count = 0
    allocated_count = 0

    allocated = []
    reorganized_df = []

    for it, (image, condition, centroid) in enumerate(shuffled_df):
        if (it <= FIRST_N_NONTARGET_TRIALS and condition == "NonTarget"): 
            reorganized_df.append([image, condition, centroid])
            non_target_count += 1

        elif (it <= FIRST_N_NONTARGET_TRIALS and condition == "Target"):
            allocated.append([image, condition, centroid])
            allocated_count += 1

        elif(it >= FIRST_N_NONTARGET_TRIALS):
            
            if (condition == "Target" and non_target_count >= TARGET_SEPERATION):
                reorganized_df.append([image, condition, centroid])
                non_target_count = 0

            elif(condition == "Target" and non_target_count < TARGET_SEPERATION):
                
                allocated.append([image, condition, centroid])
                allocated_count += 1

            elif(condition == "NonTarget" and non_target_count >= TARGET_SEPERATION):
                if(allocated_count > 0):  
                    reorganized_df.append(allocated[0])
                    allocated_count -= 1
                    allocated.pop(0) # To avoid duplicates
                    
                    non_target_count = 0
                    reorganized_df.append([image, condition, centroid])
                    non_target_count += 1

                else:
                    reorganized_df.append([image, condition, centroid])
                    non_target_count += 1

            elif(condition == "NonTarget" and non_target_count < TARGET_SEPERATION):
                reorganized_df.append([image, condition, centroid])
                non_target_count += 1
    
    imgs    = [row[0] for row in reorganized_df]
    stims   = [row[1] for row in reorganized_df]
    cent    = [row[2] for row in reorganized_df]
  
    tc = 0
    for tr in reorganized_df:
        #print(tr[0])
        if(tr[1] == "Target"):
            tc += 1

    print("\n======== After looping =======")
    print("\nSize: ", len(reorganized_df))
    print("Nº targets: ", tc)
    print("Unique: ", len(np.unique(reorganized_df)))

    trial_count = 0
    non_target_count = len(reorganized_df) - tc

    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
 
        # --- Prepare to start Routine "trial" ---
        continueRoutine = True
        # update component parameters for each repeat
        trialImage.setImage(imgs[trial_count ])
        print("Image: ",imgs[trial_count ], " || Condition: ", stims[trial_count], " || Count: ", trial_count )
        if stims[trial_count] == 'Target': # Changes color of the stimulus depending on its class: target/non-target
            stim_square.lineColor = [1,1,1]
            stim_square.fillColor = [1,1,1]
        elif stims[trial_count] == 'NonTarget': 
            non_target_count -= 1
            # Because there are no blank spaces between the images, a diferentiation between two consecutive non-targets is necessary
            if(non_target_count % 2 == 0 or non_target_count == 0):
                stim_square.fillColor = [-0.25, -0.25, -0.25]
                stim_square.lineColor = [0, 0, 0]
            else:
                stim_square.fillColor = [-0.75, -0.75, -0.75]
                stim_square.lineColor = [-0.75, -0.75, -0.75]

        if(trial_count == len(reorganized_df) - 1): 
            # Protection against crashes (Sometimes a trial gets "eaten" with this correction algor. Its rare though )
            # Breaking the loop here does not seem to break P sychoPy
            break

        trial_count +=1
           
        '''================================================================================='''
        '''================================================================================='''
        '''================================================================================='''

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
        while continueRoutine and routineTimer.getTime() < ITI:
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
                if tThisFlipGlobal > trialImage.tStartRefresh + ITI-frameTolerance:
                    # keep track of stop time/frame for later
                    trialImage.tStop = t  # not accounting for scr refresh
                    trialImage.frameNStop = frameN  # exact frame index
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
                if tThisFlipGlobal > stim_square.tStartRefresh + ITI-frameTolerance:
                    # keep track of stop time/frame for later
                    stim_square.tStop = t  # not accounting for scr refresh
                    stim_square.frameNStop = frameN  # exact frame index
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
            routineTimer.addTime(-ITI)
        
    # completed 1.0 repeats of 'trials'
    
    
    # --- Prepare to start Routine "trial_BlockScreen" ---

    continueRoutine = True
    # update component parameters for each repeat
    trial_Blocktext.setText(f"When you are ready to start the next trial block, press the SPACEBAR!")
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

    if not os.path.exists(stim_order_files_path): # Check if the directory already exists
        os.makedirs(stim_order_files_path, exist_ok=True)

    participant_folder = stim_order_files_path + f"/EEG_{expInfo['participant']}_{ioSession}"
    if not os.path.exists(participant_folder):
        os.makedirs(participant_folder)
    
    trial_block_count+=1

    df = pd.DataFrame({"Image" : imgs, "Condition" : stims, "Centroid" : cent})
    df.to_excel(participant_folder + f"/trial{trial_block_count}.xlsx")

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

logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
win.close()
core.quit()
