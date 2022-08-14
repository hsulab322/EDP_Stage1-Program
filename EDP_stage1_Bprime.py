#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.2),
    on 十二月 06, 2020, at 00:55
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
from psychopy.platform_specific.win32 import THREAD_PRIORITY_NORMAL

from driveapi import driveapi

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding


from psychopy.hardware import keyboard
import random


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment sessions
psychopyVersion = '2020.1.2'
expName = 'EDP_stage1'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
print(filename)

####################

## determine if application is a script file or frozen exe
# if getattr(sys, 'frozen', False):
#     application_path = os.path.dirname(sys.executable)
# elif __file__:
#     application_path = os.path.dirname(__file__)

# print('\n',application_path,'\n')
# filename = application_path + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
# print(filename)

#####################

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\user\\Desktop\\EDP_stage1\\EDP_stage1_new.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 720], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='lightgray', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='pix')
# 
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

G = 2000
l = -300
g = 300

text_L_list = [-2000,None,None,None,None,None,None,None,None]
text_x1pos_list = [1000,None,None,None,None,None,None,None,None]
text_x1neg_list = [None,None,None,None,None,None,None,None,None]
text_L2_list = [None,None,None,None,None,None,None,None,None]
text_x2pos_list = [None,None,None,None,None,None,None,None,None]
text_x3pos_list = [None,None,None,None,None,None,None,None,None]
text_x4pos_list = [None,None,None,None,None,None,None,None,None]
text_x5pos_list = [None,None,None,None,None,None,None,None,None]
text_x6pos_list = [None,None,None,None,None,None,None,None,None]
text_x7pos_list = [None,None,None,None,None,None,None,None,None]
text_x8pos_list = [None,None,None,None,None,None,None,None,None]
text_G2_list = [None,None,None,None,None,None,None,None,None]
text_x2neg_list = [None,None,None,None,None,None,None,None,None]
text_x3neg_list = [None,None,None,None,None,None,None,None,None]
text_x4neg_list = [None,None,None,None,None,None,None,None,None]
text_x5neg_list = [None,None,None,None,None,None,None,None,None]
text_x6neg_list = [None,None,None,None,None,None,None,None,None]
text_x7neg_list = [None,None,None,None,None,None,None,None,None]
text_x8neg_list = [None,None,None,None,None,None,None,None,None]
L = text_L_list[-1]
x1pos = text_x1pos_list[-1]
x1neg = text_x1neg_list[-1]
L2 = text_L2_list[-1]
x2pos = text_x2pos_list[-1]
x3pos = text_x3pos_list[-1]
x4pos = text_x4pos_list[-1]
x5pos = text_x5pos_list[-1]
x6pos = text_x6pos_list[-1]
x7pos = text_x7pos_list[-1]
x8pos = text_x8pos_list[-1]
G2 = text_G2_list[-1]
x2neg = text_x2neg_list[-1]
x3neg = text_x3neg_list[-1]
x4neg = text_x4neg_list[-1]
x5neg = text_x5neg_list[-1]
x6neg = text_x6neg_list[-1]
x7neg = text_x7neg_list[-1]
x8neg = text_x8neg_list[-1]
all_point_data_list=[text_L_list,text_x1pos_list,text_x1neg_list,text_L2_list,text_G2_list,text_x2pos_list,text_x3pos_list,text_x4pos_list,text_x5pos_list,text_x6pos_list,text_x7pos_list,text_x8pos_list,text_x2neg_list,text_x3neg_list,text_x4neg_list,text_x5neg_list,text_x6neg_list,text_x7neg_list,text_x8neg_list]
trial_order = ['L','x1pos','x1neg','L2','G2','x2pos','x3pos','x4pos','x5pos','x6pos','x7pos','x8pos','x2neg','x3neg','x4neg','x5neg','x6neg','x7neg','x8neg']


#x2+: 5 x3+: 6 ... x8+: 11
#x2-: 12 x3+: 13 ... x8+: 18

trial_order_all = [0,1,2,3,4,5,12,6,13,7,14,8,15,9,16,10,17,11,18]




# Initialize components for Routine "phase"##################################### phase開始畫面
phaseClock = core.Clock() # phaseClock紀錄時間
interface_phase = visual.ImageStim(
    win=win,
    name='interface_phase', 
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(1280,720),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
buttonOK_phase = visual.ImageStim(
    win=win,
    name='buttonOK_phase', 
    image='./interface/buttonOK.png', mask=None,
    ori=0, pos=(0, -300), size=(150,76),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

mouse_phase = event.Mouse(win=win)
x, y = [None, None]
mouse_phase.mouseClock = core.Clock()


interface_phase_list=['./interface/phase1.png', './interface/phase2.png', './interface/phase3.png']
interface_list = ['./interface/L.png', './interface/x1pos.png','./interface/x1neg.png', './interface/L2.png', './interface/xipos.png', './interface/G2.png', './interface/xineg.png']

# Initialize components for Routine "Choice"######################################## Choice
ChoiceClock = core.Clock() # 紀錄選擇的時間
interface_Choice = visual.ImageStim(
    win=win,
    name='interface_Choice', 
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(1280,720),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
instruction_Choice = visual.ImageStim(
    win=win,
    name='instruction_Choice', 
    image='./interface/Choice_instruction.png', mask=None,
    ori=0, pos=(0,300), size=(753,75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

mouse_Choice = event.Mouse(win=win)
x, y = [None, None]
mouse_Choice.mouseClock = core.Clock()
mouse_Choice_Confirm = event.Mouse(win=win)
x, y = [None, None]
mouse_Choice_Confirm.mouseClock = core.Clock()

buttonA = visual.ImageStim(
    win=win,
    name='buttonA', 
    image='./interface/buttonA.png', mask=None,
    ori=0, pos=(-282.4,-189.5), size=(128,72),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

buttonB = visual.ImageStim(
    win=win,
    name='buttonB', 
    image='./interface/buttonB.png', mask=None,
    ori=0, pos=(263.5,-189.5), size=(128,72),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

text_Aup_Choice = visual.TextStim(win=win, name='text_Aup_Choice',
    text=None,
    font='Arial',
    pos=(-150.6,75.8), height=35, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

text_Adown_Choice = visual.TextStim(win=win, name='text_Adown_Choice',
    text=None,
    font='Arial',
    pos=(-150.6,-69.8), height=35, wrapWidth=None, ori=0,   ## 原本 pos(-150.6,-75.8)
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

text_Bmiddle_Choice = visual.TextStim(win=win, name='text_Bmiddle_Choice',
    text=None,
    font='Arial',
    pos=(376.5,3), height=35, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

text_Bup_Choice = visual.TextStim(win=win, name='text_Bup_Choice',
    text=None,
    font='Arial',
    pos=(395,75.8), height=35, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);

text_Bdown_Choice = visual.TextStim(win=win, name='text_Bdown_Choice',
    text=None,
    font='Arial',
    pos=(395,-72.8), height=35, wrapWidth=None, ori=0, ####(395,-75.8)
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);

buttonOK_Choice = visual.ImageStim(
    win=win,
    name='buttonOK_Choice', 
    image=None, mask=None,
    ori=0, pos=(0, -350), size=(120,62),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)


# Initialize components for Routine "interval"
intervalClock = core.Clock()
cross = visual.ShapeStim(
    win=win, name='cross', vertices='cross',
    size=(30,30),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

nextTrial = visual.ImageStim(
    win=win,
    name='nextTrial', 
    image='./interface/nextTrial.png', mask=None,
    ori=0, pos=(0, 0), size=(1548,124),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)


# Initialize components for Routine "endExp"
endExpClock = core.Clock()
text_endExp = visual.TextStim(win=win, name='endExp',
    text='實驗結束',
    font='Arial',
    pos=(0, 0), height=40, wrapWidth=1280, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-0.0);
buttonOK_endExp = visual.ImageStim(
    win=win,
    name='buttonOK_endExp', 
    image='./interface/buttonOK.png', mask=None,
    ori=0, pos=(0, -300), size=(150,76),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

mouse_endExp = event.Mouse(win=win)
x, y = [None, None]
mouse_endExp.mouseClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

thisExp.addData("Subject",expInfo['participant'])
 


###################################################################################################################
for i in trial_order_all: # trial 順序
    text_Aup_Choice.text = ''
    text_Adown_Choice.text = ''
    text_Bmiddle_Choice.text = ''
    text_Bup_Choice.text = ''
    text_Bdown_Choice.text = ''

#phase1
    if i == 0:
        # L
        interface_phase.image = interface_phase_list[0]
        interface_Choice.image = interface_list[0]
        text_Adown_Choice.color = 'red'
        # ------Prepare to start Routine "phase"-------
        continueRoutine = True
        # update component parameters for each repeat
        # setup some python lists for storing info about the mouse_phase
        mouse_phase.clicked_name = []


        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        phaseComponents = [interface_phase, buttonOK_phase, mouse_phase] #button_resp
        for thisComponent in phaseComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        phaseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

        # -------Run Routine "phase"-------
        while continueRoutine:
            # get current time
            t = phaseClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=phaseClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *interface_phase* updates
            if interface_phase.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                interface_phase.frameNStart = frameN  # exact frame index
                interface_phase.tStart = t  # local t and not account for scr refresh
                interface_phase.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(interface_phase, 'tStartRefresh')  # time at next scr refresh
                interface_phase.setAutoDraw(True)
            
            # *buttonOK_phase* updates
            if buttonOK_phase.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                buttonOK_phase.frameNStart = frameN  # exact frame index
                buttonOK_phase.tStart = t  # local t and not account for scr refresh
                buttonOK_phase.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(buttonOK_phase, 'tStartRefresh')  # time at next scr refresh
                buttonOK_phase.setAutoDraw(True)

            # *mouse_phase* updates
            if mouse_phase.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_phase.frameNStart = frameN  # exact frame index
                mouse_phase.tStart = t  # local t and not account for scr refresh
                mouse_phase.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_phase, 'tStartRefresh')  # time at next scr refresh
                mouse_phase.status = STARTED
                mouse_phase.mouseClock.reset()
                prevButtonState = mouse_phase.getPressed()  # if button is down already this ISN'T a new click
            if mouse_phase.status == STARTED:  # only update if started and not finished!
                buttons = mouse_phase.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [buttonOK_phase]:
                            if obj.contains(mouse_phase):
                                gotValidClick = True
                                mouse_phase.clicked_name.append(obj.name)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False    
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in phaseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
            

        # -------Ending Routine "phase"-------
        for thisComponent in phaseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
                thisComponent.tStopRefresh = tThisFlipGlobal
        #thisExp.addData('interface_phase1.start', interface_phase.tStartRefresh)
        #thisExp.addData('interface_phase1.end', interface_phase.tStopRefresh)
        # store data for thisExp (ExperimentHandler)
        #thisExp.nextEntry()


        # the Routine "phase" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # ------Prepare to start Routine "interval"-------
        continueRoutine = True
        routineTimer.add(0.1000000) # 2s
        # update component parameters for each repeat
        # keep track of which components have finished
        intervalComponents = [cross]
        for thisComponent in intervalComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        intervalClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

        # -------Run Routine "interval"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = intervalClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=intervalClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cross* updates
            if cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cross.frameNStart = frameN  # exact frame index
                cross.tStart = t  # local t and not account for scr refresh
                cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
                cross.setAutoDraw(True)
            if cross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cross.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    cross.tStop = t  # not accounting for scr refresh
                    cross.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(cross, 'tStopRefresh')  # time at next scr refresh
                    cross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in intervalComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "interval"-------
        for thisComponent in intervalComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
    elif i == 1:
        # x1pos
        interface_Choice.image = interface_list[1]
        text_Bmiddle_Choice.color = 'blue'
    elif i == 2:
        # x1neg
        interface_Choice.image = interface_list[2]
        text_Bmiddle_Choice.color = 'red'
    elif i == 3:
        # L2
        interface_Choice.image = interface_list[3]
        text_Bup_Choice.color = 'blue'
        text_Bdown_Choice.color = 'red'
    elif i == 4:
        # G2
        interface_Choice.image = interface_list[5]    



#phase2
    if i == 5:
        # xipos
        interface_Choice.image = interface_list[4]
        text_Aup_Choice.color = 'blue'        
        interface_phase.image = interface_phase_list[1]

        # ------Prepare to start Routine "phase"-------
        continueRoutine = True
        # update component parameters for each repeat
        # setup some python lists for storing info about the mouse_phase
        mouse_phase.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        phaseComponents = [interface_phase, buttonOK_phase, mouse_phase]
        for thisComponent in phaseComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        phaseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

        # -------Run Routine "phase"-------
        while continueRoutine:
            # get current time
            t = phaseClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=phaseClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *interface_phase* updates
            if interface_phase.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                interface_phase.frameNStart = frameN  # exact frame index
                interface_phase.tStart = t  # local t and not account for scr refresh
                interface_phase.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(interface_phase, 'tStartRefresh')  # time at next scr refresh
                interface_phase.setAutoDraw(True)
            
            # *buttonOK_phase* updates
            if buttonOK_phase.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                buttonOK_phase.frameNStart = frameN  # exact frame index
                buttonOK_phase.tStart = t  # local t and not account for scr refresh
                buttonOK_phase.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(buttonOK_phase, 'tStartRefresh')  # time at next scr refresh
                buttonOK_phase.setAutoDraw(True)


            # *mouse_phase* updates
            if mouse_phase.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_phase.frameNStart = frameN  # exact frame index
                mouse_phase.tStart = t  # local t and not account for scr refresh
                mouse_phase.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_phase, 'tStartRefresh')  # time at next scr refresh
                mouse_phase.status = STARTED
                mouse_phase.mouseClock.reset()
                prevButtonState = mouse_phase.getPressed()  # if button is down already this ISN'T a new click
            if mouse_phase.status == STARTED:  # only update if started and not finished!
                buttons = mouse_phase.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [buttonOK_phase]:
                            if obj.contains(mouse_phase):
                                gotValidClick = True
                                mouse_phase.clicked_name.append(obj.name)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False

            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in phaseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "phase"-------
        for thisComponent in phaseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
                thisComponent.tStopRefresh = tThisFlipGlobal
        #thisExp.addData('interface_phase3.started', interface_phase.tStartRefresh)
        #thisExp.addData('interface_phase3.stopped', interface_phase.tStopRefresh)
        # store data for thisExp (ExperimentHandler)
        #thisExp.nextEntry()

        # the Routine "phase" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # ------Prepare to start Routine "interval"-------
        continueRoutine = True
        routineTimer.add(0.100000) # 2s
        # update component parameters for each repeat
        # keep track of which components have finished
        intervalComponents = [cross]
        for thisComponent in intervalComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        intervalClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

        # -------Run Routine "interval"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = intervalClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=intervalClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cross* updates
            if cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cross.frameNStart = frameN  # exact frame index
                cross.tStart = t  # local t and not account for scr refresh
                cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
                cross.setAutoDraw(True)
            if cross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cross.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    cross.tStop = t  # not accounting for scr refresh
                    cross.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(cross, 'tStopRefresh')  # time at next scr refresh
                    cross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in intervalComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "interval"-------
        for thisComponent in intervalComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
    
    elif i > 5 and i < 12:
        interface_Choice.image = interface_list[4]
        text_Aup_Choice.color = 'blue'
    elif i >= 12:
        # xineg
        interface_Choice.image = interface_list[6]

######################################(Phase和各data point的圖完成) ###################################################################


    target = all_point_data_list[i][0]
    step = target
    thisTrialChoice = []
    for n in range(0,2):   ## 5 tasks次數
        currentChoice =''
        buttonA.image='./interface/buttonA.png'
        buttonB.image='./interface/buttonB.png'
        buttonOK_Choice.image=None
        choosePressed = False
        # ------Prepare to start Routine "Choice"-------
        continueRoutine = True
        # update component parameters for each repeat
        # setup some python lists for storing info about the mouse_Choice
        mouse_Choice.clicked_name = []
        mouse_Choice_Confirm.clicked_name = []
        gotValidClick = False  # until a click is received
        
        if i == 0:
            text_Adown_Choice.text = text_L_list[n]
        elif i == 1:
            text_Bmiddle_Choice.text = text_x1pos_list[n]
        elif i == 2:
            text_Adown_Choice.text = L
            text_Bmiddle_Choice.text = text_x1neg_list[n]
        elif i == 3:
            text_Bup_Choice.text = x1pos
            text_Bdown_Choice.text = text_L2_list[n]
        elif i == 4:
            text_Bup_Choice.text = text_G2_list[n]
            text_Bdown_Choice.text = x1neg

        elif i == 5:
            text_Aup_Choice.text = x1pos
            text_Bup_Choice.text = text_x2pos_list[n]
            text_Bdown_Choice.text = L2
        elif i == 6:
            text_Aup_Choice.text = x2pos
            text_Bup_Choice.text = text_x3pos_list[n]
            text_Bdown_Choice.text = L2
        elif i == 7:
            text_Aup_Choice.text = x3pos
            text_Bup_Choice.text = text_x4pos_list[n]
            text_Bdown_Choice.text = L2
        elif i == 8:
            text_Aup_Choice.text = x4pos
            text_Bup_Choice.text = text_x5pos_list[n]
            text_Bdown_Choice.text = L2
        elif i == 9:
            text_Aup_Choice.text = x5pos
            text_Bup_Choice.text = text_x6pos_list[n]
            text_Bdown_Choice.text = L2
        elif i == 10:
            text_Aup_Choice.text = x6pos
            text_Bup_Choice.text = text_x7pos_list[n]
            text_Bdown_Choice.text = L2
        elif i == 11:
            text_Aup_Choice.text = x7pos
            text_Bup_Choice.text = text_x8pos_list[n]
            text_Bdown_Choice.text = L2
        elif i == 12:
            text_Adown_Choice.text = x1neg
            text_Bup_Choice.text = G2
            text_Bdown_Choice.text = text_x2neg_list[n]
        elif i == 13:
            text_Adown_Choice.text = x2neg
            text_Bup_Choice.text = G2
            text_Bdown_Choice.text = text_x3neg_list[n]
        elif i == 14:
            text_Adown_Choice.text = x3neg
            text_Bup_Choice.text = G2
            text_Bdown_Choice.text = text_x4neg_list[n]
        elif i == 15:
            text_Adown_Choice.text = x4neg
            text_Bup_Choice.text = G2
            text_Bdown_Choice.text = text_x5neg_list[n]
        elif i == 16:
            text_Adown_Choice.text = x5neg
            text_Bup_Choice.text = G2
            text_Bdown_Choice.text = text_x6neg_list[n]
        elif i == 17:
            text_Adown_Choice.text = x6neg
            text_Bup_Choice.text = G2
            text_Bdown_Choice.text = text_x7neg_list[n]
        elif i == 18:
            text_Adown_Choice.text = x7neg
            text_Bup_Choice.text = G2
            text_Bdown_Choice.text = text_x8neg_list[n]
        
        # keep track of which components have finished
        ChoiceComponents = [interface_Choice, instruction_Choice, mouse_Choice, mouse_Choice_Confirm, buttonA, buttonB, text_Aup_Choice, text_Adown_Choice, text_Bmiddle_Choice, text_Bup_Choice, text_Bdown_Choice, buttonOK_Choice]
        for thisComponent in ChoiceComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ChoiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

        # -------Run Routine "Choice"-------
        validChoice = False
        while continueRoutine:
            # get current time
            t = ChoiceClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ChoiceClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *interface_Choice* updates
            if interface_Choice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                interface_Choice.frameNStart = frameN  # exact frame index
                interface_Choice.tStart = t  # local t and not account for scr refresh
                interface_Choice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(interface_Choice, 'tStartRefresh')  # time at next scr refresh
                interface_Choice.setAutoDraw(True)
            # *instruction_Choice* updates
            if instruction_Choice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                instruction_Choice.frameNStart = frameN  # exact frame index
                instruction_Choice.tStart = t  # local t and not account for scr refresh
                instruction_Choice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(instruction_Choice, 'tStartRefresh')  # time at next scr refresh
                instruction_Choice.setAutoDraw(True)
            # *mouse_Choice* updates
            if mouse_Choice.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_Choice.frameNStart = frameN  # exact frame index
                mouse_Choice.tStart = t  # local t and not account for scr refresh
                mouse_Choice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_Choice, 'tStartRefresh')  # time at next scr refresh
                mouse_Choice.status = STARTED
                mouse_Choice.mouseClock.reset()
                prevButtonState = mouse_Choice.getPressed()  # if button is down already this ISN'T a new click
            if mouse_Choice.status == STARTED:  # only update if started and not finished!
                buttons = mouse_Choice.getPressed()
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [buttonA,buttonB]:
                        if obj.contains(mouse_Choice):
                            gotValidClick = True
                            mouse_Choice.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        if mouse_Choice.isPressedIn(buttonA): 
                            currentChoice = "A"
                            buttonB.image='./interface/buttonB.png'
                            buttonA.image='./interface/buttonA_selected.png'
                            buttonOK_Choice.image='./interface/buttonOK.png'
                            validChoice = True
                        elif mouse_Choice.isPressedIn(buttonB):
                            currentChoice = "B"
                            buttonB.image='./interface/buttonB_selected.png'
                            buttonA.image='./interface/buttonA.png'
                            buttonOK_Choice.image='./interface/buttonOK.png'
                            validChoice = True

                buttons = mouse_Choice.getPressed()
                if sum(buttons) > 0 and validChoice:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    for obj in [buttonOK_Choice]:
                        if obj.contains(mouse_Choice):
                            continueRoutine = False        


            # *buttonOK_phase* updates
            if buttonOK_Choice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                buttonOK_Choice.frameNStart = frameN  # exact frame index
                buttonOK_Choice.tStart = t  # local t and not account for scr refresh
                buttonOK_Choice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(buttonOK_phase, 'tStartRefresh')  # time at next scr refresh
                buttonOK_Choice.setAutoDraw(True)
                

            # *buttonA* updates
            if buttonA.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                buttonA.frameNStart = frameN  # exact frame index
                buttonA.tStart = t  # local t and not account for scr refresh
                buttonA.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(buttonA, 'tStartRefresh')  # time at next scr refresh
                buttonA.setAutoDraw(True)
            
            # *buttonB* updates
            if buttonB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                buttonB.frameNStart = frameN  # exact frame index
                buttonB.tStart = t  # local t and not account for scr refresh
                buttonB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(buttonB, 'tStartRefresh')  # time at next scr refresh
                buttonB.setAutoDraw(True)
            
            # *text_Aup_Choice* updates
            if text_Aup_Choice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_Aup_Choice.frameNStart = frameN  # exact frame index
                text_Aup_Choice.tStart = t  # local t and not account for scr refresh
                text_Aup_Choice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_Aup_Choice, 'tStartRefresh')  # time at next scr refresh
                text_Aup_Choice.setAutoDraw(True)
            
            # *text_Adown_Choice* updates
            if text_Adown_Choice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_Adown_Choice.frameNStart = frameN  # exact frame index
                text_Adown_Choice.tStart = t  # local t and not account for scr refresh
                text_Adown_Choice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_Adown_Choice, 'tStartRefresh')  # time at next scr refresh
                text_Adown_Choice.setAutoDraw(True)
            
            # *text_Bmiddle_Choice* updates
            if text_Bmiddle_Choice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_Bmiddle_Choice.frameNStart = frameN  # exact frame index
                text_Bmiddle_Choice.tStart = t  # local t and not account for scr refresh
                text_Bmiddle_Choice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_Bmiddle_Choice, 'tStartRefresh')  # time at next scr refresh
                text_Bmiddle_Choice.setAutoDraw(True)
            
            # *text_Bup_Choice* updates
            if text_Bup_Choice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_Bup_Choice.frameNStart = frameN  # exact frame index
                text_Bup_Choice.tStart = t  # local t and not account for scr refresh
                text_Bup_Choice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_Bup_Choice, 'tStartRefresh')  # time at next scr refresh
                text_Bup_Choice.setAutoDraw(True)
            
            # *text_Bdown_Choice* updates
            if text_Bdown_Choice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_Bdown_Choice.frameNStart = frameN  # exact frame index
                text_Bdown_Choice.tStart = t  # local t and not account for scr refresh
                text_Bdown_Choice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_Bdown_Choice, 'tStartRefresh')  # time at next scr refresh
                text_Bdown_Choice.setAutoDraw(True)



            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                print(currentChoice)
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ChoiceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
                

        # -------Ending Routine "Choice"-------
        for thisComponent in ChoiceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
                thisComponent.tStopRefresh = tThisFlipGlobal
                

        if currentChoice == "A": 
            thisTrialChoice.append('A')
            if i == 0:
                target = target-(1/(2**(n+1)))*abs(step)
            else:
                target = target+(1/(2**(n+1)))*abs(step)
            
        elif currentChoice == "B": 
            thisTrialChoice.append('B')
            if i == 0 :
                target = target+(1/(2**(n+1)))*abs(step)
            else:
                target = target-(1/(2**(n+1)))*abs(step)
                
        if target%5 !=0 :
            target = (round(target/5))*5
        target = int(target)

        if i == 0:
            text_L_list[n+1] = target
        elif i == 1:
            text_x1pos_list[n+1] = target
        elif i == 2:
            text_x1neg_list[n+1] = target
        elif i == 3:
            text_L2_list[n+1] = target
        elif i == 4:
            text_G2_list[n+1] = target
        elif i == 5:
            text_x2pos_list[n+1] = target
        elif i == 6:
            text_x3pos_list[n+1] = target
        elif i == 7:
            text_x4pos_list[n+1] = target
        elif i == 8:
            text_x5pos_list[n+1] = target
        elif i == 9:
            text_x6pos_list[n+1] = target
        elif i == 10:
            text_x7pos_list[n+1] = target
        elif i == 11:
            text_x8pos_list[n+1] = target
        elif i == 12:
            text_x2neg_list[n+1] = target
        elif i == 13:
            text_x3neg_list[n+1] = target
        elif i == 14:
            text_x4neg_list[n+1] = target
        elif i == 15:
            text_x5neg_list[n+1] = target
        elif i == 16:
            text_x6neg_list[n+1] = target
        elif i == 17:
            text_x7neg_list[n+1] = target
        elif i == 18:
            text_x8neg_list[n+1] = target
            
        # store data for thisExp (ExperimentHandler)
        thisExp.addData('Choice_'+trial_order[i]+'_'+str(n+1)+'.start', interface_Choice.tStartRefresh)
        thisExp.addData('Choice_'+trial_order[i]+'_'+str(n+1)+'.end', interface_Choice.tStopRefresh)
        thisExp.addData(trial_order[i]+'_list', all_point_data_list[i])
        thisExp.addData(trial_order[i]+'_choice_list', thisTrialChoice)
        #thisExp.nextEntry()


        # the Routine "Choice" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()

        # ------Prepare to start Routine "interval"-------
        continueRoutine = True
        routineTimer.add(0.100000) # 2s
        # update component parameters for each repeat
        # keep track of which components have finished
        intervalComponents = [cross]
        for thisComponent in intervalComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        intervalClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

        # -------Run Routine "interval"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = intervalClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=intervalClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cross* updates
            if cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cross.frameNStart = frameN  # exact frame index
                cross.tStart = t  # local t and not account for scr refresh
                cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
                cross.setAutoDraw(True)
            if cross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cross.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    cross.tStop = t  # not accounting for scr refresh
                    cross.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(cross, 'tStopRefresh')  # time at next scr refresh
                    cross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in intervalComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "interval"-------
        for thisComponent in intervalComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
    
    if i == 0:
        text_L_list[-1] = int(target)
        L = text_L_list[-1]
    elif i == 1:
        text_x1pos_list[-1] = int(target)
        x1pos = text_x1pos_list[-1]
        text_x1neg_list[0] = (round(int((1/2)*L)/5))*5
    elif i == 2:
        text_x1neg_list[-1] = int(target)
        x1neg = text_x1neg_list[-1]
        text_L2_list[0] = int(l-x1pos)
        text_G2_list[0] = int(g-x1neg)
    elif i == 3:
        text_L2_list[-1] = int(target)
        L2 = text_L2_list[-1]
        text_x2pos_list[0] = int(x1pos+l-L2)
    elif i == 4:
        text_G2_list[-1] = int(target)
        G2 = text_G2_list[-1]
        text_x2neg_list[0] = int(x1neg+g-G2)

    elif i == 5:
        text_x2pos_list[-1] = int(target)
        x2pos = text_x2pos_list[-1]
        text_x3pos_list[0] = int(x2pos+l-L2)
    elif i == 6:
        text_x3pos_list[-1] = int(target)
        x3pos = text_x3pos_list[-1]
        text_x4pos_list[0] = int(x3pos+l-L2)
    elif i == 7:
        text_x4pos_list[-1] = int(target)
        x4pos = text_x4pos_list[-1]
        text_x5pos_list[0] = int(x4pos+l-L2)
    elif i == 8:
        text_x5pos_list[-1] = int(target)
        x5pos = text_x5pos_list[-1]
        text_x6pos_list[0] = int(x5pos+l-L2)
    elif i == 9:
        text_x6pos_list[-1] = int(target)
        x6pos = text_x6pos_list[-1]
        text_x7pos_list[0] =int(x6pos+l-L2)
    elif i == 10:
        text_x7pos_list[-1] = int(target)
        x7pos = text_x7pos_list[-1]
        text_x8pos_list[0] = int(x7pos+l-L2)
    elif i == 11:
        text_x8pos_list[-1] = int(target)
        x8pos = text_x8pos_list[-1]
    elif i == 12:
        text_x2neg_list[-1] = int(target)
        x2neg = text_x2neg_list[-1]
        text_x3neg_list[0] = int(x2neg+g-G2)
    elif i == 13:
        text_x3neg_list[-1] = int(target)
        x3neg = text_x3neg_list[-1]
        text_x4neg_list[0] = int(x3neg+g-G2)
    elif i == 14:
        text_x4neg_list[-1] = int(target)
        x4neg = text_x4neg_list[-1]
        text_x5neg_list[0] = int(x4neg+g-G2)
    elif i == 15:
        text_x5neg_list[-1] = int(target)
        x5neg = text_x5neg_list[-1]
        text_x6neg_list[0] = int(x5neg+g-G2)
    elif i == 16:
        text_x6neg_list[-1] = int(target)
        x6neg = text_x6neg_list[-1]
        text_x7neg_list[0] = int(x6neg+g-G2)
    elif i == 17:
        text_x7neg_list[-1] = int(target)
        x7neg = text_x7neg_list[-1]
        text_x8neg_list[0] = int(x7neg+g-G2)
    elif i == 18:
        text_x8neg_list[-1] = int(target)
        x8neg = text_x8neg_list[-1]


    # store data for thisExp (ExperimentHandler)
    thisExp.addData(trial_order[i], all_point_data_list[i][-1])
    thisExp.addData(trial_order[i]+'_list', all_point_data_list[i])

    # ------Prepare to start Routine "interval"-------
    continueRoutine = True
    routineTimer.add(0.100000) #5s
    # update component parameters for each repeat
    # keep track of which components have finished
    intervalComponents = [nextTrial]
    for thisComponent in intervalComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    intervalClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "interval"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = intervalClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=intervalClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *nextTrial* updates
        if nextTrial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            nextTrial.frameNStart = frameN  # exact frame index
            nextTrial.tStart = t  # local t and not account for scr refresh
            nextTrial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nextTrial, 'tStartRefresh')  # time at next scr refresh
            nextTrial.setAutoDraw(True)
        if nextTrial.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > nextTrial.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                nextTrial.tStop = t  # not accounting for scr refresh
                nextTrial.frameNStop = frameN  # exact frame index
                win.timeOnFlip(nextTrial, 'tStopRefresh')  # time at next scr refresh
                nextTrial.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in intervalComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "interval"-------
    for thisComponent in intervalComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)


# ------Prepare to start Routine "random_2"-------#############################################################################
# -------Run Routine "random_2"-------
# -------Ending Routine "random_2"-------
# ------Prepare to start Routine "outcome"-------##############################################
# -------Run Routine "outcome"-------
# -------Ending Routine "outcome"-------
# ------Prepare to start Routine "result"-------

# ------Prepare to start Routine "endExp"-------
continueRoutine = True
# update component parameters for each repeat
#incentive

mouse_endExp.clicked_name = []
# keep track of which components have finished
endExpComponents = [buttonOK_endExp,mouse_endExp,text_endExp]
for thisComponent in endExpComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endExpClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1


# -------Run Routine "endExp"-------
while continueRoutine:
    # get current time
    t = endExpClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endExpClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *buttonOK_endExp* updates
    if buttonOK_endExp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        buttonOK_endExp.frameNStart = frameN  # exact frame index
        buttonOK_endExp.tStart = t  # local t and not account for scr refresh
        buttonOK_endExp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(buttonOK_endExp, 'tStartRefresh')  # time at next scr refresh
        buttonOK_endExp.setAutoDraw(True)

    # *text_endExp* updates
    if text_endExp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_endExp.frameNStart = frameN  # exact frame index
        text_endExp.tStart = t  # local t and not account for scr refresh
        text_endExp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_endExp, 'tStartRefresh')  # time at next scr refresh
        text_endExp.setAutoDraw(True)
    
    if mouse_endExp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_endExp.frameNStart = frameN  # exact frame index
        mouse_endExp.tStart = t  # local t and not account for scr refresh
        mouse_endExp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_endExp, 'tStartRefresh')  # time at next scr refresh
        mouse_endExp.status = STARTED
        mouse_endExp.mouseClock.reset()
        prevButtonState = mouse_endExp.getPressed()  # if button is down already this ISN'T a new click
    if mouse_endExp.status == STARTED:  # only update if started and not finished!
        buttons = mouse_endExp.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [buttonOK_endExp]:
                    if obj.contains(mouse_endExp):
                        gotValidClick = True
                        mouse_endExp.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False    
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endExpComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "endExp"-------
for thisComponent in endExpComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "endExp" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()


# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)

#####drive api

creds = driveapi.getCreds("driveapi/token.json")
folderid = driveapi.create_folder(expInfo['participant'], creds)
driveapi.upload_to_folder(folderid, filename+'.csv', creds)

##########################
logging.flush()



# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
