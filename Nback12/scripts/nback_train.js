//获取视口尺寸
let viewport_width = window.innerWidth;
let viewport_height = window.innerHeight;

let myPassage = document.querySelector('p');
let mySpan = document.querySelectorAll('span');
let myDiv = document.querySelectorAll('div');

//设定难度常量
const difficulty1 = 5;
const difficulty2 = 6;
const difficulty3 = 7;
const eps = 1e-10;//防止分母除以0；

//let acc = 0;//准确率
let length = 0;//数组长度
if(!sessionStorage.getItem('length')){
    length = difficulty1;
}else{
    length = +sessionStorage.getItem('length');
}

let trainNum = 0;//记录训练轮次
let corrNum = 0;//记录正确轮次
//sessionStorage的数据只在同一个标签页内保留
//监测是否存在trainNum和corrNum,若不存在则将数据存入session，表示一个n-back训练开始
if(!sessionStorage.getItem('corrNum')){
    sessionStorage.setItem('trainNum',trainNum.toString());
    sessionStorage.setItem('corrNum',corrNum.toString());
}


//设置margin---------------------------------------------------------------------------------------------------
function setMargin(){
    myPassage.style.marginTop = 0.1*viewport_height + 'px';
}

document.addEventListener('DOMContentLoaded', setMargin)

//按下任意按键，进行n-back范式训练，给出结果和反应时间-------------------------------------------------------------------------
let startTrainFlag= false;//开始训练标志位，用于每一个训练的epoches
let reactTime;//记录反应时间

//获得随机数数组，用来生成题目
function getRandomNum(length){
    let r = new Array(length);
    let a;
    r[0] = Math.floor(Math.random() * 9) + 1;
    for(let i = 1; i < length; i++){
        do{
            a = Math.floor(Math.random() * 9) + 1;
            r[i]=a;
        }while(r[i]===r[i-1]);
    }
    return r;
}

function getRandomN(length){
    let r = Math.floor(Math.random() * (length-1)) + 1;
    return r;
}

// let numArr = getRandomNum(4);
// let n = getRandomN(4);

async function runExample(numArr,n,lastTime){
    //隐藏段落文字
    myPassage.textContent = "训练组";
    //隐藏网格数字
    for(let i = 0; i < mySpan.length; i++){
        mySpan[i].textContent = '';
    }

    for(let i = 0; i < numArr.length; i++){
        myDiv[numArr[i]].style.backgroundColor = 'green';

        //色块显示2S
        await new Promise(resolve=>{
                setTimeout(()=>{
                    //最后一个方块不能灭，所以这里有一个条件判断
                    if(i<numArr.length-1) {
                        myDiv[numArr[i]].style.backgroundColor = 'grey';
                    }
                    resolve();
                }, lastTime)
            }
        );
    }
    //显示问题
    myPassage.textContent = `从最后一个方块往前数${n}次，绿色方块出现的位置是？`;
    reactTime = Date.now();
}

function judgeResult(length,n,numArr,event){
    let result;
    reactTime = Date.now()-reactTime;
    let q = length-n-1;
    if(event.key === numArr[q].toString() ){
        result = "正确";
        //若正确则正确轮次+1
        corrNum = +sessionStorage.getItem('corrNum');
        corrNum++;
        sessionStorage.setItem('corrNum',corrNum.toString());
    }else{
        result = "错误";
    }
    //总训练轮次+1
    trainNum = +sessionStorage.getItem('trainNum');
    trainNum++;
    sessionStorage.setItem('trainNum',trainNum.toString());

    if(trainNum%5===0&&trainNum!==0){
        if( sessionStorage.getItem('corrNum') >=4){
            lastTime = lastTime - 100;
        }else{
            lastTime = lastTime + 100;
        }
        sessionStorage.setItem('lastTime', lastTime.toString());
        sessionStorage.setItem('corrNum','0');
    }


    return result;



}

let lastTime = 800;
if(sessionStorage.getItem('lastTime') === false){
    sessionStorage.setItem('lastTime',lastTime.toString());
}else{
    lastTime = +sessionStorage.getItem('lastTime');
    console.log('lasttime',lastTime);
}

//这里按下任意键开始训练
document.addEventListener("keydown", ()=>{
    let a = +sessionStorage.getItem('trainNum');//一元加号法将字符串转换为number
    let b = +sessionStorage.getItem('corrNum');//一元加号法将字符串转换为number
    let acc = b/Math.max(a,eps);

    //自适应难度
    // if(acc<0.6||a<5){
    //     length = difficulty1;
    // }else if(acc>=0.6&&acc<0.8){
    //     length = difficulty2;
    // }else{
    //     length = difficulty3;
    // }

    //length = difficulty1;

    //难度自适应：根据每5次的正确率（>4），讲lastTime+-0.1S
    // if(a%5===0&&a!==0){
    //     if(b>=4){
    //         lastTime = lastTime - 100;
    //     }else{
    //         lastTime = lastTime + 100;
    //     }
    //     sessionStorage.setItem('lastTime', lastTime.toString());
    //     sessionStorage.setItem('corrNum','0');
    // }


    let numArr = getRandomNum(length);
    let n = getRandomN(length);



    if(startTrainFlag===false){
        startTrainFlag = true;
        runExample(numArr,n,lastTime).then(()=> {
            //这里按下按键答题
            document.addEventListener("keydown", ()=>{
                let result = judgeResult(length,n,numArr,event);
                startTrainFlag = false;
                //控制训练的总轮次
                //小于设定的训练次数则跳转至结果显示页面，否则跳转至else选定的界面
                if(a<100) {
                    window.location.href = 'nback_result.html?result=' + encodeURIComponent(result) + '&reactTime=' + encodeURIComponent(reactTime);
                }else{
                    //训练完毕，清空数据，返回指定页面
                    sessionStorage.deleteItem('corrNum');
                    sessionStorage.deleteItem('trainNum');

                    //结束训练，跳转
                    if(window.confirm("恭喜你完成了训练！")){
                        window.location.href = '../Nback/index.html';
                    }else{
                        window.location.href = '../Nback/index.html';
                    }

                    //window.confirm('恭喜你完成了训练！')
                    //window.location.href = 'nback_index.html';
                }
            })
        });
    }
});

