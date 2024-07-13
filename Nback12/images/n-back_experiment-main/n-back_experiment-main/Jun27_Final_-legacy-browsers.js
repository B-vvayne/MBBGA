/*********************** 
 * N-Back_Primary *
 ***********************/


// store info about the experiment session:
let expName = 'N-BACK_primary';  // from the Builder filename that created this script
let expInfo = {
    'participant': '',
    '年级': '',
    '班级': '',
    '性别': '',
};

// Start code blocks for 'Before Experiment'
// Run 'Before Experiment' code from code_condition
import * as random from 'random';
var conditions, fixation_lists, image_lists, n_values;
n_values = [1, 2];
image_lists = [["01.png", "02.png", "03.png", "04.png", "05.png", "06.png", "07.png", "08.png", "09.png"], ["01.png", "02.png", "03.png", "04.png", "05.png", "06.png", "07.png", "08.png", "09.png", "10.png", "11.png", "12.png", "13.png", "14.png", "15.png", "16.png", "17.png", "18.png"]];
fixation_lists = [["up.png", "down.png", "left.png", "right.png", "center.png", "lu.png", "ru.png", "ld.png", "rd.png"], ["center.png"]];
conditions = [];
for (var n, _pj_c = 0, _pj_a = n_values, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
    n = _pj_a[_pj_c];
    for (var image_list, _pj_f = 0, _pj_d = image_lists, _pj_e = _pj_d.length; (_pj_f < _pj_e); _pj_f += 1) {
        image_list = _pj_d[_pj_f];
        for (var fixation_list, _pj_i = 0, _pj_g = fixation_lists, _pj_h = _pj_g.length; (_pj_i < _pj_h); _pj_i += 1) {
            fixation_list = _pj_g[_pj_i];
            conditions.push([n, image_list, fixation_list]);
        }
    }
}
util.shuffle(conditions);

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0.0, 0.0, 0.0]),
  units: 'pix',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(InsFrameRoutineBegin());
flowScheduler.add(InsFrameRoutineEachFrame());
flowScheduler.add(InsFrameRoutineEnd());
flowScheduler.add(prepareRoutineBegin());
flowScheduler.add(prepareRoutineEachFrame());
flowScheduler.add(prepareRoutineEnd());
const condition1LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(condition1LoopBegin(condition1LoopScheduler));
flowScheduler.add(condition1LoopScheduler);
flowScheduler.add(condition1LoopEnd);



flowScheduler.add(prepareRoutineBegin());
flowScheduler.add(prepareRoutineEachFrame());
flowScheduler.add(prepareRoutineEnd());
const condition2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(condition2LoopBegin(condition2LoopScheduler));
flowScheduler.add(condition2LoopScheduler);
flowScheduler.add(condition2LoopEnd);



flowScheduler.add(prepareRoutineBegin());
flowScheduler.add(prepareRoutineEachFrame());
flowScheduler.add(prepareRoutineEnd());
const condition3LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(condition3LoopBegin(condition3LoopScheduler));
flowScheduler.add(condition3LoopScheduler);
flowScheduler.add(condition3LoopEnd);



flowScheduler.add(prepareRoutineBegin());
flowScheduler.add(prepareRoutineEachFrame());
flowScheduler.add(prepareRoutineEnd());
const condition4LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(condition4LoopBegin(condition4LoopScheduler));
flowScheduler.add(condition4LoopScheduler);
flowScheduler.add(condition4LoopEnd);



flowScheduler.add(prepareRoutineBegin());
flowScheduler.add(prepareRoutineEachFrame());
flowScheduler.add(prepareRoutineEnd());
const condition5LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(condition5LoopBegin(condition5LoopScheduler));
flowScheduler.add(condition5LoopScheduler);
flowScheduler.add(condition5LoopEnd);



flowScheduler.add(prepareRoutineBegin());
flowScheduler.add(prepareRoutineEachFrame());
flowScheduler.add(prepareRoutineEnd());
const condition6LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(condition6LoopBegin(condition6LoopScheduler));
flowScheduler.add(condition6LoopScheduler);
flowScheduler.add(condition6LoopEnd);



flowScheduler.add(prepareRoutineBegin());
flowScheduler.add(prepareRoutineEachFrame());
flowScheduler.add(prepareRoutineEnd());
const condition7LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(condition7LoopBegin(condition7LoopScheduler));
flowScheduler.add(condition7LoopScheduler);
flowScheduler.add(condition7LoopEnd);



flowScheduler.add(prepareRoutineBegin());
flowScheduler.add(prepareRoutineEachFrame());
flowScheduler.add(prepareRoutineEnd());
const condition8LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(condition8LoopBegin(condition8LoopScheduler));
flowScheduler.add(condition8LoopScheduler);
flowScheduler.add(condition8LoopEnd);



flowScheduler.add(thanksRoutineBegin());
flowScheduler.add(thanksRoutineEachFrame());
flowScheduler.add(thanksRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'ins700x350.png', 'path': 'ins700x350.png'},
    {'name': 'ins_1-back_700x350.png', 'path': 'ins_1-back_700x350.png'},
    {'name': 'ins_2-back_700x350.png', 'path': 'ins_2-back_700x350.png'},
    {'name': '01.png', 'path': '01.png'},
    {'name': 'default.png', 'path': 'https://pavlovia.org/assets/default/default.png'},
    {'name': '02.png', 'path': '02.png'},
    {'name': 'background_grey.png', 'path': 'background_grey.png'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2024.1.4';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var InsFrameClock;
var key_resp;
var ins_start;
var prepareClock;
var key_resp_6;
var ins_1back;
var ins_2back;
var pic_01png_2;
var pic_02png_2;
var StimClock;
var image_bac;
var n_value;
var num;
var testnum;
var thisimage;
var key_resp_2;
var sound_true;
var sound_false;
var feedbackClock;
var image_bac_2;
var msg;
var msgcolor;
var ntext;
var ncolor;
var msg_response;
var fixation_img;
var thanksClock;
var text_3;
var key_resp_3;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "InsFrame"
  InsFrameClock = new util.Clock();
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  ins_start = new visual.ImageStim({
    win : psychoJS.window,
    name : 'ins_start', units : undefined, 
    image : 'ins700x350.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [700, 350],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "prepare"
  prepareClock = new util.Clock();
  key_resp_6 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  ins_1back = new visual.ImageStim({
    win : psychoJS.window,
    name : 'ins_1back', units : undefined, 
    image : 'ins_1-back_700x350.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [700, 350],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  ins_2back = new visual.ImageStim({
    win : psychoJS.window,
    name : 'ins_2back', units : undefined, 
    image : 'ins_2-back_700x350.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [700, 350],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  pic_01png_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'pic_01png_2', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 100), 0], size : [70, 70],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  pic_02png_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'pic_02png_2', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [100, 0], size : [70, 70],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  // Initialize components for Routine "Stim"
  StimClock = new util.Clock();
  image_bac = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_bac', units : undefined, 
    image : 'background_grey.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [500, 500],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  n_value = new visual.TextStim({
    win: psychoJS.window,
    name: 'n_value',
    text: '',
    font: undefined,
    units: undefined, 
    pos: [0, 275], height: 20.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'Arabic',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  num = new visual.TextStim({
    win: psychoJS.window,
    name: 'num',
    text: 'No.',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 45), 275], height: 20.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  testnum = new visual.TextStim({
    win: psychoJS.window,
    name: 'testnum',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 20), 275], height: 20.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  thisimage = new visual.ImageStim({
    win : psychoJS.window,
    name : 'thisimage', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [60, 60],
    color : new util.Color([1.0, 1.0, 1.0]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  sound_true = new sound.Sound({
      win: psychoJS.window,
      value: 'A',
      secs: 0.1,
      });
  sound_true.setVolume(2.0);
  sound_false = new sound.Sound({
      win: psychoJS.window,
      value: 'A',
      secs: 0.2,
      });
  sound_false.setVolume(1.0);
  // Initialize components for Routine "feedback"
  feedbackClock = new util.Clock();
  image_bac_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_bac_2', units : undefined, 
    image : 'background_grey.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [500, 500],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  // Run 'Begin Experiment' code from feedback_code
  msg = "";
  msgcolor = "";
  ntext = "";
  ncolor = "";
  
  msg_response = new visual.TextStim({
    win: psychoJS.window,
    name: 'msg_response',
    text: '',
    font: 'simsong',
    units: undefined, 
    pos: [0, 275], height: 30.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  fixation_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fixation_img', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [30, 30],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  // Initialize components for Routine "thanks"
  thanksClock = new util.Clock();
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: '感谢你参加我们的实验！\n现在你可以挑选一个自己的礼品了！',
    font: 'simsong',
    units: undefined, 
    pos: [0, 0], height: 35.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _key_resp_allKeys;
var InsFrameComponents;
function InsFrameRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'InsFrame' ---
    t = 0;
    InsFrameClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('InsFrame.started', globalClock.getTime());
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    InsFrameComponents = [];
    InsFrameComponents.push(key_resp);
    InsFrameComponents.push(ins_start);
    
    InsFrameComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function InsFrameRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'InsFrame' ---
    // get current time
    t = InsFrameClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }
    
    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        key_resp.duration = _key_resp_allKeys[_key_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *ins_start* updates
    if (t >= 0.0 && ins_start.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ins_start.tStart = t;  // (not accounting for frame time here)
      ins_start.frameNStart = frameN;  // exact frame index
      
      ins_start.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    InsFrameComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function InsFrameRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'InsFrame' ---
    InsFrameComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('InsFrame.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        psychoJS.experiment.addData('key_resp.duration', key_resp.duration);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "InsFrame" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var numcount;
var piccenpos_cr;
var piccenpos_ar;
var condition;
var condi;
var pre_img;
var rom_imgs;
var match_list;
var ram;
var stim_list_pre;
var remaining;
var stim_list;
var num_elements;
var answer_list;
var preimg_list;
var allimg_list;
var _key_resp_6_allKeys;
var prepareComponents;
function prepareRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'prepare' ---
    t = 0;
    prepareClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('prepare.started', globalClock.getTime());
    // Run 'Begin Routine' code from anslist_code
    numcount = 1;
    piccenpos_cr = [166, 0, (- 166)];
    piccenpos_ar = [166, 0, (- 166)];
    condition = conditions.pop();
    [n, image_list, fixation_list] = condition;
    condi = {"n=": n, "len=": image_list.length, "fix=": fixation_list.length};
    psychoJS.experiment.addData("condition", condi);
    console.log("N\u503c", n, "\u56fe\u8868\u957f\u5ea6", image_list.length, "\u6ce8\u89c6\u70b9\u8868\u957f\u5ea6", fixation_list.length, conditions.length);
    pre_img = [];
    rom_imgs = image_list.copy();
    for (var _, _pj_c = 0, _pj_a = util.range(n), _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        _ = _pj_a[_pj_c];
        temp = random.choice(rom_imgs);
        pre_img.push(temp);
        rom_imgs.remove(temp);
    }
    match_list = [];
    ram = util.range((9 * n));
    for (var _, _pj_c = 0, _pj_a = ram, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        _ = _pj_a[_pj_c];
        match_image = random.choice(image_list);
        match_list.push([match_image, match_image]);
    }
    for (var item, _pj_c = 0, _pj_a = match_list, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        item = _pj_a[_pj_c];
        temp = image_list.copy();
        n1 = n;
        while ((n1 > 1)) {
            temp.remove(item[(n - n1)]);
            item.insert(((n - n1) + 1), random.choice(temp));
            n1 -= 1;
        }
    }
    stim_list_pre = match_list.copy();
    remaining = (45 - (match_list.length * (n + 1)));
    while ((remaining > 0)) {
        new_image = random.choice(image_list);
        index = random.randint(0, stim_list_pre.length);
        if ((index < n)) {
            stim_list_pre.insert(index, [new_image]);
            remaining -= 1;
        } else {
            if ((index < stim_list_pre.length)) {
                prev_image = stim_list_pre[(index - n)][0];
                next_image = stim_list_pre[index][0];
                if (((new_image !== prev_image) && (new_image !== next_image))) {
                    stim_list_pre.insert(index, [new_image]);
                    remaining -= 1;
                }
            } else {
                if ((new_image !== stim_list_pre[(index - n)][0])) {
                    stim_list_pre.insert(index, [new_image]);
                    remaining -= 1;
                }
            }
        }
    }
    stim_list = [];
    for (var stim, _pj_c = 0, _pj_a = stim_list_pre, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        stim = _pj_a[_pj_c];
        if ((stim.length > 1)) {
            for (var s, _pj_f = 0, _pj_d = stim, _pj_e = _pj_d.length; (_pj_f < _pj_e); _pj_f += 1) {
                s = _pj_d[_pj_f];
                stim_list.push(s);
            }
        } else {
            stim_list.push(stim[0]);
        }
    }
    num_elements = stim_list.length;
    answer_list = [];
    if ((n === 1)) {
        preimg_list = ["01.png"];
    } else {
        preimg_list = ["01.png", "02.png"];
    }
    allimg_list = (preimg_list + stim_list);
    for (var i, _pj_c = 0, _pj_a = util.range(n, allimg_list.length), _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        i = _pj_a[_pj_c];
        if ((allimg_list[i] === allimg_list[(i - n)])) {
            answer_list.push("f");
        } else {
            answer_list.push("j");
        }
    }
    if ((n === 1)) {
        ncolor = "yellow";
        ntext = "-1-";
    } else {
        ncolor = "purple";
        ntext = "-2-";
    }
    
    key_resp_6.keys = undefined;
    key_resp_6.rt = undefined;
    _key_resp_6_allKeys = [];
    pic_01png_2.setImage('01.png');
    pic_02png_2.setImage('02.png');
    // keep track of which components have finished
    prepareComponents = [];
    prepareComponents.push(key_resp_6);
    prepareComponents.push(ins_1back);
    prepareComponents.push(ins_2back);
    prepareComponents.push(pic_01png_2);
    prepareComponents.push(pic_02png_2);
    
    prepareComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function prepareRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'prepare' ---
    // get current time
    t = prepareClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_6* updates
    if (t >= 0.0 && key_resp_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_6.tStart = t;  // (not accounting for frame time here)
      key_resp_6.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_6.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.clearEvents(); });
    }
    
    if (key_resp_6.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_6.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_6_allKeys = _key_resp_6_allKeys.concat(theseKeys);
      if (_key_resp_6_allKeys.length > 0) {
        key_resp_6.keys = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].name;  // just the last key pressed
        key_resp_6.rt = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].rt;
        key_resp_6.duration = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *ins_1back* updates
    if (((n == 1)) && ins_1back.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ins_1back.tStart = t;  // (not accounting for frame time here)
      ins_1back.frameNStart = frameN;  // exact frame index
      
      ins_1back.setAutoDraw(true);
    }
    
    
    // *ins_2back* updates
    if (((n == 2)) && ins_2back.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ins_2back.tStart = t;  // (not accounting for frame time here)
      ins_2back.frameNStart = frameN;  // exact frame index
      
      ins_2back.setAutoDraw(true);
    }
    
    
    // *pic_01png_2* updates
    if (t >= 0 && pic_01png_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pic_01png_2.tStart = t;  // (not accounting for frame time here)
      pic_01png_2.frameNStart = frameN;  // exact frame index
      
      pic_01png_2.setAutoDraw(true);
    }
    
    
    // *pic_02png_2* updates
    if (((n == 2)) && pic_02png_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pic_02png_2.tStart = t;  // (not accounting for frame time here)
      pic_02png_2.frameNStart = frameN;  // exact frame index
      
      pic_02png_2.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    prepareComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function prepareRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'prepare' ---
    prepareComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('prepare.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_6.corr, level);
    }
    psychoJS.experiment.addData('key_resp_6.keys', key_resp_6.keys);
    if (typeof key_resp_6.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_6.rt', key_resp_6.rt);
        psychoJS.experiment.addData('key_resp_6.duration', key_resp_6.duration);
        routineTimer.reset();
        }
    
    key_resp_6.stop();
    // the Routine "prepare" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var condition1;
function condition1LoopBegin(condition1LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    condition1 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 20, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'condition1'
    });
    psychoJS.experiment.addLoop(condition1); // add the loop to the experiment
    currentLoop = condition1;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    condition1.forEach(function() {
      snapshot = condition1.getSnapshot();
    
      condition1LoopScheduler.add(importConditions(snapshot));
      condition1LoopScheduler.add(StimRoutineBegin(snapshot));
      condition1LoopScheduler.add(StimRoutineEachFrame());
      condition1LoopScheduler.add(StimRoutineEnd(snapshot));
      condition1LoopScheduler.add(feedbackRoutineBegin(snapshot));
      condition1LoopScheduler.add(feedbackRoutineEachFrame());
      condition1LoopScheduler.add(feedbackRoutineEnd(snapshot));
      condition1LoopScheduler.add(condition1LoopEndIteration(condition1LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function condition1LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(condition1);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function condition1LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var condition2;
function condition2LoopBegin(condition2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    condition2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 20, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'condition2'
    });
    psychoJS.experiment.addLoop(condition2); // add the loop to the experiment
    currentLoop = condition2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    condition2.forEach(function() {
      snapshot = condition2.getSnapshot();
    
      condition2LoopScheduler.add(importConditions(snapshot));
      condition2LoopScheduler.add(StimRoutineBegin(snapshot));
      condition2LoopScheduler.add(StimRoutineEachFrame());
      condition2LoopScheduler.add(StimRoutineEnd(snapshot));
      condition2LoopScheduler.add(feedbackRoutineBegin(snapshot));
      condition2LoopScheduler.add(feedbackRoutineEachFrame());
      condition2LoopScheduler.add(feedbackRoutineEnd(snapshot));
      condition2LoopScheduler.add(condition2LoopEndIteration(condition2LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function condition2LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(condition2);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function condition2LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var condition3;
function condition3LoopBegin(condition3LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    condition3 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 20, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'condition3'
    });
    psychoJS.experiment.addLoop(condition3); // add the loop to the experiment
    currentLoop = condition3;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    condition3.forEach(function() {
      snapshot = condition3.getSnapshot();
    
      condition3LoopScheduler.add(importConditions(snapshot));
      condition3LoopScheduler.add(StimRoutineBegin(snapshot));
      condition3LoopScheduler.add(StimRoutineEachFrame());
      condition3LoopScheduler.add(StimRoutineEnd(snapshot));
      condition3LoopScheduler.add(feedbackRoutineBegin(snapshot));
      condition3LoopScheduler.add(feedbackRoutineEachFrame());
      condition3LoopScheduler.add(feedbackRoutineEnd(snapshot));
      condition3LoopScheduler.add(condition3LoopEndIteration(condition3LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function condition3LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(condition3);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function condition3LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var condition4;
function condition4LoopBegin(condition4LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    condition4 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 20, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'condition4'
    });
    psychoJS.experiment.addLoop(condition4); // add the loop to the experiment
    currentLoop = condition4;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    condition4.forEach(function() {
      snapshot = condition4.getSnapshot();
    
      condition4LoopScheduler.add(importConditions(snapshot));
      condition4LoopScheduler.add(StimRoutineBegin(snapshot));
      condition4LoopScheduler.add(StimRoutineEachFrame());
      condition4LoopScheduler.add(StimRoutineEnd(snapshot));
      condition4LoopScheduler.add(feedbackRoutineBegin(snapshot));
      condition4LoopScheduler.add(feedbackRoutineEachFrame());
      condition4LoopScheduler.add(feedbackRoutineEnd(snapshot));
      condition4LoopScheduler.add(condition4LoopEndIteration(condition4LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function condition4LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(condition4);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function condition4LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var condition5;
function condition5LoopBegin(condition5LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    condition5 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 20, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'condition5'
    });
    psychoJS.experiment.addLoop(condition5); // add the loop to the experiment
    currentLoop = condition5;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    condition5.forEach(function() {
      snapshot = condition5.getSnapshot();
    
      condition5LoopScheduler.add(importConditions(snapshot));
      condition5LoopScheduler.add(StimRoutineBegin(snapshot));
      condition5LoopScheduler.add(StimRoutineEachFrame());
      condition5LoopScheduler.add(StimRoutineEnd(snapshot));
      condition5LoopScheduler.add(feedbackRoutineBegin(snapshot));
      condition5LoopScheduler.add(feedbackRoutineEachFrame());
      condition5LoopScheduler.add(feedbackRoutineEnd(snapshot));
      condition5LoopScheduler.add(condition5LoopEndIteration(condition5LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function condition5LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(condition5);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function condition5LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var condition6;
function condition6LoopBegin(condition6LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    condition6 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 20, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'condition6'
    });
    psychoJS.experiment.addLoop(condition6); // add the loop to the experiment
    currentLoop = condition6;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    condition6.forEach(function() {
      snapshot = condition6.getSnapshot();
    
      condition6LoopScheduler.add(importConditions(snapshot));
      condition6LoopScheduler.add(StimRoutineBegin(snapshot));
      condition6LoopScheduler.add(StimRoutineEachFrame());
      condition6LoopScheduler.add(StimRoutineEnd(snapshot));
      condition6LoopScheduler.add(feedbackRoutineBegin(snapshot));
      condition6LoopScheduler.add(feedbackRoutineEachFrame());
      condition6LoopScheduler.add(feedbackRoutineEnd(snapshot));
      condition6LoopScheduler.add(condition6LoopEndIteration(condition6LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function condition6LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(condition6);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function condition6LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var condition7;
function condition7LoopBegin(condition7LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    condition7 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 20, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'condition7'
    });
    psychoJS.experiment.addLoop(condition7); // add the loop to the experiment
    currentLoop = condition7;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    condition7.forEach(function() {
      snapshot = condition7.getSnapshot();
    
      condition7LoopScheduler.add(importConditions(snapshot));
      condition7LoopScheduler.add(StimRoutineBegin(snapshot));
      condition7LoopScheduler.add(StimRoutineEachFrame());
      condition7LoopScheduler.add(StimRoutineEnd(snapshot));
      condition7LoopScheduler.add(feedbackRoutineBegin(snapshot));
      condition7LoopScheduler.add(feedbackRoutineEachFrame());
      condition7LoopScheduler.add(feedbackRoutineEnd(snapshot));
      condition7LoopScheduler.add(condition7LoopEndIteration(condition7LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function condition7LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(condition7);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function condition7LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var condition8;
function condition8LoopBegin(condition8LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    condition8 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 20, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'condition8'
    });
    psychoJS.experiment.addLoop(condition8); // add the loop to the experiment
    currentLoop = condition8;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    condition8.forEach(function() {
      snapshot = condition8.getSnapshot();
    
      condition8LoopScheduler.add(importConditions(snapshot));
      condition8LoopScheduler.add(StimRoutineBegin(snapshot));
      condition8LoopScheduler.add(StimRoutineEachFrame());
      condition8LoopScheduler.add(StimRoutineEnd(snapshot));
      condition8LoopScheduler.add(feedbackRoutineBegin(snapshot));
      condition8LoopScheduler.add(feedbackRoutineEachFrame());
      condition8LoopScheduler.add(feedbackRoutineEnd(snapshot));
      condition8LoopScheduler.add(condition8LoopEndIteration(condition8LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function condition8LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(condition8);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function condition8LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var this_number;
var this_image;
var response;
var piccenpos;
var ans;
var _key_resp_2_allKeys;
var StimComponents;
function StimRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Stim' ---
    t = 0;
    StimClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('Stim.started', globalClock.getTime());
    // Run 'Begin Routine' code from code_exe
    this_number = numcount;
    this_image = stim_list[(numcount - 1)];
    response = "";
    util.shuffle(piccenpos_cr);
    util.shuffle(piccenpos_ar);
    piccenpos = [piccenpos_cr[0], piccenpos_ar[0]];
    ans = answer_list[(numcount - 1)];
    psychoJS.experiment.addData("ans", ans);
    console.log("begin routine ", "count", numcount, "img", this_image, "ans", ans);
    if (key_resp_2.corr) {
        response = true;
    } else {
        response = false;
    }
    
    n_value.setColor(new util.Color(ncolor));
    n_value.setText(ntext);
    testnum.setText(this_number);
    thisimage.setPos(piccenpos);
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    sound_true.setValue('A');
    sound_true.secs=0.1;
    sound_true.setVolume(2.0);
    sound_false.setValue('B');
    sound_false.secs=0.2;
    sound_false.setVolume(4.0);
    // keep track of which components have finished
    StimComponents = [];
    StimComponents.push(image_bac);
    StimComponents.push(n_value);
    StimComponents.push(num);
    StimComponents.push(testnum);
    StimComponents.push(thisimage);
    StimComponents.push(key_resp_2);
    StimComponents.push(sound_true);
    StimComponents.push(sound_false);
    
    StimComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function StimRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Stim' ---
    // get current time
    t = StimClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_bac* updates
    if (t >= 0.0 && image_bac.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_bac.tStart = t;  // (not accounting for frame time here)
      image_bac.frameNStart = frameN;  // exact frame index
      
      image_bac.setAutoDraw(true);
    }
    
    
    // *n_value* updates
    if (t >= 0.0 && n_value.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      n_value.tStart = t;  // (not accounting for frame time here)
      n_value.frameNStart = frameN;  // exact frame index
      
      n_value.setAutoDraw(true);
    }
    
    
    // *num* updates
    if (t >= 0 && num.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      num.tStart = t;  // (not accounting for frame time here)
      num.frameNStart = frameN;  // exact frame index
      
      num.setAutoDraw(true);
    }
    
    
    // *testnum* updates
    if (t >= 0 && testnum.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      testnum.tStart = t;  // (not accounting for frame time here)
      testnum.frameNStart = frameN;  // exact frame index
      
      testnum.setAutoDraw(true);
    }
    
    
    if (thisimage.status === PsychoJS.Status.STARTED){ // only update if being drawn
      thisimage.setImage(this_image, false);
    }
    
    // *thisimage* updates
    if (t >= 0 && thisimage.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      thisimage.tStart = t;  // (not accounting for frame time here)
      thisimage.frameNStart = frameN;  // exact frame index
      
      thisimage.setAutoDraw(true);
    }
    
    
    // *key_resp_2* updates
    if (t >= 0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      key_resp_2.clock.reset();
      key_resp_2.start();
      key_resp_2.clearEvents();
    }
    
    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['f', 'j'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[0].name;  // just the first key pressed
        key_resp_2.rt = _key_resp_2_allKeys[0].rt;
        key_resp_2.duration = _key_resp_2_allKeys[0].duration;
        // was this correct?
        if (key_resp_2.keys == ans) {
            key_resp_2.corr = 1;
        } else {
            key_resp_2.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // start/stop sound_true
    if (((response == True)) && sound_true.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sound_true.tStart = t;  // (not accounting for frame time here)
      sound_true.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sound_true.play(); });  // screen flip
      sound_true.status = PsychoJS.Status.STARTED;
    }
    if (sound_true.status === PsychoJS.Status.STARTED && t >= (sound_true.tStart + 0.1)) {
      if (t >= sound_true.tStart + 0.5) {
        sound_true.stop();  // stop the sound (if longer than duration)
        sound_true.status = PsychoJS.Status.FINISHED;
      }
    }
    // start/stop sound_false
    if (((response == False)) && sound_false.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sound_false.tStart = t;  // (not accounting for frame time here)
      sound_false.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sound_false.play(); });  // screen flip
      sound_false.status = PsychoJS.Status.STARTED;
    }
    if (sound_false.status === PsychoJS.Status.STARTED && t >= (sound_false.tStart + 0.2)) {
      if (t >= sound_false.tStart + 0.5) {
        sound_false.stop();  // stop the sound (if longer than duration)
        sound_false.status = PsychoJS.Status.FINISHED;
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    StimComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function StimRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Stim' ---
    StimComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Stim.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_exe
    numcount += 1;
    
    // was no response the correct answer?!
    if (key_resp_2.keys === undefined) {
      if (['None','none',undefined].includes(ans)) {
         key_resp_2.corr = 1;  // correct non-response
      } else {
         key_resp_2.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_2.corr, level);
    }
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    psychoJS.experiment.addData('key_resp_2.corr', key_resp_2.corr);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        psychoJS.experiment.addData('key_resp_2.duration', key_resp_2.duration);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    sound_true.stop();  // ensure sound has stopped at end of Routine
    sound_false.stop();  // ensure sound has stopped at end of Routine
    // the Routine "Stim" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var fiximg;
var feedbackComponents;
function feedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback' ---
    t = 0;
    feedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.500000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('feedback.started', globalClock.getTime());
    // Run 'Begin Routine' code from feedback_code
    util.shuffle(fixation_list);
    fiximg = fixation_list[0];
    if (key_resp_2.corr) {
        response = true;
        msg = "\u7b54\u5bf9\u4e86!";
        msgcolor = "green";
    } else {
        response = false;
        msg = "\u7b54\u9519\u4e86!";
        msgcolor = "red";
    }
    
    msg_response.setColor(new util.Color(msgcolor));
    msg_response.setText(msg);
    fixation_img.setImage(fiximg);
    // keep track of which components have finished
    feedbackComponents = [];
    feedbackComponents.push(image_bac_2);
    feedbackComponents.push(msg_response);
    feedbackComponents.push(fixation_img);
    
    feedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function feedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback' ---
    // get current time
    t = feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_bac_2* updates
    if (t >= 0 && image_bac_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_bac_2.tStart = t;  // (not accounting for frame time here)
      image_bac_2.frameNStart = frameN;  // exact frame index
      
      image_bac_2.setAutoDraw(true);
    }
    
    frameRemains = 0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_bac_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_bac_2.setAutoDraw(false);
    }
    
    
    // *msg_response* updates
    if (t >= 0 && msg_response.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      msg_response.tStart = t;  // (not accounting for frame time here)
      msg_response.frameNStart = frameN;  // exact frame index
      
      msg_response.setAutoDraw(true);
    }
    
    frameRemains = 0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (msg_response.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      msg_response.setAutoDraw(false);
    }
    
    
    // *fixation_img* updates
    if (t >= 0.0 && fixation_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation_img.tStart = t;  // (not accounting for frame time here)
      fixation_img.frameNStart = frameN;  // exact frame index
      
      fixation_img.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixation_img.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixation_img.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    feedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function feedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback' ---
    feedbackComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('feedback.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_3_allKeys;
var thanksComponents;
function thanksRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'thanks' ---
    t = 0;
    thanksClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('thanks.started', globalClock.getTime());
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    // keep track of which components have finished
    thanksComponents = [];
    thanksComponents.push(text_3);
    thanksComponents.push(key_resp_3);
    
    thanksComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function thanksRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'thanks' ---
    // get current time
    t = thanksClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_3* updates
    if (t >= 0.0 && text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_3.tStart = t;  // (not accounting for frame time here)
      text_3.frameNStart = frameN;  // exact frame index
      
      text_3.setAutoDraw(true);
    }
    
    
    // *key_resp_3* updates
    if (t >= 0.0 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
    }
    
    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
        key_resp_3.duration = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    thanksComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function thanksRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'thanks' ---
    thanksComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('thanks.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_3.corr, level);
    }
    psychoJS.experiment.addData('key_resp_3.keys', key_resp_3.keys);
    if (typeof key_resp_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_3.rt', key_resp_3.rt);
        psychoJS.experiment.addData('key_resp_3.duration', key_resp_3.duration);
        routineTimer.reset();
        }
    
    key_resp_3.stop();
    // the Routine "thanks" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
