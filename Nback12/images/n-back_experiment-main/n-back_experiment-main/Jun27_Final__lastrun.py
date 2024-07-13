#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.1.4),
    on Mon Jul  8 22:31:05 2024
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
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from code_condition
import random

# 变量定义
n_values = [2, 2, 1]
i = 1
image_lists = [
    ['01.png', '02.png', '03.png', '04.png', '05.png', '06.png', '07.png', '08.png', '09.png', '10.png', '11.png', '12.png', '13.png', '14.png', '15.png', '16.png', '17.png', '18.png'],
    ["01.png", "02.png", "03.png", "04.png", "05.png", "06.png", "07.png", "08.png", "09.png"]
]
fixation_lists = [
    ['up.png', 'down.png', 'left.png', 'right.png', 'center.png', 'lu.png', 'ru.png', 'ld.png', 'rd.png'],
    ['center.png']
]

# 生成所有条件的列表
conditions = []
for n in n_values:
    for image_list in image_lists:
        for fixation_list in fixation_lists:
            conditions.append((i, n, image_list, fixation_list))
            i = i + 1
print(conditions)
# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.1.4'
expName = 'N-BACK_primary'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': '',
    '年级': '',
    '班级': '',
    '性别': '',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1440, 900]
_loggingLevel = logging.getLevel('exp')
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # override logging level
    _loggingLevel = logging.getLevel(
        prefs.piloting['pilotLoggingLevel']
    )

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'],expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/Users/yangyiwei/Desktop/stu/bme大赛/n-back_experiment-main/Jun27_Final__lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(_loggingLevel)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=_loggingLevel)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[0.0000, 0.0000, 0.0000], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='pix', 
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0.0000, 0.0000, 0.0000]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'pix'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.mouseVisible = False
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('key_resp') is None:
        # initialise key_resp
        key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp',
        )
    if deviceManager.getDevice('key_resp_6') is None:
        # initialise key_resp_6
        key_resp_6 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_6',
        )
    if deviceManager.getDevice('key_resp_2') is None:
        # initialise key_resp_2
        key_resp_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_2',
        )
    # create speaker 'sound_true'
    deviceManager.addDevice(
        deviceName='sound_true',
        deviceClass='psychopy.hardware.speaker.SpeakerDevice',
        index=-1
    )
    # create speaker 'sound_false'
    deviceManager.addDevice(
        deviceName='sound_false',
        deviceClass='psychopy.hardware.speaker.SpeakerDevice',
        index=-1
    )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "InsFrame" ---
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    ins_start = visual.ImageStim(
        win=win,
        name='ins_start', 
        image='ins700x350.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(700, 350),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    
    # --- Initialize components for Routine "prepare" ---
    key_resp_6 = keyboard.Keyboard(deviceName='key_resp_6')
    ins_1back = visual.ImageStim(
        win=win,
        name='ins_1back', 
        image='ins_1-back_700x350.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(700, 350),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    ins_2back = visual.ImageStim(
        win=win,
        name='ins_2back', 
        image='ins_2-back_700x350.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(700, 350),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    pic_01png_2 = visual.ImageStim(
        win=win,
        name='pic_01png_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-100, 0), size=(70, 70),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    pic_02png_2 = visual.ImageStim(
        win=win,
        name='pic_02png_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(100, 0), size=(70, 70),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    
    # --- Initialize components for Routine "Stim" ---
    image_bac = visual.ImageStim(
        win=win,
        name='image_bac', 
        image='background_grey.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(500, 500),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    n_value = visual.TextStim(win=win, name='n_value',
        text='',
        font=None,
        pos=(0, 275), height=20.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=-2.0);
    num = visual.TextStim(win=win, name='num',
        text='No.',
        font='Open Sans',
        pos=(-45, 275), height=20.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    testnum = visual.TextStim(win=win, name='testnum',
        text='',
        font='Open Sans',
        pos=(-20, 275), height=20.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    thisimage = visual.ImageStim(
        win=win,
        name='thisimage', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(60, 60),
        color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    sound_true = sound.Sound(
        'A', 
        secs=0.1, 
        stereo=True, 
        hamming=True, 
        speaker='sound_true',    name='sound_true'
    )
    sound_true.setVolume(2.0)
    sound_false = sound.Sound(
        'A', 
        secs=0.2, 
        stereo=True, 
        hamming=False, 
        speaker='sound_false',    name='sound_false'
    )
    sound_false.setVolume(1.0)
    
    # --- Initialize components for Routine "feedback" ---
    image_bac_2 = visual.ImageStim(
        win=win,
        name='image_bac_2', 
        image='background_grey.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(500, 500),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    # Run 'Begin Experiment' code from feedback_code
    msg = ''
    msgcolor = ''
    ntext = '' 
    ncolor=''
    
    msg_response = visual.TextStim(win=win, name='msg_response',
        text='',
        font='simsong',
        pos=(0, 275), height=30.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    fixation_img = visual.ImageStim(
        win=win,
        name='fixation_img', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(30, 30),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    
    # --- Initialize components for Routine "prepare" ---
    key_resp_6 = keyboard.Keyboard(deviceName='key_resp_6')
    ins_1back = visual.ImageStim(
        win=win,
        name='ins_1back', 
        image='ins_1-back_700x350.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(700, 350),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    ins_2back = visual.ImageStim(
        win=win,
        name='ins_2back', 
        image='ins_2-back_700x350.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(700, 350),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    pic_01png_2 = visual.ImageStim(
        win=win,
        name='pic_01png_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-100, 0), size=(70, 70),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    pic_02png_2 = visual.ImageStim(
        win=win,
        name='pic_02png_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(100, 0), size=(70, 70),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    
    # --- Initialize components for Routine "Stim" ---
    image_bac = visual.ImageStim(
        win=win,
        name='image_bac', 
        image='background_grey.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(500, 500),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    n_value = visual.TextStim(win=win, name='n_value',
        text='',
        font=None,
        pos=(0, 275), height=20.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=-2.0);
    num = visual.TextStim(win=win, name='num',
        text='No.',
        font='Open Sans',
        pos=(-45, 275), height=20.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    testnum = visual.TextStim(win=win, name='testnum',
        text='',
        font='Open Sans',
        pos=(-20, 275), height=20.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    thisimage = visual.ImageStim(
        win=win,
        name='thisimage', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(60, 60),
        color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    sound_true = sound.Sound(
        'A', 
        secs=0.1, 
        stereo=True, 
        hamming=True, 
        speaker='sound_true',    name='sound_true'
    )
    sound_true.setVolume(2.0)
    sound_false = sound.Sound(
        'A', 
        secs=0.2, 
        stereo=True, 
        hamming=False, 
        speaker='sound_false',    name='sound_false'
    )
    sound_false.setVolume(1.0)
    
    # --- Initialize components for Routine "feedback" ---
    image_bac_2 = visual.ImageStim(
        win=win,
        name='image_bac_2', 
        image='background_grey.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(500, 500),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    # Run 'Begin Experiment' code from feedback_code
    msg = ''
    msgcolor = ''
    ntext = '' 
    ncolor=''
    
    msg_response = visual.TextStim(win=win, name='msg_response',
        text='',
        font='simsong',
        pos=(0, 275), height=30.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    fixation_img = visual.ImageStim(
        win=win,
        name='fixation_img', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(30, 30),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    
    # --- Initialize components for Routine "prepare" ---
    key_resp_6 = keyboard.Keyboard(deviceName='key_resp_6')
    ins_1back = visual.ImageStim(
        win=win,
        name='ins_1back', 
        image='ins_1-back_700x350.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(700, 350),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    ins_2back = visual.ImageStim(
        win=win,
        name='ins_2back', 
        image='ins_2-back_700x350.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(700, 350),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    pic_01png_2 = visual.ImageStim(
        win=win,
        name='pic_01png_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-100, 0), size=(70, 70),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    pic_02png_2 = visual.ImageStim(
        win=win,
        name='pic_02png_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(100, 0), size=(70, 70),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    
    # --- Initialize components for Routine "Stim" ---
    image_bac = visual.ImageStim(
        win=win,
        name='image_bac', 
        image='background_grey.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(500, 500),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    n_value = visual.TextStim(win=win, name='n_value',
        text='',
        font=None,
        pos=(0, 275), height=20.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=-2.0);
    num = visual.TextStim(win=win, name='num',
        text='No.',
        font='Open Sans',
        pos=(-45, 275), height=20.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    testnum = visual.TextStim(win=win, name='testnum',
        text='',
        font='Open Sans',
        pos=(-20, 275), height=20.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    thisimage = visual.ImageStim(
        win=win,
        name='thisimage', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(60, 60),
        color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    sound_true = sound.Sound(
        'A', 
        secs=0.1, 
        stereo=True, 
        hamming=True, 
        speaker='sound_true',    name='sound_true'
    )
    sound_true.setVolume(2.0)
    sound_false = sound.Sound(
        'A', 
        secs=0.2, 
        stereo=True, 
        hamming=False, 
        speaker='sound_false',    name='sound_false'
    )
    sound_false.setVolume(1.0)
    
    # --- Initialize components for Routine "feedback" ---
    image_bac_2 = visual.ImageStim(
        win=win,
        name='image_bac_2', 
        image='background_grey.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(500, 500),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    # Run 'Begin Experiment' code from feedback_code
    msg = ''
    msgcolor = ''
    ntext = '' 
    ncolor=''
    
    msg_response = visual.TextStim(win=win, name='msg_response',
        text='',
        font='simsong',
        pos=(0, 275), height=30.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    fixation_img = visual.ImageStim(
        win=win,
        name='fixation_img', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(30, 30),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    
    # --- Initialize components for Routine "prepare" ---
    key_resp_6 = keyboard.Keyboard(deviceName='key_resp_6')
    ins_1back = visual.ImageStim(
        win=win,
        name='ins_1back', 
        image='ins_1-back_700x350.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(700, 350),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    ins_2back = visual.ImageStim(
        win=win,
        name='ins_2back', 
        image='ins_2-back_700x350.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(700, 350),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    pic_01png_2 = visual.ImageStim(
        win=win,
        name='pic_01png_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-100, 0), size=(70, 70),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    pic_02png_2 = visual.ImageStim(
        win=win,
        name='pic_02png_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(100, 0), size=(70, 70),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    
    # --- Initialize components for Routine "Stim" ---
    image_bac = visual.ImageStim(
        win=win,
        name='image_bac', 
        image='background_grey.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(500, 500),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    n_value = visual.TextStim(win=win, name='n_value',
        text='',
        font=None,
        pos=(0, 275), height=20.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=-2.0);
    num = visual.TextStim(win=win, name='num',
        text='No.',
        font='Open Sans',
        pos=(-45, 275), height=20.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    testnum = visual.TextStim(win=win, name='testnum',
        text='',
        font='Open Sans',
        pos=(-20, 275), height=20.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    thisimage = visual.ImageStim(
        win=win,
        name='thisimage', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(60, 60),
        color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    sound_true = sound.Sound(
        'A', 
        secs=0.1, 
        stereo=True, 
        hamming=True, 
        speaker='sound_true',    name='sound_true'
    )
    sound_true.setVolume(2.0)
    sound_false = sound.Sound(
        'A', 
        secs=0.2, 
        stereo=True, 
        hamming=False, 
        speaker='sound_false',    name='sound_false'
    )
    sound_false.setVolume(1.0)
    
    # --- Initialize components for Routine "feedback" ---
    image_bac_2 = visual.ImageStim(
        win=win,
        name='image_bac_2', 
        image='background_grey.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(500, 500),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    # Run 'Begin Experiment' code from feedback_code
    msg = ''
    msgcolor = ''
    ntext = '' 
    ncolor=''
    
    msg_response = visual.TextStim(win=win, name='msg_response',
        text='',
        font='simsong',
        pos=(0, 275), height=30.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    fixation_img = visual.ImageStim(
        win=win,
        name='fixation_img', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(30, 30),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    
    # --- Initialize components for Routine "prepare" ---
    key_resp_6 = keyboard.Keyboard(deviceName='key_resp_6')
    ins_1back = visual.ImageStim(
        win=win,
        name='ins_1back', 
        image='ins_1-back_700x350.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(700, 350),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    ins_2back = visual.ImageStim(
        win=win,
        name='ins_2back', 
        image='ins_2-back_700x350.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(700, 350),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    pic_01png_2 = visual.ImageStim(
        win=win,
        name='pic_01png_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-100, 0), size=(70, 70),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    pic_02png_2 = visual.ImageStim(
        win=win,
        name='pic_02png_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(100, 0), size=(70, 70),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    
    # --- Initialize components for Routine "Stim" ---
    image_bac = visual.ImageStim(
        win=win,
        name='image_bac', 
        image='background_grey.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(500, 500),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    n_value = visual.TextStim(win=win, name='n_value',
        text='',
        font=None,
        pos=(0, 275), height=20.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=-2.0);
    num = visual.TextStim(win=win, name='num',
        text='No.',
        font='Open Sans',
        pos=(-45, 275), height=20.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    testnum = visual.TextStim(win=win, name='testnum',
        text='',
        font='Open Sans',
        pos=(-20, 275), height=20.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    thisimage = visual.ImageStim(
        win=win,
        name='thisimage', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(60, 60),
        color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    sound_true = sound.Sound(
        'A', 
        secs=0.1, 
        stereo=True, 
        hamming=True, 
        speaker='sound_true',    name='sound_true'
    )
    sound_true.setVolume(2.0)
    sound_false = sound.Sound(
        'A', 
        secs=0.2, 
        stereo=True, 
        hamming=False, 
        speaker='sound_false',    name='sound_false'
    )
    sound_false.setVolume(1.0)
    
    # --- Initialize components for Routine "feedback" ---
    image_bac_2 = visual.ImageStim(
        win=win,
        name='image_bac_2', 
        image='background_grey.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(500, 500),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    # Run 'Begin Experiment' code from feedback_code
    msg = ''
    msgcolor = ''
    ntext = '' 
    ncolor=''
    
    msg_response = visual.TextStim(win=win, name='msg_response',
        text='',
        font='simsong',
        pos=(0, 275), height=30.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    fixation_img = visual.ImageStim(
        win=win,
        name='fixation_img', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(30, 30),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    
    # --- Initialize components for Routine "prepare" ---
    key_resp_6 = keyboard.Keyboard(deviceName='key_resp_6')
    ins_1back = visual.ImageStim(
        win=win,
        name='ins_1back', 
        image='ins_1-back_700x350.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(700, 350),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    ins_2back = visual.ImageStim(
        win=win,
        name='ins_2back', 
        image='ins_2-back_700x350.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(700, 350),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    pic_01png_2 = visual.ImageStim(
        win=win,
        name='pic_01png_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-100, 0), size=(70, 70),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    pic_02png_2 = visual.ImageStim(
        win=win,
        name='pic_02png_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(100, 0), size=(70, 70),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    
    # --- Initialize components for Routine "Stim" ---
    image_bac = visual.ImageStim(
        win=win,
        name='image_bac', 
        image='background_grey.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(500, 500),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    n_value = visual.TextStim(win=win, name='n_value',
        text='',
        font=None,
        pos=(0, 275), height=20.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=-2.0);
    num = visual.TextStim(win=win, name='num',
        text='No.',
        font='Open Sans',
        pos=(-45, 275), height=20.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    testnum = visual.TextStim(win=win, name='testnum',
        text='',
        font='Open Sans',
        pos=(-20, 275), height=20.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    thisimage = visual.ImageStim(
        win=win,
        name='thisimage', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(60, 60),
        color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    sound_true = sound.Sound(
        'A', 
        secs=0.1, 
        stereo=True, 
        hamming=True, 
        speaker='sound_true',    name='sound_true'
    )
    sound_true.setVolume(2.0)
    sound_false = sound.Sound(
        'A', 
        secs=0.2, 
        stereo=True, 
        hamming=False, 
        speaker='sound_false',    name='sound_false'
    )
    sound_false.setVolume(1.0)
    
    # --- Initialize components for Routine "feedback" ---
    image_bac_2 = visual.ImageStim(
        win=win,
        name='image_bac_2', 
        image='background_grey.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(500, 500),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    # Run 'Begin Experiment' code from feedback_code
    msg = ''
    msgcolor = ''
    ntext = '' 
    ncolor=''
    
    msg_response = visual.TextStim(win=win, name='msg_response',
        text='',
        font='simsong',
        pos=(0, 275), height=30.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    fixation_img = visual.ImageStim(
        win=win,
        name='fixation_img', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(30, 30),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    
    # --- Initialize components for Routine "prepare" ---
    key_resp_6 = keyboard.Keyboard(deviceName='key_resp_6')
    ins_1back = visual.ImageStim(
        win=win,
        name='ins_1back', 
        image='ins_1-back_700x350.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(700, 350),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    ins_2back = visual.ImageStim(
        win=win,
        name='ins_2back', 
        image='ins_2-back_700x350.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(700, 350),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    pic_01png_2 = visual.ImageStim(
        win=win,
        name='pic_01png_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-100, 0), size=(70, 70),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    pic_02png_2 = visual.ImageStim(
        win=win,
        name='pic_02png_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(100, 0), size=(70, 70),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    
    # --- Initialize components for Routine "Stim" ---
    image_bac = visual.ImageStim(
        win=win,
        name='image_bac', 
        image='background_grey.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(500, 500),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    n_value = visual.TextStim(win=win, name='n_value',
        text='',
        font=None,
        pos=(0, 275), height=20.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=-2.0);
    num = visual.TextStim(win=win, name='num',
        text='No.',
        font='Open Sans',
        pos=(-45, 275), height=20.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    testnum = visual.TextStim(win=win, name='testnum',
        text='',
        font='Open Sans',
        pos=(-20, 275), height=20.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    thisimage = visual.ImageStim(
        win=win,
        name='thisimage', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(60, 60),
        color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    sound_true = sound.Sound(
        'A', 
        secs=0.1, 
        stereo=True, 
        hamming=True, 
        speaker='sound_true',    name='sound_true'
    )
    sound_true.setVolume(2.0)
    sound_false = sound.Sound(
        'A', 
        secs=0.2, 
        stereo=True, 
        hamming=False, 
        speaker='sound_false',    name='sound_false'
    )
    sound_false.setVolume(1.0)
    
    # --- Initialize components for Routine "feedback" ---
    image_bac_2 = visual.ImageStim(
        win=win,
        name='image_bac_2', 
        image='background_grey.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(500, 500),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    # Run 'Begin Experiment' code from feedback_code
    msg = ''
    msgcolor = ''
    ntext = '' 
    ncolor=''
    
    msg_response = visual.TextStim(win=win, name='msg_response',
        text='',
        font='simsong',
        pos=(0, 275), height=30.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    fixation_img = visual.ImageStim(
        win=win,
        name='fixation_img', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(30, 30),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    
    # --- Initialize components for Routine "prepare" ---
    key_resp_6 = keyboard.Keyboard(deviceName='key_resp_6')
    ins_1back = visual.ImageStim(
        win=win,
        name='ins_1back', 
        image='ins_1-back_700x350.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(700, 350),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    ins_2back = visual.ImageStim(
        win=win,
        name='ins_2back', 
        image='ins_2-back_700x350.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(700, 350),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    pic_01png_2 = visual.ImageStim(
        win=win,
        name='pic_01png_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-100, 0), size=(70, 70),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    pic_02png_2 = visual.ImageStim(
        win=win,
        name='pic_02png_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(100, 0), size=(70, 70),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    
    # --- Initialize components for Routine "Stim" ---
    image_bac = visual.ImageStim(
        win=win,
        name='image_bac', 
        image='background_grey.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(500, 500),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    n_value = visual.TextStim(win=win, name='n_value',
        text='',
        font=None,
        pos=(0, 275), height=20.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=-2.0);
    num = visual.TextStim(win=win, name='num',
        text='No.',
        font='Open Sans',
        pos=(-45, 275), height=20.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    testnum = visual.TextStim(win=win, name='testnum',
        text='',
        font='Open Sans',
        pos=(-20, 275), height=20.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    thisimage = visual.ImageStim(
        win=win,
        name='thisimage', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(60, 60),
        color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    sound_true = sound.Sound(
        'A', 
        secs=0.1, 
        stereo=True, 
        hamming=True, 
        speaker='sound_true',    name='sound_true'
    )
    sound_true.setVolume(2.0)
    sound_false = sound.Sound(
        'A', 
        secs=0.2, 
        stereo=True, 
        hamming=False, 
        speaker='sound_false',    name='sound_false'
    )
    sound_false.setVolume(1.0)
    
    # --- Initialize components for Routine "feedback" ---
    image_bac_2 = visual.ImageStim(
        win=win,
        name='image_bac_2', 
        image='background_grey.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(500, 500),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    # Run 'Begin Experiment' code from feedback_code
    msg = ''
    msgcolor = ''
    ntext = '' 
    ncolor=''
    
    msg_response = visual.TextStim(win=win, name='msg_response',
        text='',
        font='simsong',
        pos=(0, 275), height=30.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    fixation_img = visual.ImageStim(
        win=win,
        name='fixation_img', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(30, 30),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    
    # --- Initialize components for Routine "prepare" ---
    key_resp_6 = keyboard.Keyboard(deviceName='key_resp_6')
    ins_1back = visual.ImageStim(
        win=win,
        name='ins_1back', 
        image='ins_1-back_700x350.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(700, 350),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    ins_2back = visual.ImageStim(
        win=win,
        name='ins_2back', 
        image='ins_2-back_700x350.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(700, 350),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    pic_01png_2 = visual.ImageStim(
        win=win,
        name='pic_01png_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-100, 0), size=(70, 70),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    pic_02png_2 = visual.ImageStim(
        win=win,
        name='pic_02png_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(100, 0), size=(70, 70),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    
    # --- Initialize components for Routine "Stim" ---
    image_bac = visual.ImageStim(
        win=win,
        name='image_bac', 
        image='background_grey.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(500, 500),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    n_value = visual.TextStim(win=win, name='n_value',
        text='',
        font=None,
        pos=(0, 275), height=20.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=-2.0);
    num = visual.TextStim(win=win, name='num',
        text='No.',
        font='Open Sans',
        pos=(-45, 275), height=20.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    testnum = visual.TextStim(win=win, name='testnum',
        text='',
        font='Open Sans',
        pos=(-20, 275), height=20.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    thisimage = visual.ImageStim(
        win=win,
        name='thisimage', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(60, 60),
        color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    sound_true = sound.Sound(
        'A', 
        secs=0.1, 
        stereo=True, 
        hamming=True, 
        speaker='sound_true',    name='sound_true'
    )
    sound_true.setVolume(2.0)
    sound_false = sound.Sound(
        'A', 
        secs=0.2, 
        stereo=True, 
        hamming=False, 
        speaker='sound_false',    name='sound_false'
    )
    sound_false.setVolume(1.0)
    
    # --- Initialize components for Routine "feedback" ---
    image_bac_2 = visual.ImageStim(
        win=win,
        name='image_bac_2', 
        image='background_grey.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(500, 500),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    # Run 'Begin Experiment' code from feedback_code
    msg = ''
    msgcolor = ''
    ntext = '' 
    ncolor=''
    
    msg_response = visual.TextStim(win=win, name='msg_response',
        text='',
        font='simsong',
        pos=(0, 275), height=30.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    fixation_img = visual.ImageStim(
        win=win,
        name='fixation_img', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(30, 30),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    
    # --- Initialize components for Routine "prepare" ---
    key_resp_6 = keyboard.Keyboard(deviceName='key_resp_6')
    ins_1back = visual.ImageStim(
        win=win,
        name='ins_1back', 
        image='ins_1-back_700x350.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(700, 350),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    ins_2back = visual.ImageStim(
        win=win,
        name='ins_2back', 
        image='ins_2-back_700x350.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(700, 350),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    pic_01png_2 = visual.ImageStim(
        win=win,
        name='pic_01png_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-100, 0), size=(70, 70),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    pic_02png_2 = visual.ImageStim(
        win=win,
        name='pic_02png_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(100, 0), size=(70, 70),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    
    # --- Initialize components for Routine "Stim" ---
    image_bac = visual.ImageStim(
        win=win,
        name='image_bac', 
        image='background_grey.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(500, 500),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    n_value = visual.TextStim(win=win, name='n_value',
        text='',
        font=None,
        pos=(0, 275), height=20.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=-2.0);
    num = visual.TextStim(win=win, name='num',
        text='No.',
        font='Open Sans',
        pos=(-45, 275), height=20.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    testnum = visual.TextStim(win=win, name='testnum',
        text='',
        font='Open Sans',
        pos=(-20, 275), height=20.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    thisimage = visual.ImageStim(
        win=win,
        name='thisimage', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(60, 60),
        color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    sound_true = sound.Sound(
        'A', 
        secs=0.1, 
        stereo=True, 
        hamming=True, 
        speaker='sound_true',    name='sound_true'
    )
    sound_true.setVolume(2.0)
    sound_false = sound.Sound(
        'A', 
        secs=0.2, 
        stereo=True, 
        hamming=False, 
        speaker='sound_false',    name='sound_false'
    )
    sound_false.setVolume(1.0)
    
    # --- Initialize components for Routine "feedback" ---
    image_bac_2 = visual.ImageStim(
        win=win,
        name='image_bac_2', 
        image='background_grey.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(500, 500),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    # Run 'Begin Experiment' code from feedback_code
    msg = ''
    msgcolor = ''
    ntext = '' 
    ncolor=''
    
    msg_response = visual.TextStim(win=win, name='msg_response',
        text='',
        font='simsong',
        pos=(0, 275), height=30.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    fixation_img = visual.ImageStim(
        win=win,
        name='fixation_img', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(30, 30),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    
    # --- Initialize components for Routine "prepare" ---
    key_resp_6 = keyboard.Keyboard(deviceName='key_resp_6')
    ins_1back = visual.ImageStim(
        win=win,
        name='ins_1back', 
        image='ins_1-back_700x350.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(700, 350),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    ins_2back = visual.ImageStim(
        win=win,
        name='ins_2back', 
        image='ins_2-back_700x350.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(700, 350),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    pic_01png_2 = visual.ImageStim(
        win=win,
        name='pic_01png_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-100, 0), size=(70, 70),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    pic_02png_2 = visual.ImageStim(
        win=win,
        name='pic_02png_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(100, 0), size=(70, 70),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    
    # --- Initialize components for Routine "Stim" ---
    image_bac = visual.ImageStim(
        win=win,
        name='image_bac', 
        image='background_grey.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(500, 500),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    n_value = visual.TextStim(win=win, name='n_value',
        text='',
        font=None,
        pos=(0, 275), height=20.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=-2.0);
    num = visual.TextStim(win=win, name='num',
        text='No.',
        font='Open Sans',
        pos=(-45, 275), height=20.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    testnum = visual.TextStim(win=win, name='testnum',
        text='',
        font='Open Sans',
        pos=(-20, 275), height=20.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    thisimage = visual.ImageStim(
        win=win,
        name='thisimage', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(60, 60),
        color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    sound_true = sound.Sound(
        'A', 
        secs=0.1, 
        stereo=True, 
        hamming=True, 
        speaker='sound_true',    name='sound_true'
    )
    sound_true.setVolume(2.0)
    sound_false = sound.Sound(
        'A', 
        secs=0.2, 
        stereo=True, 
        hamming=False, 
        speaker='sound_false',    name='sound_false'
    )
    sound_false.setVolume(1.0)
    
    # --- Initialize components for Routine "feedback" ---
    image_bac_2 = visual.ImageStim(
        win=win,
        name='image_bac_2', 
        image='background_grey.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(500, 500),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    # Run 'Begin Experiment' code from feedback_code
    msg = ''
    msgcolor = ''
    ntext = '' 
    ncolor=''
    
    msg_response = visual.TextStim(win=win, name='msg_response',
        text='',
        font='simsong',
        pos=(0, 275), height=30.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    fixation_img = visual.ImageStim(
        win=win,
        name='fixation_img', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(30, 30),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    
    # --- Initialize components for Routine "prepare" ---
    key_resp_6 = keyboard.Keyboard(deviceName='key_resp_6')
    ins_1back = visual.ImageStim(
        win=win,
        name='ins_1back', 
        image='ins_1-back_700x350.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(700, 350),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    ins_2back = visual.ImageStim(
        win=win,
        name='ins_2back', 
        image='ins_2-back_700x350.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(700, 350),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    pic_01png_2 = visual.ImageStim(
        win=win,
        name='pic_01png_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-100, 0), size=(70, 70),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    pic_02png_2 = visual.ImageStim(
        win=win,
        name='pic_02png_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(100, 0), size=(70, 70),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    
    # --- Initialize components for Routine "Stim" ---
    image_bac = visual.ImageStim(
        win=win,
        name='image_bac', 
        image='background_grey.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(500, 500),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    n_value = visual.TextStim(win=win, name='n_value',
        text='',
        font=None,
        pos=(0, 275), height=20.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=-2.0);
    num = visual.TextStim(win=win, name='num',
        text='No.',
        font='Open Sans',
        pos=(-45, 275), height=20.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    testnum = visual.TextStim(win=win, name='testnum',
        text='',
        font='Open Sans',
        pos=(-20, 275), height=20.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    thisimage = visual.ImageStim(
        win=win,
        name='thisimage', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(60, 60),
        color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    sound_true = sound.Sound(
        'A', 
        secs=0.1, 
        stereo=True, 
        hamming=True, 
        speaker='sound_true',    name='sound_true'
    )
    sound_true.setVolume(2.0)
    sound_false = sound.Sound(
        'A', 
        secs=0.2, 
        stereo=True, 
        hamming=False, 
        speaker='sound_false',    name='sound_false'
    )
    sound_false.setVolume(1.0)
    
    # --- Initialize components for Routine "feedback" ---
    image_bac_2 = visual.ImageStim(
        win=win,
        name='image_bac_2', 
        image='background_grey.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(500, 500),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    # Run 'Begin Experiment' code from feedback_code
    msg = ''
    msgcolor = ''
    ntext = '' 
    ncolor=''
    
    msg_response = visual.TextStim(win=win, name='msg_response',
        text='',
        font='simsong',
        pos=(0, 275), height=30.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    fixation_img = visual.ImageStim(
        win=win,
        name='fixation_img', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(30, 30),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "InsFrame" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('InsFrame.started', globalClock.getTime(format='float'))
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    InsFrameComponents = [key_resp, ins_start]
    for thisComponent in InsFrameComponents:
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
    
    # --- Run Routine "InsFrame" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp* updates
        waitOnFlip = False
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            # update status
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                key_resp.duration = _key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *ins_start* updates
        
        # if ins_start is starting this frame...
        if ins_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ins_start.frameNStart = frameN  # exact frame index
            ins_start.tStart = t  # local t and not account for scr refresh
            ins_start.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ins_start, 'tStartRefresh')  # time at next scr refresh
            # update status
            ins_start.status = STARTED
            ins_start.setAutoDraw(True)
        
        # if ins_start is active this frame...
        if ins_start.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InsFrameComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "InsFrame" ---
    for thisComponent in InsFrameComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('InsFrame.stopped', globalClock.getTime(format='float'))
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    thisExp.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        thisExp.addData('key_resp.rt', key_resp.rt)
        thisExp.addData('key_resp.duration', key_resp.duration)
    thisExp.nextEntry()
    # the Routine "InsFrame" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "prepare" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('prepare.started', globalClock.getTime(format='float'))
    # Run 'Begin Routine' code from anslist_code
    # set environment
    numcount = 1
    num_i = 0
    piccenpos_cr = [166, 0, -166]
    piccenpos_ar = [166, 0, -166]
    
    # select condition
    condition = conditions.pop()
    i, n, image_list, fixation_list = condition
    num_i = i
    
    # add condition details to data document
    condi = {
        'i=': i,
        'n=': n,
        'len=': len(image_list),
        'fix=': len(fixation_list)
    }
    thisExp.addData('condition', condi)
    print('第',i,'组','N值', n, '图表长度', len(image_list), '注视点表长度', len(fixation_list))
    
    # analyze the image list
    pre_img = []
    rom_imgs = image_list.copy()
    for _ in range(n):
        temp = random.choice(rom_imgs)
        pre_img.append(temp)
        rom_imgs.remove(temp)
    
    # 生成匹配刺激列表 match_list
    match_list = []
    ram = range(9 * n)
    for _ in ram:
        match_image = random.choice(image_list)
        match_list.append([match_image, match_image])
    for item in match_list:
        temp = image_list.copy()
        n1 = n
        while n1 > 1:
            temp.remove(item[n - n1])
            item.insert(n - n1 + 1, random.choice(temp))
            n1 -= 1
    
    # 生成刺激列表 stim_list
    stim_list_pre = match_list.copy()  # 复制匹配刺激列表作为基础
    remaining = 45 - len(match_list) * (n + 1)  # 剩余待插入元素的数量
    while remaining > 0:
        new_image = random.choice(image_list)
        index = random.randint(0, len(stim_list_pre))  # 随机选择插入位置
        if index < n:
            stim_list_pre.insert(index, [new_image])  # 在选择的位置插入新元素
            remaining -= 1
        elif index < len(stim_list_pre):
            prev_image = stim_list_pre[index - n][0]
            next_image = stim_list_pre[index][0]
    
            if new_image != prev_image and new_image != next_image:
                stim_list_pre.insert(index, [new_image])  # 在选择的位置插入新元素
                remaining -= 1
        else:
            if new_image != stim_list_pre[index - n][0]:
                stim_list_pre.insert(index, [new_image])
                remaining -= 1
    
    stim_list = []
    # 迭代遍历原始刺激列表拆包
    for stim in stim_list_pre:
        if len(stim) > 1:  # 成对的元素
            for s in stim:
                stim_list.append(s)
        else:  # 单个元素
            stim_list.append(stim[0])
    
    # 计算转换后列表中的元素数量
    num_elements = len(stim_list)
    
    # 复制 stim_list 生成 answer_list
    answer_list = []
    
    if n == 1:
        preimg_list=['01.png']
    else:
        preimg_list=['01.png','02.png']
        
    allimg_list = preimg_list + stim_list
    #anscount = 0
    for i in range(n, len(allimg_list)):
        if allimg_list[i] == allimg_list[i - n]:
            answer_list.append('f')
            #anscount += 1
        else:
            answer_list.append('j')
            
    if n == 1:
        ncolor = 'yellow'
        ntext = '-1-'
    else :
        ncolor = 'purple'
        ntext = '-2-'
        
    #print("before experiment stim_list:", stim_list)
    #print("before experiment answer_list:",answer_list)
    key_resp_6.keys = []
    key_resp_6.rt = []
    _key_resp_6_allKeys = []
    pic_01png_2.setImage('01.png')
    pic_02png_2.setImage('02.png')
    # keep track of which components have finished
    prepareComponents = [key_resp_6, ins_1back, ins_2back, pic_01png_2, pic_02png_2]
    for thisComponent in prepareComponents:
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
    
    # --- Run Routine "prepare" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_6* updates
        waitOnFlip = False
        
        # if key_resp_6 is starting this frame...
        if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.tStart = t  # local t and not account for scr refresh
            key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_6.started')
            # update status
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_6.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_6.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_6_allKeys.extend(theseKeys)
            if len(_key_resp_6_allKeys):
                key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                key_resp_6.duration = _key_resp_6_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *ins_1back* updates
        
        # if ins_1back is starting this frame...
        if ins_1back.status == NOT_STARTED and n ==1:
            # keep track of start time/frame for later
            ins_1back.frameNStart = frameN  # exact frame index
            ins_1back.tStart = t  # local t and not account for scr refresh
            ins_1back.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ins_1back, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ins_1back.started')
            # update status
            ins_1back.status = STARTED
            ins_1back.setAutoDraw(True)
        
        # if ins_1back is active this frame...
        if ins_1back.status == STARTED:
            # update params
            pass
        
        # *ins_2back* updates
        
        # if ins_2back is starting this frame...
        if ins_2back.status == NOT_STARTED and n ==2:
            # keep track of start time/frame for later
            ins_2back.frameNStart = frameN  # exact frame index
            ins_2back.tStart = t  # local t and not account for scr refresh
            ins_2back.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ins_2back, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ins_2back.started')
            # update status
            ins_2back.status = STARTED
            ins_2back.setAutoDraw(True)
        
        # if ins_2back is active this frame...
        if ins_2back.status == STARTED:
            # update params
            pass
        
        # *pic_01png_2* updates
        
        # if pic_01png_2 is starting this frame...
        if pic_01png_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            pic_01png_2.frameNStart = frameN  # exact frame index
            pic_01png_2.tStart = t  # local t and not account for scr refresh
            pic_01png_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pic_01png_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pic_01png_2.started')
            # update status
            pic_01png_2.status = STARTED
            pic_01png_2.setAutoDraw(True)
        
        # if pic_01png_2 is active this frame...
        if pic_01png_2.status == STARTED:
            # update params
            pass
        
        # *pic_02png_2* updates
        
        # if pic_02png_2 is starting this frame...
        if pic_02png_2.status == NOT_STARTED and n == 2:
            # keep track of start time/frame for later
            pic_02png_2.frameNStart = frameN  # exact frame index
            pic_02png_2.tStart = t  # local t and not account for scr refresh
            pic_02png_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pic_02png_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pic_02png_2.started')
            # update status
            pic_02png_2.status = STARTED
            pic_02png_2.setAutoDraw(True)
        
        # if pic_02png_2 is active this frame...
        if pic_02png_2.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prepareComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prepare" ---
    for thisComponent in prepareComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('prepare.stopped', globalClock.getTime(format='float'))
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys = None
    thisExp.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        thisExp.addData('key_resp_6.rt', key_resp_6.rt)
        thisExp.addData('key_resp_6.duration', key_resp_6.duration)
    thisExp.nextEntry()
    # the Routine "prepare" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    condition12 = data.TrialHandler(nReps=30.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='condition12')
    thisExp.addLoop(condition12)  # add the loop to the experiment
    thisCondition12 = condition12.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCondition12.rgb)
    if thisCondition12 != None:
        for paramName in thisCondition12:
            globals()[paramName] = thisCondition12[paramName]
    
    for thisCondition12 in condition12:
        currentLoop = condition12
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisCondition12.rgb)
        if thisCondition12 != None:
            for paramName in thisCondition12:
                globals()[paramName] = thisCondition12[paramName]
        
        # --- Prepare to start Routine "Stim" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Stim.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from code_exe
        this_number = numcount
        this_image = stim_list[numcount-1]
        duration = 0.5
        if num_i == 10:
            duration = 0.3
        if num_i == 9:
            duration = 0.3
        if num_i == 2:
            duration = 0.3
        if num_i == 1:
            duration = 0.3
        if num_i == 4:
            duration = 0.3
        if num_i == 3:
            duration = 0.3
        response = ''
        #the central position of picture
        shuffle(piccenpos_cr)
        shuffle(piccenpos_ar)
        piccenpos = (piccenpos_cr[0], piccenpos_ar[0])
        
        ans = answer_list[numcount-1]
        thisExp.addData('ans', ans)
        print("begin routine ","count",numcount,"img",this_image,"ans",ans)
        
        if key_resp_2.corr:
            response = True
        
        else : 
            response = False
        n_value.setColor(ncolor, colorSpace='rgb')
        n_value.setText(ntext)
        testnum.setText(this_number)
        thisimage.setPos(piccenpos)
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        sound_true.setSound('A', secs=0.1, hamming=True)
        sound_true.setVolume(2.0, log=False)
        sound_true.seek(0)
        sound_false.setSound('B', secs=0.2, hamming=False)
        sound_false.setVolume(4.0, log=False)
        sound_false.seek(0)
        # keep track of which components have finished
        StimComponents = [image_bac, n_value, num, testnum, thisimage, key_resp_2, sound_true, sound_false]
        for thisComponent in StimComponents:
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
        
        # --- Run Routine "Stim" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_bac* updates
            
            # if image_bac is starting this frame...
            if image_bac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_bac.frameNStart = frameN  # exact frame index
                image_bac.tStart = t  # local t and not account for scr refresh
                image_bac.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_bac, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_bac.started')
                # update status
                image_bac.status = STARTED
                image_bac.setAutoDraw(True)
            
            # if image_bac is active this frame...
            if image_bac.status == STARTED:
                # update params
                pass
            
            # *n_value* updates
            
            # if n_value is starting this frame...
            if n_value.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                n_value.frameNStart = frameN  # exact frame index
                n_value.tStart = t  # local t and not account for scr refresh
                n_value.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(n_value, 'tStartRefresh')  # time at next scr refresh
                # update status
                n_value.status = STARTED
                n_value.setAutoDraw(True)
            
            # if n_value is active this frame...
            if n_value.status == STARTED:
                # update params
                pass
            
            # *num* updates
            
            # if num is starting this frame...
            if num.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                num.frameNStart = frameN  # exact frame index
                num.tStart = t  # local t and not account for scr refresh
                num.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(num, 'tStartRefresh')  # time at next scr refresh
                # update status
                num.status = STARTED
                num.setAutoDraw(True)
            
            # if num is active this frame...
            if num.status == STARTED:
                # update params
                pass
            
            # *testnum* updates
            
            # if testnum is starting this frame...
            if testnum.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                testnum.frameNStart = frameN  # exact frame index
                testnum.tStart = t  # local t and not account for scr refresh
                testnum.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(testnum, 'tStartRefresh')  # time at next scr refresh
                # update status
                testnum.status = STARTED
                testnum.setAutoDraw(True)
            
            # if testnum is active this frame...
            if testnum.status == STARTED:
                # update params
                pass
            
            # *thisimage* updates
            
            # if thisimage is starting this frame...
            if thisimage.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                thisimage.frameNStart = frameN  # exact frame index
                thisimage.tStart = t  # local t and not account for scr refresh
                thisimage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(thisimage, 'tStartRefresh')  # time at next scr refresh
                # update status
                thisimage.status = STARTED
                thisimage.setAutoDraw(True)
            
            # if thisimage is active this frame...
            if thisimage.status == STARTED:
                # update params
                thisimage.setImage(this_image, log=False)
            
            # if thisimage is stopping this frame...
            if thisimage.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > thisimage.tStartRefresh + duration-frameTolerance:
                    # keep track of stop time/frame for later
                    thisimage.tStop = t  # not accounting for scr refresh
                    thisimage.tStopRefresh = tThisFlipGlobal  # on global time
                    thisimage.frameNStop = frameN  # exact frame index
                    # update status
                    thisimage.status = FINISHED
                    thisimage.setAutoDraw(False)
            
            # *key_resp_2* updates
            
            # if key_resp_2 is starting this frame...
            if key_resp_2.status == NOT_STARTED and t >= 0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                key_resp_2.clock.reset()  # now t=0
                key_resp_2.clearEvents(eventType='keyboard')
            if key_resp_2.status == STARTED:
                theseKeys = key_resp_2.getKeys(keyList=['f','j'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[0].name  # just the first key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[0].rt
                    key_resp_2.duration = _key_resp_2_allKeys[0].duration
                    # was this correct?
                    if (key_resp_2.keys == str(ans)) or (key_resp_2.keys == ans):
                        key_resp_2.corr = 1
                    else:
                        key_resp_2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # if sound_true is starting this frame...
            if sound_true.status == NOT_STARTED and response==True:
                # keep track of start time/frame for later
                sound_true.frameNStart = frameN  # exact frame index
                sound_true.tStart = t  # local t and not account for scr refresh
                sound_true.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound_true.status = STARTED
                sound_true.play(when=win)  # sync with win flip
            
            # if sound_true is stopping this frame...
            if sound_true.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_true.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_true.tStop = t  # not accounting for scr refresh
                    sound_true.tStopRefresh = tThisFlipGlobal  # on global time
                    sound_true.frameNStop = frameN  # exact frame index
                    # update status
                    sound_true.status = FINISHED
                    sound_true.stop()
            # update sound_true status according to whether it's playing
            if sound_true.isPlaying:
                sound_true.status = STARTED
            elif sound_true.isFinished:
                sound_true.status = FINISHED
            
            # if sound_false is starting this frame...
            if sound_false.status == NOT_STARTED and response==False:
                # keep track of start time/frame for later
                sound_false.frameNStart = frameN  # exact frame index
                sound_false.tStart = t  # local t and not account for scr refresh
                sound_false.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound_false.status = STARTED
                sound_false.play(when=win)  # sync with win flip
            
            # if sound_false is stopping this frame...
            if sound_false.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_false.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_false.tStop = t  # not accounting for scr refresh
                    sound_false.tStopRefresh = tThisFlipGlobal  # on global time
                    sound_false.frameNStop = frameN  # exact frame index
                    # update status
                    sound_false.status = FINISHED
                    sound_false.stop()
            # update sound_false status according to whether it's playing
            if sound_false.isPlaying:
                sound_false.status = STARTED
            elif sound_false.isFinished:
                sound_false.status = FINISHED
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in StimComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Stim" ---
        for thisComponent in StimComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Stim.stopped', globalClock.getTime(format='float'))
        # Run 'End Routine' code from code_exe
        numcount += 1
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
            # was no response the correct answer?!
            if str(ans).lower() == 'none':
               key_resp_2.corr = 1;  # correct non-response
            else:
               key_resp_2.corr = 0;  # failed to respond (incorrectly)
        # store data for condition12 (TrialHandler)
        condition12.addData('key_resp_2.keys',key_resp_2.keys)
        condition12.addData('key_resp_2.corr', key_resp_2.corr)
        if key_resp_2.keys != None:  # we had a response
            condition12.addData('key_resp_2.rt', key_resp_2.rt)
            condition12.addData('key_resp_2.duration', key_resp_2.duration)
        sound_true.pause()  # ensure sound has stopped at end of Routine
        sound_false.pause()  # ensure sound has stopped at end of Routine
        # the Routine "Stim" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedback" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('feedback.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from feedback_code
        shuffle(fixation_list)
        fiximg = fixation_list[0]
        
        
        #监听按键信息并给出反馈
        if key_resp_2.corr:
            response = True
            msg = '答对了!'
            msgcolor = 'green'
        
        else : 
            response = False
            msg = '答错了!'
            msgcolor = 'red'
        
        
        
        msg_response.setColor(msgcolor, colorSpace='rgb')
        msg_response.setText(msg)
        fixation_img.setImage(fiximg)
        # keep track of which components have finished
        feedbackComponents = [image_bac_2, msg_response, fixation_img]
        for thisComponent in feedbackComponents:
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
        
        # --- Run Routine "feedback" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_bac_2* updates
            
            # if image_bac_2 is starting this frame...
            if image_bac_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                image_bac_2.frameNStart = frameN  # exact frame index
                image_bac_2.tStart = t  # local t and not account for scr refresh
                image_bac_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_bac_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_bac_2.started')
                # update status
                image_bac_2.status = STARTED
                image_bac_2.setAutoDraw(True)
            
            # if image_bac_2 is active this frame...
            if image_bac_2.status == STARTED:
                # update params
                pass
            
            # if image_bac_2 is stopping this frame...
            if image_bac_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_bac_2.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_bac_2.tStop = t  # not accounting for scr refresh
                    image_bac_2.tStopRefresh = tThisFlipGlobal  # on global time
                    image_bac_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_bac_2.stopped')
                    # update status
                    image_bac_2.status = FINISHED
                    image_bac_2.setAutoDraw(False)
            
            # *msg_response* updates
            
            # if msg_response is starting this frame...
            if msg_response.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                msg_response.frameNStart = frameN  # exact frame index
                msg_response.tStart = t  # local t and not account for scr refresh
                msg_response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(msg_response, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'msg_response.started')
                # update status
                msg_response.status = STARTED
                msg_response.setAutoDraw(True)
            
            # if msg_response is active this frame...
            if msg_response.status == STARTED:
                # update params
                pass
            
            # if msg_response is stopping this frame...
            if msg_response.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > msg_response.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    msg_response.tStop = t  # not accounting for scr refresh
                    msg_response.tStopRefresh = tThisFlipGlobal  # on global time
                    msg_response.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'msg_response.stopped')
                    # update status
                    msg_response.status = FINISHED
                    msg_response.setAutoDraw(False)
            
            # *fixation_img* updates
            
            # if fixation_img is starting this frame...
            if fixation_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_img.frameNStart = frameN  # exact frame index
                fixation_img.tStart = t  # local t and not account for scr refresh
                fixation_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_img, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_img.started')
                # update status
                fixation_img.status = STARTED
                fixation_img.setAutoDraw(True)
            
            # if fixation_img is active this frame...
            if fixation_img.status == STARTED:
                # update params
                pass
            
            # if fixation_img is stopping this frame...
            if fixation_img.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_img.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_img.tStop = t  # not accounting for scr refresh
                    fixation_img.tStopRefresh = tThisFlipGlobal  # on global time
                    fixation_img.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_img.stopped')
                    # update status
                    fixation_img.status = FINISHED
                    fixation_img.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback" ---
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('feedback.stopped', globalClock.getTime(format='float'))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 30.0 repeats of 'condition12'
    
    
    # --- Prepare to start Routine "prepare" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('prepare.started', globalClock.getTime(format='float'))
    # Run 'Begin Routine' code from anslist_code
    # set environment
    numcount = 1
    num_i = 0
    piccenpos_cr = [166, 0, -166]
    piccenpos_ar = [166, 0, -166]
    
    # select condition
    condition = conditions.pop()
    i, n, image_list, fixation_list = condition
    num_i = i
    
    # add condition details to data document
    condi = {
        'i=': i,
        'n=': n,
        'len=': len(image_list),
        'fix=': len(fixation_list)
    }
    thisExp.addData('condition', condi)
    print('第',i,'组','N值', n, '图表长度', len(image_list), '注视点表长度', len(fixation_list))
    
    # analyze the image list
    pre_img = []
    rom_imgs = image_list.copy()
    for _ in range(n):
        temp = random.choice(rom_imgs)
        pre_img.append(temp)
        rom_imgs.remove(temp)
    
    # 生成匹配刺激列表 match_list
    match_list = []
    ram = range(9 * n)
    for _ in ram:
        match_image = random.choice(image_list)
        match_list.append([match_image, match_image])
    for item in match_list:
        temp = image_list.copy()
        n1 = n
        while n1 > 1:
            temp.remove(item[n - n1])
            item.insert(n - n1 + 1, random.choice(temp))
            n1 -= 1
    
    # 生成刺激列表 stim_list
    stim_list_pre = match_list.copy()  # 复制匹配刺激列表作为基础
    remaining = 45 - len(match_list) * (n + 1)  # 剩余待插入元素的数量
    while remaining > 0:
        new_image = random.choice(image_list)
        index = random.randint(0, len(stim_list_pre))  # 随机选择插入位置
        if index < n:
            stim_list_pre.insert(index, [new_image])  # 在选择的位置插入新元素
            remaining -= 1
        elif index < len(stim_list_pre):
            prev_image = stim_list_pre[index - n][0]
            next_image = stim_list_pre[index][0]
    
            if new_image != prev_image and new_image != next_image:
                stim_list_pre.insert(index, [new_image])  # 在选择的位置插入新元素
                remaining -= 1
        else:
            if new_image != stim_list_pre[index - n][0]:
                stim_list_pre.insert(index, [new_image])
                remaining -= 1
    
    stim_list = []
    # 迭代遍历原始刺激列表拆包
    for stim in stim_list_pre:
        if len(stim) > 1:  # 成对的元素
            for s in stim:
                stim_list.append(s)
        else:  # 单个元素
            stim_list.append(stim[0])
    
    # 计算转换后列表中的元素数量
    num_elements = len(stim_list)
    
    # 复制 stim_list 生成 answer_list
    answer_list = []
    
    if n == 1:
        preimg_list=['01.png']
    else:
        preimg_list=['01.png','02.png']
        
    allimg_list = preimg_list + stim_list
    #anscount = 0
    for i in range(n, len(allimg_list)):
        if allimg_list[i] == allimg_list[i - n]:
            answer_list.append('f')
            #anscount += 1
        else:
            answer_list.append('j')
            
    if n == 1:
        ncolor = 'yellow'
        ntext = '-1-'
    else :
        ncolor = 'purple'
        ntext = '-2-'
        
    #print("before experiment stim_list:", stim_list)
    #print("before experiment answer_list:",answer_list)
    key_resp_6.keys = []
    key_resp_6.rt = []
    _key_resp_6_allKeys = []
    pic_01png_2.setImage('01.png')
    pic_02png_2.setImage('02.png')
    # keep track of which components have finished
    prepareComponents = [key_resp_6, ins_1back, ins_2back, pic_01png_2, pic_02png_2]
    for thisComponent in prepareComponents:
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
    
    # --- Run Routine "prepare" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_6* updates
        waitOnFlip = False
        
        # if key_resp_6 is starting this frame...
        if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.tStart = t  # local t and not account for scr refresh
            key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_6.started')
            # update status
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_6.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_6.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_6_allKeys.extend(theseKeys)
            if len(_key_resp_6_allKeys):
                key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                key_resp_6.duration = _key_resp_6_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *ins_1back* updates
        
        # if ins_1back is starting this frame...
        if ins_1back.status == NOT_STARTED and n ==1:
            # keep track of start time/frame for later
            ins_1back.frameNStart = frameN  # exact frame index
            ins_1back.tStart = t  # local t and not account for scr refresh
            ins_1back.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ins_1back, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ins_1back.started')
            # update status
            ins_1back.status = STARTED
            ins_1back.setAutoDraw(True)
        
        # if ins_1back is active this frame...
        if ins_1back.status == STARTED:
            # update params
            pass
        
        # *ins_2back* updates
        
        # if ins_2back is starting this frame...
        if ins_2back.status == NOT_STARTED and n ==2:
            # keep track of start time/frame for later
            ins_2back.frameNStart = frameN  # exact frame index
            ins_2back.tStart = t  # local t and not account for scr refresh
            ins_2back.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ins_2back, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ins_2back.started')
            # update status
            ins_2back.status = STARTED
            ins_2back.setAutoDraw(True)
        
        # if ins_2back is active this frame...
        if ins_2back.status == STARTED:
            # update params
            pass
        
        # *pic_01png_2* updates
        
        # if pic_01png_2 is starting this frame...
        if pic_01png_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            pic_01png_2.frameNStart = frameN  # exact frame index
            pic_01png_2.tStart = t  # local t and not account for scr refresh
            pic_01png_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pic_01png_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pic_01png_2.started')
            # update status
            pic_01png_2.status = STARTED
            pic_01png_2.setAutoDraw(True)
        
        # if pic_01png_2 is active this frame...
        if pic_01png_2.status == STARTED:
            # update params
            pass
        
        # *pic_02png_2* updates
        
        # if pic_02png_2 is starting this frame...
        if pic_02png_2.status == NOT_STARTED and n == 2:
            # keep track of start time/frame for later
            pic_02png_2.frameNStart = frameN  # exact frame index
            pic_02png_2.tStart = t  # local t and not account for scr refresh
            pic_02png_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pic_02png_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pic_02png_2.started')
            # update status
            pic_02png_2.status = STARTED
            pic_02png_2.setAutoDraw(True)
        
        # if pic_02png_2 is active this frame...
        if pic_02png_2.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prepareComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prepare" ---
    for thisComponent in prepareComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('prepare.stopped', globalClock.getTime(format='float'))
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys = None
    thisExp.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        thisExp.addData('key_resp_6.rt', key_resp_6.rt)
        thisExp.addData('key_resp_6.duration', key_resp_6.duration)
    thisExp.nextEntry()
    # the Routine "prepare" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    condition11 = data.TrialHandler(nReps=30.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='condition11')
    thisExp.addLoop(condition11)  # add the loop to the experiment
    thisCondition11 = condition11.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCondition11.rgb)
    if thisCondition11 != None:
        for paramName in thisCondition11:
            globals()[paramName] = thisCondition11[paramName]
    
    for thisCondition11 in condition11:
        currentLoop = condition11
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisCondition11.rgb)
        if thisCondition11 != None:
            for paramName in thisCondition11:
                globals()[paramName] = thisCondition11[paramName]
        
        # --- Prepare to start Routine "Stim" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Stim.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from code_exe
        this_number = numcount
        this_image = stim_list[numcount-1]
        duration = 0.5
        if num_i == 10:
            duration = 0.3
        if num_i == 9:
            duration = 0.3
        if num_i == 2:
            duration = 0.3
        if num_i == 1:
            duration = 0.3
        if num_i == 4:
            duration = 0.3
        if num_i == 3:
            duration = 0.3
        response = ''
        #the central position of picture
        shuffle(piccenpos_cr)
        shuffle(piccenpos_ar)
        piccenpos = (piccenpos_cr[0], piccenpos_ar[0])
        
        ans = answer_list[numcount-1]
        thisExp.addData('ans', ans)
        print("begin routine ","count",numcount,"img",this_image,"ans",ans)
        
        if key_resp_2.corr:
            response = True
        
        else : 
            response = False
        n_value.setColor(ncolor, colorSpace='rgb')
        n_value.setText(ntext)
        testnum.setText(this_number)
        thisimage.setPos(piccenpos)
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        sound_true.setSound('A', secs=0.1, hamming=True)
        sound_true.setVolume(2.0, log=False)
        sound_true.seek(0)
        sound_false.setSound('B', secs=0.2, hamming=False)
        sound_false.setVolume(4.0, log=False)
        sound_false.seek(0)
        # keep track of which components have finished
        StimComponents = [image_bac, n_value, num, testnum, thisimage, key_resp_2, sound_true, sound_false]
        for thisComponent in StimComponents:
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
        
        # --- Run Routine "Stim" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_bac* updates
            
            # if image_bac is starting this frame...
            if image_bac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_bac.frameNStart = frameN  # exact frame index
                image_bac.tStart = t  # local t and not account for scr refresh
                image_bac.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_bac, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_bac.started')
                # update status
                image_bac.status = STARTED
                image_bac.setAutoDraw(True)
            
            # if image_bac is active this frame...
            if image_bac.status == STARTED:
                # update params
                pass
            
            # *n_value* updates
            
            # if n_value is starting this frame...
            if n_value.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                n_value.frameNStart = frameN  # exact frame index
                n_value.tStart = t  # local t and not account for scr refresh
                n_value.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(n_value, 'tStartRefresh')  # time at next scr refresh
                # update status
                n_value.status = STARTED
                n_value.setAutoDraw(True)
            
            # if n_value is active this frame...
            if n_value.status == STARTED:
                # update params
                pass
            
            # *num* updates
            
            # if num is starting this frame...
            if num.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                num.frameNStart = frameN  # exact frame index
                num.tStart = t  # local t and not account for scr refresh
                num.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(num, 'tStartRefresh')  # time at next scr refresh
                # update status
                num.status = STARTED
                num.setAutoDraw(True)
            
            # if num is active this frame...
            if num.status == STARTED:
                # update params
                pass
            
            # *testnum* updates
            
            # if testnum is starting this frame...
            if testnum.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                testnum.frameNStart = frameN  # exact frame index
                testnum.tStart = t  # local t and not account for scr refresh
                testnum.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(testnum, 'tStartRefresh')  # time at next scr refresh
                # update status
                testnum.status = STARTED
                testnum.setAutoDraw(True)
            
            # if testnum is active this frame...
            if testnum.status == STARTED:
                # update params
                pass
            
            # *thisimage* updates
            
            # if thisimage is starting this frame...
            if thisimage.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                thisimage.frameNStart = frameN  # exact frame index
                thisimage.tStart = t  # local t and not account for scr refresh
                thisimage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(thisimage, 'tStartRefresh')  # time at next scr refresh
                # update status
                thisimage.status = STARTED
                thisimage.setAutoDraw(True)
            
            # if thisimage is active this frame...
            if thisimage.status == STARTED:
                # update params
                thisimage.setImage(this_image, log=False)
            
            # if thisimage is stopping this frame...
            if thisimage.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > thisimage.tStartRefresh + duration-frameTolerance:
                    # keep track of stop time/frame for later
                    thisimage.tStop = t  # not accounting for scr refresh
                    thisimage.tStopRefresh = tThisFlipGlobal  # on global time
                    thisimage.frameNStop = frameN  # exact frame index
                    # update status
                    thisimage.status = FINISHED
                    thisimage.setAutoDraw(False)
            
            # *key_resp_2* updates
            
            # if key_resp_2 is starting this frame...
            if key_resp_2.status == NOT_STARTED and t >= 0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                key_resp_2.clock.reset()  # now t=0
                key_resp_2.clearEvents(eventType='keyboard')
            if key_resp_2.status == STARTED:
                theseKeys = key_resp_2.getKeys(keyList=['f','j'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[0].name  # just the first key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[0].rt
                    key_resp_2.duration = _key_resp_2_allKeys[0].duration
                    # was this correct?
                    if (key_resp_2.keys == str(ans)) or (key_resp_2.keys == ans):
                        key_resp_2.corr = 1
                    else:
                        key_resp_2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # if sound_true is starting this frame...
            if sound_true.status == NOT_STARTED and response==True:
                # keep track of start time/frame for later
                sound_true.frameNStart = frameN  # exact frame index
                sound_true.tStart = t  # local t and not account for scr refresh
                sound_true.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound_true.status = STARTED
                sound_true.play(when=win)  # sync with win flip
            
            # if sound_true is stopping this frame...
            if sound_true.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_true.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_true.tStop = t  # not accounting for scr refresh
                    sound_true.tStopRefresh = tThisFlipGlobal  # on global time
                    sound_true.frameNStop = frameN  # exact frame index
                    # update status
                    sound_true.status = FINISHED
                    sound_true.stop()
            # update sound_true status according to whether it's playing
            if sound_true.isPlaying:
                sound_true.status = STARTED
            elif sound_true.isFinished:
                sound_true.status = FINISHED
            
            # if sound_false is starting this frame...
            if sound_false.status == NOT_STARTED and response==False:
                # keep track of start time/frame for later
                sound_false.frameNStart = frameN  # exact frame index
                sound_false.tStart = t  # local t and not account for scr refresh
                sound_false.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound_false.status = STARTED
                sound_false.play(when=win)  # sync with win flip
            
            # if sound_false is stopping this frame...
            if sound_false.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_false.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_false.tStop = t  # not accounting for scr refresh
                    sound_false.tStopRefresh = tThisFlipGlobal  # on global time
                    sound_false.frameNStop = frameN  # exact frame index
                    # update status
                    sound_false.status = FINISHED
                    sound_false.stop()
            # update sound_false status according to whether it's playing
            if sound_false.isPlaying:
                sound_false.status = STARTED
            elif sound_false.isFinished:
                sound_false.status = FINISHED
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in StimComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Stim" ---
        for thisComponent in StimComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Stim.stopped', globalClock.getTime(format='float'))
        # Run 'End Routine' code from code_exe
        numcount += 1
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
            # was no response the correct answer?!
            if str(ans).lower() == 'none':
               key_resp_2.corr = 1;  # correct non-response
            else:
               key_resp_2.corr = 0;  # failed to respond (incorrectly)
        # store data for condition11 (TrialHandler)
        condition11.addData('key_resp_2.keys',key_resp_2.keys)
        condition11.addData('key_resp_2.corr', key_resp_2.corr)
        if key_resp_2.keys != None:  # we had a response
            condition11.addData('key_resp_2.rt', key_resp_2.rt)
            condition11.addData('key_resp_2.duration', key_resp_2.duration)
        sound_true.pause()  # ensure sound has stopped at end of Routine
        sound_false.pause()  # ensure sound has stopped at end of Routine
        # the Routine "Stim" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedback" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('feedback.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from feedback_code
        shuffle(fixation_list)
        fiximg = fixation_list[0]
        
        
        #监听按键信息并给出反馈
        if key_resp_2.corr:
            response = True
            msg = '答对了!'
            msgcolor = 'green'
        
        else : 
            response = False
            msg = '答错了!'
            msgcolor = 'red'
        
        
        
        msg_response.setColor(msgcolor, colorSpace='rgb')
        msg_response.setText(msg)
        fixation_img.setImage(fiximg)
        # keep track of which components have finished
        feedbackComponents = [image_bac_2, msg_response, fixation_img]
        for thisComponent in feedbackComponents:
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
        
        # --- Run Routine "feedback" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_bac_2* updates
            
            # if image_bac_2 is starting this frame...
            if image_bac_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                image_bac_2.frameNStart = frameN  # exact frame index
                image_bac_2.tStart = t  # local t and not account for scr refresh
                image_bac_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_bac_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_bac_2.started')
                # update status
                image_bac_2.status = STARTED
                image_bac_2.setAutoDraw(True)
            
            # if image_bac_2 is active this frame...
            if image_bac_2.status == STARTED:
                # update params
                pass
            
            # if image_bac_2 is stopping this frame...
            if image_bac_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_bac_2.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_bac_2.tStop = t  # not accounting for scr refresh
                    image_bac_2.tStopRefresh = tThisFlipGlobal  # on global time
                    image_bac_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_bac_2.stopped')
                    # update status
                    image_bac_2.status = FINISHED
                    image_bac_2.setAutoDraw(False)
            
            # *msg_response* updates
            
            # if msg_response is starting this frame...
            if msg_response.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                msg_response.frameNStart = frameN  # exact frame index
                msg_response.tStart = t  # local t and not account for scr refresh
                msg_response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(msg_response, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'msg_response.started')
                # update status
                msg_response.status = STARTED
                msg_response.setAutoDraw(True)
            
            # if msg_response is active this frame...
            if msg_response.status == STARTED:
                # update params
                pass
            
            # if msg_response is stopping this frame...
            if msg_response.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > msg_response.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    msg_response.tStop = t  # not accounting for scr refresh
                    msg_response.tStopRefresh = tThisFlipGlobal  # on global time
                    msg_response.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'msg_response.stopped')
                    # update status
                    msg_response.status = FINISHED
                    msg_response.setAutoDraw(False)
            
            # *fixation_img* updates
            
            # if fixation_img is starting this frame...
            if fixation_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_img.frameNStart = frameN  # exact frame index
                fixation_img.tStart = t  # local t and not account for scr refresh
                fixation_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_img, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_img.started')
                # update status
                fixation_img.status = STARTED
                fixation_img.setAutoDraw(True)
            
            # if fixation_img is active this frame...
            if fixation_img.status == STARTED:
                # update params
                pass
            
            # if fixation_img is stopping this frame...
            if fixation_img.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_img.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_img.tStop = t  # not accounting for scr refresh
                    fixation_img.tStopRefresh = tThisFlipGlobal  # on global time
                    fixation_img.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_img.stopped')
                    # update status
                    fixation_img.status = FINISHED
                    fixation_img.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback" ---
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('feedback.stopped', globalClock.getTime(format='float'))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 30.0 repeats of 'condition11'
    
    
    # --- Prepare to start Routine "prepare" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('prepare.started', globalClock.getTime(format='float'))
    # Run 'Begin Routine' code from anslist_code
    # set environment
    numcount = 1
    num_i = 0
    piccenpos_cr = [166, 0, -166]
    piccenpos_ar = [166, 0, -166]
    
    # select condition
    condition = conditions.pop()
    i, n, image_list, fixation_list = condition
    num_i = i
    
    # add condition details to data document
    condi = {
        'i=': i,
        'n=': n,
        'len=': len(image_list),
        'fix=': len(fixation_list)
    }
    thisExp.addData('condition', condi)
    print('第',i,'组','N值', n, '图表长度', len(image_list), '注视点表长度', len(fixation_list))
    
    # analyze the image list
    pre_img = []
    rom_imgs = image_list.copy()
    for _ in range(n):
        temp = random.choice(rom_imgs)
        pre_img.append(temp)
        rom_imgs.remove(temp)
    
    # 生成匹配刺激列表 match_list
    match_list = []
    ram = range(9 * n)
    for _ in ram:
        match_image = random.choice(image_list)
        match_list.append([match_image, match_image])
    for item in match_list:
        temp = image_list.copy()
        n1 = n
        while n1 > 1:
            temp.remove(item[n - n1])
            item.insert(n - n1 + 1, random.choice(temp))
            n1 -= 1
    
    # 生成刺激列表 stim_list
    stim_list_pre = match_list.copy()  # 复制匹配刺激列表作为基础
    remaining = 45 - len(match_list) * (n + 1)  # 剩余待插入元素的数量
    while remaining > 0:
        new_image = random.choice(image_list)
        index = random.randint(0, len(stim_list_pre))  # 随机选择插入位置
        if index < n:
            stim_list_pre.insert(index, [new_image])  # 在选择的位置插入新元素
            remaining -= 1
        elif index < len(stim_list_pre):
            prev_image = stim_list_pre[index - n][0]
            next_image = stim_list_pre[index][0]
    
            if new_image != prev_image and new_image != next_image:
                stim_list_pre.insert(index, [new_image])  # 在选择的位置插入新元素
                remaining -= 1
        else:
            if new_image != stim_list_pre[index - n][0]:
                stim_list_pre.insert(index, [new_image])
                remaining -= 1
    
    stim_list = []
    # 迭代遍历原始刺激列表拆包
    for stim in stim_list_pre:
        if len(stim) > 1:  # 成对的元素
            for s in stim:
                stim_list.append(s)
        else:  # 单个元素
            stim_list.append(stim[0])
    
    # 计算转换后列表中的元素数量
    num_elements = len(stim_list)
    
    # 复制 stim_list 生成 answer_list
    answer_list = []
    
    if n == 1:
        preimg_list=['01.png']
    else:
        preimg_list=['01.png','02.png']
        
    allimg_list = preimg_list + stim_list
    #anscount = 0
    for i in range(n, len(allimg_list)):
        if allimg_list[i] == allimg_list[i - n]:
            answer_list.append('f')
            #anscount += 1
        else:
            answer_list.append('j')
            
    if n == 1:
        ncolor = 'yellow'
        ntext = '-1-'
    else :
        ncolor = 'purple'
        ntext = '-2-'
        
    #print("before experiment stim_list:", stim_list)
    #print("before experiment answer_list:",answer_list)
    key_resp_6.keys = []
    key_resp_6.rt = []
    _key_resp_6_allKeys = []
    pic_01png_2.setImage('01.png')
    pic_02png_2.setImage('02.png')
    # keep track of which components have finished
    prepareComponents = [key_resp_6, ins_1back, ins_2back, pic_01png_2, pic_02png_2]
    for thisComponent in prepareComponents:
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
    
    # --- Run Routine "prepare" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_6* updates
        waitOnFlip = False
        
        # if key_resp_6 is starting this frame...
        if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.tStart = t  # local t and not account for scr refresh
            key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_6.started')
            # update status
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_6.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_6.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_6_allKeys.extend(theseKeys)
            if len(_key_resp_6_allKeys):
                key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                key_resp_6.duration = _key_resp_6_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *ins_1back* updates
        
        # if ins_1back is starting this frame...
        if ins_1back.status == NOT_STARTED and n ==1:
            # keep track of start time/frame for later
            ins_1back.frameNStart = frameN  # exact frame index
            ins_1back.tStart = t  # local t and not account for scr refresh
            ins_1back.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ins_1back, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ins_1back.started')
            # update status
            ins_1back.status = STARTED
            ins_1back.setAutoDraw(True)
        
        # if ins_1back is active this frame...
        if ins_1back.status == STARTED:
            # update params
            pass
        
        # *ins_2back* updates
        
        # if ins_2back is starting this frame...
        if ins_2back.status == NOT_STARTED and n ==2:
            # keep track of start time/frame for later
            ins_2back.frameNStart = frameN  # exact frame index
            ins_2back.tStart = t  # local t and not account for scr refresh
            ins_2back.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ins_2back, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ins_2back.started')
            # update status
            ins_2back.status = STARTED
            ins_2back.setAutoDraw(True)
        
        # if ins_2back is active this frame...
        if ins_2back.status == STARTED:
            # update params
            pass
        
        # *pic_01png_2* updates
        
        # if pic_01png_2 is starting this frame...
        if pic_01png_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            pic_01png_2.frameNStart = frameN  # exact frame index
            pic_01png_2.tStart = t  # local t and not account for scr refresh
            pic_01png_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pic_01png_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pic_01png_2.started')
            # update status
            pic_01png_2.status = STARTED
            pic_01png_2.setAutoDraw(True)
        
        # if pic_01png_2 is active this frame...
        if pic_01png_2.status == STARTED:
            # update params
            pass
        
        # *pic_02png_2* updates
        
        # if pic_02png_2 is starting this frame...
        if pic_02png_2.status == NOT_STARTED and n == 2:
            # keep track of start time/frame for later
            pic_02png_2.frameNStart = frameN  # exact frame index
            pic_02png_2.tStart = t  # local t and not account for scr refresh
            pic_02png_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pic_02png_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pic_02png_2.started')
            # update status
            pic_02png_2.status = STARTED
            pic_02png_2.setAutoDraw(True)
        
        # if pic_02png_2 is active this frame...
        if pic_02png_2.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prepareComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prepare" ---
    for thisComponent in prepareComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('prepare.stopped', globalClock.getTime(format='float'))
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys = None
    thisExp.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        thisExp.addData('key_resp_6.rt', key_resp_6.rt)
        thisExp.addData('key_resp_6.duration', key_resp_6.duration)
    thisExp.nextEntry()
    # the Routine "prepare" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    condition10 = data.TrialHandler(nReps=30.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='condition10')
    thisExp.addLoop(condition10)  # add the loop to the experiment
    thisCondition10 = condition10.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCondition10.rgb)
    if thisCondition10 != None:
        for paramName in thisCondition10:
            globals()[paramName] = thisCondition10[paramName]
    
    for thisCondition10 in condition10:
        currentLoop = condition10
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisCondition10.rgb)
        if thisCondition10 != None:
            for paramName in thisCondition10:
                globals()[paramName] = thisCondition10[paramName]
        
        # --- Prepare to start Routine "Stim" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Stim.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from code_exe
        this_number = numcount
        this_image = stim_list[numcount-1]
        duration = 0.5
        if num_i == 10:
            duration = 0.3
        if num_i == 9:
            duration = 0.3
        if num_i == 2:
            duration = 0.3
        if num_i == 1:
            duration = 0.3
        if num_i == 4:
            duration = 0.3
        if num_i == 3:
            duration = 0.3
        response = ''
        #the central position of picture
        shuffle(piccenpos_cr)
        shuffle(piccenpos_ar)
        piccenpos = (piccenpos_cr[0], piccenpos_ar[0])
        
        ans = answer_list[numcount-1]
        thisExp.addData('ans', ans)
        print("begin routine ","count",numcount,"img",this_image,"ans",ans)
        
        if key_resp_2.corr:
            response = True
        
        else : 
            response = False
        n_value.setColor(ncolor, colorSpace='rgb')
        n_value.setText(ntext)
        testnum.setText(this_number)
        thisimage.setPos(piccenpos)
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        sound_true.setSound('A', secs=0.1, hamming=True)
        sound_true.setVolume(2.0, log=False)
        sound_true.seek(0)
        sound_false.setSound('B', secs=0.2, hamming=False)
        sound_false.setVolume(4.0, log=False)
        sound_false.seek(0)
        # keep track of which components have finished
        StimComponents = [image_bac, n_value, num, testnum, thisimage, key_resp_2, sound_true, sound_false]
        for thisComponent in StimComponents:
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
        
        # --- Run Routine "Stim" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_bac* updates
            
            # if image_bac is starting this frame...
            if image_bac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_bac.frameNStart = frameN  # exact frame index
                image_bac.tStart = t  # local t and not account for scr refresh
                image_bac.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_bac, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_bac.started')
                # update status
                image_bac.status = STARTED
                image_bac.setAutoDraw(True)
            
            # if image_bac is active this frame...
            if image_bac.status == STARTED:
                # update params
                pass
            
            # *n_value* updates
            
            # if n_value is starting this frame...
            if n_value.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                n_value.frameNStart = frameN  # exact frame index
                n_value.tStart = t  # local t and not account for scr refresh
                n_value.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(n_value, 'tStartRefresh')  # time at next scr refresh
                # update status
                n_value.status = STARTED
                n_value.setAutoDraw(True)
            
            # if n_value is active this frame...
            if n_value.status == STARTED:
                # update params
                pass
            
            # *num* updates
            
            # if num is starting this frame...
            if num.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                num.frameNStart = frameN  # exact frame index
                num.tStart = t  # local t and not account for scr refresh
                num.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(num, 'tStartRefresh')  # time at next scr refresh
                # update status
                num.status = STARTED
                num.setAutoDraw(True)
            
            # if num is active this frame...
            if num.status == STARTED:
                # update params
                pass
            
            # *testnum* updates
            
            # if testnum is starting this frame...
            if testnum.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                testnum.frameNStart = frameN  # exact frame index
                testnum.tStart = t  # local t and not account for scr refresh
                testnum.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(testnum, 'tStartRefresh')  # time at next scr refresh
                # update status
                testnum.status = STARTED
                testnum.setAutoDraw(True)
            
            # if testnum is active this frame...
            if testnum.status == STARTED:
                # update params
                pass
            
            # *thisimage* updates
            
            # if thisimage is starting this frame...
            if thisimage.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                thisimage.frameNStart = frameN  # exact frame index
                thisimage.tStart = t  # local t and not account for scr refresh
                thisimage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(thisimage, 'tStartRefresh')  # time at next scr refresh
                # update status
                thisimage.status = STARTED
                thisimage.setAutoDraw(True)
            
            # if thisimage is active this frame...
            if thisimage.status == STARTED:
                # update params
                thisimage.setImage(this_image, log=False)
            
            # if thisimage is stopping this frame...
            if thisimage.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > thisimage.tStartRefresh + duration-frameTolerance:
                    # keep track of stop time/frame for later
                    thisimage.tStop = t  # not accounting for scr refresh
                    thisimage.tStopRefresh = tThisFlipGlobal  # on global time
                    thisimage.frameNStop = frameN  # exact frame index
                    # update status
                    thisimage.status = FINISHED
                    thisimage.setAutoDraw(False)
            
            # *key_resp_2* updates
            
            # if key_resp_2 is starting this frame...
            if key_resp_2.status == NOT_STARTED and t >= 0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                key_resp_2.clock.reset()  # now t=0
                key_resp_2.clearEvents(eventType='keyboard')
            if key_resp_2.status == STARTED:
                theseKeys = key_resp_2.getKeys(keyList=['f','j'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[0].name  # just the first key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[0].rt
                    key_resp_2.duration = _key_resp_2_allKeys[0].duration
                    # was this correct?
                    if (key_resp_2.keys == str(ans)) or (key_resp_2.keys == ans):
                        key_resp_2.corr = 1
                    else:
                        key_resp_2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # if sound_true is starting this frame...
            if sound_true.status == NOT_STARTED and response==True:
                # keep track of start time/frame for later
                sound_true.frameNStart = frameN  # exact frame index
                sound_true.tStart = t  # local t and not account for scr refresh
                sound_true.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound_true.status = STARTED
                sound_true.play(when=win)  # sync with win flip
            
            # if sound_true is stopping this frame...
            if sound_true.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_true.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_true.tStop = t  # not accounting for scr refresh
                    sound_true.tStopRefresh = tThisFlipGlobal  # on global time
                    sound_true.frameNStop = frameN  # exact frame index
                    # update status
                    sound_true.status = FINISHED
                    sound_true.stop()
            # update sound_true status according to whether it's playing
            if sound_true.isPlaying:
                sound_true.status = STARTED
            elif sound_true.isFinished:
                sound_true.status = FINISHED
            
            # if sound_false is starting this frame...
            if sound_false.status == NOT_STARTED and response==False:
                # keep track of start time/frame for later
                sound_false.frameNStart = frameN  # exact frame index
                sound_false.tStart = t  # local t and not account for scr refresh
                sound_false.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound_false.status = STARTED
                sound_false.play(when=win)  # sync with win flip
            
            # if sound_false is stopping this frame...
            if sound_false.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_false.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_false.tStop = t  # not accounting for scr refresh
                    sound_false.tStopRefresh = tThisFlipGlobal  # on global time
                    sound_false.frameNStop = frameN  # exact frame index
                    # update status
                    sound_false.status = FINISHED
                    sound_false.stop()
            # update sound_false status according to whether it's playing
            if sound_false.isPlaying:
                sound_false.status = STARTED
            elif sound_false.isFinished:
                sound_false.status = FINISHED
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in StimComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Stim" ---
        for thisComponent in StimComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Stim.stopped', globalClock.getTime(format='float'))
        # Run 'End Routine' code from code_exe
        numcount += 1
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
            # was no response the correct answer?!
            if str(ans).lower() == 'none':
               key_resp_2.corr = 1;  # correct non-response
            else:
               key_resp_2.corr = 0;  # failed to respond (incorrectly)
        # store data for condition10 (TrialHandler)
        condition10.addData('key_resp_2.keys',key_resp_2.keys)
        condition10.addData('key_resp_2.corr', key_resp_2.corr)
        if key_resp_2.keys != None:  # we had a response
            condition10.addData('key_resp_2.rt', key_resp_2.rt)
            condition10.addData('key_resp_2.duration', key_resp_2.duration)
        sound_true.pause()  # ensure sound has stopped at end of Routine
        sound_false.pause()  # ensure sound has stopped at end of Routine
        # the Routine "Stim" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedback" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('feedback.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from feedback_code
        shuffle(fixation_list)
        fiximg = fixation_list[0]
        
        
        #监听按键信息并给出反馈
        if key_resp_2.corr:
            response = True
            msg = '答对了!'
            msgcolor = 'green'
        
        else : 
            response = False
            msg = '答错了!'
            msgcolor = 'red'
        
        
        
        msg_response.setColor(msgcolor, colorSpace='rgb')
        msg_response.setText(msg)
        fixation_img.setImage(fiximg)
        # keep track of which components have finished
        feedbackComponents = [image_bac_2, msg_response, fixation_img]
        for thisComponent in feedbackComponents:
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
        
        # --- Run Routine "feedback" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_bac_2* updates
            
            # if image_bac_2 is starting this frame...
            if image_bac_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                image_bac_2.frameNStart = frameN  # exact frame index
                image_bac_2.tStart = t  # local t and not account for scr refresh
                image_bac_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_bac_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_bac_2.started')
                # update status
                image_bac_2.status = STARTED
                image_bac_2.setAutoDraw(True)
            
            # if image_bac_2 is active this frame...
            if image_bac_2.status == STARTED:
                # update params
                pass
            
            # if image_bac_2 is stopping this frame...
            if image_bac_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_bac_2.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_bac_2.tStop = t  # not accounting for scr refresh
                    image_bac_2.tStopRefresh = tThisFlipGlobal  # on global time
                    image_bac_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_bac_2.stopped')
                    # update status
                    image_bac_2.status = FINISHED
                    image_bac_2.setAutoDraw(False)
            
            # *msg_response* updates
            
            # if msg_response is starting this frame...
            if msg_response.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                msg_response.frameNStart = frameN  # exact frame index
                msg_response.tStart = t  # local t and not account for scr refresh
                msg_response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(msg_response, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'msg_response.started')
                # update status
                msg_response.status = STARTED
                msg_response.setAutoDraw(True)
            
            # if msg_response is active this frame...
            if msg_response.status == STARTED:
                # update params
                pass
            
            # if msg_response is stopping this frame...
            if msg_response.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > msg_response.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    msg_response.tStop = t  # not accounting for scr refresh
                    msg_response.tStopRefresh = tThisFlipGlobal  # on global time
                    msg_response.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'msg_response.stopped')
                    # update status
                    msg_response.status = FINISHED
                    msg_response.setAutoDraw(False)
            
            # *fixation_img* updates
            
            # if fixation_img is starting this frame...
            if fixation_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_img.frameNStart = frameN  # exact frame index
                fixation_img.tStart = t  # local t and not account for scr refresh
                fixation_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_img, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_img.started')
                # update status
                fixation_img.status = STARTED
                fixation_img.setAutoDraw(True)
            
            # if fixation_img is active this frame...
            if fixation_img.status == STARTED:
                # update params
                pass
            
            # if fixation_img is stopping this frame...
            if fixation_img.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_img.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_img.tStop = t  # not accounting for scr refresh
                    fixation_img.tStopRefresh = tThisFlipGlobal  # on global time
                    fixation_img.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_img.stopped')
                    # update status
                    fixation_img.status = FINISHED
                    fixation_img.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback" ---
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('feedback.stopped', globalClock.getTime(format='float'))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 30.0 repeats of 'condition10'
    
    
    # --- Prepare to start Routine "prepare" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('prepare.started', globalClock.getTime(format='float'))
    # Run 'Begin Routine' code from anslist_code
    # set environment
    numcount = 1
    num_i = 0
    piccenpos_cr = [166, 0, -166]
    piccenpos_ar = [166, 0, -166]
    
    # select condition
    condition = conditions.pop()
    i, n, image_list, fixation_list = condition
    num_i = i
    
    # add condition details to data document
    condi = {
        'i=': i,
        'n=': n,
        'len=': len(image_list),
        'fix=': len(fixation_list)
    }
    thisExp.addData('condition', condi)
    print('第',i,'组','N值', n, '图表长度', len(image_list), '注视点表长度', len(fixation_list))
    
    # analyze the image list
    pre_img = []
    rom_imgs = image_list.copy()
    for _ in range(n):
        temp = random.choice(rom_imgs)
        pre_img.append(temp)
        rom_imgs.remove(temp)
    
    # 生成匹配刺激列表 match_list
    match_list = []
    ram = range(9 * n)
    for _ in ram:
        match_image = random.choice(image_list)
        match_list.append([match_image, match_image])
    for item in match_list:
        temp = image_list.copy()
        n1 = n
        while n1 > 1:
            temp.remove(item[n - n1])
            item.insert(n - n1 + 1, random.choice(temp))
            n1 -= 1
    
    # 生成刺激列表 stim_list
    stim_list_pre = match_list.copy()  # 复制匹配刺激列表作为基础
    remaining = 45 - len(match_list) * (n + 1)  # 剩余待插入元素的数量
    while remaining > 0:
        new_image = random.choice(image_list)
        index = random.randint(0, len(stim_list_pre))  # 随机选择插入位置
        if index < n:
            stim_list_pre.insert(index, [new_image])  # 在选择的位置插入新元素
            remaining -= 1
        elif index < len(stim_list_pre):
            prev_image = stim_list_pre[index - n][0]
            next_image = stim_list_pre[index][0]
    
            if new_image != prev_image and new_image != next_image:
                stim_list_pre.insert(index, [new_image])  # 在选择的位置插入新元素
                remaining -= 1
        else:
            if new_image != stim_list_pre[index - n][0]:
                stim_list_pre.insert(index, [new_image])
                remaining -= 1
    
    stim_list = []
    # 迭代遍历原始刺激列表拆包
    for stim in stim_list_pre:
        if len(stim) > 1:  # 成对的元素
            for s in stim:
                stim_list.append(s)
        else:  # 单个元素
            stim_list.append(stim[0])
    
    # 计算转换后列表中的元素数量
    num_elements = len(stim_list)
    
    # 复制 stim_list 生成 answer_list
    answer_list = []
    
    if n == 1:
        preimg_list=['01.png']
    else:
        preimg_list=['01.png','02.png']
        
    allimg_list = preimg_list + stim_list
    #anscount = 0
    for i in range(n, len(allimg_list)):
        if allimg_list[i] == allimg_list[i - n]:
            answer_list.append('f')
            #anscount += 1
        else:
            answer_list.append('j')
            
    if n == 1:
        ncolor = 'yellow'
        ntext = '-1-'
    else :
        ncolor = 'purple'
        ntext = '-2-'
        
    #print("before experiment stim_list:", stim_list)
    #print("before experiment answer_list:",answer_list)
    key_resp_6.keys = []
    key_resp_6.rt = []
    _key_resp_6_allKeys = []
    pic_01png_2.setImage('01.png')
    pic_02png_2.setImage('02.png')
    # keep track of which components have finished
    prepareComponents = [key_resp_6, ins_1back, ins_2back, pic_01png_2, pic_02png_2]
    for thisComponent in prepareComponents:
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
    
    # --- Run Routine "prepare" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_6* updates
        waitOnFlip = False
        
        # if key_resp_6 is starting this frame...
        if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.tStart = t  # local t and not account for scr refresh
            key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_6.started')
            # update status
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_6.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_6.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_6_allKeys.extend(theseKeys)
            if len(_key_resp_6_allKeys):
                key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                key_resp_6.duration = _key_resp_6_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *ins_1back* updates
        
        # if ins_1back is starting this frame...
        if ins_1back.status == NOT_STARTED and n ==1:
            # keep track of start time/frame for later
            ins_1back.frameNStart = frameN  # exact frame index
            ins_1back.tStart = t  # local t and not account for scr refresh
            ins_1back.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ins_1back, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ins_1back.started')
            # update status
            ins_1back.status = STARTED
            ins_1back.setAutoDraw(True)
        
        # if ins_1back is active this frame...
        if ins_1back.status == STARTED:
            # update params
            pass
        
        # *ins_2back* updates
        
        # if ins_2back is starting this frame...
        if ins_2back.status == NOT_STARTED and n ==2:
            # keep track of start time/frame for later
            ins_2back.frameNStart = frameN  # exact frame index
            ins_2back.tStart = t  # local t and not account for scr refresh
            ins_2back.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ins_2back, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ins_2back.started')
            # update status
            ins_2back.status = STARTED
            ins_2back.setAutoDraw(True)
        
        # if ins_2back is active this frame...
        if ins_2back.status == STARTED:
            # update params
            pass
        
        # *pic_01png_2* updates
        
        # if pic_01png_2 is starting this frame...
        if pic_01png_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            pic_01png_2.frameNStart = frameN  # exact frame index
            pic_01png_2.tStart = t  # local t and not account for scr refresh
            pic_01png_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pic_01png_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pic_01png_2.started')
            # update status
            pic_01png_2.status = STARTED
            pic_01png_2.setAutoDraw(True)
        
        # if pic_01png_2 is active this frame...
        if pic_01png_2.status == STARTED:
            # update params
            pass
        
        # *pic_02png_2* updates
        
        # if pic_02png_2 is starting this frame...
        if pic_02png_2.status == NOT_STARTED and n == 2:
            # keep track of start time/frame for later
            pic_02png_2.frameNStart = frameN  # exact frame index
            pic_02png_2.tStart = t  # local t and not account for scr refresh
            pic_02png_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pic_02png_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pic_02png_2.started')
            # update status
            pic_02png_2.status = STARTED
            pic_02png_2.setAutoDraw(True)
        
        # if pic_02png_2 is active this frame...
        if pic_02png_2.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prepareComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prepare" ---
    for thisComponent in prepareComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('prepare.stopped', globalClock.getTime(format='float'))
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys = None
    thisExp.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        thisExp.addData('key_resp_6.rt', key_resp_6.rt)
        thisExp.addData('key_resp_6.duration', key_resp_6.duration)
    thisExp.nextEntry()
    # the Routine "prepare" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    condition9 = data.TrialHandler(nReps=30.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='condition9')
    thisExp.addLoop(condition9)  # add the loop to the experiment
    thisCondition9 = condition9.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCondition9.rgb)
    if thisCondition9 != None:
        for paramName in thisCondition9:
            globals()[paramName] = thisCondition9[paramName]
    
    for thisCondition9 in condition9:
        currentLoop = condition9
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisCondition9.rgb)
        if thisCondition9 != None:
            for paramName in thisCondition9:
                globals()[paramName] = thisCondition9[paramName]
        
        # --- Prepare to start Routine "Stim" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Stim.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from code_exe
        this_number = numcount
        this_image = stim_list[numcount-1]
        duration = 0.5
        if num_i == 10:
            duration = 0.3
        if num_i == 9:
            duration = 0.3
        if num_i == 2:
            duration = 0.3
        if num_i == 1:
            duration = 0.3
        if num_i == 4:
            duration = 0.3
        if num_i == 3:
            duration = 0.3
        response = ''
        #the central position of picture
        shuffle(piccenpos_cr)
        shuffle(piccenpos_ar)
        piccenpos = (piccenpos_cr[0], piccenpos_ar[0])
        
        ans = answer_list[numcount-1]
        thisExp.addData('ans', ans)
        print("begin routine ","count",numcount,"img",this_image,"ans",ans)
        
        if key_resp_2.corr:
            response = True
        
        else : 
            response = False
        n_value.setColor(ncolor, colorSpace='rgb')
        n_value.setText(ntext)
        testnum.setText(this_number)
        thisimage.setPos(piccenpos)
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        sound_true.setSound('A', secs=0.1, hamming=True)
        sound_true.setVolume(2.0, log=False)
        sound_true.seek(0)
        sound_false.setSound('B', secs=0.2, hamming=False)
        sound_false.setVolume(4.0, log=False)
        sound_false.seek(0)
        # keep track of which components have finished
        StimComponents = [image_bac, n_value, num, testnum, thisimage, key_resp_2, sound_true, sound_false]
        for thisComponent in StimComponents:
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
        
        # --- Run Routine "Stim" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_bac* updates
            
            # if image_bac is starting this frame...
            if image_bac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_bac.frameNStart = frameN  # exact frame index
                image_bac.tStart = t  # local t and not account for scr refresh
                image_bac.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_bac, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_bac.started')
                # update status
                image_bac.status = STARTED
                image_bac.setAutoDraw(True)
            
            # if image_bac is active this frame...
            if image_bac.status == STARTED:
                # update params
                pass
            
            # *n_value* updates
            
            # if n_value is starting this frame...
            if n_value.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                n_value.frameNStart = frameN  # exact frame index
                n_value.tStart = t  # local t and not account for scr refresh
                n_value.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(n_value, 'tStartRefresh')  # time at next scr refresh
                # update status
                n_value.status = STARTED
                n_value.setAutoDraw(True)
            
            # if n_value is active this frame...
            if n_value.status == STARTED:
                # update params
                pass
            
            # *num* updates
            
            # if num is starting this frame...
            if num.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                num.frameNStart = frameN  # exact frame index
                num.tStart = t  # local t and not account for scr refresh
                num.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(num, 'tStartRefresh')  # time at next scr refresh
                # update status
                num.status = STARTED
                num.setAutoDraw(True)
            
            # if num is active this frame...
            if num.status == STARTED:
                # update params
                pass
            
            # *testnum* updates
            
            # if testnum is starting this frame...
            if testnum.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                testnum.frameNStart = frameN  # exact frame index
                testnum.tStart = t  # local t and not account for scr refresh
                testnum.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(testnum, 'tStartRefresh')  # time at next scr refresh
                # update status
                testnum.status = STARTED
                testnum.setAutoDraw(True)
            
            # if testnum is active this frame...
            if testnum.status == STARTED:
                # update params
                pass
            
            # *thisimage* updates
            
            # if thisimage is starting this frame...
            if thisimage.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                thisimage.frameNStart = frameN  # exact frame index
                thisimage.tStart = t  # local t and not account for scr refresh
                thisimage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(thisimage, 'tStartRefresh')  # time at next scr refresh
                # update status
                thisimage.status = STARTED
                thisimage.setAutoDraw(True)
            
            # if thisimage is active this frame...
            if thisimage.status == STARTED:
                # update params
                thisimage.setImage(this_image, log=False)
            
            # if thisimage is stopping this frame...
            if thisimage.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > thisimage.tStartRefresh + duration-frameTolerance:
                    # keep track of stop time/frame for later
                    thisimage.tStop = t  # not accounting for scr refresh
                    thisimage.tStopRefresh = tThisFlipGlobal  # on global time
                    thisimage.frameNStop = frameN  # exact frame index
                    # update status
                    thisimage.status = FINISHED
                    thisimage.setAutoDraw(False)
            
            # *key_resp_2* updates
            
            # if key_resp_2 is starting this frame...
            if key_resp_2.status == NOT_STARTED and t >= 0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                key_resp_2.clock.reset()  # now t=0
                key_resp_2.clearEvents(eventType='keyboard')
            if key_resp_2.status == STARTED:
                theseKeys = key_resp_2.getKeys(keyList=['f','j'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[0].name  # just the first key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[0].rt
                    key_resp_2.duration = _key_resp_2_allKeys[0].duration
                    # was this correct?
                    if (key_resp_2.keys == str(ans)) or (key_resp_2.keys == ans):
                        key_resp_2.corr = 1
                    else:
                        key_resp_2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # if sound_true is starting this frame...
            if sound_true.status == NOT_STARTED and response==True:
                # keep track of start time/frame for later
                sound_true.frameNStart = frameN  # exact frame index
                sound_true.tStart = t  # local t and not account for scr refresh
                sound_true.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound_true.status = STARTED
                sound_true.play(when=win)  # sync with win flip
            
            # if sound_true is stopping this frame...
            if sound_true.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_true.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_true.tStop = t  # not accounting for scr refresh
                    sound_true.tStopRefresh = tThisFlipGlobal  # on global time
                    sound_true.frameNStop = frameN  # exact frame index
                    # update status
                    sound_true.status = FINISHED
                    sound_true.stop()
            # update sound_true status according to whether it's playing
            if sound_true.isPlaying:
                sound_true.status = STARTED
            elif sound_true.isFinished:
                sound_true.status = FINISHED
            
            # if sound_false is starting this frame...
            if sound_false.status == NOT_STARTED and response==False:
                # keep track of start time/frame for later
                sound_false.frameNStart = frameN  # exact frame index
                sound_false.tStart = t  # local t and not account for scr refresh
                sound_false.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound_false.status = STARTED
                sound_false.play(when=win)  # sync with win flip
            
            # if sound_false is stopping this frame...
            if sound_false.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_false.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_false.tStop = t  # not accounting for scr refresh
                    sound_false.tStopRefresh = tThisFlipGlobal  # on global time
                    sound_false.frameNStop = frameN  # exact frame index
                    # update status
                    sound_false.status = FINISHED
                    sound_false.stop()
            # update sound_false status according to whether it's playing
            if sound_false.isPlaying:
                sound_false.status = STARTED
            elif sound_false.isFinished:
                sound_false.status = FINISHED
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in StimComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Stim" ---
        for thisComponent in StimComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Stim.stopped', globalClock.getTime(format='float'))
        # Run 'End Routine' code from code_exe
        numcount += 1
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
            # was no response the correct answer?!
            if str(ans).lower() == 'none':
               key_resp_2.corr = 1;  # correct non-response
            else:
               key_resp_2.corr = 0;  # failed to respond (incorrectly)
        # store data for condition9 (TrialHandler)
        condition9.addData('key_resp_2.keys',key_resp_2.keys)
        condition9.addData('key_resp_2.corr', key_resp_2.corr)
        if key_resp_2.keys != None:  # we had a response
            condition9.addData('key_resp_2.rt', key_resp_2.rt)
            condition9.addData('key_resp_2.duration', key_resp_2.duration)
        sound_true.pause()  # ensure sound has stopped at end of Routine
        sound_false.pause()  # ensure sound has stopped at end of Routine
        # the Routine "Stim" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedback" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('feedback.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from feedback_code
        shuffle(fixation_list)
        fiximg = fixation_list[0]
        
        
        #监听按键信息并给出反馈
        if key_resp_2.corr:
            response = True
            msg = '答对了!'
            msgcolor = 'green'
        
        else : 
            response = False
            msg = '答错了!'
            msgcolor = 'red'
        
        
        
        msg_response.setColor(msgcolor, colorSpace='rgb')
        msg_response.setText(msg)
        fixation_img.setImage(fiximg)
        # keep track of which components have finished
        feedbackComponents = [image_bac_2, msg_response, fixation_img]
        for thisComponent in feedbackComponents:
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
        
        # --- Run Routine "feedback" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_bac_2* updates
            
            # if image_bac_2 is starting this frame...
            if image_bac_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                image_bac_2.frameNStart = frameN  # exact frame index
                image_bac_2.tStart = t  # local t and not account for scr refresh
                image_bac_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_bac_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_bac_2.started')
                # update status
                image_bac_2.status = STARTED
                image_bac_2.setAutoDraw(True)
            
            # if image_bac_2 is active this frame...
            if image_bac_2.status == STARTED:
                # update params
                pass
            
            # if image_bac_2 is stopping this frame...
            if image_bac_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_bac_2.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_bac_2.tStop = t  # not accounting for scr refresh
                    image_bac_2.tStopRefresh = tThisFlipGlobal  # on global time
                    image_bac_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_bac_2.stopped')
                    # update status
                    image_bac_2.status = FINISHED
                    image_bac_2.setAutoDraw(False)
            
            # *msg_response* updates
            
            # if msg_response is starting this frame...
            if msg_response.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                msg_response.frameNStart = frameN  # exact frame index
                msg_response.tStart = t  # local t and not account for scr refresh
                msg_response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(msg_response, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'msg_response.started')
                # update status
                msg_response.status = STARTED
                msg_response.setAutoDraw(True)
            
            # if msg_response is active this frame...
            if msg_response.status == STARTED:
                # update params
                pass
            
            # if msg_response is stopping this frame...
            if msg_response.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > msg_response.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    msg_response.tStop = t  # not accounting for scr refresh
                    msg_response.tStopRefresh = tThisFlipGlobal  # on global time
                    msg_response.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'msg_response.stopped')
                    # update status
                    msg_response.status = FINISHED
                    msg_response.setAutoDraw(False)
            
            # *fixation_img* updates
            
            # if fixation_img is starting this frame...
            if fixation_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_img.frameNStart = frameN  # exact frame index
                fixation_img.tStart = t  # local t and not account for scr refresh
                fixation_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_img, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_img.started')
                # update status
                fixation_img.status = STARTED
                fixation_img.setAutoDraw(True)
            
            # if fixation_img is active this frame...
            if fixation_img.status == STARTED:
                # update params
                pass
            
            # if fixation_img is stopping this frame...
            if fixation_img.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_img.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_img.tStop = t  # not accounting for scr refresh
                    fixation_img.tStopRefresh = tThisFlipGlobal  # on global time
                    fixation_img.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_img.stopped')
                    # update status
                    fixation_img.status = FINISHED
                    fixation_img.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback" ---
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('feedback.stopped', globalClock.getTime(format='float'))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 30.0 repeats of 'condition9'
    
    
    # --- Prepare to start Routine "prepare" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('prepare.started', globalClock.getTime(format='float'))
    # Run 'Begin Routine' code from anslist_code
    # set environment
    numcount = 1
    num_i = 0
    piccenpos_cr = [166, 0, -166]
    piccenpos_ar = [166, 0, -166]
    
    # select condition
    condition = conditions.pop()
    i, n, image_list, fixation_list = condition
    num_i = i
    
    # add condition details to data document
    condi = {
        'i=': i,
        'n=': n,
        'len=': len(image_list),
        'fix=': len(fixation_list)
    }
    thisExp.addData('condition', condi)
    print('第',i,'组','N值', n, '图表长度', len(image_list), '注视点表长度', len(fixation_list))
    
    # analyze the image list
    pre_img = []
    rom_imgs = image_list.copy()
    for _ in range(n):
        temp = random.choice(rom_imgs)
        pre_img.append(temp)
        rom_imgs.remove(temp)
    
    # 生成匹配刺激列表 match_list
    match_list = []
    ram = range(9 * n)
    for _ in ram:
        match_image = random.choice(image_list)
        match_list.append([match_image, match_image])
    for item in match_list:
        temp = image_list.copy()
        n1 = n
        while n1 > 1:
            temp.remove(item[n - n1])
            item.insert(n - n1 + 1, random.choice(temp))
            n1 -= 1
    
    # 生成刺激列表 stim_list
    stim_list_pre = match_list.copy()  # 复制匹配刺激列表作为基础
    remaining = 45 - len(match_list) * (n + 1)  # 剩余待插入元素的数量
    while remaining > 0:
        new_image = random.choice(image_list)
        index = random.randint(0, len(stim_list_pre))  # 随机选择插入位置
        if index < n:
            stim_list_pre.insert(index, [new_image])  # 在选择的位置插入新元素
            remaining -= 1
        elif index < len(stim_list_pre):
            prev_image = stim_list_pre[index - n][0]
            next_image = stim_list_pre[index][0]
    
            if new_image != prev_image and new_image != next_image:
                stim_list_pre.insert(index, [new_image])  # 在选择的位置插入新元素
                remaining -= 1
        else:
            if new_image != stim_list_pre[index - n][0]:
                stim_list_pre.insert(index, [new_image])
                remaining -= 1
    
    stim_list = []
    # 迭代遍历原始刺激列表拆包
    for stim in stim_list_pre:
        if len(stim) > 1:  # 成对的元素
            for s in stim:
                stim_list.append(s)
        else:  # 单个元素
            stim_list.append(stim[0])
    
    # 计算转换后列表中的元素数量
    num_elements = len(stim_list)
    
    # 复制 stim_list 生成 answer_list
    answer_list = []
    
    if n == 1:
        preimg_list=['01.png']
    else:
        preimg_list=['01.png','02.png']
        
    allimg_list = preimg_list + stim_list
    #anscount = 0
    for i in range(n, len(allimg_list)):
        if allimg_list[i] == allimg_list[i - n]:
            answer_list.append('f')
            #anscount += 1
        else:
            answer_list.append('j')
            
    if n == 1:
        ncolor = 'yellow'
        ntext = '-1-'
    else :
        ncolor = 'purple'
        ntext = '-2-'
        
    #print("before experiment stim_list:", stim_list)
    #print("before experiment answer_list:",answer_list)
    key_resp_6.keys = []
    key_resp_6.rt = []
    _key_resp_6_allKeys = []
    pic_01png_2.setImage('01.png')
    pic_02png_2.setImage('02.png')
    # keep track of which components have finished
    prepareComponents = [key_resp_6, ins_1back, ins_2back, pic_01png_2, pic_02png_2]
    for thisComponent in prepareComponents:
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
    
    # --- Run Routine "prepare" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_6* updates
        waitOnFlip = False
        
        # if key_resp_6 is starting this frame...
        if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.tStart = t  # local t and not account for scr refresh
            key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_6.started')
            # update status
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_6.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_6.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_6_allKeys.extend(theseKeys)
            if len(_key_resp_6_allKeys):
                key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                key_resp_6.duration = _key_resp_6_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *ins_1back* updates
        
        # if ins_1back is starting this frame...
        if ins_1back.status == NOT_STARTED and n ==1:
            # keep track of start time/frame for later
            ins_1back.frameNStart = frameN  # exact frame index
            ins_1back.tStart = t  # local t and not account for scr refresh
            ins_1back.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ins_1back, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ins_1back.started')
            # update status
            ins_1back.status = STARTED
            ins_1back.setAutoDraw(True)
        
        # if ins_1back is active this frame...
        if ins_1back.status == STARTED:
            # update params
            pass
        
        # *ins_2back* updates
        
        # if ins_2back is starting this frame...
        if ins_2back.status == NOT_STARTED and n ==2:
            # keep track of start time/frame for later
            ins_2back.frameNStart = frameN  # exact frame index
            ins_2back.tStart = t  # local t and not account for scr refresh
            ins_2back.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ins_2back, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ins_2back.started')
            # update status
            ins_2back.status = STARTED
            ins_2back.setAutoDraw(True)
        
        # if ins_2back is active this frame...
        if ins_2back.status == STARTED:
            # update params
            pass
        
        # *pic_01png_2* updates
        
        # if pic_01png_2 is starting this frame...
        if pic_01png_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            pic_01png_2.frameNStart = frameN  # exact frame index
            pic_01png_2.tStart = t  # local t and not account for scr refresh
            pic_01png_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pic_01png_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pic_01png_2.started')
            # update status
            pic_01png_2.status = STARTED
            pic_01png_2.setAutoDraw(True)
        
        # if pic_01png_2 is active this frame...
        if pic_01png_2.status == STARTED:
            # update params
            pass
        
        # *pic_02png_2* updates
        
        # if pic_02png_2 is starting this frame...
        if pic_02png_2.status == NOT_STARTED and n == 2:
            # keep track of start time/frame for later
            pic_02png_2.frameNStart = frameN  # exact frame index
            pic_02png_2.tStart = t  # local t and not account for scr refresh
            pic_02png_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pic_02png_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pic_02png_2.started')
            # update status
            pic_02png_2.status = STARTED
            pic_02png_2.setAutoDraw(True)
        
        # if pic_02png_2 is active this frame...
        if pic_02png_2.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prepareComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prepare" ---
    for thisComponent in prepareComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('prepare.stopped', globalClock.getTime(format='float'))
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys = None
    thisExp.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        thisExp.addData('key_resp_6.rt', key_resp_6.rt)
        thisExp.addData('key_resp_6.duration', key_resp_6.duration)
    thisExp.nextEntry()
    # the Routine "prepare" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    condition8 = data.TrialHandler(nReps=30.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='condition8')
    thisExp.addLoop(condition8)  # add the loop to the experiment
    thisCondition8 = condition8.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCondition8.rgb)
    if thisCondition8 != None:
        for paramName in thisCondition8:
            globals()[paramName] = thisCondition8[paramName]
    
    for thisCondition8 in condition8:
        currentLoop = condition8
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisCondition8.rgb)
        if thisCondition8 != None:
            for paramName in thisCondition8:
                globals()[paramName] = thisCondition8[paramName]
        
        # --- Prepare to start Routine "Stim" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Stim.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from code_exe
        this_number = numcount
        this_image = stim_list[numcount-1]
        duration = 0.5
        if num_i == 10:
            duration = 0.3
        if num_i == 9:
            duration = 0.3
        if num_i == 2:
            duration = 0.3
        if num_i == 1:
            duration = 0.3
        if num_i == 4:
            duration = 0.3
        if num_i == 3:
            duration = 0.3
        response = ''
        #the central position of picture
        shuffle(piccenpos_cr)
        shuffle(piccenpos_ar)
        piccenpos = (piccenpos_cr[0], piccenpos_ar[0])
        
        ans = answer_list[numcount-1]
        thisExp.addData('ans', ans)
        print("begin routine ","count",numcount,"img",this_image,"ans",ans)
        
        if key_resp_2.corr:
            response = True
        
        else : 
            response = False
        n_value.setColor(ncolor, colorSpace='rgb')
        n_value.setText(ntext)
        testnum.setText(this_number)
        thisimage.setPos(piccenpos)
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        sound_true.setSound('A', secs=0.1, hamming=True)
        sound_true.setVolume(2.0, log=False)
        sound_true.seek(0)
        sound_false.setSound('B', secs=0.2, hamming=False)
        sound_false.setVolume(4.0, log=False)
        sound_false.seek(0)
        # keep track of which components have finished
        StimComponents = [image_bac, n_value, num, testnum, thisimage, key_resp_2, sound_true, sound_false]
        for thisComponent in StimComponents:
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
        
        # --- Run Routine "Stim" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_bac* updates
            
            # if image_bac is starting this frame...
            if image_bac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_bac.frameNStart = frameN  # exact frame index
                image_bac.tStart = t  # local t and not account for scr refresh
                image_bac.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_bac, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_bac.started')
                # update status
                image_bac.status = STARTED
                image_bac.setAutoDraw(True)
            
            # if image_bac is active this frame...
            if image_bac.status == STARTED:
                # update params
                pass
            
            # *n_value* updates
            
            # if n_value is starting this frame...
            if n_value.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                n_value.frameNStart = frameN  # exact frame index
                n_value.tStart = t  # local t and not account for scr refresh
                n_value.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(n_value, 'tStartRefresh')  # time at next scr refresh
                # update status
                n_value.status = STARTED
                n_value.setAutoDraw(True)
            
            # if n_value is active this frame...
            if n_value.status == STARTED:
                # update params
                pass
            
            # *num* updates
            
            # if num is starting this frame...
            if num.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                num.frameNStart = frameN  # exact frame index
                num.tStart = t  # local t and not account for scr refresh
                num.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(num, 'tStartRefresh')  # time at next scr refresh
                # update status
                num.status = STARTED
                num.setAutoDraw(True)
            
            # if num is active this frame...
            if num.status == STARTED:
                # update params
                pass
            
            # *testnum* updates
            
            # if testnum is starting this frame...
            if testnum.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                testnum.frameNStart = frameN  # exact frame index
                testnum.tStart = t  # local t and not account for scr refresh
                testnum.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(testnum, 'tStartRefresh')  # time at next scr refresh
                # update status
                testnum.status = STARTED
                testnum.setAutoDraw(True)
            
            # if testnum is active this frame...
            if testnum.status == STARTED:
                # update params
                pass
            
            # *thisimage* updates
            
            # if thisimage is starting this frame...
            if thisimage.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                thisimage.frameNStart = frameN  # exact frame index
                thisimage.tStart = t  # local t and not account for scr refresh
                thisimage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(thisimage, 'tStartRefresh')  # time at next scr refresh
                # update status
                thisimage.status = STARTED
                thisimage.setAutoDraw(True)
            
            # if thisimage is active this frame...
            if thisimage.status == STARTED:
                # update params
                thisimage.setImage(this_image, log=False)
            
            # if thisimage is stopping this frame...
            if thisimage.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > thisimage.tStartRefresh + duration-frameTolerance:
                    # keep track of stop time/frame for later
                    thisimage.tStop = t  # not accounting for scr refresh
                    thisimage.tStopRefresh = tThisFlipGlobal  # on global time
                    thisimage.frameNStop = frameN  # exact frame index
                    # update status
                    thisimage.status = FINISHED
                    thisimage.setAutoDraw(False)
            
            # *key_resp_2* updates
            
            # if key_resp_2 is starting this frame...
            if key_resp_2.status == NOT_STARTED and t >= 0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                key_resp_2.clock.reset()  # now t=0
                key_resp_2.clearEvents(eventType='keyboard')
            if key_resp_2.status == STARTED:
                theseKeys = key_resp_2.getKeys(keyList=['f','j'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[0].name  # just the first key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[0].rt
                    key_resp_2.duration = _key_resp_2_allKeys[0].duration
                    # was this correct?
                    if (key_resp_2.keys == str(ans)) or (key_resp_2.keys == ans):
                        key_resp_2.corr = 1
                    else:
                        key_resp_2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # if sound_true is starting this frame...
            if sound_true.status == NOT_STARTED and response==True:
                # keep track of start time/frame for later
                sound_true.frameNStart = frameN  # exact frame index
                sound_true.tStart = t  # local t and not account for scr refresh
                sound_true.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound_true.status = STARTED
                sound_true.play(when=win)  # sync with win flip
            
            # if sound_true is stopping this frame...
            if sound_true.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_true.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_true.tStop = t  # not accounting for scr refresh
                    sound_true.tStopRefresh = tThisFlipGlobal  # on global time
                    sound_true.frameNStop = frameN  # exact frame index
                    # update status
                    sound_true.status = FINISHED
                    sound_true.stop()
            # update sound_true status according to whether it's playing
            if sound_true.isPlaying:
                sound_true.status = STARTED
            elif sound_true.isFinished:
                sound_true.status = FINISHED
            
            # if sound_false is starting this frame...
            if sound_false.status == NOT_STARTED and response==False:
                # keep track of start time/frame for later
                sound_false.frameNStart = frameN  # exact frame index
                sound_false.tStart = t  # local t and not account for scr refresh
                sound_false.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound_false.status = STARTED
                sound_false.play(when=win)  # sync with win flip
            
            # if sound_false is stopping this frame...
            if sound_false.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_false.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_false.tStop = t  # not accounting for scr refresh
                    sound_false.tStopRefresh = tThisFlipGlobal  # on global time
                    sound_false.frameNStop = frameN  # exact frame index
                    # update status
                    sound_false.status = FINISHED
                    sound_false.stop()
            # update sound_false status according to whether it's playing
            if sound_false.isPlaying:
                sound_false.status = STARTED
            elif sound_false.isFinished:
                sound_false.status = FINISHED
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in StimComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Stim" ---
        for thisComponent in StimComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Stim.stopped', globalClock.getTime(format='float'))
        # Run 'End Routine' code from code_exe
        numcount += 1
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
            # was no response the correct answer?!
            if str(ans).lower() == 'none':
               key_resp_2.corr = 1;  # correct non-response
            else:
               key_resp_2.corr = 0;  # failed to respond (incorrectly)
        # store data for condition8 (TrialHandler)
        condition8.addData('key_resp_2.keys',key_resp_2.keys)
        condition8.addData('key_resp_2.corr', key_resp_2.corr)
        if key_resp_2.keys != None:  # we had a response
            condition8.addData('key_resp_2.rt', key_resp_2.rt)
            condition8.addData('key_resp_2.duration', key_resp_2.duration)
        sound_true.pause()  # ensure sound has stopped at end of Routine
        sound_false.pause()  # ensure sound has stopped at end of Routine
        # the Routine "Stim" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedback" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('feedback.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from feedback_code
        shuffle(fixation_list)
        fiximg = fixation_list[0]
        
        
        #监听按键信息并给出反馈
        if key_resp_2.corr:
            response = True
            msg = '答对了!'
            msgcolor = 'green'
        
        else : 
            response = False
            msg = '答错了!'
            msgcolor = 'red'
        
        
        
        msg_response.setColor(msgcolor, colorSpace='rgb')
        msg_response.setText(msg)
        fixation_img.setImage(fiximg)
        # keep track of which components have finished
        feedbackComponents = [image_bac_2, msg_response, fixation_img]
        for thisComponent in feedbackComponents:
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
        
        # --- Run Routine "feedback" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_bac_2* updates
            
            # if image_bac_2 is starting this frame...
            if image_bac_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                image_bac_2.frameNStart = frameN  # exact frame index
                image_bac_2.tStart = t  # local t and not account for scr refresh
                image_bac_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_bac_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_bac_2.started')
                # update status
                image_bac_2.status = STARTED
                image_bac_2.setAutoDraw(True)
            
            # if image_bac_2 is active this frame...
            if image_bac_2.status == STARTED:
                # update params
                pass
            
            # if image_bac_2 is stopping this frame...
            if image_bac_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_bac_2.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_bac_2.tStop = t  # not accounting for scr refresh
                    image_bac_2.tStopRefresh = tThisFlipGlobal  # on global time
                    image_bac_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_bac_2.stopped')
                    # update status
                    image_bac_2.status = FINISHED
                    image_bac_2.setAutoDraw(False)
            
            # *msg_response* updates
            
            # if msg_response is starting this frame...
            if msg_response.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                msg_response.frameNStart = frameN  # exact frame index
                msg_response.tStart = t  # local t and not account for scr refresh
                msg_response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(msg_response, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'msg_response.started')
                # update status
                msg_response.status = STARTED
                msg_response.setAutoDraw(True)
            
            # if msg_response is active this frame...
            if msg_response.status == STARTED:
                # update params
                pass
            
            # if msg_response is stopping this frame...
            if msg_response.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > msg_response.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    msg_response.tStop = t  # not accounting for scr refresh
                    msg_response.tStopRefresh = tThisFlipGlobal  # on global time
                    msg_response.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'msg_response.stopped')
                    # update status
                    msg_response.status = FINISHED
                    msg_response.setAutoDraw(False)
            
            # *fixation_img* updates
            
            # if fixation_img is starting this frame...
            if fixation_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_img.frameNStart = frameN  # exact frame index
                fixation_img.tStart = t  # local t and not account for scr refresh
                fixation_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_img, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_img.started')
                # update status
                fixation_img.status = STARTED
                fixation_img.setAutoDraw(True)
            
            # if fixation_img is active this frame...
            if fixation_img.status == STARTED:
                # update params
                pass
            
            # if fixation_img is stopping this frame...
            if fixation_img.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_img.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_img.tStop = t  # not accounting for scr refresh
                    fixation_img.tStopRefresh = tThisFlipGlobal  # on global time
                    fixation_img.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_img.stopped')
                    # update status
                    fixation_img.status = FINISHED
                    fixation_img.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback" ---
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('feedback.stopped', globalClock.getTime(format='float'))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 30.0 repeats of 'condition8'
    
    
    # --- Prepare to start Routine "prepare" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('prepare.started', globalClock.getTime(format='float'))
    # Run 'Begin Routine' code from anslist_code
    # set environment
    numcount = 1
    num_i = 0
    piccenpos_cr = [166, 0, -166]
    piccenpos_ar = [166, 0, -166]
    
    # select condition
    condition = conditions.pop()
    i, n, image_list, fixation_list = condition
    num_i = i
    
    # add condition details to data document
    condi = {
        'i=': i,
        'n=': n,
        'len=': len(image_list),
        'fix=': len(fixation_list)
    }
    thisExp.addData('condition', condi)
    print('第',i,'组','N值', n, '图表长度', len(image_list), '注视点表长度', len(fixation_list))
    
    # analyze the image list
    pre_img = []
    rom_imgs = image_list.copy()
    for _ in range(n):
        temp = random.choice(rom_imgs)
        pre_img.append(temp)
        rom_imgs.remove(temp)
    
    # 生成匹配刺激列表 match_list
    match_list = []
    ram = range(9 * n)
    for _ in ram:
        match_image = random.choice(image_list)
        match_list.append([match_image, match_image])
    for item in match_list:
        temp = image_list.copy()
        n1 = n
        while n1 > 1:
            temp.remove(item[n - n1])
            item.insert(n - n1 + 1, random.choice(temp))
            n1 -= 1
    
    # 生成刺激列表 stim_list
    stim_list_pre = match_list.copy()  # 复制匹配刺激列表作为基础
    remaining = 45 - len(match_list) * (n + 1)  # 剩余待插入元素的数量
    while remaining > 0:
        new_image = random.choice(image_list)
        index = random.randint(0, len(stim_list_pre))  # 随机选择插入位置
        if index < n:
            stim_list_pre.insert(index, [new_image])  # 在选择的位置插入新元素
            remaining -= 1
        elif index < len(stim_list_pre):
            prev_image = stim_list_pre[index - n][0]
            next_image = stim_list_pre[index][0]
    
            if new_image != prev_image and new_image != next_image:
                stim_list_pre.insert(index, [new_image])  # 在选择的位置插入新元素
                remaining -= 1
        else:
            if new_image != stim_list_pre[index - n][0]:
                stim_list_pre.insert(index, [new_image])
                remaining -= 1
    
    stim_list = []
    # 迭代遍历原始刺激列表拆包
    for stim in stim_list_pre:
        if len(stim) > 1:  # 成对的元素
            for s in stim:
                stim_list.append(s)
        else:  # 单个元素
            stim_list.append(stim[0])
    
    # 计算转换后列表中的元素数量
    num_elements = len(stim_list)
    
    # 复制 stim_list 生成 answer_list
    answer_list = []
    
    if n == 1:
        preimg_list=['01.png']
    else:
        preimg_list=['01.png','02.png']
        
    allimg_list = preimg_list + stim_list
    #anscount = 0
    for i in range(n, len(allimg_list)):
        if allimg_list[i] == allimg_list[i - n]:
            answer_list.append('f')
            #anscount += 1
        else:
            answer_list.append('j')
            
    if n == 1:
        ncolor = 'yellow'
        ntext = '-1-'
    else :
        ncolor = 'purple'
        ntext = '-2-'
        
    #print("before experiment stim_list:", stim_list)
    #print("before experiment answer_list:",answer_list)
    key_resp_6.keys = []
    key_resp_6.rt = []
    _key_resp_6_allKeys = []
    pic_01png_2.setImage('01.png')
    pic_02png_2.setImage('02.png')
    # keep track of which components have finished
    prepareComponents = [key_resp_6, ins_1back, ins_2back, pic_01png_2, pic_02png_2]
    for thisComponent in prepareComponents:
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
    
    # --- Run Routine "prepare" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_6* updates
        waitOnFlip = False
        
        # if key_resp_6 is starting this frame...
        if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.tStart = t  # local t and not account for scr refresh
            key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_6.started')
            # update status
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_6.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_6.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_6_allKeys.extend(theseKeys)
            if len(_key_resp_6_allKeys):
                key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                key_resp_6.duration = _key_resp_6_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *ins_1back* updates
        
        # if ins_1back is starting this frame...
        if ins_1back.status == NOT_STARTED and n ==1:
            # keep track of start time/frame for later
            ins_1back.frameNStart = frameN  # exact frame index
            ins_1back.tStart = t  # local t and not account for scr refresh
            ins_1back.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ins_1back, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ins_1back.started')
            # update status
            ins_1back.status = STARTED
            ins_1back.setAutoDraw(True)
        
        # if ins_1back is active this frame...
        if ins_1back.status == STARTED:
            # update params
            pass
        
        # *ins_2back* updates
        
        # if ins_2back is starting this frame...
        if ins_2back.status == NOT_STARTED and n ==2:
            # keep track of start time/frame for later
            ins_2back.frameNStart = frameN  # exact frame index
            ins_2back.tStart = t  # local t and not account for scr refresh
            ins_2back.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ins_2back, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ins_2back.started')
            # update status
            ins_2back.status = STARTED
            ins_2back.setAutoDraw(True)
        
        # if ins_2back is active this frame...
        if ins_2back.status == STARTED:
            # update params
            pass
        
        # *pic_01png_2* updates
        
        # if pic_01png_2 is starting this frame...
        if pic_01png_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            pic_01png_2.frameNStart = frameN  # exact frame index
            pic_01png_2.tStart = t  # local t and not account for scr refresh
            pic_01png_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pic_01png_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pic_01png_2.started')
            # update status
            pic_01png_2.status = STARTED
            pic_01png_2.setAutoDraw(True)
        
        # if pic_01png_2 is active this frame...
        if pic_01png_2.status == STARTED:
            # update params
            pass
        
        # *pic_02png_2* updates
        
        # if pic_02png_2 is starting this frame...
        if pic_02png_2.status == NOT_STARTED and n == 2:
            # keep track of start time/frame for later
            pic_02png_2.frameNStart = frameN  # exact frame index
            pic_02png_2.tStart = t  # local t and not account for scr refresh
            pic_02png_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pic_02png_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pic_02png_2.started')
            # update status
            pic_02png_2.status = STARTED
            pic_02png_2.setAutoDraw(True)
        
        # if pic_02png_2 is active this frame...
        if pic_02png_2.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prepareComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prepare" ---
    for thisComponent in prepareComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('prepare.stopped', globalClock.getTime(format='float'))
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys = None
    thisExp.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        thisExp.addData('key_resp_6.rt', key_resp_6.rt)
        thisExp.addData('key_resp_6.duration', key_resp_6.duration)
    thisExp.nextEntry()
    # the Routine "prepare" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    condition7 = data.TrialHandler(nReps=30.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='condition7')
    thisExp.addLoop(condition7)  # add the loop to the experiment
    thisCondition7 = condition7.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCondition7.rgb)
    if thisCondition7 != None:
        for paramName in thisCondition7:
            globals()[paramName] = thisCondition7[paramName]
    
    for thisCondition7 in condition7:
        currentLoop = condition7
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisCondition7.rgb)
        if thisCondition7 != None:
            for paramName in thisCondition7:
                globals()[paramName] = thisCondition7[paramName]
        
        # --- Prepare to start Routine "Stim" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Stim.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from code_exe
        this_number = numcount
        this_image = stim_list[numcount-1]
        duration = 0.5
        if num_i == 10:
            duration = 0.3
        if num_i == 9:
            duration = 0.3
        if num_i == 2:
            duration = 0.3
        if num_i == 1:
            duration = 0.3
        if num_i == 4:
            duration = 0.3
        if num_i == 3:
            duration = 0.3
        response = ''
        #the central position of picture
        shuffle(piccenpos_cr)
        shuffle(piccenpos_ar)
        piccenpos = (piccenpos_cr[0], piccenpos_ar[0])
        
        ans = answer_list[numcount-1]
        thisExp.addData('ans', ans)
        print("begin routine ","count",numcount,"img",this_image,"ans",ans)
        
        if key_resp_2.corr:
            response = True
        
        else : 
            response = False
        n_value.setColor(ncolor, colorSpace='rgb')
        n_value.setText(ntext)
        testnum.setText(this_number)
        thisimage.setPos(piccenpos)
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        sound_true.setSound('A', secs=0.1, hamming=True)
        sound_true.setVolume(2.0, log=False)
        sound_true.seek(0)
        sound_false.setSound('B', secs=0.2, hamming=False)
        sound_false.setVolume(4.0, log=False)
        sound_false.seek(0)
        # keep track of which components have finished
        StimComponents = [image_bac, n_value, num, testnum, thisimage, key_resp_2, sound_true, sound_false]
        for thisComponent in StimComponents:
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
        
        # --- Run Routine "Stim" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_bac* updates
            
            # if image_bac is starting this frame...
            if image_bac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_bac.frameNStart = frameN  # exact frame index
                image_bac.tStart = t  # local t and not account for scr refresh
                image_bac.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_bac, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_bac.started')
                # update status
                image_bac.status = STARTED
                image_bac.setAutoDraw(True)
            
            # if image_bac is active this frame...
            if image_bac.status == STARTED:
                # update params
                pass
            
            # *n_value* updates
            
            # if n_value is starting this frame...
            if n_value.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                n_value.frameNStart = frameN  # exact frame index
                n_value.tStart = t  # local t and not account for scr refresh
                n_value.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(n_value, 'tStartRefresh')  # time at next scr refresh
                # update status
                n_value.status = STARTED
                n_value.setAutoDraw(True)
            
            # if n_value is active this frame...
            if n_value.status == STARTED:
                # update params
                pass
            
            # *num* updates
            
            # if num is starting this frame...
            if num.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                num.frameNStart = frameN  # exact frame index
                num.tStart = t  # local t and not account for scr refresh
                num.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(num, 'tStartRefresh')  # time at next scr refresh
                # update status
                num.status = STARTED
                num.setAutoDraw(True)
            
            # if num is active this frame...
            if num.status == STARTED:
                # update params
                pass
            
            # *testnum* updates
            
            # if testnum is starting this frame...
            if testnum.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                testnum.frameNStart = frameN  # exact frame index
                testnum.tStart = t  # local t and not account for scr refresh
                testnum.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(testnum, 'tStartRefresh')  # time at next scr refresh
                # update status
                testnum.status = STARTED
                testnum.setAutoDraw(True)
            
            # if testnum is active this frame...
            if testnum.status == STARTED:
                # update params
                pass
            
            # *thisimage* updates
            
            # if thisimage is starting this frame...
            if thisimage.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                thisimage.frameNStart = frameN  # exact frame index
                thisimage.tStart = t  # local t and not account for scr refresh
                thisimage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(thisimage, 'tStartRefresh')  # time at next scr refresh
                # update status
                thisimage.status = STARTED
                thisimage.setAutoDraw(True)
            
            # if thisimage is active this frame...
            if thisimage.status == STARTED:
                # update params
                thisimage.setImage(this_image, log=False)
            
            # if thisimage is stopping this frame...
            if thisimage.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > thisimage.tStartRefresh + duration-frameTolerance:
                    # keep track of stop time/frame for later
                    thisimage.tStop = t  # not accounting for scr refresh
                    thisimage.tStopRefresh = tThisFlipGlobal  # on global time
                    thisimage.frameNStop = frameN  # exact frame index
                    # update status
                    thisimage.status = FINISHED
                    thisimage.setAutoDraw(False)
            
            # *key_resp_2* updates
            
            # if key_resp_2 is starting this frame...
            if key_resp_2.status == NOT_STARTED and t >= 0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                key_resp_2.clock.reset()  # now t=0
                key_resp_2.clearEvents(eventType='keyboard')
            if key_resp_2.status == STARTED:
                theseKeys = key_resp_2.getKeys(keyList=['f','j'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[0].name  # just the first key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[0].rt
                    key_resp_2.duration = _key_resp_2_allKeys[0].duration
                    # was this correct?
                    if (key_resp_2.keys == str(ans)) or (key_resp_2.keys == ans):
                        key_resp_2.corr = 1
                    else:
                        key_resp_2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # if sound_true is starting this frame...
            if sound_true.status == NOT_STARTED and response==True:
                # keep track of start time/frame for later
                sound_true.frameNStart = frameN  # exact frame index
                sound_true.tStart = t  # local t and not account for scr refresh
                sound_true.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound_true.status = STARTED
                sound_true.play(when=win)  # sync with win flip
            
            # if sound_true is stopping this frame...
            if sound_true.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_true.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_true.tStop = t  # not accounting for scr refresh
                    sound_true.tStopRefresh = tThisFlipGlobal  # on global time
                    sound_true.frameNStop = frameN  # exact frame index
                    # update status
                    sound_true.status = FINISHED
                    sound_true.stop()
            # update sound_true status according to whether it's playing
            if sound_true.isPlaying:
                sound_true.status = STARTED
            elif sound_true.isFinished:
                sound_true.status = FINISHED
            
            # if sound_false is starting this frame...
            if sound_false.status == NOT_STARTED and response==False:
                # keep track of start time/frame for later
                sound_false.frameNStart = frameN  # exact frame index
                sound_false.tStart = t  # local t and not account for scr refresh
                sound_false.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound_false.status = STARTED
                sound_false.play(when=win)  # sync with win flip
            
            # if sound_false is stopping this frame...
            if sound_false.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_false.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_false.tStop = t  # not accounting for scr refresh
                    sound_false.tStopRefresh = tThisFlipGlobal  # on global time
                    sound_false.frameNStop = frameN  # exact frame index
                    # update status
                    sound_false.status = FINISHED
                    sound_false.stop()
            # update sound_false status according to whether it's playing
            if sound_false.isPlaying:
                sound_false.status = STARTED
            elif sound_false.isFinished:
                sound_false.status = FINISHED
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in StimComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Stim" ---
        for thisComponent in StimComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Stim.stopped', globalClock.getTime(format='float'))
        # Run 'End Routine' code from code_exe
        numcount += 1
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
            # was no response the correct answer?!
            if str(ans).lower() == 'none':
               key_resp_2.corr = 1;  # correct non-response
            else:
               key_resp_2.corr = 0;  # failed to respond (incorrectly)
        # store data for condition7 (TrialHandler)
        condition7.addData('key_resp_2.keys',key_resp_2.keys)
        condition7.addData('key_resp_2.corr', key_resp_2.corr)
        if key_resp_2.keys != None:  # we had a response
            condition7.addData('key_resp_2.rt', key_resp_2.rt)
            condition7.addData('key_resp_2.duration', key_resp_2.duration)
        sound_true.pause()  # ensure sound has stopped at end of Routine
        sound_false.pause()  # ensure sound has stopped at end of Routine
        # the Routine "Stim" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedback" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('feedback.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from feedback_code
        shuffle(fixation_list)
        fiximg = fixation_list[0]
        
        
        #监听按键信息并给出反馈
        if key_resp_2.corr:
            response = True
            msg = '答对了!'
            msgcolor = 'green'
        
        else : 
            response = False
            msg = '答错了!'
            msgcolor = 'red'
        
        
        
        msg_response.setColor(msgcolor, colorSpace='rgb')
        msg_response.setText(msg)
        fixation_img.setImage(fiximg)
        # keep track of which components have finished
        feedbackComponents = [image_bac_2, msg_response, fixation_img]
        for thisComponent in feedbackComponents:
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
        
        # --- Run Routine "feedback" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_bac_2* updates
            
            # if image_bac_2 is starting this frame...
            if image_bac_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                image_bac_2.frameNStart = frameN  # exact frame index
                image_bac_2.tStart = t  # local t and not account for scr refresh
                image_bac_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_bac_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_bac_2.started')
                # update status
                image_bac_2.status = STARTED
                image_bac_2.setAutoDraw(True)
            
            # if image_bac_2 is active this frame...
            if image_bac_2.status == STARTED:
                # update params
                pass
            
            # if image_bac_2 is stopping this frame...
            if image_bac_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_bac_2.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_bac_2.tStop = t  # not accounting for scr refresh
                    image_bac_2.tStopRefresh = tThisFlipGlobal  # on global time
                    image_bac_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_bac_2.stopped')
                    # update status
                    image_bac_2.status = FINISHED
                    image_bac_2.setAutoDraw(False)
            
            # *msg_response* updates
            
            # if msg_response is starting this frame...
            if msg_response.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                msg_response.frameNStart = frameN  # exact frame index
                msg_response.tStart = t  # local t and not account for scr refresh
                msg_response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(msg_response, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'msg_response.started')
                # update status
                msg_response.status = STARTED
                msg_response.setAutoDraw(True)
            
            # if msg_response is active this frame...
            if msg_response.status == STARTED:
                # update params
                pass
            
            # if msg_response is stopping this frame...
            if msg_response.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > msg_response.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    msg_response.tStop = t  # not accounting for scr refresh
                    msg_response.tStopRefresh = tThisFlipGlobal  # on global time
                    msg_response.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'msg_response.stopped')
                    # update status
                    msg_response.status = FINISHED
                    msg_response.setAutoDraw(False)
            
            # *fixation_img* updates
            
            # if fixation_img is starting this frame...
            if fixation_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_img.frameNStart = frameN  # exact frame index
                fixation_img.tStart = t  # local t and not account for scr refresh
                fixation_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_img, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_img.started')
                # update status
                fixation_img.status = STARTED
                fixation_img.setAutoDraw(True)
            
            # if fixation_img is active this frame...
            if fixation_img.status == STARTED:
                # update params
                pass
            
            # if fixation_img is stopping this frame...
            if fixation_img.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_img.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_img.tStop = t  # not accounting for scr refresh
                    fixation_img.tStopRefresh = tThisFlipGlobal  # on global time
                    fixation_img.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_img.stopped')
                    # update status
                    fixation_img.status = FINISHED
                    fixation_img.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback" ---
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('feedback.stopped', globalClock.getTime(format='float'))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 30.0 repeats of 'condition7'
    
    
    # --- Prepare to start Routine "prepare" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('prepare.started', globalClock.getTime(format='float'))
    # Run 'Begin Routine' code from anslist_code
    # set environment
    numcount = 1
    num_i = 0
    piccenpos_cr = [166, 0, -166]
    piccenpos_ar = [166, 0, -166]
    
    # select condition
    condition = conditions.pop()
    i, n, image_list, fixation_list = condition
    num_i = i
    
    # add condition details to data document
    condi = {
        'i=': i,
        'n=': n,
        'len=': len(image_list),
        'fix=': len(fixation_list)
    }
    thisExp.addData('condition', condi)
    print('第',i,'组','N值', n, '图表长度', len(image_list), '注视点表长度', len(fixation_list))
    
    # analyze the image list
    pre_img = []
    rom_imgs = image_list.copy()
    for _ in range(n):
        temp = random.choice(rom_imgs)
        pre_img.append(temp)
        rom_imgs.remove(temp)
    
    # 生成匹配刺激列表 match_list
    match_list = []
    ram = range(9 * n)
    for _ in ram:
        match_image = random.choice(image_list)
        match_list.append([match_image, match_image])
    for item in match_list:
        temp = image_list.copy()
        n1 = n
        while n1 > 1:
            temp.remove(item[n - n1])
            item.insert(n - n1 + 1, random.choice(temp))
            n1 -= 1
    
    # 生成刺激列表 stim_list
    stim_list_pre = match_list.copy()  # 复制匹配刺激列表作为基础
    remaining = 45 - len(match_list) * (n + 1)  # 剩余待插入元素的数量
    while remaining > 0:
        new_image = random.choice(image_list)
        index = random.randint(0, len(stim_list_pre))  # 随机选择插入位置
        if index < n:
            stim_list_pre.insert(index, [new_image])  # 在选择的位置插入新元素
            remaining -= 1
        elif index < len(stim_list_pre):
            prev_image = stim_list_pre[index - n][0]
            next_image = stim_list_pre[index][0]
    
            if new_image != prev_image and new_image != next_image:
                stim_list_pre.insert(index, [new_image])  # 在选择的位置插入新元素
                remaining -= 1
        else:
            if new_image != stim_list_pre[index - n][0]:
                stim_list_pre.insert(index, [new_image])
                remaining -= 1
    
    stim_list = []
    # 迭代遍历原始刺激列表拆包
    for stim in stim_list_pre:
        if len(stim) > 1:  # 成对的元素
            for s in stim:
                stim_list.append(s)
        else:  # 单个元素
            stim_list.append(stim[0])
    
    # 计算转换后列表中的元素数量
    num_elements = len(stim_list)
    
    # 复制 stim_list 生成 answer_list
    answer_list = []
    
    if n == 1:
        preimg_list=['01.png']
    else:
        preimg_list=['01.png','02.png']
        
    allimg_list = preimg_list + stim_list
    #anscount = 0
    for i in range(n, len(allimg_list)):
        if allimg_list[i] == allimg_list[i - n]:
            answer_list.append('f')
            #anscount += 1
        else:
            answer_list.append('j')
            
    if n == 1:
        ncolor = 'yellow'
        ntext = '-1-'
    else :
        ncolor = 'purple'
        ntext = '-2-'
        
    #print("before experiment stim_list:", stim_list)
    #print("before experiment answer_list:",answer_list)
    key_resp_6.keys = []
    key_resp_6.rt = []
    _key_resp_6_allKeys = []
    pic_01png_2.setImage('01.png')
    pic_02png_2.setImage('02.png')
    # keep track of which components have finished
    prepareComponents = [key_resp_6, ins_1back, ins_2back, pic_01png_2, pic_02png_2]
    for thisComponent in prepareComponents:
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
    
    # --- Run Routine "prepare" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_6* updates
        waitOnFlip = False
        
        # if key_resp_6 is starting this frame...
        if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.tStart = t  # local t and not account for scr refresh
            key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_6.started')
            # update status
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_6.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_6.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_6_allKeys.extend(theseKeys)
            if len(_key_resp_6_allKeys):
                key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                key_resp_6.duration = _key_resp_6_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *ins_1back* updates
        
        # if ins_1back is starting this frame...
        if ins_1back.status == NOT_STARTED and n ==1:
            # keep track of start time/frame for later
            ins_1back.frameNStart = frameN  # exact frame index
            ins_1back.tStart = t  # local t and not account for scr refresh
            ins_1back.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ins_1back, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ins_1back.started')
            # update status
            ins_1back.status = STARTED
            ins_1back.setAutoDraw(True)
        
        # if ins_1back is active this frame...
        if ins_1back.status == STARTED:
            # update params
            pass
        
        # *ins_2back* updates
        
        # if ins_2back is starting this frame...
        if ins_2back.status == NOT_STARTED and n ==2:
            # keep track of start time/frame for later
            ins_2back.frameNStart = frameN  # exact frame index
            ins_2back.tStart = t  # local t and not account for scr refresh
            ins_2back.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ins_2back, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ins_2back.started')
            # update status
            ins_2back.status = STARTED
            ins_2back.setAutoDraw(True)
        
        # if ins_2back is active this frame...
        if ins_2back.status == STARTED:
            # update params
            pass
        
        # *pic_01png_2* updates
        
        # if pic_01png_2 is starting this frame...
        if pic_01png_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            pic_01png_2.frameNStart = frameN  # exact frame index
            pic_01png_2.tStart = t  # local t and not account for scr refresh
            pic_01png_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pic_01png_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pic_01png_2.started')
            # update status
            pic_01png_2.status = STARTED
            pic_01png_2.setAutoDraw(True)
        
        # if pic_01png_2 is active this frame...
        if pic_01png_2.status == STARTED:
            # update params
            pass
        
        # *pic_02png_2* updates
        
        # if pic_02png_2 is starting this frame...
        if pic_02png_2.status == NOT_STARTED and n == 2:
            # keep track of start time/frame for later
            pic_02png_2.frameNStart = frameN  # exact frame index
            pic_02png_2.tStart = t  # local t and not account for scr refresh
            pic_02png_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pic_02png_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pic_02png_2.started')
            # update status
            pic_02png_2.status = STARTED
            pic_02png_2.setAutoDraw(True)
        
        # if pic_02png_2 is active this frame...
        if pic_02png_2.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prepareComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prepare" ---
    for thisComponent in prepareComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('prepare.stopped', globalClock.getTime(format='float'))
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys = None
    thisExp.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        thisExp.addData('key_resp_6.rt', key_resp_6.rt)
        thisExp.addData('key_resp_6.duration', key_resp_6.duration)
    thisExp.nextEntry()
    # the Routine "prepare" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    condition6 = data.TrialHandler(nReps=30.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='condition6')
    thisExp.addLoop(condition6)  # add the loop to the experiment
    thisCondition6 = condition6.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCondition6.rgb)
    if thisCondition6 != None:
        for paramName in thisCondition6:
            globals()[paramName] = thisCondition6[paramName]
    
    for thisCondition6 in condition6:
        currentLoop = condition6
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisCondition6.rgb)
        if thisCondition6 != None:
            for paramName in thisCondition6:
                globals()[paramName] = thisCondition6[paramName]
        
        # --- Prepare to start Routine "Stim" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Stim.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from code_exe
        this_number = numcount
        this_image = stim_list[numcount-1]
        duration = 0.5
        if num_i == 10:
            duration = 0.3
        if num_i == 9:
            duration = 0.3
        if num_i == 2:
            duration = 0.3
        if num_i == 1:
            duration = 0.3
        if num_i == 4:
            duration = 0.3
        if num_i == 3:
            duration = 0.3
        response = ''
        #the central position of picture
        shuffle(piccenpos_cr)
        shuffle(piccenpos_ar)
        piccenpos = (piccenpos_cr[0], piccenpos_ar[0])
        
        ans = answer_list[numcount-1]
        thisExp.addData('ans', ans)
        print("begin routine ","count",numcount,"img",this_image,"ans",ans)
        
        if key_resp_2.corr:
            response = True
        
        else : 
            response = False
        n_value.setColor(ncolor, colorSpace='rgb')
        n_value.setText(ntext)
        testnum.setText(this_number)
        thisimage.setPos(piccenpos)
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        sound_true.setSound('A', secs=0.1, hamming=True)
        sound_true.setVolume(2.0, log=False)
        sound_true.seek(0)
        sound_false.setSound('B', secs=0.2, hamming=False)
        sound_false.setVolume(4.0, log=False)
        sound_false.seek(0)
        # keep track of which components have finished
        StimComponents = [image_bac, n_value, num, testnum, thisimage, key_resp_2, sound_true, sound_false]
        for thisComponent in StimComponents:
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
        
        # --- Run Routine "Stim" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_bac* updates
            
            # if image_bac is starting this frame...
            if image_bac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_bac.frameNStart = frameN  # exact frame index
                image_bac.tStart = t  # local t and not account for scr refresh
                image_bac.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_bac, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_bac.started')
                # update status
                image_bac.status = STARTED
                image_bac.setAutoDraw(True)
            
            # if image_bac is active this frame...
            if image_bac.status == STARTED:
                # update params
                pass
            
            # *n_value* updates
            
            # if n_value is starting this frame...
            if n_value.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                n_value.frameNStart = frameN  # exact frame index
                n_value.tStart = t  # local t and not account for scr refresh
                n_value.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(n_value, 'tStartRefresh')  # time at next scr refresh
                # update status
                n_value.status = STARTED
                n_value.setAutoDraw(True)
            
            # if n_value is active this frame...
            if n_value.status == STARTED:
                # update params
                pass
            
            # *num* updates
            
            # if num is starting this frame...
            if num.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                num.frameNStart = frameN  # exact frame index
                num.tStart = t  # local t and not account for scr refresh
                num.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(num, 'tStartRefresh')  # time at next scr refresh
                # update status
                num.status = STARTED
                num.setAutoDraw(True)
            
            # if num is active this frame...
            if num.status == STARTED:
                # update params
                pass
            
            # *testnum* updates
            
            # if testnum is starting this frame...
            if testnum.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                testnum.frameNStart = frameN  # exact frame index
                testnum.tStart = t  # local t and not account for scr refresh
                testnum.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(testnum, 'tStartRefresh')  # time at next scr refresh
                # update status
                testnum.status = STARTED
                testnum.setAutoDraw(True)
            
            # if testnum is active this frame...
            if testnum.status == STARTED:
                # update params
                pass
            
            # *thisimage* updates
            
            # if thisimage is starting this frame...
            if thisimage.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                thisimage.frameNStart = frameN  # exact frame index
                thisimage.tStart = t  # local t and not account for scr refresh
                thisimage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(thisimage, 'tStartRefresh')  # time at next scr refresh
                # update status
                thisimage.status = STARTED
                thisimage.setAutoDraw(True)
            
            # if thisimage is active this frame...
            if thisimage.status == STARTED:
                # update params
                thisimage.setImage(this_image, log=False)
            
            # if thisimage is stopping this frame...
            if thisimage.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > thisimage.tStartRefresh + duration-frameTolerance:
                    # keep track of stop time/frame for later
                    thisimage.tStop = t  # not accounting for scr refresh
                    thisimage.tStopRefresh = tThisFlipGlobal  # on global time
                    thisimage.frameNStop = frameN  # exact frame index
                    # update status
                    thisimage.status = FINISHED
                    thisimage.setAutoDraw(False)
            
            # *key_resp_2* updates
            
            # if key_resp_2 is starting this frame...
            if key_resp_2.status == NOT_STARTED and t >= 0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                key_resp_2.clock.reset()  # now t=0
                key_resp_2.clearEvents(eventType='keyboard')
            if key_resp_2.status == STARTED:
                theseKeys = key_resp_2.getKeys(keyList=['f','j'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[0].name  # just the first key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[0].rt
                    key_resp_2.duration = _key_resp_2_allKeys[0].duration
                    # was this correct?
                    if (key_resp_2.keys == str(ans)) or (key_resp_2.keys == ans):
                        key_resp_2.corr = 1
                    else:
                        key_resp_2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # if sound_true is starting this frame...
            if sound_true.status == NOT_STARTED and response==True:
                # keep track of start time/frame for later
                sound_true.frameNStart = frameN  # exact frame index
                sound_true.tStart = t  # local t and not account for scr refresh
                sound_true.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound_true.status = STARTED
                sound_true.play(when=win)  # sync with win flip
            
            # if sound_true is stopping this frame...
            if sound_true.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_true.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_true.tStop = t  # not accounting for scr refresh
                    sound_true.tStopRefresh = tThisFlipGlobal  # on global time
                    sound_true.frameNStop = frameN  # exact frame index
                    # update status
                    sound_true.status = FINISHED
                    sound_true.stop()
            # update sound_true status according to whether it's playing
            if sound_true.isPlaying:
                sound_true.status = STARTED
            elif sound_true.isFinished:
                sound_true.status = FINISHED
            
            # if sound_false is starting this frame...
            if sound_false.status == NOT_STARTED and response==False:
                # keep track of start time/frame for later
                sound_false.frameNStart = frameN  # exact frame index
                sound_false.tStart = t  # local t and not account for scr refresh
                sound_false.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound_false.status = STARTED
                sound_false.play(when=win)  # sync with win flip
            
            # if sound_false is stopping this frame...
            if sound_false.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_false.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_false.tStop = t  # not accounting for scr refresh
                    sound_false.tStopRefresh = tThisFlipGlobal  # on global time
                    sound_false.frameNStop = frameN  # exact frame index
                    # update status
                    sound_false.status = FINISHED
                    sound_false.stop()
            # update sound_false status according to whether it's playing
            if sound_false.isPlaying:
                sound_false.status = STARTED
            elif sound_false.isFinished:
                sound_false.status = FINISHED
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in StimComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Stim" ---
        for thisComponent in StimComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Stim.stopped', globalClock.getTime(format='float'))
        # Run 'End Routine' code from code_exe
        numcount += 1
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
            # was no response the correct answer?!
            if str(ans).lower() == 'none':
               key_resp_2.corr = 1;  # correct non-response
            else:
               key_resp_2.corr = 0;  # failed to respond (incorrectly)
        # store data for condition6 (TrialHandler)
        condition6.addData('key_resp_2.keys',key_resp_2.keys)
        condition6.addData('key_resp_2.corr', key_resp_2.corr)
        if key_resp_2.keys != None:  # we had a response
            condition6.addData('key_resp_2.rt', key_resp_2.rt)
            condition6.addData('key_resp_2.duration', key_resp_2.duration)
        sound_true.pause()  # ensure sound has stopped at end of Routine
        sound_false.pause()  # ensure sound has stopped at end of Routine
        # the Routine "Stim" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedback" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('feedback.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from feedback_code
        shuffle(fixation_list)
        fiximg = fixation_list[0]
        
        
        #监听按键信息并给出反馈
        if key_resp_2.corr:
            response = True
            msg = '答对了!'
            msgcolor = 'green'
        
        else : 
            response = False
            msg = '答错了!'
            msgcolor = 'red'
        
        
        
        msg_response.setColor(msgcolor, colorSpace='rgb')
        msg_response.setText(msg)
        fixation_img.setImage(fiximg)
        # keep track of which components have finished
        feedbackComponents = [image_bac_2, msg_response, fixation_img]
        for thisComponent in feedbackComponents:
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
        
        # --- Run Routine "feedback" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_bac_2* updates
            
            # if image_bac_2 is starting this frame...
            if image_bac_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                image_bac_2.frameNStart = frameN  # exact frame index
                image_bac_2.tStart = t  # local t and not account for scr refresh
                image_bac_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_bac_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_bac_2.started')
                # update status
                image_bac_2.status = STARTED
                image_bac_2.setAutoDraw(True)
            
            # if image_bac_2 is active this frame...
            if image_bac_2.status == STARTED:
                # update params
                pass
            
            # if image_bac_2 is stopping this frame...
            if image_bac_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_bac_2.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_bac_2.tStop = t  # not accounting for scr refresh
                    image_bac_2.tStopRefresh = tThisFlipGlobal  # on global time
                    image_bac_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_bac_2.stopped')
                    # update status
                    image_bac_2.status = FINISHED
                    image_bac_2.setAutoDraw(False)
            
            # *msg_response* updates
            
            # if msg_response is starting this frame...
            if msg_response.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                msg_response.frameNStart = frameN  # exact frame index
                msg_response.tStart = t  # local t and not account for scr refresh
                msg_response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(msg_response, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'msg_response.started')
                # update status
                msg_response.status = STARTED
                msg_response.setAutoDraw(True)
            
            # if msg_response is active this frame...
            if msg_response.status == STARTED:
                # update params
                pass
            
            # if msg_response is stopping this frame...
            if msg_response.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > msg_response.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    msg_response.tStop = t  # not accounting for scr refresh
                    msg_response.tStopRefresh = tThisFlipGlobal  # on global time
                    msg_response.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'msg_response.stopped')
                    # update status
                    msg_response.status = FINISHED
                    msg_response.setAutoDraw(False)
            
            # *fixation_img* updates
            
            # if fixation_img is starting this frame...
            if fixation_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_img.frameNStart = frameN  # exact frame index
                fixation_img.tStart = t  # local t and not account for scr refresh
                fixation_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_img, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_img.started')
                # update status
                fixation_img.status = STARTED
                fixation_img.setAutoDraw(True)
            
            # if fixation_img is active this frame...
            if fixation_img.status == STARTED:
                # update params
                pass
            
            # if fixation_img is stopping this frame...
            if fixation_img.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_img.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_img.tStop = t  # not accounting for scr refresh
                    fixation_img.tStopRefresh = tThisFlipGlobal  # on global time
                    fixation_img.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_img.stopped')
                    # update status
                    fixation_img.status = FINISHED
                    fixation_img.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback" ---
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('feedback.stopped', globalClock.getTime(format='float'))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 30.0 repeats of 'condition6'
    
    
    # --- Prepare to start Routine "prepare" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('prepare.started', globalClock.getTime(format='float'))
    # Run 'Begin Routine' code from anslist_code
    # set environment
    numcount = 1
    num_i = 0
    piccenpos_cr = [166, 0, -166]
    piccenpos_ar = [166, 0, -166]
    
    # select condition
    condition = conditions.pop()
    i, n, image_list, fixation_list = condition
    num_i = i
    
    # add condition details to data document
    condi = {
        'i=': i,
        'n=': n,
        'len=': len(image_list),
        'fix=': len(fixation_list)
    }
    thisExp.addData('condition', condi)
    print('第',i,'组','N值', n, '图表长度', len(image_list), '注视点表长度', len(fixation_list))
    
    # analyze the image list
    pre_img = []
    rom_imgs = image_list.copy()
    for _ in range(n):
        temp = random.choice(rom_imgs)
        pre_img.append(temp)
        rom_imgs.remove(temp)
    
    # 生成匹配刺激列表 match_list
    match_list = []
    ram = range(9 * n)
    for _ in ram:
        match_image = random.choice(image_list)
        match_list.append([match_image, match_image])
    for item in match_list:
        temp = image_list.copy()
        n1 = n
        while n1 > 1:
            temp.remove(item[n - n1])
            item.insert(n - n1 + 1, random.choice(temp))
            n1 -= 1
    
    # 生成刺激列表 stim_list
    stim_list_pre = match_list.copy()  # 复制匹配刺激列表作为基础
    remaining = 45 - len(match_list) * (n + 1)  # 剩余待插入元素的数量
    while remaining > 0:
        new_image = random.choice(image_list)
        index = random.randint(0, len(stim_list_pre))  # 随机选择插入位置
        if index < n:
            stim_list_pre.insert(index, [new_image])  # 在选择的位置插入新元素
            remaining -= 1
        elif index < len(stim_list_pre):
            prev_image = stim_list_pre[index - n][0]
            next_image = stim_list_pre[index][0]
    
            if new_image != prev_image and new_image != next_image:
                stim_list_pre.insert(index, [new_image])  # 在选择的位置插入新元素
                remaining -= 1
        else:
            if new_image != stim_list_pre[index - n][0]:
                stim_list_pre.insert(index, [new_image])
                remaining -= 1
    
    stim_list = []
    # 迭代遍历原始刺激列表拆包
    for stim in stim_list_pre:
        if len(stim) > 1:  # 成对的元素
            for s in stim:
                stim_list.append(s)
        else:  # 单个元素
            stim_list.append(stim[0])
    
    # 计算转换后列表中的元素数量
    num_elements = len(stim_list)
    
    # 复制 stim_list 生成 answer_list
    answer_list = []
    
    if n == 1:
        preimg_list=['01.png']
    else:
        preimg_list=['01.png','02.png']
        
    allimg_list = preimg_list + stim_list
    #anscount = 0
    for i in range(n, len(allimg_list)):
        if allimg_list[i] == allimg_list[i - n]:
            answer_list.append('f')
            #anscount += 1
        else:
            answer_list.append('j')
            
    if n == 1:
        ncolor = 'yellow'
        ntext = '-1-'
    else :
        ncolor = 'purple'
        ntext = '-2-'
        
    #print("before experiment stim_list:", stim_list)
    #print("before experiment answer_list:",answer_list)
    key_resp_6.keys = []
    key_resp_6.rt = []
    _key_resp_6_allKeys = []
    pic_01png_2.setImage('01.png')
    pic_02png_2.setImage('02.png')
    # keep track of which components have finished
    prepareComponents = [key_resp_6, ins_1back, ins_2back, pic_01png_2, pic_02png_2]
    for thisComponent in prepareComponents:
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
    
    # --- Run Routine "prepare" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_6* updates
        waitOnFlip = False
        
        # if key_resp_6 is starting this frame...
        if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.tStart = t  # local t and not account for scr refresh
            key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_6.started')
            # update status
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_6.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_6.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_6_allKeys.extend(theseKeys)
            if len(_key_resp_6_allKeys):
                key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                key_resp_6.duration = _key_resp_6_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *ins_1back* updates
        
        # if ins_1back is starting this frame...
        if ins_1back.status == NOT_STARTED and n ==1:
            # keep track of start time/frame for later
            ins_1back.frameNStart = frameN  # exact frame index
            ins_1back.tStart = t  # local t and not account for scr refresh
            ins_1back.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ins_1back, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ins_1back.started')
            # update status
            ins_1back.status = STARTED
            ins_1back.setAutoDraw(True)
        
        # if ins_1back is active this frame...
        if ins_1back.status == STARTED:
            # update params
            pass
        
        # *ins_2back* updates
        
        # if ins_2back is starting this frame...
        if ins_2back.status == NOT_STARTED and n ==2:
            # keep track of start time/frame for later
            ins_2back.frameNStart = frameN  # exact frame index
            ins_2back.tStart = t  # local t and not account for scr refresh
            ins_2back.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ins_2back, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ins_2back.started')
            # update status
            ins_2back.status = STARTED
            ins_2back.setAutoDraw(True)
        
        # if ins_2back is active this frame...
        if ins_2back.status == STARTED:
            # update params
            pass
        
        # *pic_01png_2* updates
        
        # if pic_01png_2 is starting this frame...
        if pic_01png_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            pic_01png_2.frameNStart = frameN  # exact frame index
            pic_01png_2.tStart = t  # local t and not account for scr refresh
            pic_01png_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pic_01png_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pic_01png_2.started')
            # update status
            pic_01png_2.status = STARTED
            pic_01png_2.setAutoDraw(True)
        
        # if pic_01png_2 is active this frame...
        if pic_01png_2.status == STARTED:
            # update params
            pass
        
        # *pic_02png_2* updates
        
        # if pic_02png_2 is starting this frame...
        if pic_02png_2.status == NOT_STARTED and n == 2:
            # keep track of start time/frame for later
            pic_02png_2.frameNStart = frameN  # exact frame index
            pic_02png_2.tStart = t  # local t and not account for scr refresh
            pic_02png_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pic_02png_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pic_02png_2.started')
            # update status
            pic_02png_2.status = STARTED
            pic_02png_2.setAutoDraw(True)
        
        # if pic_02png_2 is active this frame...
        if pic_02png_2.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prepareComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prepare" ---
    for thisComponent in prepareComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('prepare.stopped', globalClock.getTime(format='float'))
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys = None
    thisExp.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        thisExp.addData('key_resp_6.rt', key_resp_6.rt)
        thisExp.addData('key_resp_6.duration', key_resp_6.duration)
    thisExp.nextEntry()
    # the Routine "prepare" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    condition5 = data.TrialHandler(nReps=30.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='condition5')
    thisExp.addLoop(condition5)  # add the loop to the experiment
    thisCondition5 = condition5.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCondition5.rgb)
    if thisCondition5 != None:
        for paramName in thisCondition5:
            globals()[paramName] = thisCondition5[paramName]
    
    for thisCondition5 in condition5:
        currentLoop = condition5
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisCondition5.rgb)
        if thisCondition5 != None:
            for paramName in thisCondition5:
                globals()[paramName] = thisCondition5[paramName]
        
        # --- Prepare to start Routine "Stim" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Stim.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from code_exe
        this_number = numcount
        this_image = stim_list[numcount-1]
        duration = 0.5
        if num_i == 10:
            duration = 0.3
        if num_i == 9:
            duration = 0.3
        if num_i == 2:
            duration = 0.3
        if num_i == 1:
            duration = 0.3
        if num_i == 4:
            duration = 0.3
        if num_i == 3:
            duration = 0.3
        response = ''
        #the central position of picture
        shuffle(piccenpos_cr)
        shuffle(piccenpos_ar)
        piccenpos = (piccenpos_cr[0], piccenpos_ar[0])
        
        ans = answer_list[numcount-1]
        thisExp.addData('ans', ans)
        print("begin routine ","count",numcount,"img",this_image,"ans",ans)
        
        if key_resp_2.corr:
            response = True
        
        else : 
            response = False
        n_value.setColor(ncolor, colorSpace='rgb')
        n_value.setText(ntext)
        testnum.setText(this_number)
        thisimage.setPos(piccenpos)
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        sound_true.setSound('A', secs=0.1, hamming=True)
        sound_true.setVolume(2.0, log=False)
        sound_true.seek(0)
        sound_false.setSound('B', secs=0.2, hamming=False)
        sound_false.setVolume(4.0, log=False)
        sound_false.seek(0)
        # keep track of which components have finished
        StimComponents = [image_bac, n_value, num, testnum, thisimage, key_resp_2, sound_true, sound_false]
        for thisComponent in StimComponents:
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
        
        # --- Run Routine "Stim" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_bac* updates
            
            # if image_bac is starting this frame...
            if image_bac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_bac.frameNStart = frameN  # exact frame index
                image_bac.tStart = t  # local t and not account for scr refresh
                image_bac.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_bac, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_bac.started')
                # update status
                image_bac.status = STARTED
                image_bac.setAutoDraw(True)
            
            # if image_bac is active this frame...
            if image_bac.status == STARTED:
                # update params
                pass
            
            # *n_value* updates
            
            # if n_value is starting this frame...
            if n_value.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                n_value.frameNStart = frameN  # exact frame index
                n_value.tStart = t  # local t and not account for scr refresh
                n_value.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(n_value, 'tStartRefresh')  # time at next scr refresh
                # update status
                n_value.status = STARTED
                n_value.setAutoDraw(True)
            
            # if n_value is active this frame...
            if n_value.status == STARTED:
                # update params
                pass
            
            # *num* updates
            
            # if num is starting this frame...
            if num.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                num.frameNStart = frameN  # exact frame index
                num.tStart = t  # local t and not account for scr refresh
                num.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(num, 'tStartRefresh')  # time at next scr refresh
                # update status
                num.status = STARTED
                num.setAutoDraw(True)
            
            # if num is active this frame...
            if num.status == STARTED:
                # update params
                pass
            
            # *testnum* updates
            
            # if testnum is starting this frame...
            if testnum.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                testnum.frameNStart = frameN  # exact frame index
                testnum.tStart = t  # local t and not account for scr refresh
                testnum.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(testnum, 'tStartRefresh')  # time at next scr refresh
                # update status
                testnum.status = STARTED
                testnum.setAutoDraw(True)
            
            # if testnum is active this frame...
            if testnum.status == STARTED:
                # update params
                pass
            
            # *thisimage* updates
            
            # if thisimage is starting this frame...
            if thisimage.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                thisimage.frameNStart = frameN  # exact frame index
                thisimage.tStart = t  # local t and not account for scr refresh
                thisimage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(thisimage, 'tStartRefresh')  # time at next scr refresh
                # update status
                thisimage.status = STARTED
                thisimage.setAutoDraw(True)
            
            # if thisimage is active this frame...
            if thisimage.status == STARTED:
                # update params
                thisimage.setImage(this_image, log=False)
            
            # if thisimage is stopping this frame...
            if thisimage.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > thisimage.tStartRefresh + duration-frameTolerance:
                    # keep track of stop time/frame for later
                    thisimage.tStop = t  # not accounting for scr refresh
                    thisimage.tStopRefresh = tThisFlipGlobal  # on global time
                    thisimage.frameNStop = frameN  # exact frame index
                    # update status
                    thisimage.status = FINISHED
                    thisimage.setAutoDraw(False)
            
            # *key_resp_2* updates
            
            # if key_resp_2 is starting this frame...
            if key_resp_2.status == NOT_STARTED and t >= 0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                key_resp_2.clock.reset()  # now t=0
                key_resp_2.clearEvents(eventType='keyboard')
            if key_resp_2.status == STARTED:
                theseKeys = key_resp_2.getKeys(keyList=['f','j'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[0].name  # just the first key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[0].rt
                    key_resp_2.duration = _key_resp_2_allKeys[0].duration
                    # was this correct?
                    if (key_resp_2.keys == str(ans)) or (key_resp_2.keys == ans):
                        key_resp_2.corr = 1
                    else:
                        key_resp_2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # if sound_true is starting this frame...
            if sound_true.status == NOT_STARTED and response==True:
                # keep track of start time/frame for later
                sound_true.frameNStart = frameN  # exact frame index
                sound_true.tStart = t  # local t and not account for scr refresh
                sound_true.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound_true.status = STARTED
                sound_true.play(when=win)  # sync with win flip
            
            # if sound_true is stopping this frame...
            if sound_true.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_true.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_true.tStop = t  # not accounting for scr refresh
                    sound_true.tStopRefresh = tThisFlipGlobal  # on global time
                    sound_true.frameNStop = frameN  # exact frame index
                    # update status
                    sound_true.status = FINISHED
                    sound_true.stop()
            # update sound_true status according to whether it's playing
            if sound_true.isPlaying:
                sound_true.status = STARTED
            elif sound_true.isFinished:
                sound_true.status = FINISHED
            
            # if sound_false is starting this frame...
            if sound_false.status == NOT_STARTED and response==False:
                # keep track of start time/frame for later
                sound_false.frameNStart = frameN  # exact frame index
                sound_false.tStart = t  # local t and not account for scr refresh
                sound_false.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound_false.status = STARTED
                sound_false.play(when=win)  # sync with win flip
            
            # if sound_false is stopping this frame...
            if sound_false.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_false.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_false.tStop = t  # not accounting for scr refresh
                    sound_false.tStopRefresh = tThisFlipGlobal  # on global time
                    sound_false.frameNStop = frameN  # exact frame index
                    # update status
                    sound_false.status = FINISHED
                    sound_false.stop()
            # update sound_false status according to whether it's playing
            if sound_false.isPlaying:
                sound_false.status = STARTED
            elif sound_false.isFinished:
                sound_false.status = FINISHED
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in StimComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Stim" ---
        for thisComponent in StimComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Stim.stopped', globalClock.getTime(format='float'))
        # Run 'End Routine' code from code_exe
        numcount += 1
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
            # was no response the correct answer?!
            if str(ans).lower() == 'none':
               key_resp_2.corr = 1;  # correct non-response
            else:
               key_resp_2.corr = 0;  # failed to respond (incorrectly)
        # store data for condition5 (TrialHandler)
        condition5.addData('key_resp_2.keys',key_resp_2.keys)
        condition5.addData('key_resp_2.corr', key_resp_2.corr)
        if key_resp_2.keys != None:  # we had a response
            condition5.addData('key_resp_2.rt', key_resp_2.rt)
            condition5.addData('key_resp_2.duration', key_resp_2.duration)
        sound_true.pause()  # ensure sound has stopped at end of Routine
        sound_false.pause()  # ensure sound has stopped at end of Routine
        # the Routine "Stim" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedback" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('feedback.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from feedback_code
        shuffle(fixation_list)
        fiximg = fixation_list[0]
        
        
        #监听按键信息并给出反馈
        if key_resp_2.corr:
            response = True
            msg = '答对了!'
            msgcolor = 'green'
        
        else : 
            response = False
            msg = '答错了!'
            msgcolor = 'red'
        
        
        
        msg_response.setColor(msgcolor, colorSpace='rgb')
        msg_response.setText(msg)
        fixation_img.setImage(fiximg)
        # keep track of which components have finished
        feedbackComponents = [image_bac_2, msg_response, fixation_img]
        for thisComponent in feedbackComponents:
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
        
        # --- Run Routine "feedback" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_bac_2* updates
            
            # if image_bac_2 is starting this frame...
            if image_bac_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                image_bac_2.frameNStart = frameN  # exact frame index
                image_bac_2.tStart = t  # local t and not account for scr refresh
                image_bac_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_bac_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_bac_2.started')
                # update status
                image_bac_2.status = STARTED
                image_bac_2.setAutoDraw(True)
            
            # if image_bac_2 is active this frame...
            if image_bac_2.status == STARTED:
                # update params
                pass
            
            # if image_bac_2 is stopping this frame...
            if image_bac_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_bac_2.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_bac_2.tStop = t  # not accounting for scr refresh
                    image_bac_2.tStopRefresh = tThisFlipGlobal  # on global time
                    image_bac_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_bac_2.stopped')
                    # update status
                    image_bac_2.status = FINISHED
                    image_bac_2.setAutoDraw(False)
            
            # *msg_response* updates
            
            # if msg_response is starting this frame...
            if msg_response.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                msg_response.frameNStart = frameN  # exact frame index
                msg_response.tStart = t  # local t and not account for scr refresh
                msg_response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(msg_response, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'msg_response.started')
                # update status
                msg_response.status = STARTED
                msg_response.setAutoDraw(True)
            
            # if msg_response is active this frame...
            if msg_response.status == STARTED:
                # update params
                pass
            
            # if msg_response is stopping this frame...
            if msg_response.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > msg_response.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    msg_response.tStop = t  # not accounting for scr refresh
                    msg_response.tStopRefresh = tThisFlipGlobal  # on global time
                    msg_response.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'msg_response.stopped')
                    # update status
                    msg_response.status = FINISHED
                    msg_response.setAutoDraw(False)
            
            # *fixation_img* updates
            
            # if fixation_img is starting this frame...
            if fixation_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_img.frameNStart = frameN  # exact frame index
                fixation_img.tStart = t  # local t and not account for scr refresh
                fixation_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_img, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_img.started')
                # update status
                fixation_img.status = STARTED
                fixation_img.setAutoDraw(True)
            
            # if fixation_img is active this frame...
            if fixation_img.status == STARTED:
                # update params
                pass
            
            # if fixation_img is stopping this frame...
            if fixation_img.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_img.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_img.tStop = t  # not accounting for scr refresh
                    fixation_img.tStopRefresh = tThisFlipGlobal  # on global time
                    fixation_img.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_img.stopped')
                    # update status
                    fixation_img.status = FINISHED
                    fixation_img.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback" ---
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('feedback.stopped', globalClock.getTime(format='float'))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 30.0 repeats of 'condition5'
    
    
    # --- Prepare to start Routine "prepare" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('prepare.started', globalClock.getTime(format='float'))
    # Run 'Begin Routine' code from anslist_code
    # set environment
    numcount = 1
    num_i = 0
    piccenpos_cr = [166, 0, -166]
    piccenpos_ar = [166, 0, -166]
    
    # select condition
    condition = conditions.pop()
    i, n, image_list, fixation_list = condition
    num_i = i
    
    # add condition details to data document
    condi = {
        'i=': i,
        'n=': n,
        'len=': len(image_list),
        'fix=': len(fixation_list)
    }
    thisExp.addData('condition', condi)
    print('第',i,'组','N值', n, '图表长度', len(image_list), '注视点表长度', len(fixation_list))
    
    # analyze the image list
    pre_img = []
    rom_imgs = image_list.copy()
    for _ in range(n):
        temp = random.choice(rom_imgs)
        pre_img.append(temp)
        rom_imgs.remove(temp)
    
    # 生成匹配刺激列表 match_list
    match_list = []
    ram = range(9 * n)
    for _ in ram:
        match_image = random.choice(image_list)
        match_list.append([match_image, match_image])
    for item in match_list:
        temp = image_list.copy()
        n1 = n
        while n1 > 1:
            temp.remove(item[n - n1])
            item.insert(n - n1 + 1, random.choice(temp))
            n1 -= 1
    
    # 生成刺激列表 stim_list
    stim_list_pre = match_list.copy()  # 复制匹配刺激列表作为基础
    remaining = 45 - len(match_list) * (n + 1)  # 剩余待插入元素的数量
    while remaining > 0:
        new_image = random.choice(image_list)
        index = random.randint(0, len(stim_list_pre))  # 随机选择插入位置
        if index < n:
            stim_list_pre.insert(index, [new_image])  # 在选择的位置插入新元素
            remaining -= 1
        elif index < len(stim_list_pre):
            prev_image = stim_list_pre[index - n][0]
            next_image = stim_list_pre[index][0]
    
            if new_image != prev_image and new_image != next_image:
                stim_list_pre.insert(index, [new_image])  # 在选择的位置插入新元素
                remaining -= 1
        else:
            if new_image != stim_list_pre[index - n][0]:
                stim_list_pre.insert(index, [new_image])
                remaining -= 1
    
    stim_list = []
    # 迭代遍历原始刺激列表拆包
    for stim in stim_list_pre:
        if len(stim) > 1:  # 成对的元素
            for s in stim:
                stim_list.append(s)
        else:  # 单个元素
            stim_list.append(stim[0])
    
    # 计算转换后列表中的元素数量
    num_elements = len(stim_list)
    
    # 复制 stim_list 生成 answer_list
    answer_list = []
    
    if n == 1:
        preimg_list=['01.png']
    else:
        preimg_list=['01.png','02.png']
        
    allimg_list = preimg_list + stim_list
    #anscount = 0
    for i in range(n, len(allimg_list)):
        if allimg_list[i] == allimg_list[i - n]:
            answer_list.append('f')
            #anscount += 1
        else:
            answer_list.append('j')
            
    if n == 1:
        ncolor = 'yellow'
        ntext = '-1-'
    else :
        ncolor = 'purple'
        ntext = '-2-'
        
    #print("before experiment stim_list:", stim_list)
    #print("before experiment answer_list:",answer_list)
    key_resp_6.keys = []
    key_resp_6.rt = []
    _key_resp_6_allKeys = []
    pic_01png_2.setImage('01.png')
    pic_02png_2.setImage('02.png')
    # keep track of which components have finished
    prepareComponents = [key_resp_6, ins_1back, ins_2back, pic_01png_2, pic_02png_2]
    for thisComponent in prepareComponents:
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
    
    # --- Run Routine "prepare" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_6* updates
        waitOnFlip = False
        
        # if key_resp_6 is starting this frame...
        if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.tStart = t  # local t and not account for scr refresh
            key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_6.started')
            # update status
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_6.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_6.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_6_allKeys.extend(theseKeys)
            if len(_key_resp_6_allKeys):
                key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                key_resp_6.duration = _key_resp_6_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *ins_1back* updates
        
        # if ins_1back is starting this frame...
        if ins_1back.status == NOT_STARTED and n ==1:
            # keep track of start time/frame for later
            ins_1back.frameNStart = frameN  # exact frame index
            ins_1back.tStart = t  # local t and not account for scr refresh
            ins_1back.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ins_1back, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ins_1back.started')
            # update status
            ins_1back.status = STARTED
            ins_1back.setAutoDraw(True)
        
        # if ins_1back is active this frame...
        if ins_1back.status == STARTED:
            # update params
            pass
        
        # *ins_2back* updates
        
        # if ins_2back is starting this frame...
        if ins_2back.status == NOT_STARTED and n ==2:
            # keep track of start time/frame for later
            ins_2back.frameNStart = frameN  # exact frame index
            ins_2back.tStart = t  # local t and not account for scr refresh
            ins_2back.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ins_2back, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ins_2back.started')
            # update status
            ins_2back.status = STARTED
            ins_2back.setAutoDraw(True)
        
        # if ins_2back is active this frame...
        if ins_2back.status == STARTED:
            # update params
            pass
        
        # *pic_01png_2* updates
        
        # if pic_01png_2 is starting this frame...
        if pic_01png_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            pic_01png_2.frameNStart = frameN  # exact frame index
            pic_01png_2.tStart = t  # local t and not account for scr refresh
            pic_01png_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pic_01png_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pic_01png_2.started')
            # update status
            pic_01png_2.status = STARTED
            pic_01png_2.setAutoDraw(True)
        
        # if pic_01png_2 is active this frame...
        if pic_01png_2.status == STARTED:
            # update params
            pass
        
        # *pic_02png_2* updates
        
        # if pic_02png_2 is starting this frame...
        if pic_02png_2.status == NOT_STARTED and n == 2:
            # keep track of start time/frame for later
            pic_02png_2.frameNStart = frameN  # exact frame index
            pic_02png_2.tStart = t  # local t and not account for scr refresh
            pic_02png_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pic_02png_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pic_02png_2.started')
            # update status
            pic_02png_2.status = STARTED
            pic_02png_2.setAutoDraw(True)
        
        # if pic_02png_2 is active this frame...
        if pic_02png_2.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prepareComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prepare" ---
    for thisComponent in prepareComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('prepare.stopped', globalClock.getTime(format='float'))
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys = None
    thisExp.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        thisExp.addData('key_resp_6.rt', key_resp_6.rt)
        thisExp.addData('key_resp_6.duration', key_resp_6.duration)
    thisExp.nextEntry()
    # the Routine "prepare" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    condition4 = data.TrialHandler(nReps=30.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='condition4')
    thisExp.addLoop(condition4)  # add the loop to the experiment
    thisCondition4 = condition4.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCondition4.rgb)
    if thisCondition4 != None:
        for paramName in thisCondition4:
            globals()[paramName] = thisCondition4[paramName]
    
    for thisCondition4 in condition4:
        currentLoop = condition4
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisCondition4.rgb)
        if thisCondition4 != None:
            for paramName in thisCondition4:
                globals()[paramName] = thisCondition4[paramName]
        
        # --- Prepare to start Routine "Stim" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Stim.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from code_exe
        this_number = numcount
        this_image = stim_list[numcount-1]
        duration = 0.5
        if num_i == 10:
            duration = 0.3
        if num_i == 9:
            duration = 0.3
        if num_i == 2:
            duration = 0.3
        if num_i == 1:
            duration = 0.3
        if num_i == 4:
            duration = 0.3
        if num_i == 3:
            duration = 0.3
        response = ''
        #the central position of picture
        shuffle(piccenpos_cr)
        shuffle(piccenpos_ar)
        piccenpos = (piccenpos_cr[0], piccenpos_ar[0])
        
        ans = answer_list[numcount-1]
        thisExp.addData('ans', ans)
        print("begin routine ","count",numcount,"img",this_image,"ans",ans)
        
        if key_resp_2.corr:
            response = True
        
        else : 
            response = False
        n_value.setColor(ncolor, colorSpace='rgb')
        n_value.setText(ntext)
        testnum.setText(this_number)
        thisimage.setPos(piccenpos)
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        sound_true.setSound('A', secs=0.1, hamming=True)
        sound_true.setVolume(2.0, log=False)
        sound_true.seek(0)
        sound_false.setSound('B', secs=0.2, hamming=False)
        sound_false.setVolume(4.0, log=False)
        sound_false.seek(0)
        # keep track of which components have finished
        StimComponents = [image_bac, n_value, num, testnum, thisimage, key_resp_2, sound_true, sound_false]
        for thisComponent in StimComponents:
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
        
        # --- Run Routine "Stim" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_bac* updates
            
            # if image_bac is starting this frame...
            if image_bac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_bac.frameNStart = frameN  # exact frame index
                image_bac.tStart = t  # local t and not account for scr refresh
                image_bac.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_bac, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_bac.started')
                # update status
                image_bac.status = STARTED
                image_bac.setAutoDraw(True)
            
            # if image_bac is active this frame...
            if image_bac.status == STARTED:
                # update params
                pass
            
            # *n_value* updates
            
            # if n_value is starting this frame...
            if n_value.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                n_value.frameNStart = frameN  # exact frame index
                n_value.tStart = t  # local t and not account for scr refresh
                n_value.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(n_value, 'tStartRefresh')  # time at next scr refresh
                # update status
                n_value.status = STARTED
                n_value.setAutoDraw(True)
            
            # if n_value is active this frame...
            if n_value.status == STARTED:
                # update params
                pass
            
            # *num* updates
            
            # if num is starting this frame...
            if num.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                num.frameNStart = frameN  # exact frame index
                num.tStart = t  # local t and not account for scr refresh
                num.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(num, 'tStartRefresh')  # time at next scr refresh
                # update status
                num.status = STARTED
                num.setAutoDraw(True)
            
            # if num is active this frame...
            if num.status == STARTED:
                # update params
                pass
            
            # *testnum* updates
            
            # if testnum is starting this frame...
            if testnum.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                testnum.frameNStart = frameN  # exact frame index
                testnum.tStart = t  # local t and not account for scr refresh
                testnum.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(testnum, 'tStartRefresh')  # time at next scr refresh
                # update status
                testnum.status = STARTED
                testnum.setAutoDraw(True)
            
            # if testnum is active this frame...
            if testnum.status == STARTED:
                # update params
                pass
            
            # *thisimage* updates
            
            # if thisimage is starting this frame...
            if thisimage.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                thisimage.frameNStart = frameN  # exact frame index
                thisimage.tStart = t  # local t and not account for scr refresh
                thisimage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(thisimage, 'tStartRefresh')  # time at next scr refresh
                # update status
                thisimage.status = STARTED
                thisimage.setAutoDraw(True)
            
            # if thisimage is active this frame...
            if thisimage.status == STARTED:
                # update params
                thisimage.setImage(this_image, log=False)
            
            # if thisimage is stopping this frame...
            if thisimage.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > thisimage.tStartRefresh + duration-frameTolerance:
                    # keep track of stop time/frame for later
                    thisimage.tStop = t  # not accounting for scr refresh
                    thisimage.tStopRefresh = tThisFlipGlobal  # on global time
                    thisimage.frameNStop = frameN  # exact frame index
                    # update status
                    thisimage.status = FINISHED
                    thisimage.setAutoDraw(False)
            
            # *key_resp_2* updates
            
            # if key_resp_2 is starting this frame...
            if key_resp_2.status == NOT_STARTED and t >= 0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                key_resp_2.clock.reset()  # now t=0
                key_resp_2.clearEvents(eventType='keyboard')
            if key_resp_2.status == STARTED:
                theseKeys = key_resp_2.getKeys(keyList=['f','j'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[0].name  # just the first key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[0].rt
                    key_resp_2.duration = _key_resp_2_allKeys[0].duration
                    # was this correct?
                    if (key_resp_2.keys == str(ans)) or (key_resp_2.keys == ans):
                        key_resp_2.corr = 1
                    else:
                        key_resp_2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # if sound_true is starting this frame...
            if sound_true.status == NOT_STARTED and response==True:
                # keep track of start time/frame for later
                sound_true.frameNStart = frameN  # exact frame index
                sound_true.tStart = t  # local t and not account for scr refresh
                sound_true.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound_true.status = STARTED
                sound_true.play(when=win)  # sync with win flip
            
            # if sound_true is stopping this frame...
            if sound_true.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_true.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_true.tStop = t  # not accounting for scr refresh
                    sound_true.tStopRefresh = tThisFlipGlobal  # on global time
                    sound_true.frameNStop = frameN  # exact frame index
                    # update status
                    sound_true.status = FINISHED
                    sound_true.stop()
            # update sound_true status according to whether it's playing
            if sound_true.isPlaying:
                sound_true.status = STARTED
            elif sound_true.isFinished:
                sound_true.status = FINISHED
            
            # if sound_false is starting this frame...
            if sound_false.status == NOT_STARTED and response==False:
                # keep track of start time/frame for later
                sound_false.frameNStart = frameN  # exact frame index
                sound_false.tStart = t  # local t and not account for scr refresh
                sound_false.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound_false.status = STARTED
                sound_false.play(when=win)  # sync with win flip
            
            # if sound_false is stopping this frame...
            if sound_false.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_false.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_false.tStop = t  # not accounting for scr refresh
                    sound_false.tStopRefresh = tThisFlipGlobal  # on global time
                    sound_false.frameNStop = frameN  # exact frame index
                    # update status
                    sound_false.status = FINISHED
                    sound_false.stop()
            # update sound_false status according to whether it's playing
            if sound_false.isPlaying:
                sound_false.status = STARTED
            elif sound_false.isFinished:
                sound_false.status = FINISHED
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in StimComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Stim" ---
        for thisComponent in StimComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Stim.stopped', globalClock.getTime(format='float'))
        # Run 'End Routine' code from code_exe
        numcount += 1
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
            # was no response the correct answer?!
            if str(ans).lower() == 'none':
               key_resp_2.corr = 1;  # correct non-response
            else:
               key_resp_2.corr = 0;  # failed to respond (incorrectly)
        # store data for condition4 (TrialHandler)
        condition4.addData('key_resp_2.keys',key_resp_2.keys)
        condition4.addData('key_resp_2.corr', key_resp_2.corr)
        if key_resp_2.keys != None:  # we had a response
            condition4.addData('key_resp_2.rt', key_resp_2.rt)
            condition4.addData('key_resp_2.duration', key_resp_2.duration)
        sound_true.pause()  # ensure sound has stopped at end of Routine
        sound_false.pause()  # ensure sound has stopped at end of Routine
        # the Routine "Stim" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedback" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('feedback.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from feedback_code
        shuffle(fixation_list)
        fiximg = fixation_list[0]
        
        
        #监听按键信息并给出反馈
        if key_resp_2.corr:
            response = True
            msg = '答对了!'
            msgcolor = 'green'
        
        else : 
            response = False
            msg = '答错了!'
            msgcolor = 'red'
        
        
        
        msg_response.setColor(msgcolor, colorSpace='rgb')
        msg_response.setText(msg)
        fixation_img.setImage(fiximg)
        # keep track of which components have finished
        feedbackComponents = [image_bac_2, msg_response, fixation_img]
        for thisComponent in feedbackComponents:
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
        
        # --- Run Routine "feedback" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_bac_2* updates
            
            # if image_bac_2 is starting this frame...
            if image_bac_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                image_bac_2.frameNStart = frameN  # exact frame index
                image_bac_2.tStart = t  # local t and not account for scr refresh
                image_bac_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_bac_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_bac_2.started')
                # update status
                image_bac_2.status = STARTED
                image_bac_2.setAutoDraw(True)
            
            # if image_bac_2 is active this frame...
            if image_bac_2.status == STARTED:
                # update params
                pass
            
            # if image_bac_2 is stopping this frame...
            if image_bac_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_bac_2.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_bac_2.tStop = t  # not accounting for scr refresh
                    image_bac_2.tStopRefresh = tThisFlipGlobal  # on global time
                    image_bac_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_bac_2.stopped')
                    # update status
                    image_bac_2.status = FINISHED
                    image_bac_2.setAutoDraw(False)
            
            # *msg_response* updates
            
            # if msg_response is starting this frame...
            if msg_response.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                msg_response.frameNStart = frameN  # exact frame index
                msg_response.tStart = t  # local t and not account for scr refresh
                msg_response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(msg_response, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'msg_response.started')
                # update status
                msg_response.status = STARTED
                msg_response.setAutoDraw(True)
            
            # if msg_response is active this frame...
            if msg_response.status == STARTED:
                # update params
                pass
            
            # if msg_response is stopping this frame...
            if msg_response.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > msg_response.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    msg_response.tStop = t  # not accounting for scr refresh
                    msg_response.tStopRefresh = tThisFlipGlobal  # on global time
                    msg_response.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'msg_response.stopped')
                    # update status
                    msg_response.status = FINISHED
                    msg_response.setAutoDraw(False)
            
            # *fixation_img* updates
            
            # if fixation_img is starting this frame...
            if fixation_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_img.frameNStart = frameN  # exact frame index
                fixation_img.tStart = t  # local t and not account for scr refresh
                fixation_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_img, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_img.started')
                # update status
                fixation_img.status = STARTED
                fixation_img.setAutoDraw(True)
            
            # if fixation_img is active this frame...
            if fixation_img.status == STARTED:
                # update params
                pass
            
            # if fixation_img is stopping this frame...
            if fixation_img.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_img.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_img.tStop = t  # not accounting for scr refresh
                    fixation_img.tStopRefresh = tThisFlipGlobal  # on global time
                    fixation_img.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_img.stopped')
                    # update status
                    fixation_img.status = FINISHED
                    fixation_img.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback" ---
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('feedback.stopped', globalClock.getTime(format='float'))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 30.0 repeats of 'condition4'
    
    
    # --- Prepare to start Routine "prepare" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('prepare.started', globalClock.getTime(format='float'))
    # Run 'Begin Routine' code from anslist_code
    # set environment
    numcount = 1
    num_i = 0
    piccenpos_cr = [166, 0, -166]
    piccenpos_ar = [166, 0, -166]
    
    # select condition
    condition = conditions.pop()
    i, n, image_list, fixation_list = condition
    num_i = i
    
    # add condition details to data document
    condi = {
        'i=': i,
        'n=': n,
        'len=': len(image_list),
        'fix=': len(fixation_list)
    }
    thisExp.addData('condition', condi)
    print('第',i,'组','N值', n, '图表长度', len(image_list), '注视点表长度', len(fixation_list))
    
    # analyze the image list
    pre_img = []
    rom_imgs = image_list.copy()
    for _ in range(n):
        temp = random.choice(rom_imgs)
        pre_img.append(temp)
        rom_imgs.remove(temp)
    
    # 生成匹配刺激列表 match_list
    match_list = []
    ram = range(9 * n)
    for _ in ram:
        match_image = random.choice(image_list)
        match_list.append([match_image, match_image])
    for item in match_list:
        temp = image_list.copy()
        n1 = n
        while n1 > 1:
            temp.remove(item[n - n1])
            item.insert(n - n1 + 1, random.choice(temp))
            n1 -= 1
    
    # 生成刺激列表 stim_list
    stim_list_pre = match_list.copy()  # 复制匹配刺激列表作为基础
    remaining = 45 - len(match_list) * (n + 1)  # 剩余待插入元素的数量
    while remaining > 0:
        new_image = random.choice(image_list)
        index = random.randint(0, len(stim_list_pre))  # 随机选择插入位置
        if index < n:
            stim_list_pre.insert(index, [new_image])  # 在选择的位置插入新元素
            remaining -= 1
        elif index < len(stim_list_pre):
            prev_image = stim_list_pre[index - n][0]
            next_image = stim_list_pre[index][0]
    
            if new_image != prev_image and new_image != next_image:
                stim_list_pre.insert(index, [new_image])  # 在选择的位置插入新元素
                remaining -= 1
        else:
            if new_image != stim_list_pre[index - n][0]:
                stim_list_pre.insert(index, [new_image])
                remaining -= 1
    
    stim_list = []
    # 迭代遍历原始刺激列表拆包
    for stim in stim_list_pre:
        if len(stim) > 1:  # 成对的元素
            for s in stim:
                stim_list.append(s)
        else:  # 单个元素
            stim_list.append(stim[0])
    
    # 计算转换后列表中的元素数量
    num_elements = len(stim_list)
    
    # 复制 stim_list 生成 answer_list
    answer_list = []
    
    if n == 1:
        preimg_list=['01.png']
    else:
        preimg_list=['01.png','02.png']
        
    allimg_list = preimg_list + stim_list
    #anscount = 0
    for i in range(n, len(allimg_list)):
        if allimg_list[i] == allimg_list[i - n]:
            answer_list.append('f')
            #anscount += 1
        else:
            answer_list.append('j')
            
    if n == 1:
        ncolor = 'yellow'
        ntext = '-1-'
    else :
        ncolor = 'purple'
        ntext = '-2-'
        
    #print("before experiment stim_list:", stim_list)
    #print("before experiment answer_list:",answer_list)
    key_resp_6.keys = []
    key_resp_6.rt = []
    _key_resp_6_allKeys = []
    pic_01png_2.setImage('01.png')
    pic_02png_2.setImage('02.png')
    # keep track of which components have finished
    prepareComponents = [key_resp_6, ins_1back, ins_2back, pic_01png_2, pic_02png_2]
    for thisComponent in prepareComponents:
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
    
    # --- Run Routine "prepare" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_6* updates
        waitOnFlip = False
        
        # if key_resp_6 is starting this frame...
        if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.tStart = t  # local t and not account for scr refresh
            key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_6.started')
            # update status
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_6.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_6.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_6_allKeys.extend(theseKeys)
            if len(_key_resp_6_allKeys):
                key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                key_resp_6.duration = _key_resp_6_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *ins_1back* updates
        
        # if ins_1back is starting this frame...
        if ins_1back.status == NOT_STARTED and n ==1:
            # keep track of start time/frame for later
            ins_1back.frameNStart = frameN  # exact frame index
            ins_1back.tStart = t  # local t and not account for scr refresh
            ins_1back.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ins_1back, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ins_1back.started')
            # update status
            ins_1back.status = STARTED
            ins_1back.setAutoDraw(True)
        
        # if ins_1back is active this frame...
        if ins_1back.status == STARTED:
            # update params
            pass
        
        # *ins_2back* updates
        
        # if ins_2back is starting this frame...
        if ins_2back.status == NOT_STARTED and n ==2:
            # keep track of start time/frame for later
            ins_2back.frameNStart = frameN  # exact frame index
            ins_2back.tStart = t  # local t and not account for scr refresh
            ins_2back.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ins_2back, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ins_2back.started')
            # update status
            ins_2back.status = STARTED
            ins_2back.setAutoDraw(True)
        
        # if ins_2back is active this frame...
        if ins_2back.status == STARTED:
            # update params
            pass
        
        # *pic_01png_2* updates
        
        # if pic_01png_2 is starting this frame...
        if pic_01png_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            pic_01png_2.frameNStart = frameN  # exact frame index
            pic_01png_2.tStart = t  # local t and not account for scr refresh
            pic_01png_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pic_01png_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pic_01png_2.started')
            # update status
            pic_01png_2.status = STARTED
            pic_01png_2.setAutoDraw(True)
        
        # if pic_01png_2 is active this frame...
        if pic_01png_2.status == STARTED:
            # update params
            pass
        
        # *pic_02png_2* updates
        
        # if pic_02png_2 is starting this frame...
        if pic_02png_2.status == NOT_STARTED and n == 2:
            # keep track of start time/frame for later
            pic_02png_2.frameNStart = frameN  # exact frame index
            pic_02png_2.tStart = t  # local t and not account for scr refresh
            pic_02png_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pic_02png_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pic_02png_2.started')
            # update status
            pic_02png_2.status = STARTED
            pic_02png_2.setAutoDraw(True)
        
        # if pic_02png_2 is active this frame...
        if pic_02png_2.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prepareComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prepare" ---
    for thisComponent in prepareComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('prepare.stopped', globalClock.getTime(format='float'))
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys = None
    thisExp.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        thisExp.addData('key_resp_6.rt', key_resp_6.rt)
        thisExp.addData('key_resp_6.duration', key_resp_6.duration)
    thisExp.nextEntry()
    # the Routine "prepare" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    condition3 = data.TrialHandler(nReps=30.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='condition3')
    thisExp.addLoop(condition3)  # add the loop to the experiment
    thisCondition3 = condition3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCondition3.rgb)
    if thisCondition3 != None:
        for paramName in thisCondition3:
            globals()[paramName] = thisCondition3[paramName]
    
    for thisCondition3 in condition3:
        currentLoop = condition3
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisCondition3.rgb)
        if thisCondition3 != None:
            for paramName in thisCondition3:
                globals()[paramName] = thisCondition3[paramName]
        
        # --- Prepare to start Routine "Stim" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Stim.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from code_exe
        this_number = numcount
        this_image = stim_list[numcount-1]
        duration = 0.5
        if num_i == 10:
            duration = 0.3
        if num_i == 9:
            duration = 0.3
        if num_i == 2:
            duration = 0.3
        if num_i == 1:
            duration = 0.3
        if num_i == 4:
            duration = 0.3
        if num_i == 3:
            duration = 0.3
        response = ''
        #the central position of picture
        shuffle(piccenpos_cr)
        shuffle(piccenpos_ar)
        piccenpos = (piccenpos_cr[0], piccenpos_ar[0])
        
        ans = answer_list[numcount-1]
        thisExp.addData('ans', ans)
        print("begin routine ","count",numcount,"img",this_image,"ans",ans)
        
        if key_resp_2.corr:
            response = True
        
        else : 
            response = False
        n_value.setColor(ncolor, colorSpace='rgb')
        n_value.setText(ntext)
        testnum.setText(this_number)
        thisimage.setPos(piccenpos)
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        sound_true.setSound('A', secs=0.1, hamming=True)
        sound_true.setVolume(2.0, log=False)
        sound_true.seek(0)
        sound_false.setSound('B', secs=0.2, hamming=False)
        sound_false.setVolume(4.0, log=False)
        sound_false.seek(0)
        # keep track of which components have finished
        StimComponents = [image_bac, n_value, num, testnum, thisimage, key_resp_2, sound_true, sound_false]
        for thisComponent in StimComponents:
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
        
        # --- Run Routine "Stim" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_bac* updates
            
            # if image_bac is starting this frame...
            if image_bac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_bac.frameNStart = frameN  # exact frame index
                image_bac.tStart = t  # local t and not account for scr refresh
                image_bac.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_bac, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_bac.started')
                # update status
                image_bac.status = STARTED
                image_bac.setAutoDraw(True)
            
            # if image_bac is active this frame...
            if image_bac.status == STARTED:
                # update params
                pass
            
            # *n_value* updates
            
            # if n_value is starting this frame...
            if n_value.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                n_value.frameNStart = frameN  # exact frame index
                n_value.tStart = t  # local t and not account for scr refresh
                n_value.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(n_value, 'tStartRefresh')  # time at next scr refresh
                # update status
                n_value.status = STARTED
                n_value.setAutoDraw(True)
            
            # if n_value is active this frame...
            if n_value.status == STARTED:
                # update params
                pass
            
            # *num* updates
            
            # if num is starting this frame...
            if num.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                num.frameNStart = frameN  # exact frame index
                num.tStart = t  # local t and not account for scr refresh
                num.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(num, 'tStartRefresh')  # time at next scr refresh
                # update status
                num.status = STARTED
                num.setAutoDraw(True)
            
            # if num is active this frame...
            if num.status == STARTED:
                # update params
                pass
            
            # *testnum* updates
            
            # if testnum is starting this frame...
            if testnum.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                testnum.frameNStart = frameN  # exact frame index
                testnum.tStart = t  # local t and not account for scr refresh
                testnum.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(testnum, 'tStartRefresh')  # time at next scr refresh
                # update status
                testnum.status = STARTED
                testnum.setAutoDraw(True)
            
            # if testnum is active this frame...
            if testnum.status == STARTED:
                # update params
                pass
            
            # *thisimage* updates
            
            # if thisimage is starting this frame...
            if thisimage.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                thisimage.frameNStart = frameN  # exact frame index
                thisimage.tStart = t  # local t and not account for scr refresh
                thisimage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(thisimage, 'tStartRefresh')  # time at next scr refresh
                # update status
                thisimage.status = STARTED
                thisimage.setAutoDraw(True)
            
            # if thisimage is active this frame...
            if thisimage.status == STARTED:
                # update params
                thisimage.setImage(this_image, log=False)
            
            # if thisimage is stopping this frame...
            if thisimage.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > thisimage.tStartRefresh + duration-frameTolerance:
                    # keep track of stop time/frame for later
                    thisimage.tStop = t  # not accounting for scr refresh
                    thisimage.tStopRefresh = tThisFlipGlobal  # on global time
                    thisimage.frameNStop = frameN  # exact frame index
                    # update status
                    thisimage.status = FINISHED
                    thisimage.setAutoDraw(False)
            
            # *key_resp_2* updates
            
            # if key_resp_2 is starting this frame...
            if key_resp_2.status == NOT_STARTED and t >= 0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                key_resp_2.clock.reset()  # now t=0
                key_resp_2.clearEvents(eventType='keyboard')
            if key_resp_2.status == STARTED:
                theseKeys = key_resp_2.getKeys(keyList=['f','j'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[0].name  # just the first key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[0].rt
                    key_resp_2.duration = _key_resp_2_allKeys[0].duration
                    # was this correct?
                    if (key_resp_2.keys == str(ans)) or (key_resp_2.keys == ans):
                        key_resp_2.corr = 1
                    else:
                        key_resp_2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # if sound_true is starting this frame...
            if sound_true.status == NOT_STARTED and response==True:
                # keep track of start time/frame for later
                sound_true.frameNStart = frameN  # exact frame index
                sound_true.tStart = t  # local t and not account for scr refresh
                sound_true.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound_true.status = STARTED
                sound_true.play(when=win)  # sync with win flip
            
            # if sound_true is stopping this frame...
            if sound_true.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_true.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_true.tStop = t  # not accounting for scr refresh
                    sound_true.tStopRefresh = tThisFlipGlobal  # on global time
                    sound_true.frameNStop = frameN  # exact frame index
                    # update status
                    sound_true.status = FINISHED
                    sound_true.stop()
            # update sound_true status according to whether it's playing
            if sound_true.isPlaying:
                sound_true.status = STARTED
            elif sound_true.isFinished:
                sound_true.status = FINISHED
            
            # if sound_false is starting this frame...
            if sound_false.status == NOT_STARTED and response==False:
                # keep track of start time/frame for later
                sound_false.frameNStart = frameN  # exact frame index
                sound_false.tStart = t  # local t and not account for scr refresh
                sound_false.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound_false.status = STARTED
                sound_false.play(when=win)  # sync with win flip
            
            # if sound_false is stopping this frame...
            if sound_false.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_false.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_false.tStop = t  # not accounting for scr refresh
                    sound_false.tStopRefresh = tThisFlipGlobal  # on global time
                    sound_false.frameNStop = frameN  # exact frame index
                    # update status
                    sound_false.status = FINISHED
                    sound_false.stop()
            # update sound_false status according to whether it's playing
            if sound_false.isPlaying:
                sound_false.status = STARTED
            elif sound_false.isFinished:
                sound_false.status = FINISHED
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in StimComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Stim" ---
        for thisComponent in StimComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Stim.stopped', globalClock.getTime(format='float'))
        # Run 'End Routine' code from code_exe
        numcount += 1
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
            # was no response the correct answer?!
            if str(ans).lower() == 'none':
               key_resp_2.corr = 1;  # correct non-response
            else:
               key_resp_2.corr = 0;  # failed to respond (incorrectly)
        # store data for condition3 (TrialHandler)
        condition3.addData('key_resp_2.keys',key_resp_2.keys)
        condition3.addData('key_resp_2.corr', key_resp_2.corr)
        if key_resp_2.keys != None:  # we had a response
            condition3.addData('key_resp_2.rt', key_resp_2.rt)
            condition3.addData('key_resp_2.duration', key_resp_2.duration)
        sound_true.pause()  # ensure sound has stopped at end of Routine
        sound_false.pause()  # ensure sound has stopped at end of Routine
        # the Routine "Stim" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedback" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('feedback.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from feedback_code
        shuffle(fixation_list)
        fiximg = fixation_list[0]
        
        
        #监听按键信息并给出反馈
        if key_resp_2.corr:
            response = True
            msg = '答对了!'
            msgcolor = 'green'
        
        else : 
            response = False
            msg = '答错了!'
            msgcolor = 'red'
        
        
        
        msg_response.setColor(msgcolor, colorSpace='rgb')
        msg_response.setText(msg)
        fixation_img.setImage(fiximg)
        # keep track of which components have finished
        feedbackComponents = [image_bac_2, msg_response, fixation_img]
        for thisComponent in feedbackComponents:
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
        
        # --- Run Routine "feedback" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_bac_2* updates
            
            # if image_bac_2 is starting this frame...
            if image_bac_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                image_bac_2.frameNStart = frameN  # exact frame index
                image_bac_2.tStart = t  # local t and not account for scr refresh
                image_bac_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_bac_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_bac_2.started')
                # update status
                image_bac_2.status = STARTED
                image_bac_2.setAutoDraw(True)
            
            # if image_bac_2 is active this frame...
            if image_bac_2.status == STARTED:
                # update params
                pass
            
            # if image_bac_2 is stopping this frame...
            if image_bac_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_bac_2.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_bac_2.tStop = t  # not accounting for scr refresh
                    image_bac_2.tStopRefresh = tThisFlipGlobal  # on global time
                    image_bac_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_bac_2.stopped')
                    # update status
                    image_bac_2.status = FINISHED
                    image_bac_2.setAutoDraw(False)
            
            # *msg_response* updates
            
            # if msg_response is starting this frame...
            if msg_response.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                msg_response.frameNStart = frameN  # exact frame index
                msg_response.tStart = t  # local t and not account for scr refresh
                msg_response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(msg_response, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'msg_response.started')
                # update status
                msg_response.status = STARTED
                msg_response.setAutoDraw(True)
            
            # if msg_response is active this frame...
            if msg_response.status == STARTED:
                # update params
                pass
            
            # if msg_response is stopping this frame...
            if msg_response.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > msg_response.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    msg_response.tStop = t  # not accounting for scr refresh
                    msg_response.tStopRefresh = tThisFlipGlobal  # on global time
                    msg_response.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'msg_response.stopped')
                    # update status
                    msg_response.status = FINISHED
                    msg_response.setAutoDraw(False)
            
            # *fixation_img* updates
            
            # if fixation_img is starting this frame...
            if fixation_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_img.frameNStart = frameN  # exact frame index
                fixation_img.tStart = t  # local t and not account for scr refresh
                fixation_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_img, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_img.started')
                # update status
                fixation_img.status = STARTED
                fixation_img.setAutoDraw(True)
            
            # if fixation_img is active this frame...
            if fixation_img.status == STARTED:
                # update params
                pass
            
            # if fixation_img is stopping this frame...
            if fixation_img.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_img.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_img.tStop = t  # not accounting for scr refresh
                    fixation_img.tStopRefresh = tThisFlipGlobal  # on global time
                    fixation_img.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_img.stopped')
                    # update status
                    fixation_img.status = FINISHED
                    fixation_img.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback" ---
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('feedback.stopped', globalClock.getTime(format='float'))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 30.0 repeats of 'condition3'
    
    
    # --- Prepare to start Routine "prepare" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('prepare.started', globalClock.getTime(format='float'))
    # Run 'Begin Routine' code from anslist_code
    # set environment
    numcount = 1
    num_i = 0
    piccenpos_cr = [166, 0, -166]
    piccenpos_ar = [166, 0, -166]
    
    # select condition
    condition = conditions.pop()
    i, n, image_list, fixation_list = condition
    num_i = i
    
    # add condition details to data document
    condi = {
        'i=': i,
        'n=': n,
        'len=': len(image_list),
        'fix=': len(fixation_list)
    }
    thisExp.addData('condition', condi)
    print('第',i,'组','N值', n, '图表长度', len(image_list), '注视点表长度', len(fixation_list))
    
    # analyze the image list
    pre_img = []
    rom_imgs = image_list.copy()
    for _ in range(n):
        temp = random.choice(rom_imgs)
        pre_img.append(temp)
        rom_imgs.remove(temp)
    
    # 生成匹配刺激列表 match_list
    match_list = []
    ram = range(9 * n)
    for _ in ram:
        match_image = random.choice(image_list)
        match_list.append([match_image, match_image])
    for item in match_list:
        temp = image_list.copy()
        n1 = n
        while n1 > 1:
            temp.remove(item[n - n1])
            item.insert(n - n1 + 1, random.choice(temp))
            n1 -= 1
    
    # 生成刺激列表 stim_list
    stim_list_pre = match_list.copy()  # 复制匹配刺激列表作为基础
    remaining = 45 - len(match_list) * (n + 1)  # 剩余待插入元素的数量
    while remaining > 0:
        new_image = random.choice(image_list)
        index = random.randint(0, len(stim_list_pre))  # 随机选择插入位置
        if index < n:
            stim_list_pre.insert(index, [new_image])  # 在选择的位置插入新元素
            remaining -= 1
        elif index < len(stim_list_pre):
            prev_image = stim_list_pre[index - n][0]
            next_image = stim_list_pre[index][0]
    
            if new_image != prev_image and new_image != next_image:
                stim_list_pre.insert(index, [new_image])  # 在选择的位置插入新元素
                remaining -= 1
        else:
            if new_image != stim_list_pre[index - n][0]:
                stim_list_pre.insert(index, [new_image])
                remaining -= 1
    
    stim_list = []
    # 迭代遍历原始刺激列表拆包
    for stim in stim_list_pre:
        if len(stim) > 1:  # 成对的元素
            for s in stim:
                stim_list.append(s)
        else:  # 单个元素
            stim_list.append(stim[0])
    
    # 计算转换后列表中的元素数量
    num_elements = len(stim_list)
    
    # 复制 stim_list 生成 answer_list
    answer_list = []
    
    if n == 1:
        preimg_list=['01.png']
    else:
        preimg_list=['01.png','02.png']
        
    allimg_list = preimg_list + stim_list
    #anscount = 0
    for i in range(n, len(allimg_list)):
        if allimg_list[i] == allimg_list[i - n]:
            answer_list.append('f')
            #anscount += 1
        else:
            answer_list.append('j')
            
    if n == 1:
        ncolor = 'yellow'
        ntext = '-1-'
    else :
        ncolor = 'purple'
        ntext = '-2-'
        
    #print("before experiment stim_list:", stim_list)
    #print("before experiment answer_list:",answer_list)
    key_resp_6.keys = []
    key_resp_6.rt = []
    _key_resp_6_allKeys = []
    pic_01png_2.setImage('01.png')
    pic_02png_2.setImage('02.png')
    # keep track of which components have finished
    prepareComponents = [key_resp_6, ins_1back, ins_2back, pic_01png_2, pic_02png_2]
    for thisComponent in prepareComponents:
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
    
    # --- Run Routine "prepare" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_6* updates
        waitOnFlip = False
        
        # if key_resp_6 is starting this frame...
        if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.tStart = t  # local t and not account for scr refresh
            key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_6.started')
            # update status
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_6.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_6.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_6_allKeys.extend(theseKeys)
            if len(_key_resp_6_allKeys):
                key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                key_resp_6.duration = _key_resp_6_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *ins_1back* updates
        
        # if ins_1back is starting this frame...
        if ins_1back.status == NOT_STARTED and n ==1:
            # keep track of start time/frame for later
            ins_1back.frameNStart = frameN  # exact frame index
            ins_1back.tStart = t  # local t and not account for scr refresh
            ins_1back.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ins_1back, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ins_1back.started')
            # update status
            ins_1back.status = STARTED
            ins_1back.setAutoDraw(True)
        
        # if ins_1back is active this frame...
        if ins_1back.status == STARTED:
            # update params
            pass
        
        # *ins_2back* updates
        
        # if ins_2back is starting this frame...
        if ins_2back.status == NOT_STARTED and n ==2:
            # keep track of start time/frame for later
            ins_2back.frameNStart = frameN  # exact frame index
            ins_2back.tStart = t  # local t and not account for scr refresh
            ins_2back.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ins_2back, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ins_2back.started')
            # update status
            ins_2back.status = STARTED
            ins_2back.setAutoDraw(True)
        
        # if ins_2back is active this frame...
        if ins_2back.status == STARTED:
            # update params
            pass
        
        # *pic_01png_2* updates
        
        # if pic_01png_2 is starting this frame...
        if pic_01png_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            pic_01png_2.frameNStart = frameN  # exact frame index
            pic_01png_2.tStart = t  # local t and not account for scr refresh
            pic_01png_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pic_01png_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pic_01png_2.started')
            # update status
            pic_01png_2.status = STARTED
            pic_01png_2.setAutoDraw(True)
        
        # if pic_01png_2 is active this frame...
        if pic_01png_2.status == STARTED:
            # update params
            pass
        
        # *pic_02png_2* updates
        
        # if pic_02png_2 is starting this frame...
        if pic_02png_2.status == NOT_STARTED and n == 2:
            # keep track of start time/frame for later
            pic_02png_2.frameNStart = frameN  # exact frame index
            pic_02png_2.tStart = t  # local t and not account for scr refresh
            pic_02png_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pic_02png_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pic_02png_2.started')
            # update status
            pic_02png_2.status = STARTED
            pic_02png_2.setAutoDraw(True)
        
        # if pic_02png_2 is active this frame...
        if pic_02png_2.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prepareComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prepare" ---
    for thisComponent in prepareComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('prepare.stopped', globalClock.getTime(format='float'))
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys = None
    thisExp.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        thisExp.addData('key_resp_6.rt', key_resp_6.rt)
        thisExp.addData('key_resp_6.duration', key_resp_6.duration)
    thisExp.nextEntry()
    # the Routine "prepare" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    condition2 = data.TrialHandler(nReps=30.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='condition2')
    thisExp.addLoop(condition2)  # add the loop to the experiment
    thisCondition2 = condition2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCondition2.rgb)
    if thisCondition2 != None:
        for paramName in thisCondition2:
            globals()[paramName] = thisCondition2[paramName]
    
    for thisCondition2 in condition2:
        currentLoop = condition2
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisCondition2.rgb)
        if thisCondition2 != None:
            for paramName in thisCondition2:
                globals()[paramName] = thisCondition2[paramName]
        
        # --- Prepare to start Routine "Stim" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Stim.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from code_exe
        this_number = numcount
        this_image = stim_list[numcount-1]
        duration = 0.5
        if num_i == 10:
            duration = 0.3
        if num_i == 9:
            duration = 0.3
        if num_i == 2:
            duration = 0.3
        if num_i == 1:
            duration = 0.3
        if num_i == 4:
            duration = 0.3
        if num_i == 3:
            duration = 0.3
        response = ''
        #the central position of picture
        shuffle(piccenpos_cr)
        shuffle(piccenpos_ar)
        piccenpos = (piccenpos_cr[0], piccenpos_ar[0])
        
        ans = answer_list[numcount-1]
        thisExp.addData('ans', ans)
        print("begin routine ","count",numcount,"img",this_image,"ans",ans)
        
        if key_resp_2.corr:
            response = True
        
        else : 
            response = False
        n_value.setColor(ncolor, colorSpace='rgb')
        n_value.setText(ntext)
        testnum.setText(this_number)
        thisimage.setPos(piccenpos)
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        sound_true.setSound('A', secs=0.1, hamming=True)
        sound_true.setVolume(2.0, log=False)
        sound_true.seek(0)
        sound_false.setSound('B', secs=0.2, hamming=False)
        sound_false.setVolume(4.0, log=False)
        sound_false.seek(0)
        # keep track of which components have finished
        StimComponents = [image_bac, n_value, num, testnum, thisimage, key_resp_2, sound_true, sound_false]
        for thisComponent in StimComponents:
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
        
        # --- Run Routine "Stim" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_bac* updates
            
            # if image_bac is starting this frame...
            if image_bac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_bac.frameNStart = frameN  # exact frame index
                image_bac.tStart = t  # local t and not account for scr refresh
                image_bac.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_bac, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_bac.started')
                # update status
                image_bac.status = STARTED
                image_bac.setAutoDraw(True)
            
            # if image_bac is active this frame...
            if image_bac.status == STARTED:
                # update params
                pass
            
            # *n_value* updates
            
            # if n_value is starting this frame...
            if n_value.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                n_value.frameNStart = frameN  # exact frame index
                n_value.tStart = t  # local t and not account for scr refresh
                n_value.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(n_value, 'tStartRefresh')  # time at next scr refresh
                # update status
                n_value.status = STARTED
                n_value.setAutoDraw(True)
            
            # if n_value is active this frame...
            if n_value.status == STARTED:
                # update params
                pass
            
            # *num* updates
            
            # if num is starting this frame...
            if num.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                num.frameNStart = frameN  # exact frame index
                num.tStart = t  # local t and not account for scr refresh
                num.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(num, 'tStartRefresh')  # time at next scr refresh
                # update status
                num.status = STARTED
                num.setAutoDraw(True)
            
            # if num is active this frame...
            if num.status == STARTED:
                # update params
                pass
            
            # *testnum* updates
            
            # if testnum is starting this frame...
            if testnum.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                testnum.frameNStart = frameN  # exact frame index
                testnum.tStart = t  # local t and not account for scr refresh
                testnum.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(testnum, 'tStartRefresh')  # time at next scr refresh
                # update status
                testnum.status = STARTED
                testnum.setAutoDraw(True)
            
            # if testnum is active this frame...
            if testnum.status == STARTED:
                # update params
                pass
            
            # *thisimage* updates
            
            # if thisimage is starting this frame...
            if thisimage.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                thisimage.frameNStart = frameN  # exact frame index
                thisimage.tStart = t  # local t and not account for scr refresh
                thisimage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(thisimage, 'tStartRefresh')  # time at next scr refresh
                # update status
                thisimage.status = STARTED
                thisimage.setAutoDraw(True)
            
            # if thisimage is active this frame...
            if thisimage.status == STARTED:
                # update params
                thisimage.setImage(this_image, log=False)
            
            # if thisimage is stopping this frame...
            if thisimage.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > thisimage.tStartRefresh + duration-frameTolerance:
                    # keep track of stop time/frame for later
                    thisimage.tStop = t  # not accounting for scr refresh
                    thisimage.tStopRefresh = tThisFlipGlobal  # on global time
                    thisimage.frameNStop = frameN  # exact frame index
                    # update status
                    thisimage.status = FINISHED
                    thisimage.setAutoDraw(False)
            
            # *key_resp_2* updates
            
            # if key_resp_2 is starting this frame...
            if key_resp_2.status == NOT_STARTED and t >= 0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                key_resp_2.clock.reset()  # now t=0
                key_resp_2.clearEvents(eventType='keyboard')
            if key_resp_2.status == STARTED:
                theseKeys = key_resp_2.getKeys(keyList=['f','j'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[0].name  # just the first key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[0].rt
                    key_resp_2.duration = _key_resp_2_allKeys[0].duration
                    # was this correct?
                    if (key_resp_2.keys == str(ans)) or (key_resp_2.keys == ans):
                        key_resp_2.corr = 1
                    else:
                        key_resp_2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # if sound_true is starting this frame...
            if sound_true.status == NOT_STARTED and response==True:
                # keep track of start time/frame for later
                sound_true.frameNStart = frameN  # exact frame index
                sound_true.tStart = t  # local t and not account for scr refresh
                sound_true.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound_true.status = STARTED
                sound_true.play(when=win)  # sync with win flip
            
            # if sound_true is stopping this frame...
            if sound_true.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_true.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_true.tStop = t  # not accounting for scr refresh
                    sound_true.tStopRefresh = tThisFlipGlobal  # on global time
                    sound_true.frameNStop = frameN  # exact frame index
                    # update status
                    sound_true.status = FINISHED
                    sound_true.stop()
            # update sound_true status according to whether it's playing
            if sound_true.isPlaying:
                sound_true.status = STARTED
            elif sound_true.isFinished:
                sound_true.status = FINISHED
            
            # if sound_false is starting this frame...
            if sound_false.status == NOT_STARTED and response==False:
                # keep track of start time/frame for later
                sound_false.frameNStart = frameN  # exact frame index
                sound_false.tStart = t  # local t and not account for scr refresh
                sound_false.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound_false.status = STARTED
                sound_false.play(when=win)  # sync with win flip
            
            # if sound_false is stopping this frame...
            if sound_false.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_false.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_false.tStop = t  # not accounting for scr refresh
                    sound_false.tStopRefresh = tThisFlipGlobal  # on global time
                    sound_false.frameNStop = frameN  # exact frame index
                    # update status
                    sound_false.status = FINISHED
                    sound_false.stop()
            # update sound_false status according to whether it's playing
            if sound_false.isPlaying:
                sound_false.status = STARTED
            elif sound_false.isFinished:
                sound_false.status = FINISHED
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in StimComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Stim" ---
        for thisComponent in StimComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Stim.stopped', globalClock.getTime(format='float'))
        # Run 'End Routine' code from code_exe
        numcount += 1
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
            # was no response the correct answer?!
            if str(ans).lower() == 'none':
               key_resp_2.corr = 1;  # correct non-response
            else:
               key_resp_2.corr = 0;  # failed to respond (incorrectly)
        # store data for condition2 (TrialHandler)
        condition2.addData('key_resp_2.keys',key_resp_2.keys)
        condition2.addData('key_resp_2.corr', key_resp_2.corr)
        if key_resp_2.keys != None:  # we had a response
            condition2.addData('key_resp_2.rt', key_resp_2.rt)
            condition2.addData('key_resp_2.duration', key_resp_2.duration)
        sound_true.pause()  # ensure sound has stopped at end of Routine
        sound_false.pause()  # ensure sound has stopped at end of Routine
        # the Routine "Stim" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedback" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('feedback.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from feedback_code
        shuffle(fixation_list)
        fiximg = fixation_list[0]
        
        
        #监听按键信息并给出反馈
        if key_resp_2.corr:
            response = True
            msg = '答对了!'
            msgcolor = 'green'
        
        else : 
            response = False
            msg = '答错了!'
            msgcolor = 'red'
        
        
        
        msg_response.setColor(msgcolor, colorSpace='rgb')
        msg_response.setText(msg)
        fixation_img.setImage(fiximg)
        # keep track of which components have finished
        feedbackComponents = [image_bac_2, msg_response, fixation_img]
        for thisComponent in feedbackComponents:
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
        
        # --- Run Routine "feedback" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_bac_2* updates
            
            # if image_bac_2 is starting this frame...
            if image_bac_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                image_bac_2.frameNStart = frameN  # exact frame index
                image_bac_2.tStart = t  # local t and not account for scr refresh
                image_bac_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_bac_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_bac_2.started')
                # update status
                image_bac_2.status = STARTED
                image_bac_2.setAutoDraw(True)
            
            # if image_bac_2 is active this frame...
            if image_bac_2.status == STARTED:
                # update params
                pass
            
            # if image_bac_2 is stopping this frame...
            if image_bac_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_bac_2.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_bac_2.tStop = t  # not accounting for scr refresh
                    image_bac_2.tStopRefresh = tThisFlipGlobal  # on global time
                    image_bac_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_bac_2.stopped')
                    # update status
                    image_bac_2.status = FINISHED
                    image_bac_2.setAutoDraw(False)
            
            # *msg_response* updates
            
            # if msg_response is starting this frame...
            if msg_response.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                msg_response.frameNStart = frameN  # exact frame index
                msg_response.tStart = t  # local t and not account for scr refresh
                msg_response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(msg_response, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'msg_response.started')
                # update status
                msg_response.status = STARTED
                msg_response.setAutoDraw(True)
            
            # if msg_response is active this frame...
            if msg_response.status == STARTED:
                # update params
                pass
            
            # if msg_response is stopping this frame...
            if msg_response.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > msg_response.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    msg_response.tStop = t  # not accounting for scr refresh
                    msg_response.tStopRefresh = tThisFlipGlobal  # on global time
                    msg_response.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'msg_response.stopped')
                    # update status
                    msg_response.status = FINISHED
                    msg_response.setAutoDraw(False)
            
            # *fixation_img* updates
            
            # if fixation_img is starting this frame...
            if fixation_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_img.frameNStart = frameN  # exact frame index
                fixation_img.tStart = t  # local t and not account for scr refresh
                fixation_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_img, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_img.started')
                # update status
                fixation_img.status = STARTED
                fixation_img.setAutoDraw(True)
            
            # if fixation_img is active this frame...
            if fixation_img.status == STARTED:
                # update params
                pass
            
            # if fixation_img is stopping this frame...
            if fixation_img.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_img.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_img.tStop = t  # not accounting for scr refresh
                    fixation_img.tStopRefresh = tThisFlipGlobal  # on global time
                    fixation_img.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_img.stopped')
                    # update status
                    fixation_img.status = FINISHED
                    fixation_img.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback" ---
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('feedback.stopped', globalClock.getTime(format='float'))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 30.0 repeats of 'condition2'
    
    
    # --- Prepare to start Routine "prepare" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('prepare.started', globalClock.getTime(format='float'))
    # Run 'Begin Routine' code from anslist_code
    # set environment
    numcount = 1
    num_i = 0
    piccenpos_cr = [166, 0, -166]
    piccenpos_ar = [166, 0, -166]
    
    # select condition
    condition = conditions.pop()
    i, n, image_list, fixation_list = condition
    num_i = i
    
    # add condition details to data document
    condi = {
        'i=': i,
        'n=': n,
        'len=': len(image_list),
        'fix=': len(fixation_list)
    }
    thisExp.addData('condition', condi)
    print('第',i,'组','N值', n, '图表长度', len(image_list), '注视点表长度', len(fixation_list))
    
    # analyze the image list
    pre_img = []
    rom_imgs = image_list.copy()
    for _ in range(n):
        temp = random.choice(rom_imgs)
        pre_img.append(temp)
        rom_imgs.remove(temp)
    
    # 生成匹配刺激列表 match_list
    match_list = []
    ram = range(9 * n)
    for _ in ram:
        match_image = random.choice(image_list)
        match_list.append([match_image, match_image])
    for item in match_list:
        temp = image_list.copy()
        n1 = n
        while n1 > 1:
            temp.remove(item[n - n1])
            item.insert(n - n1 + 1, random.choice(temp))
            n1 -= 1
    
    # 生成刺激列表 stim_list
    stim_list_pre = match_list.copy()  # 复制匹配刺激列表作为基础
    remaining = 45 - len(match_list) * (n + 1)  # 剩余待插入元素的数量
    while remaining > 0:
        new_image = random.choice(image_list)
        index = random.randint(0, len(stim_list_pre))  # 随机选择插入位置
        if index < n:
            stim_list_pre.insert(index, [new_image])  # 在选择的位置插入新元素
            remaining -= 1
        elif index < len(stim_list_pre):
            prev_image = stim_list_pre[index - n][0]
            next_image = stim_list_pre[index][0]
    
            if new_image != prev_image and new_image != next_image:
                stim_list_pre.insert(index, [new_image])  # 在选择的位置插入新元素
                remaining -= 1
        else:
            if new_image != stim_list_pre[index - n][0]:
                stim_list_pre.insert(index, [new_image])
                remaining -= 1
    
    stim_list = []
    # 迭代遍历原始刺激列表拆包
    for stim in stim_list_pre:
        if len(stim) > 1:  # 成对的元素
            for s in stim:
                stim_list.append(s)
        else:  # 单个元素
            stim_list.append(stim[0])
    
    # 计算转换后列表中的元素数量
    num_elements = len(stim_list)
    
    # 复制 stim_list 生成 answer_list
    answer_list = []
    
    if n == 1:
        preimg_list=['01.png']
    else:
        preimg_list=['01.png','02.png']
        
    allimg_list = preimg_list + stim_list
    #anscount = 0
    for i in range(n, len(allimg_list)):
        if allimg_list[i] == allimg_list[i - n]:
            answer_list.append('f')
            #anscount += 1
        else:
            answer_list.append('j')
            
    if n == 1:
        ncolor = 'yellow'
        ntext = '-1-'
    else :
        ncolor = 'purple'
        ntext = '-2-'
        
    #print("before experiment stim_list:", stim_list)
    #print("before experiment answer_list:",answer_list)
    key_resp_6.keys = []
    key_resp_6.rt = []
    _key_resp_6_allKeys = []
    pic_01png_2.setImage('01.png')
    pic_02png_2.setImage('02.png')
    # keep track of which components have finished
    prepareComponents = [key_resp_6, ins_1back, ins_2back, pic_01png_2, pic_02png_2]
    for thisComponent in prepareComponents:
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
    
    # --- Run Routine "prepare" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_6* updates
        waitOnFlip = False
        
        # if key_resp_6 is starting this frame...
        if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.tStart = t  # local t and not account for scr refresh
            key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_6.started')
            # update status
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_6.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_6.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_6_allKeys.extend(theseKeys)
            if len(_key_resp_6_allKeys):
                key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                key_resp_6.duration = _key_resp_6_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *ins_1back* updates
        
        # if ins_1back is starting this frame...
        if ins_1back.status == NOT_STARTED and n ==1:
            # keep track of start time/frame for later
            ins_1back.frameNStart = frameN  # exact frame index
            ins_1back.tStart = t  # local t and not account for scr refresh
            ins_1back.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ins_1back, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ins_1back.started')
            # update status
            ins_1back.status = STARTED
            ins_1back.setAutoDraw(True)
        
        # if ins_1back is active this frame...
        if ins_1back.status == STARTED:
            # update params
            pass
        
        # *ins_2back* updates
        
        # if ins_2back is starting this frame...
        if ins_2back.status == NOT_STARTED and n ==2:
            # keep track of start time/frame for later
            ins_2back.frameNStart = frameN  # exact frame index
            ins_2back.tStart = t  # local t and not account for scr refresh
            ins_2back.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ins_2back, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ins_2back.started')
            # update status
            ins_2back.status = STARTED
            ins_2back.setAutoDraw(True)
        
        # if ins_2back is active this frame...
        if ins_2back.status == STARTED:
            # update params
            pass
        
        # *pic_01png_2* updates
        
        # if pic_01png_2 is starting this frame...
        if pic_01png_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            pic_01png_2.frameNStart = frameN  # exact frame index
            pic_01png_2.tStart = t  # local t and not account for scr refresh
            pic_01png_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pic_01png_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pic_01png_2.started')
            # update status
            pic_01png_2.status = STARTED
            pic_01png_2.setAutoDraw(True)
        
        # if pic_01png_2 is active this frame...
        if pic_01png_2.status == STARTED:
            # update params
            pass
        
        # *pic_02png_2* updates
        
        # if pic_02png_2 is starting this frame...
        if pic_02png_2.status == NOT_STARTED and n == 2:
            # keep track of start time/frame for later
            pic_02png_2.frameNStart = frameN  # exact frame index
            pic_02png_2.tStart = t  # local t and not account for scr refresh
            pic_02png_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pic_02png_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pic_02png_2.started')
            # update status
            pic_02png_2.status = STARTED
            pic_02png_2.setAutoDraw(True)
        
        # if pic_02png_2 is active this frame...
        if pic_02png_2.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prepareComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prepare" ---
    for thisComponent in prepareComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('prepare.stopped', globalClock.getTime(format='float'))
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys = None
    thisExp.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        thisExp.addData('key_resp_6.rt', key_resp_6.rt)
        thisExp.addData('key_resp_6.duration', key_resp_6.duration)
    thisExp.nextEntry()
    # the Routine "prepare" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    condition1 = data.TrialHandler(nReps=30.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='condition1')
    thisExp.addLoop(condition1)  # add the loop to the experiment
    thisCondition1 = condition1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCondition1.rgb)
    if thisCondition1 != None:
        for paramName in thisCondition1:
            globals()[paramName] = thisCondition1[paramName]
    
    for thisCondition1 in condition1:
        currentLoop = condition1
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisCondition1.rgb)
        if thisCondition1 != None:
            for paramName in thisCondition1:
                globals()[paramName] = thisCondition1[paramName]
        
        # --- Prepare to start Routine "Stim" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Stim.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from code_exe
        this_number = numcount
        this_image = stim_list[numcount-1]
        duration = 0.5
        if num_i == 10:
            duration = 0.3
        if num_i == 9:
            duration = 0.3
        if num_i == 2:
            duration = 0.3
        if num_i == 1:
            duration = 0.3
        if num_i == 4:
            duration = 0.3
        if num_i == 3:
            duration = 0.3
        response = ''
        #the central position of picture
        shuffle(piccenpos_cr)
        shuffle(piccenpos_ar)
        piccenpos = (piccenpos_cr[0], piccenpos_ar[0])
        
        ans = answer_list[numcount-1]
        thisExp.addData('ans', ans)
        print("begin routine ","count",numcount,"img",this_image,"ans",ans)
        
        if key_resp_2.corr:
            response = True
        
        else : 
            response = False
        n_value.setColor(ncolor, colorSpace='rgb')
        n_value.setText(ntext)
        testnum.setText(this_number)
        thisimage.setPos(piccenpos)
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        sound_true.setSound('A', secs=0.1, hamming=True)
        sound_true.setVolume(2.0, log=False)
        sound_true.seek(0)
        sound_false.setSound('B', secs=0.2, hamming=False)
        sound_false.setVolume(4.0, log=False)
        sound_false.seek(0)
        # keep track of which components have finished
        StimComponents = [image_bac, n_value, num, testnum, thisimage, key_resp_2, sound_true, sound_false]
        for thisComponent in StimComponents:
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
        
        # --- Run Routine "Stim" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_bac* updates
            
            # if image_bac is starting this frame...
            if image_bac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_bac.frameNStart = frameN  # exact frame index
                image_bac.tStart = t  # local t and not account for scr refresh
                image_bac.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_bac, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_bac.started')
                # update status
                image_bac.status = STARTED
                image_bac.setAutoDraw(True)
            
            # if image_bac is active this frame...
            if image_bac.status == STARTED:
                # update params
                pass
            
            # *n_value* updates
            
            # if n_value is starting this frame...
            if n_value.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                n_value.frameNStart = frameN  # exact frame index
                n_value.tStart = t  # local t and not account for scr refresh
                n_value.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(n_value, 'tStartRefresh')  # time at next scr refresh
                # update status
                n_value.status = STARTED
                n_value.setAutoDraw(True)
            
            # if n_value is active this frame...
            if n_value.status == STARTED:
                # update params
                pass
            
            # *num* updates
            
            # if num is starting this frame...
            if num.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                num.frameNStart = frameN  # exact frame index
                num.tStart = t  # local t and not account for scr refresh
                num.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(num, 'tStartRefresh')  # time at next scr refresh
                # update status
                num.status = STARTED
                num.setAutoDraw(True)
            
            # if num is active this frame...
            if num.status == STARTED:
                # update params
                pass
            
            # *testnum* updates
            
            # if testnum is starting this frame...
            if testnum.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                testnum.frameNStart = frameN  # exact frame index
                testnum.tStart = t  # local t and not account for scr refresh
                testnum.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(testnum, 'tStartRefresh')  # time at next scr refresh
                # update status
                testnum.status = STARTED
                testnum.setAutoDraw(True)
            
            # if testnum is active this frame...
            if testnum.status == STARTED:
                # update params
                pass
            
            # *thisimage* updates
            
            # if thisimage is starting this frame...
            if thisimage.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                thisimage.frameNStart = frameN  # exact frame index
                thisimage.tStart = t  # local t and not account for scr refresh
                thisimage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(thisimage, 'tStartRefresh')  # time at next scr refresh
                # update status
                thisimage.status = STARTED
                thisimage.setAutoDraw(True)
            
            # if thisimage is active this frame...
            if thisimage.status == STARTED:
                # update params
                thisimage.setImage(this_image, log=False)
            
            # if thisimage is stopping this frame...
            if thisimage.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > thisimage.tStartRefresh + duration-frameTolerance:
                    # keep track of stop time/frame for later
                    thisimage.tStop = t  # not accounting for scr refresh
                    thisimage.tStopRefresh = tThisFlipGlobal  # on global time
                    thisimage.frameNStop = frameN  # exact frame index
                    # update status
                    thisimage.status = FINISHED
                    thisimage.setAutoDraw(False)
            
            # *key_resp_2* updates
            
            # if key_resp_2 is starting this frame...
            if key_resp_2.status == NOT_STARTED and t >= 0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                key_resp_2.clock.reset()  # now t=0
                key_resp_2.clearEvents(eventType='keyboard')
            if key_resp_2.status == STARTED:
                theseKeys = key_resp_2.getKeys(keyList=['f','j'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[0].name  # just the first key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[0].rt
                    key_resp_2.duration = _key_resp_2_allKeys[0].duration
                    # was this correct?
                    if (key_resp_2.keys == str(ans)) or (key_resp_2.keys == ans):
                        key_resp_2.corr = 1
                    else:
                        key_resp_2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # if sound_true is starting this frame...
            if sound_true.status == NOT_STARTED and response==True:
                # keep track of start time/frame for later
                sound_true.frameNStart = frameN  # exact frame index
                sound_true.tStart = t  # local t and not account for scr refresh
                sound_true.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound_true.status = STARTED
                sound_true.play(when=win)  # sync with win flip
            
            # if sound_true is stopping this frame...
            if sound_true.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_true.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_true.tStop = t  # not accounting for scr refresh
                    sound_true.tStopRefresh = tThisFlipGlobal  # on global time
                    sound_true.frameNStop = frameN  # exact frame index
                    # update status
                    sound_true.status = FINISHED
                    sound_true.stop()
            # update sound_true status according to whether it's playing
            if sound_true.isPlaying:
                sound_true.status = STARTED
            elif sound_true.isFinished:
                sound_true.status = FINISHED
            
            # if sound_false is starting this frame...
            if sound_false.status == NOT_STARTED and response==False:
                # keep track of start time/frame for later
                sound_false.frameNStart = frameN  # exact frame index
                sound_false.tStart = t  # local t and not account for scr refresh
                sound_false.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound_false.status = STARTED
                sound_false.play(when=win)  # sync with win flip
            
            # if sound_false is stopping this frame...
            if sound_false.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_false.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_false.tStop = t  # not accounting for scr refresh
                    sound_false.tStopRefresh = tThisFlipGlobal  # on global time
                    sound_false.frameNStop = frameN  # exact frame index
                    # update status
                    sound_false.status = FINISHED
                    sound_false.stop()
            # update sound_false status according to whether it's playing
            if sound_false.isPlaying:
                sound_false.status = STARTED
            elif sound_false.isFinished:
                sound_false.status = FINISHED
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in StimComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Stim" ---
        for thisComponent in StimComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Stim.stopped', globalClock.getTime(format='float'))
        # Run 'End Routine' code from code_exe
        numcount += 1
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
            # was no response the correct answer?!
            if str(ans).lower() == 'none':
               key_resp_2.corr = 1;  # correct non-response
            else:
               key_resp_2.corr = 0;  # failed to respond (incorrectly)
        # store data for condition1 (TrialHandler)
        condition1.addData('key_resp_2.keys',key_resp_2.keys)
        condition1.addData('key_resp_2.corr', key_resp_2.corr)
        if key_resp_2.keys != None:  # we had a response
            condition1.addData('key_resp_2.rt', key_resp_2.rt)
            condition1.addData('key_resp_2.duration', key_resp_2.duration)
        sound_true.pause()  # ensure sound has stopped at end of Routine
        sound_false.pause()  # ensure sound has stopped at end of Routine
        # the Routine "Stim" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedback" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('feedback.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from feedback_code
        shuffle(fixation_list)
        fiximg = fixation_list[0]
        
        
        #监听按键信息并给出反馈
        if key_resp_2.corr:
            response = True
            msg = '答对了!'
            msgcolor = 'green'
        
        else : 
            response = False
            msg = '答错了!'
            msgcolor = 'red'
        
        
        
        msg_response.setColor(msgcolor, colorSpace='rgb')
        msg_response.setText(msg)
        fixation_img.setImage(fiximg)
        # keep track of which components have finished
        feedbackComponents = [image_bac_2, msg_response, fixation_img]
        for thisComponent in feedbackComponents:
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
        
        # --- Run Routine "feedback" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_bac_2* updates
            
            # if image_bac_2 is starting this frame...
            if image_bac_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                image_bac_2.frameNStart = frameN  # exact frame index
                image_bac_2.tStart = t  # local t and not account for scr refresh
                image_bac_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_bac_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_bac_2.started')
                # update status
                image_bac_2.status = STARTED
                image_bac_2.setAutoDraw(True)
            
            # if image_bac_2 is active this frame...
            if image_bac_2.status == STARTED:
                # update params
                pass
            
            # if image_bac_2 is stopping this frame...
            if image_bac_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_bac_2.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_bac_2.tStop = t  # not accounting for scr refresh
                    image_bac_2.tStopRefresh = tThisFlipGlobal  # on global time
                    image_bac_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_bac_2.stopped')
                    # update status
                    image_bac_2.status = FINISHED
                    image_bac_2.setAutoDraw(False)
            
            # *msg_response* updates
            
            # if msg_response is starting this frame...
            if msg_response.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                msg_response.frameNStart = frameN  # exact frame index
                msg_response.tStart = t  # local t and not account for scr refresh
                msg_response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(msg_response, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'msg_response.started')
                # update status
                msg_response.status = STARTED
                msg_response.setAutoDraw(True)
            
            # if msg_response is active this frame...
            if msg_response.status == STARTED:
                # update params
                pass
            
            # if msg_response is stopping this frame...
            if msg_response.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > msg_response.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    msg_response.tStop = t  # not accounting for scr refresh
                    msg_response.tStopRefresh = tThisFlipGlobal  # on global time
                    msg_response.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'msg_response.stopped')
                    # update status
                    msg_response.status = FINISHED
                    msg_response.setAutoDraw(False)
            
            # *fixation_img* updates
            
            # if fixation_img is starting this frame...
            if fixation_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_img.frameNStart = frameN  # exact frame index
                fixation_img.tStart = t  # local t and not account for scr refresh
                fixation_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_img, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_img.started')
                # update status
                fixation_img.status = STARTED
                fixation_img.setAutoDraw(True)
            
            # if fixation_img is active this frame...
            if fixation_img.status == STARTED:
                # update params
                pass
            
            # if fixation_img is stopping this frame...
            if fixation_img.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_img.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_img.tStop = t  # not accounting for scr refresh
                    fixation_img.tStopRefresh = tThisFlipGlobal  # on global time
                    fixation_img.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_img.stopped')
                    # update status
                    fixation_img.status = FINISHED
                    fixation_img.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback" ---
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('feedback.stopped', globalClock.getTime(format='float'))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 30.0 repeats of 'condition1'
    
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if deviceManager.getDevice('eyetracker') is not None:
        deviceManager.removeDevice('eyetracker')
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    # shut down eyetracker, if there is one
    if deviceManager.getDevice('eyetracker') is not None:
        deviceManager.removeDevice('eyetracker')
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
