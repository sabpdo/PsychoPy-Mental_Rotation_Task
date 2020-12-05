#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.4),
    on Sun Nov  1 12:19:22 2020
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

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.4'
expName = 'MRT'  # from the Builder filename that created this script
expInfo = {'participant': '', 'Session': '001', 'Age': '', 'Sex': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sort_keys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/sabrinado/Library/CELSYS/MRT/MRT.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='white', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "testName"
testNameClock = core.Clock()
WelcomeScreen = visual.TextStim(win=win, name='WelcomeScreen',
    text='Mental Rotation Test (MRT)',
    font='Times New Roman',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "Welcome_Screen"
Welcome_ScreenClock = core.Clock()
introduction = visual.TextStim(win=win, name='introduction',
    text='This is a test of your ability to look at a drawing of a given object and find the same object within a set of dissimilar objects. The only diference between the original object and the chosen object will be that they are presented at different angles. An illustration of this principle is given below where the same single object is given in five different positions. Look at each of them to satisfy yourself that they are only presented at different angles from one another.',
    font='Times New Roman',
    pos=(0, 0.35), height=0.030, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
keyWelcome = keyboard.Keyboard()
exampleText = visual.TextStim(win=win, name='exampleText',
    text='\nBelow are two drawings of new objects. They cannot be made to match the above five drawings. Please note that you may not turn over the objects. Satisfy yourself that they are different from the above.',
    font='Times New Roman',
    pos=(0, 0), height=0.030, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
responseIndicator = visual.TextStim(win=win, name='responseIndicator',
    text='Please press ‘space’ to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.030, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
example = visual.ImageStim(
    win=win,
    name='example', 
    image='example.jpg', mask=None,
    ori=0, pos=(0, 0.15), size=(0.80, 0.18),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-4.0)
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='sample2.jpg', mask=None,
    ori=0, pos=(0, -0.25), size=(0.70, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-5.0)

# Initialize components for Routine "Example"
ExampleClock = core.Clock()
practiceProblemInstructions = visual.TextStim(win=win, name='practiceProblemInstructions',
    text='Now let’s do some sample problems. For each problem there is a primary object on the far left. You are to determine which two of four objects to the right are the same object given on the far left. In each problem always two of the four drawings are the same object as the one on the left. You are to put Xs in the boxes below the correct ones, and leave the incorrect ones blank. The first sample problem is done for you.',
    font='Times New Roman',
    pos=(0, 0.4), height=0.030, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
practiceProblemImage = visual.ImageStim(
    win=win,
    name='practiceProblemImage', 
    image='sampleProblem.jpg', mask=None,
    ori=0, pos=(0, 0), size=(1.70, 0.38),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
inputIndicatorPractice = visual.TextStim(win=win, name='inputIndicatorPractice',
    text='Please press ‘space’ to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.030, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
responseExample = keyboard.Keyboard()

# Initialize components for Routine "SampleQuestion1_2"
SampleQuestion1_2Clock = core.Clock()
sampleQuestionImage1 = visual.ImageStim(
    win=win,
    name='sampleQuestionImage1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.40, 0.31),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
inputIndicatorSampleQuestion1 = visual.TextStim(win=win, name='inputIndicatorSampleQuestion1',
    text='Please press ‘space’ to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.030, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
responseSampleQuestion1 = keyboard.Keyboard()
SampleQuestionsInstructions = visual.TextStim(win=win, name='SampleQuestionsInstructions',
    text='Do the rest of the sample problems yourself. Which two drawings of the four on the right show the same object as the one on the left? There are always two and only two correct answers for each problem. Select the two correct drawings by pressing the boxes below the drawing, selecting the picture from left to right. Keep in mind you cannot change your answer after you select it.',
    font='Times New Roman',
    pos=(0, 0.33), height=0.040, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
sampleBox1 = visual.Rect(
    win=win, name='sampleBox1',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(-0.20, -0.210),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
sampleBox2 = visual.Rect(
    win=win, name='sampleBox2',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(0.05, -0.210),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
sampleBox3 = visual.Rect(
    win=win, name='sampleBox3',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(0.30, -0.210),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
sampleBox4 = visual.Rect(
    win=win, name='sampleBox4',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(0.55, -0.210),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)
mouse3 = event.Mouse(win=win)
x, y = [None, None]
mouse3.mouseClock = core.Clock()

# Initialize components for Routine "Answer"
AnswerClock = core.Clock()
SampleAnswers = visual.TextStim(win=win, name='SampleAnswers',
    text='Answers:       (1) first and second drawings are correct\n                    (2) first and third drawings are correct\n                       (3) second and third drawings are correct',
    font='Times New Roman',
    pos=(0, 0), height=0.040, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
inputIndicatorAnswer = visual.TextStim(win=win, name='inputIndicatorAnswer',
    text='Please press ‘space’ to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.030, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
responseAnswer = keyboard.Keyboard()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
InstructionsText = visual.TextStim(win=win, name='InstructionsText',
    text='This test has two parts. You will have 3 minutes for each of the two part has 10 questions. When you have finished Part I, STOP. Please do not go on to Part II until you are asked to do so. Remember: There are always two and only two correct answers for each item.\n\nWork as quickly as you can without sacrificing accuracy. Your score on this test will reflect both the correct and incorrect responses. Therefore, it will not be to your advantage to guess unless you have some idea which choice is correct. Keep in mind that once you choose an answer and go to the next screen, you cannot change your answers.',
    font='Times New Roman',
    pos=(0, 0.15), height=0.040, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
IndicatorWarning = visual.TextStim(win=win, name='IndicatorWarning',
    text='Do Not Continue Until Asked To Do So. \n\nPress ‘space’ to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.050, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
responseInstructions = keyboard.Keyboard()

# Initialize components for Routine "Part1"
Part1Clock = core.Clock()
Part1Text = visual.TextStim(win=win, name='Part1Text',
    text='Part I.',
    font='Times New Roman',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
responsePart1 = keyboard.Keyboard()

# Initialize components for Routine "Question1"
Question1Clock = core.Clock()
image2346 = visual.ImageStim(
    win=win,
    name='image2346', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.40, 0.31),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
text = visual.TextStim(win=win, name='text',
    text='Press ‘space’ to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.050, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
responseQuestion1 = keyboard.Keyboard()
box1 = visual.Rect(
    win=win, name='box1',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(-0.15, -0.20),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
box2 = visual.Rect(
    win=win, name='box2',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(0.10, -0.2),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
box3 = visual.Rect(
    win=win, name='box3',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(0.35, -0.20),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
box4 = visual.Rect(
    win=win, name='box4',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(0.60, -0.20),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Initialize components for Routine "instr"
instrClock = core.Clock()
instrStop = visual.TextStim(win=win, name='instrStop',
    text='Stop.\n\nDo Not Continue Until Asked To Do So.',
    font='Times New Roman',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
stopIndicator = keyboard.Keyboard()

# Initialize components for Routine "Part2"
Part2Clock = core.Clock()
part2Indicator = visual.TextStim(win=win, name='part2Indicator',
    text='Part II',
    font='Times New Roman',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
part2IndicatorResponse = keyboard.Keyboard()

# Initialize components for Routine "part2Questions"
part2QuestionsClock = core.Clock()
indicatorQuestionPart2 = visual.TextStim(win=win, name='indicatorQuestionPart2',
    text='Press ‘space’ to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.050, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
keyboardIndicator = keyboard.Keyboard()
part2Images = visual.ImageStim(
    win=win,
    name='part2Images', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.40, 0.31),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
box21 = visual.Rect(
    win=win, name='box21',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(-0.15, -0.20),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
box22 = visual.Rect(
    win=win, name='box22',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(0.10, -0.20),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
box23 = visual.Rect(
    win=win, name='box23',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(0.35, -0.20),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
box24 = visual.Rect(
    win=win, name='box24',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(0.60, -0.20),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
mouse2 = event.Mouse(win=win)
x, y = [None, None]
mouse2.mouseClock = core.Clock()

# Initialize components for Routine "End"
EndClock = core.Clock()
EndScreen = visual.TextStim(win=win, name='EndScreen',
    text='Congrats! You have finished the test.\n\nThe End',
    font='Times New Roman',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
endResponse = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "testName"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
testNameComponents = [WelcomeScreen, key_resp_2]
for thisComponent in testNameComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
testNameClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "testName"-------
while continueRoutine:
    # get current time
    t = testNameClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=testNameClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *WelcomeScreen* updates
    if WelcomeScreen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        WelcomeScreen.frameNStart = frameN  # exact frame index
        WelcomeScreen.tStart = t  # local t and not account for scr refresh
        WelcomeScreen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(WelcomeScreen, 'tStartRefresh')  # time at next scr refresh
        WelcomeScreen.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=None, waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in testNameComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "testName"-------
for thisComponent in testNameComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('WelcomeScreen.started', WelcomeScreen.tStartRefresh)
thisExp.addData('WelcomeScreen.stopped', WelcomeScreen.tStopRefresh)
# the Routine "testName" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Welcome_Screen"-------
continueRoutine = True
# update component parameters for each repeat
keyWelcome.keys = []
keyWelcome.rt = []
_keyWelcome_allKeys = []
# keep track of which components have finished
Welcome_ScreenComponents = [introduction, keyWelcome, exampleText, responseIndicator, example, image_2]
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
Welcome_ScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Welcome_Screen"-------
while continueRoutine:
    # get current time
    t = Welcome_ScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Welcome_ScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *introduction* updates
    if introduction.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        introduction.frameNStart = frameN  # exact frame index
        introduction.tStart = t  # local t and not account for scr refresh
        introduction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(introduction, 'tStartRefresh')  # time at next scr refresh
        introduction.setAutoDraw(True)
    
    # *keyWelcome* updates
    waitOnFlip = False
    if keyWelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyWelcome.frameNStart = frameN  # exact frame index
        keyWelcome.tStart = t  # local t and not account for scr refresh
        keyWelcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyWelcome, 'tStartRefresh')  # time at next scr refresh
        keyWelcome.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyWelcome.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyWelcome.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyWelcome.status == STARTED and not waitOnFlip:
        theseKeys = keyWelcome.getKeys(keyList=['space'], waitRelease=False)
        _keyWelcome_allKeys.extend(theseKeys)
        if len(_keyWelcome_allKeys):
            keyWelcome.keys = _keyWelcome_allKeys[-1].name  # just the last key pressed
            keyWelcome.rt = _keyWelcome_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *exampleText* updates
    if exampleText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        exampleText.frameNStart = frameN  # exact frame index
        exampleText.tStart = t  # local t and not account for scr refresh
        exampleText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(exampleText, 'tStartRefresh')  # time at next scr refresh
        exampleText.setAutoDraw(True)
    
    # *responseIndicator* updates
    if responseIndicator.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responseIndicator.frameNStart = frameN  # exact frame index
        responseIndicator.tStart = t  # local t and not account for scr refresh
        responseIndicator.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responseIndicator, 'tStartRefresh')  # time at next scr refresh
        responseIndicator.setAutoDraw(True)
    
    # *example* updates
    if example.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        example.frameNStart = frameN  # exact frame index
        example.tStart = t  # local t and not account for scr refresh
        example.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(example, 'tStartRefresh')  # time at next scr refresh
        example.setAutoDraw(True)
    
    # *image_2* updates
    if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_2.frameNStart = frameN  # exact frame index
        image_2.tStart = t  # local t and not account for scr refresh
        image_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
        image_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Welcome_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome_Screen"-------
for thisComponent in Welcome_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('introduction.started', introduction.tStartRefresh)
thisExp.addData('introduction.stopped', introduction.tStopRefresh)
thisExp.addData('exampleText.started', exampleText.tStartRefresh)
thisExp.addData('exampleText.stopped', exampleText.tStopRefresh)
thisExp.addData('responseIndicator.started', responseIndicator.tStartRefresh)
thisExp.addData('responseIndicator.stopped', responseIndicator.tStopRefresh)
thisExp.addData('example.started', example.tStartRefresh)
thisExp.addData('example.stopped', example.tStopRefresh)
thisExp.addData('image_2.started', image_2.tStartRefresh)
thisExp.addData('image_2.stopped', image_2.tStopRefresh)
# the Routine "Welcome_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Example"-------
continueRoutine = True
# update component parameters for each repeat
responseExample.keys = []
responseExample.rt = []
_responseExample_allKeys = []
# keep track of which components have finished
ExampleComponents = [practiceProblemInstructions, practiceProblemImage, inputIndicatorPractice, responseExample]
for thisComponent in ExampleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ExampleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Example"-------
while continueRoutine:
    # get current time
    t = ExampleClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ExampleClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practiceProblemInstructions* updates
    if practiceProblemInstructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practiceProblemInstructions.frameNStart = frameN  # exact frame index
        practiceProblemInstructions.tStart = t  # local t and not account for scr refresh
        practiceProblemInstructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practiceProblemInstructions, 'tStartRefresh')  # time at next scr refresh
        practiceProblemInstructions.setAutoDraw(True)
    
    # *practiceProblemImage* updates
    if practiceProblemImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practiceProblemImage.frameNStart = frameN  # exact frame index
        practiceProblemImage.tStart = t  # local t and not account for scr refresh
        practiceProblemImage.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practiceProblemImage, 'tStartRefresh')  # time at next scr refresh
        practiceProblemImage.setAutoDraw(True)
    
    # *inputIndicatorPractice* updates
    if inputIndicatorPractice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        inputIndicatorPractice.frameNStart = frameN  # exact frame index
        inputIndicatorPractice.tStart = t  # local t and not account for scr refresh
        inputIndicatorPractice.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(inputIndicatorPractice, 'tStartRefresh')  # time at next scr refresh
        inputIndicatorPractice.setAutoDraw(True)
    
    # *responseExample* updates
    waitOnFlip = False
    if responseExample.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responseExample.frameNStart = frameN  # exact frame index
        responseExample.tStart = t  # local t and not account for scr refresh
        responseExample.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responseExample, 'tStartRefresh')  # time at next scr refresh
        responseExample.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(responseExample.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(responseExample.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if responseExample.status == STARTED and not waitOnFlip:
        theseKeys = responseExample.getKeys(keyList=['space'], waitRelease=False)
        _responseExample_allKeys.extend(theseKeys)
        if len(_responseExample_allKeys):
            responseExample.keys = _responseExample_allKeys[-1].name  # just the last key pressed
            responseExample.rt = _responseExample_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ExampleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Example"-------
for thisComponent in ExampleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('practiceProblemInstructions.started', practiceProblemInstructions.tStartRefresh)
thisExp.addData('practiceProblemInstructions.stopped', practiceProblemInstructions.tStopRefresh)
thisExp.addData('practiceProblemImage.started', practiceProblemImage.tStartRefresh)
thisExp.addData('practiceProblemImage.stopped', practiceProblemImage.tStopRefresh)
thisExp.addData('inputIndicatorPractice.started', inputIndicatorPractice.tStartRefresh)
thisExp.addData('inputIndicatorPractice.stopped', inputIndicatorPractice.tStopRefresh)
# the Routine "Example" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials3 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('sample.xlsx'),
    seed=None, name='trials3')
thisExp.addLoop(trials3)  # add the loop to the experiment
thisTrials3 = trials3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials3.rgb)
if thisTrials3 != None:
    for paramName in thisTrials3:
        exec('{} = thisTrials3[paramName]'.format(paramName))

for thisTrials3 in trials3:
    currentLoop = trials3
    # abbreviate parameter names if possible (e.g. rgb = thisTrials3.rgb)
    if thisTrials3 != None:
        for paramName in thisTrials3:
            exec('{} = thisTrials3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "SampleQuestion1_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    sampleQuestionImage1.setImage(image)
    responseSampleQuestion1.keys = []
    responseSampleQuestion1.rt = []
    _responseSampleQuestion1_allKeys = []
    sampleBox1.setFillColor('green')
    sampleBox2.setFillColor('green')
    sampleBox3.setFillColor('green')
    sampleBox4.setFillColor('green')
    # setup some python lists for storing info about the mouse3
    mouse3.x = []
    mouse3.y = []
    mouse3.leftButton = []
    mouse3.midButton = []
    mouse3.rightButton = []
    mouse3.time = []
    mouse3.clicked_name = []
    gotValidClick = False  # until a click is received
    checkboxes = [sampleBox1, sampleBox2, sampleBox3, sampleBox4]
    clicked = []
    # keep track of which components have finished
    SampleQuestion1_2Components = [sampleQuestionImage1, inputIndicatorSampleQuestion1, responseSampleQuestion1, SampleQuestionsInstructions, sampleBox1, sampleBox2, sampleBox3, sampleBox4, mouse3]
    for thisComponent in SampleQuestion1_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    SampleQuestion1_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "SampleQuestion1_2"-------
    while continueRoutine:
        # get current time
        t = SampleQuestion1_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=SampleQuestion1_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *sampleQuestionImage1* updates
        if sampleQuestionImage1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sampleQuestionImage1.frameNStart = frameN  # exact frame index
            sampleQuestionImage1.tStart = t  # local t and not account for scr refresh
            sampleQuestionImage1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sampleQuestionImage1, 'tStartRefresh')  # time at next scr refresh
            sampleQuestionImage1.setAutoDraw(True)
        
        # *inputIndicatorSampleQuestion1* updates
        if inputIndicatorSampleQuestion1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            inputIndicatorSampleQuestion1.frameNStart = frameN  # exact frame index
            inputIndicatorSampleQuestion1.tStart = t  # local t and not account for scr refresh
            inputIndicatorSampleQuestion1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(inputIndicatorSampleQuestion1, 'tStartRefresh')  # time at next scr refresh
            inputIndicatorSampleQuestion1.setAutoDraw(True)
        
        # *responseSampleQuestion1* updates
        waitOnFlip = False
        if responseSampleQuestion1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            responseSampleQuestion1.frameNStart = frameN  # exact frame index
            responseSampleQuestion1.tStart = t  # local t and not account for scr refresh
            responseSampleQuestion1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(responseSampleQuestion1, 'tStartRefresh')  # time at next scr refresh
            responseSampleQuestion1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(responseSampleQuestion1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(responseSampleQuestion1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if responseSampleQuestion1.status == STARTED and not waitOnFlip:
            theseKeys = responseSampleQuestion1.getKeys(keyList=['space'], waitRelease=False)
            _responseSampleQuestion1_allKeys.extend(theseKeys)
            if len(_responseSampleQuestion1_allKeys):
                responseSampleQuestion1.keys = _responseSampleQuestion1_allKeys[-1].name  # just the last key pressed
                responseSampleQuestion1.rt = _responseSampleQuestion1_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *SampleQuestionsInstructions* updates
        if SampleQuestionsInstructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            SampleQuestionsInstructions.frameNStart = frameN  # exact frame index
            SampleQuestionsInstructions.tStart = t  # local t and not account for scr refresh
            SampleQuestionsInstructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SampleQuestionsInstructions, 'tStartRefresh')  # time at next scr refresh
            SampleQuestionsInstructions.setAutoDraw(True)
        
        # *sampleBox1* updates
        if sampleBox1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sampleBox1.frameNStart = frameN  # exact frame index
            sampleBox1.tStart = t  # local t and not account for scr refresh
            sampleBox1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sampleBox1, 'tStartRefresh')  # time at next scr refresh
            sampleBox1.setAutoDraw(True)
        
        # *sampleBox2* updates
        if sampleBox2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sampleBox2.frameNStart = frameN  # exact frame index
            sampleBox2.tStart = t  # local t and not account for scr refresh
            sampleBox2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sampleBox2, 'tStartRefresh')  # time at next scr refresh
            sampleBox2.setAutoDraw(True)
        
        # *sampleBox3* updates
        if sampleBox3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sampleBox3.frameNStart = frameN  # exact frame index
            sampleBox3.tStart = t  # local t and not account for scr refresh
            sampleBox3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sampleBox3, 'tStartRefresh')  # time at next scr refresh
            sampleBox3.setAutoDraw(True)
        
        # *sampleBox4* updates
        if sampleBox4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sampleBox4.frameNStart = frameN  # exact frame index
            sampleBox4.tStart = t  # local t and not account for scr refresh
            sampleBox4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sampleBox4, 'tStartRefresh')  # time at next scr refresh
            sampleBox4.setAutoDraw(True)
        # *mouse3* updates
        if mouse3.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse3.frameNStart = frameN  # exact frame index
            mouse3.tStart = t  # local t and not account for scr refresh
            mouse3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse3, 'tStartRefresh')  # time at next scr refresh
            mouse3.status = STARTED
            mouse3.mouseClock.reset()
            prevButtonState = mouse3.getPressed()  # if button is down already this ISN'T a new click
        if mouse3.status == STARTED:  # only update if started and not finished!
            buttons = mouse3.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [sampleBox1, sampleBox2, sampleBox3, sampleBox4]:
                        if obj.contains(mouse3):
                            gotValidClick = True
                            mouse3.clicked_name.append(obj.name)
                    x, y = mouse3.getPos()
                    mouse3.x.append(x)
                    mouse3.y.append(y)
                    buttons = mouse3.getPressed()
                    mouse3.leftButton.append(buttons[0])
                    mouse3.midButton.append(buttons[1])
                    mouse3.rightButton.append(buttons[2])
                    mouse3.time.append(mouse3.mouseClock.getTime())
        for box in checkboxes:
            if mouse3.isPressedIn(box) and box.name not in clicked:
                box.color = "black"
                clicked.append(box.name)
        
        
        if mouse3.isPressedIn(text):
            continueRoutine = False
        
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SampleQuestion1_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "SampleQuestion1_2"-------
    for thisComponent in SampleQuestion1_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials3.addData('sampleQuestionImage1.started', sampleQuestionImage1.tStartRefresh)
    trials3.addData('sampleQuestionImage1.stopped', sampleQuestionImage1.tStopRefresh)
    trials3.addData('inputIndicatorSampleQuestion1.started', inputIndicatorSampleQuestion1.tStartRefresh)
    trials3.addData('inputIndicatorSampleQuestion1.stopped', inputIndicatorSampleQuestion1.tStopRefresh)
    trials3.addData('SampleQuestionsInstructions.started', SampleQuestionsInstructions.tStartRefresh)
    trials3.addData('SampleQuestionsInstructions.stopped', SampleQuestionsInstructions.tStopRefresh)
    trials3.addData('sampleBox1.started', sampleBox1.tStartRefresh)
    trials3.addData('sampleBox1.stopped', sampleBox1.tStopRefresh)
    trials3.addData('sampleBox2.started', sampleBox2.tStartRefresh)
    trials3.addData('sampleBox2.stopped', sampleBox2.tStopRefresh)
    trials3.addData('sampleBox3.started', sampleBox3.tStartRefresh)
    trials3.addData('sampleBox3.stopped', sampleBox3.tStopRefresh)
    trials3.addData('sampleBox4.started', sampleBox4.tStartRefresh)
    trials3.addData('sampleBox4.stopped', sampleBox4.tStopRefresh)
    # store data for trials3 (TrialHandler)
    trials3.addData('mouse3.x', mouse3.x)
    trials3.addData('mouse3.y', mouse3.y)
    trials3.addData('mouse3.leftButton', mouse3.leftButton)
    trials3.addData('mouse3.midButton', mouse3.midButton)
    trials3.addData('mouse3.rightButton', mouse3.rightButton)
    trials3.addData('mouse3.time', mouse3.time)
    trials3.addData('mouse3.clicked_name', mouse3.clicked_name)
    trials3.addData('mouse3.started', mouse3.tStart)
    trials3.addData('mouse3.stopped', mouse3.tStop)
    correct = 0
    for checkboxes in mouse3.clicked_name:
        if checkboxes in corrAnsSample:
            correct +=1
    trials3.addData('sampleCorrect', correct)
    # the Routine "SampleQuestion1_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials3'

# get names of stimulus parameters
if trials3.trialList in ([], [None], None):
    params = []
else:
    params = trials3.trialList[0].keys()
# save data for this loop
trials3.saveAsExcel(filename + '.xlsx', sheetName='trials3',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "Answer"-------
continueRoutine = True
# update component parameters for each repeat
responseAnswer.keys = []
responseAnswer.rt = []
_responseAnswer_allKeys = []
# keep track of which components have finished
AnswerComponents = [SampleAnswers, inputIndicatorAnswer, responseAnswer]
for thisComponent in AnswerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
AnswerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Answer"-------
while continueRoutine:
    # get current time
    t = AnswerClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=AnswerClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *SampleAnswers* updates
    if SampleAnswers.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        SampleAnswers.frameNStart = frameN  # exact frame index
        SampleAnswers.tStart = t  # local t and not account for scr refresh
        SampleAnswers.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(SampleAnswers, 'tStartRefresh')  # time at next scr refresh
        SampleAnswers.setAutoDraw(True)
    
    # *inputIndicatorAnswer* updates
    if inputIndicatorAnswer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        inputIndicatorAnswer.frameNStart = frameN  # exact frame index
        inputIndicatorAnswer.tStart = t  # local t and not account for scr refresh
        inputIndicatorAnswer.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(inputIndicatorAnswer, 'tStartRefresh')  # time at next scr refresh
        inputIndicatorAnswer.setAutoDraw(True)
    
    # *responseAnswer* updates
    waitOnFlip = False
    if responseAnswer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responseAnswer.frameNStart = frameN  # exact frame index
        responseAnswer.tStart = t  # local t and not account for scr refresh
        responseAnswer.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responseAnswer, 'tStartRefresh')  # time at next scr refresh
        responseAnswer.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(responseAnswer.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(responseAnswer.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if responseAnswer.status == STARTED and not waitOnFlip:
        theseKeys = responseAnswer.getKeys(keyList=['space'], waitRelease=False)
        _responseAnswer_allKeys.extend(theseKeys)
        if len(_responseAnswer_allKeys):
            responseAnswer.keys = _responseAnswer_allKeys[-1].name  # just the last key pressed
            responseAnswer.rt = _responseAnswer_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in AnswerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Answer"-------
for thisComponent in AnswerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('SampleAnswers.started', SampleAnswers.tStartRefresh)
thisExp.addData('SampleAnswers.stopped', SampleAnswers.tStopRefresh)
thisExp.addData('inputIndicatorAnswer.started', inputIndicatorAnswer.tStartRefresh)
thisExp.addData('inputIndicatorAnswer.stopped', inputIndicatorAnswer.tStopRefresh)
# the Routine "Answer" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instructions"-------
continueRoutine = True
# update component parameters for each repeat
responseInstructions.keys = []
responseInstructions.rt = []
_responseInstructions_allKeys = []
# keep track of which components have finished
InstructionsComponents = [InstructionsText, IndicatorWarning, responseInstructions]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *InstructionsText* updates
    if InstructionsText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InstructionsText.frameNStart = frameN  # exact frame index
        InstructionsText.tStart = t  # local t and not account for scr refresh
        InstructionsText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstructionsText, 'tStartRefresh')  # time at next scr refresh
        InstructionsText.setAutoDraw(True)
    
    # *IndicatorWarning* updates
    if IndicatorWarning.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        IndicatorWarning.frameNStart = frameN  # exact frame index
        IndicatorWarning.tStart = t  # local t and not account for scr refresh
        IndicatorWarning.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(IndicatorWarning, 'tStartRefresh')  # time at next scr refresh
        IndicatorWarning.setAutoDraw(True)
    
    # *responseInstructions* updates
    waitOnFlip = False
    if responseInstructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responseInstructions.frameNStart = frameN  # exact frame index
        responseInstructions.tStart = t  # local t and not account for scr refresh
        responseInstructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responseInstructions, 'tStartRefresh')  # time at next scr refresh
        responseInstructions.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(responseInstructions.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(responseInstructions.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if responseInstructions.status == STARTED and not waitOnFlip:
        theseKeys = responseInstructions.getKeys(keyList=['space'], waitRelease=False)
        _responseInstructions_allKeys.extend(theseKeys)
        if len(_responseInstructions_allKeys):
            responseInstructions.keys = _responseInstructions_allKeys[-1].name  # just the last key pressed
            responseInstructions.rt = _responseInstructions_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('InstructionsText.started', InstructionsText.tStartRefresh)
thisExp.addData('InstructionsText.stopped', InstructionsText.tStopRefresh)
thisExp.addData('IndicatorWarning.started', IndicatorWarning.tStartRefresh)
thisExp.addData('IndicatorWarning.stopped', IndicatorWarning.tStopRefresh)
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Part1"-------
continueRoutine = True
# update component parameters for each repeat
responsePart1.keys = []
responsePart1.rt = []
_responsePart1_allKeys = []
# keep track of which components have finished
Part1Components = [Part1Text, responsePart1]
for thisComponent in Part1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Part1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Part1"-------
while continueRoutine:
    # get current time
    t = Part1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Part1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Part1Text* updates
    if Part1Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Part1Text.frameNStart = frameN  # exact frame index
        Part1Text.tStart = t  # local t and not account for scr refresh
        Part1Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Part1Text, 'tStartRefresh')  # time at next scr refresh
        Part1Text.setAutoDraw(True)
    
    # *responsePart1* updates
    waitOnFlip = False
    if responsePart1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responsePart1.frameNStart = frameN  # exact frame index
        responsePart1.tStart = t  # local t and not account for scr refresh
        responsePart1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responsePart1, 'tStartRefresh')  # time at next scr refresh
        responsePart1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(responsePart1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(responsePart1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if responsePart1.status == STARTED and not waitOnFlip:
        theseKeys = responsePart1.getKeys(keyList=['space'], waitRelease=False)
        _responsePart1_allKeys.extend(theseKeys)
        if len(_responsePart1_allKeys):
            responsePart1.keys = _responsePart1_allKeys[-1].name  # just the last key pressed
            responsePart1.rt = _responsePart1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Part1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Part1"-------
for thisComponent in Part1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Part1Text.started', Part1Text.tStartRefresh)
thisExp.addData('Part1Text.stopped', Part1Text.tStopRefresh)
# the Routine "Part1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('boxCorrect.xlsx'),
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
    
    # ------Prepare to start Routine "Question1"-------
    continueRoutine = True
    # update component parameters for each repeat
    image2346.setImage(ImagePart1)
    responseQuestion1.keys = []
    responseQuestion1.rt = []
    _responseQuestion1_allKeys = []
    box1.setFillColor('green')
    box2.setFillColor('green')
    box3.setFillColor('green')
    box4.setFillColor('green')
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    checkboxes=[box1, box2, box3, box4]
    clicked=[]
    
    # keep track of which components have finished
    Question1Components = [image2346, text, responseQuestion1, box1, box2, box3, box4, mouse]
    for thisComponent in Question1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Question1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Question1"-------
    while continueRoutine:
        # get current time
        t = Question1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Question1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image2346* updates
        if image2346.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image2346.frameNStart = frameN  # exact frame index
            image2346.tStart = t  # local t and not account for scr refresh
            image2346.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image2346, 'tStartRefresh')  # time at next scr refresh
            image2346.setAutoDraw(True)
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
        # *responseQuestion1* updates
        waitOnFlip = False
        if responseQuestion1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            responseQuestion1.frameNStart = frameN  # exact frame index
            responseQuestion1.tStart = t  # local t and not account for scr refresh
            responseQuestion1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(responseQuestion1, 'tStartRefresh')  # time at next scr refresh
            responseQuestion1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(responseQuestion1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(responseQuestion1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if responseQuestion1.status == STARTED and not waitOnFlip:
            theseKeys = responseQuestion1.getKeys(keyList=['space'], waitRelease=False)
            _responseQuestion1_allKeys.extend(theseKeys)
            if len(_responseQuestion1_allKeys):
                responseQuestion1.keys = _responseQuestion1_allKeys[-1].name  # just the last key pressed
                responseQuestion1.rt = _responseQuestion1_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *box1* updates
        if box1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            box1.frameNStart = frameN  # exact frame index
            box1.tStart = t  # local t and not account for scr refresh
            box1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(box1, 'tStartRefresh')  # time at next scr refresh
            box1.setAutoDraw(True)
        
        # *box2* updates
        if box2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            box2.frameNStart = frameN  # exact frame index
            box2.tStart = t  # local t and not account for scr refresh
            box2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(box2, 'tStartRefresh')  # time at next scr refresh
            box2.setAutoDraw(True)
        
        # *box3* updates
        if box3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            box3.frameNStart = frameN  # exact frame index
            box3.tStart = t  # local t and not account for scr refresh
            box3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(box3, 'tStartRefresh')  # time at next scr refresh
            box3.setAutoDraw(True)
        
        # *box4* updates
        if box4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            box4.frameNStart = frameN  # exact frame index
            box4.tStart = t  # local t and not account for scr refresh
            box4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(box4, 'tStartRefresh')  # time at next scr refresh
            box4.setAutoDraw(True)
        # *mouse* updates
        if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [box4, box1, box2, box3]:
                        if obj.contains(mouse):
                            gotValidClick = True
                            mouse.clicked_name.append(obj.name)
                    x, y = mouse.getPos()
                    mouse.x.append(x)
                    mouse.y.append(y)
                    buttons = mouse.getPressed()
                    mouse.leftButton.append(buttons[0])
                    mouse.midButton.append(buttons[1])
                    mouse.rightButton.append(buttons[2])
                    mouse.time.append(mouse.mouseClock.getTime())
        for box in checkboxes:
            if mouse.isPressedIn(box) and box.name not in clicked:
                box.color = "black"
                clicked.append(box.name)
        
        
        if mouse.isPressedIn(text):
            continueRoutine = False
        
          
            
        
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Question1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Question1"-------
    for thisComponent in Question1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('image2346.started', image2346.tStartRefresh)
    trials.addData('image2346.stopped', image2346.tStopRefresh)
    trials.addData('text.started', text.tStartRefresh)
    trials.addData('text.stopped', text.tStopRefresh)
    trials.addData('box1.started', box1.tStartRefresh)
    trials.addData('box1.stopped', box1.tStopRefresh)
    trials.addData('box2.started', box2.tStartRefresh)
    trials.addData('box2.stopped', box2.tStopRefresh)
    trials.addData('box3.started', box3.tStartRefresh)
    trials.addData('box3.stopped', box3.tStopRefresh)
    trials.addData('box4.started', box4.tStartRefresh)
    trials.addData('box4.stopped', box4.tStopRefresh)
    # store data for trials (TrialHandler)
    trials.addData('mouse.x', mouse.x)
    trials.addData('mouse.y', mouse.y)
    trials.addData('mouse.leftButton', mouse.leftButton)
    trials.addData('mouse.midButton', mouse.midButton)
    trials.addData('mouse.rightButton', mouse.rightButton)
    trials.addData('mouse.time', mouse.time)
    trials.addData('mouse.clicked_name', mouse.clicked_name)
    trials.addData('mouse.started', mouse.tStart)
    trials.addData('mouse.stopped', mouse.tStop)
    correct=0
    for checkboxes in mouse.clicked_name:
        if checkboxes in corrAns:
            correct +=1
    trials.addData('correct', correct)
    # the Routine "Question1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "instr"-------
continueRoutine = True
# update component parameters for each repeat
stopIndicator.keys = []
stopIndicator.rt = []
_stopIndicator_allKeys = []
# keep track of which components have finished
instrComponents = [instrStop, stopIndicator]
for thisComponent in instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr"-------
while continueRoutine:
    # get current time
    t = instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrStop* updates
    if instrStop.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instrStop.frameNStart = frameN  # exact frame index
        instrStop.tStart = t  # local t and not account for scr refresh
        instrStop.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrStop, 'tStartRefresh')  # time at next scr refresh
        instrStop.setAutoDraw(True)
    
    # *stopIndicator* updates
    waitOnFlip = False
    if stopIndicator.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        stopIndicator.frameNStart = frameN  # exact frame index
        stopIndicator.tStart = t  # local t and not account for scr refresh
        stopIndicator.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(stopIndicator, 'tStartRefresh')  # time at next scr refresh
        stopIndicator.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(stopIndicator.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(stopIndicator.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if stopIndicator.status == STARTED and not waitOnFlip:
        theseKeys = stopIndicator.getKeys(keyList=['space'], waitRelease=False)
        _stopIndicator_allKeys.extend(theseKeys)
        if len(_stopIndicator_allKeys):
            stopIndicator.keys = _stopIndicator_allKeys[-1].name  # just the last key pressed
            stopIndicator.rt = _stopIndicator_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr"-------
for thisComponent in instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instrStop.started', instrStop.tStartRefresh)
thisExp.addData('instrStop.stopped', instrStop.tStopRefresh)
# the Routine "instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Part2"-------
continueRoutine = True
# update component parameters for each repeat
part2IndicatorResponse.keys = []
part2IndicatorResponse.rt = []
_part2IndicatorResponse_allKeys = []
# keep track of which components have finished
Part2Components = [part2Indicator, part2IndicatorResponse]
for thisComponent in Part2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Part2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Part2"-------
while continueRoutine:
    # get current time
    t = Part2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Part2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *part2Indicator* updates
    if part2Indicator.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        part2Indicator.frameNStart = frameN  # exact frame index
        part2Indicator.tStart = t  # local t and not account for scr refresh
        part2Indicator.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(part2Indicator, 'tStartRefresh')  # time at next scr refresh
        part2Indicator.setAutoDraw(True)
    
    # *part2IndicatorResponse* updates
    waitOnFlip = False
    if part2IndicatorResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        part2IndicatorResponse.frameNStart = frameN  # exact frame index
        part2IndicatorResponse.tStart = t  # local t and not account for scr refresh
        part2IndicatorResponse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(part2IndicatorResponse, 'tStartRefresh')  # time at next scr refresh
        part2IndicatorResponse.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(part2IndicatorResponse.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(part2IndicatorResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if part2IndicatorResponse.status == STARTED and not waitOnFlip:
        theseKeys = part2IndicatorResponse.getKeys(keyList=['space'], waitRelease=False)
        _part2IndicatorResponse_allKeys.extend(theseKeys)
        if len(_part2IndicatorResponse_allKeys):
            part2IndicatorResponse.keys = _part2IndicatorResponse_allKeys[-1].name  # just the last key pressed
            part2IndicatorResponse.rt = _part2IndicatorResponse_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Part2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Part2"-------
for thisComponent in Part2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('part2Indicator.started', part2Indicator.tStartRefresh)
thisExp.addData('part2Indicator.stopped', part2Indicator.tStopRefresh)
# the Routine "Part2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('part2QuestionsWay2.xlsx'),
    seed=None, name='trials2')
thisExp.addLoop(trials2)  # add the loop to the experiment
thisTrials2 = trials2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials2.rgb)
if thisTrials2 != None:
    for paramName in thisTrials2:
        exec('{} = thisTrials2[paramName]'.format(paramName))

for thisTrials2 in trials2:
    currentLoop = trials2
    # abbreviate parameter names if possible (e.g. rgb = thisTrials2.rgb)
    if thisTrials2 != None:
        for paramName in thisTrials2:
            exec('{} = thisTrials2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "part2Questions"-------
    continueRoutine = True
    # update component parameters for each repeat
    keyboardIndicator.keys = []
    keyboardIndicator.rt = []
    _keyboardIndicator_allKeys = []
    part2Images.setImage(image)
    box21.setFillColor('green')
    box22.setFillColor('green')
    box23.setFillColor('green')
    box24.setFillColor('green')
    # setup some python lists for storing info about the mouse2
    mouse2.x = []
    mouse2.y = []
    mouse2.leftButton = []
    mouse2.midButton = []
    mouse2.rightButton = []
    mouse2.time = []
    mouse2.clicked_name = []
    gotValidClick = False  # until a click is received
    checkboxes= [box21, box22, box23, box24]
    clicked  = []
    # keep track of which components have finished
    part2QuestionsComponents = [indicatorQuestionPart2, keyboardIndicator, part2Images, box21, box22, box23, box24, mouse2]
    for thisComponent in part2QuestionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    part2QuestionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "part2Questions"-------
    while continueRoutine:
        # get current time
        t = part2QuestionsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=part2QuestionsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *indicatorQuestionPart2* updates
        if indicatorQuestionPart2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            indicatorQuestionPart2.frameNStart = frameN  # exact frame index
            indicatorQuestionPart2.tStart = t  # local t and not account for scr refresh
            indicatorQuestionPart2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(indicatorQuestionPart2, 'tStartRefresh')  # time at next scr refresh
            indicatorQuestionPart2.setAutoDraw(True)
        
        # *keyboardIndicator* updates
        waitOnFlip = False
        if keyboardIndicator.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keyboardIndicator.frameNStart = frameN  # exact frame index
            keyboardIndicator.tStart = t  # local t and not account for scr refresh
            keyboardIndicator.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyboardIndicator, 'tStartRefresh')  # time at next scr refresh
            keyboardIndicator.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyboardIndicator.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyboardIndicator.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyboardIndicator.status == STARTED and not waitOnFlip:
            theseKeys = keyboardIndicator.getKeys(keyList=['space'], waitRelease=False)
            _keyboardIndicator_allKeys.extend(theseKeys)
            if len(_keyboardIndicator_allKeys):
                keyboardIndicator.keys = _keyboardIndicator_allKeys[-1].name  # just the last key pressed
                keyboardIndicator.rt = _keyboardIndicator_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *part2Images* updates
        if part2Images.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            part2Images.frameNStart = frameN  # exact frame index
            part2Images.tStart = t  # local t and not account for scr refresh
            part2Images.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(part2Images, 'tStartRefresh')  # time at next scr refresh
            part2Images.setAutoDraw(True)
        
        # *box21* updates
        if box21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            box21.frameNStart = frameN  # exact frame index
            box21.tStart = t  # local t and not account for scr refresh
            box21.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(box21, 'tStartRefresh')  # time at next scr refresh
            box21.setAutoDraw(True)
        
        # *box22* updates
        if box22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            box22.frameNStart = frameN  # exact frame index
            box22.tStart = t  # local t and not account for scr refresh
            box22.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(box22, 'tStartRefresh')  # time at next scr refresh
            box22.setAutoDraw(True)
        
        # *box23* updates
        if box23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            box23.frameNStart = frameN  # exact frame index
            box23.tStart = t  # local t and not account for scr refresh
            box23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(box23, 'tStartRefresh')  # time at next scr refresh
            box23.setAutoDraw(True)
        
        # *box24* updates
        if box24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            box24.frameNStart = frameN  # exact frame index
            box24.tStart = t  # local t and not account for scr refresh
            box24.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(box24, 'tStartRefresh')  # time at next scr refresh
            box24.setAutoDraw(True)
        # *mouse2* updates
        if mouse2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse2.frameNStart = frameN  # exact frame index
            mouse2.tStart = t  # local t and not account for scr refresh
            mouse2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse2, 'tStartRefresh')  # time at next scr refresh
            mouse2.status = STARTED
            mouse2.mouseClock.reset()
            prevButtonState = mouse2.getPressed()  # if button is down already this ISN'T a new click
        if mouse2.status == STARTED:  # only update if started and not finished!
            buttons = mouse2.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [box21, box22, box23, box24]:
                        if obj.contains(mouse2):
                            gotValidClick = True
                            mouse2.clicked_name.append(obj.name)
                    x, y = mouse2.getPos()
                    mouse2.x.append(x)
                    mouse2.y.append(y)
                    buttons = mouse2.getPressed()
                    mouse2.leftButton.append(buttons[0])
                    mouse2.midButton.append(buttons[1])
                    mouse2.rightButton.append(buttons[2])
                    mouse2.time.append(mouse2.mouseClock.getTime())
        for box in checkboxes:
            if mouse2.isPressedIn(box) and box.name not in clicked:
                box.color = "black"
                clicked.append(box.name)
        
        if mouse2.isPressedIn(text):
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in part2QuestionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "part2Questions"-------
    for thisComponent in part2QuestionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials2.addData('indicatorQuestionPart2.started', indicatorQuestionPart2.tStartRefresh)
    trials2.addData('indicatorQuestionPart2.stopped', indicatorQuestionPart2.tStopRefresh)
    trials2.addData('part2Images.started', part2Images.tStartRefresh)
    trials2.addData('part2Images.stopped', part2Images.tStopRefresh)
    trials2.addData('box21.started', box21.tStartRefresh)
    trials2.addData('box21.stopped', box21.tStopRefresh)
    trials2.addData('box22.started', box22.tStartRefresh)
    trials2.addData('box22.stopped', box22.tStopRefresh)
    trials2.addData('box23.started', box23.tStartRefresh)
    trials2.addData('box23.stopped', box23.tStopRefresh)
    trials2.addData('box24.started', box24.tStartRefresh)
    trials2.addData('box24.stopped', box24.tStopRefresh)
    # store data for trials2 (TrialHandler)
    trials2.addData('mouse2.x', mouse2.x)
    trials2.addData('mouse2.y', mouse2.y)
    trials2.addData('mouse2.leftButton', mouse2.leftButton)
    trials2.addData('mouse2.midButton', mouse2.midButton)
    trials2.addData('mouse2.rightButton', mouse2.rightButton)
    trials2.addData('mouse2.time', mouse2.time)
    trials2.addData('mouse2.clicked_name', mouse2.clicked_name)
    trials2.addData('mouse2.started', mouse2.tStart)
    trials2.addData('mouse2.stopped', mouse2.tStop)
    correct=0
    for checkboxes in mouse2.clicked_name:
        if checkboxes in corrAns2:
            correct +=1
    trials.addData('correct', correct)
    # the Routine "part2Questions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials2'

# get names of stimulus parameters
if trials2.trialList in ([], [None], None):
    params = []
else:
    params = trials2.trialList[0].keys()
# save data for this loop
trials2.saveAsExcel(filename + '.xlsx', sheetName='trials2',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "End"-------
continueRoutine = True
# update component parameters for each repeat
endResponse.keys = []
endResponse.rt = []
_endResponse_allKeys = []
# keep track of which components have finished
EndComponents = [EndScreen, endResponse]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "End"-------
while continueRoutine:
    # get current time
    t = EndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *EndScreen* updates
    if EndScreen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EndScreen.frameNStart = frameN  # exact frame index
        EndScreen.tStart = t  # local t and not account for scr refresh
        EndScreen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EndScreen, 'tStartRefresh')  # time at next scr refresh
        EndScreen.setAutoDraw(True)
    
    # *endResponse* updates
    waitOnFlip = False
    if endResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endResponse.frameNStart = frameN  # exact frame index
        endResponse.tStart = t  # local t and not account for scr refresh
        endResponse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endResponse, 'tStartRefresh')  # time at next scr refresh
        endResponse.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(endResponse.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(endResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if endResponse.status == STARTED and not waitOnFlip:
        theseKeys = endResponse.getKeys(keyList=None, waitRelease=False)
        _endResponse_allKeys.extend(theseKeys)
        if len(_endResponse_allKeys):
            endResponse.keys = _endResponse_allKeys[-1].name  # just the last key pressed
            endResponse.rt = _endResponse_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('EndScreen.started', EndScreen.tStartRefresh)
thisExp.addData('EndScreen.stopped', EndScreen.tStopRefresh)
# the Routine "End" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
