//获取视口尺寸
let viewport_width = window.innerWidth;
let viewport_height = window.innerHeight;


let myPassage = document.querySelector('p');
let myGrid = document.querySelector('.container');
let mySpan = document.querySelectorAll('span');
let myDiv = document.querySelectorAll('div');


//设置margin---------------------------------------------------------------------------------------------------
function setMargin(){
    myPassage.style.marginTop = 0.1*viewport_height + 'px';
}

document.addEventListener('DOMContentLoaded', setMargin)

//按下任意按键，生成n-back案例（案例中n不是随机数），给出正误判断和反应时间---------------------------------------------------------------

let startTrainFlag= false;//开始训练标志位
let reactTime;//记录反应时间
let numArr = [4,2,9,4,8,3];

async function runExample(){
    //隐藏段落文字
    myPassage.textContent = "测试组";
    //隐藏网格数字
   for(let i = 0; i < mySpan.length; i++){
       mySpan[i].textContent = '';
   }

   for(let i = 0; i < 6; i++){
       myDiv[numArr[i]].style.backgroundColor = 'green';

       //色块显示2S
         await new Promise(resolve=>{
            setTimeout(()=>{
                if(i<5) {
                    myDiv[numArr[i]].style.backgroundColor = 'grey';
                }
                    resolve();
                }, 800)
            }
        );
   }
   //显示问题
    myPassage.textContent = "从最后一个方块往前数4次，绿色方块出现的位置是？";
    reactTime = Date.now();
}

function judgeResult(event){
    let result;
    reactTime = Date.now()-reactTime;
    if(event.key === numArr[1].toString() ){
        result = "正确";
    }else{
        result = "错误";
    }
    return result;
}

document.addEventListener("keydown", ()=>{
    if(startTrainFlag===false){
        startTrainFlag = true;
        runExample().then(()=> {
            document.addEventListener("keydown", ()=>{
                let result = judgeResult(event);
                //window.location.href='nback_result.html?result='+encodeURIComponent(result)+'&reactTime='+encodeURIComponent(reactTime);
                myPassage.textContent=`${result}!反应时间为${reactTime*0.001}秒！按下任意键返回!`
                document.addEventListener("keydown", ()=>{
                        window.location.replace('../Nback/index.html');
                });
            })

        });
    }
});


