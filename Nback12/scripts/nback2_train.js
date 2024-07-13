let viewport_height = window.innerHeight;

//为引导框设置自适应上边距----------------------------------------------------------------------------------------
let myPassage = document.querySelector('p');
document.addEventListener('DOMContentLoaded', () => {
    myPassage.style.marginTop = 0.15*viewport_height + 'px';
})

const imgLastTime1 = 800;
const imgLastTime2 = 500;


let groupNum = 12;//训练组数，总共12组，前6组n，后6组n+1
let epochesNum = 30;//每组训练轮次，总共30轮次

let n = 1;//需要页面传参，n控制训练难度
if(!sessionStorage.getItem('n')){
    sessionStorage.setItem('n',n);
}else{
    n = sessionStorage.getItem('n');
}


//获取随机图片,种类为9------------------------------------------------------------------------------------------------
function getRandomImg1(){
    let r = new Array(32).fill(1);
    for (let i = 0; i < 30; i++) {
        r[i+1] = Math.floor(Math.random() * 9)+1;
    }
    return r;
}
//获取随机图片，种类为18
function getRandomImg2(){
    let r = Math.floor(Math.random() * 18)+1;
    return r.toString();
}

//生成随机位置以放置图片（除中心位置）
function getRandomPosition(){
    let r;
    do{
        r = Math.floor(Math.random() * 9);
    }while(r===4);
    return r;
}

//生成随机的箭头干扰物
function getRandomArrow(){
    let a=['up','down','left','right','ld','rd','lu','ru'];
    let r = a[Math.floor(Math.random() * 8)];
    return r;
}

//开始训练函数----------------------------------------------------------------------------------------------------------

//显示题目，判断准确性
// function train(n,ques,j,lastTime,accu){
//     let p = getRandomPosition();
//     myImgs[p].setAttribute('src',`images/${ques[j+1]}.png`);
//     let st = Date.now();
//     // while( (Date.now()-st)<800 ){
//     // //循环等待到指定的持续时间
//     // }
//     myImgs[p].setAttribute('src',`blank.png`);
//     let waitFlag=true;
//
//     //系统判断答案
//     let answer;
//     if(ques[j+1]===ques[j+1-n]){
//         answer=true;
//     }else{
//         answer=false;
//     }
//     //等待作答
//     while(waitFlag){
//         document.addEventListener("keydown", ()=>{
//             //用户认为正确
//             if(event.key ==='f'|| event.key ==='F'){
//                 waitFlag=false;
//                 if(answer){
//                     myPassage.textContent='答对了！'
//                     myPassage.style.color="green";
//                     accu[j]=1;
//                 }else{
//                     myPassage.textContent='答错了！'
//                     myPassage.style.color="red";
//                     accu[j]=0;
//                 }
//
//             }else if(event.key === 'j' || event.key ==='J'){//用户认为错误
//                 waitFlag=false;
//                 if(answer){
//                     myPassage.textContent='答错了！'
//                     myPassage.style.color="red";
//                     accu[j]=0;
//                 }else{
//                     myPassage.textContent='答对了！'
//                     myPassage.style.color="green";
//                     accu[j]=1;
//                 }
//             }else{
//
//             }
//
//         })
//     }
//     //箭头干扰
//     myImgs[4].setAttribute('src',`images/${getRandomArrow()}.png`);
//
//     st=Date.now();
//     while(Date.now()-st<1000){
//
//     }
//     myImgs[4].setAttribute('src','images/blank.png');
//
// }

let myImgs = document.querySelectorAll('img');
function train(n, ques, j, lastTime, accu) {
    let p = getRandomPosition();
    myImgs[p].setAttribute('src', `images/${ques[j+1]}.png`);

    // 使用setTimeout代替忙等待
    setTimeout(() => {
        myImgs[p].setAttribute('src', 'images/blank.png');
        let answer;
        if (ques[j+n] === ques[j]) {
            answer = true;
        } else {
            answer = false;
        }

        let waitFlag = true;
        const handleKeyDown = (event) => {
            // 根据用户的按键判断答案的正确性
            if ((event.key === 'f' || event.key === 'F') || (event.key === 'j' || event.key === 'J')) {
                waitFlag = false;
                if (event.key === 'f' || event.key === 'F') {
                    if (answer) {
                        myPassage.textContent = '答对了！';
                        myPassage.style.color = "green";
                        accu[j] = 1;
                    } else {
                        myPassage.textContent = '答错了！';
                        myPassage.style.color = "red";
                        accu[j] = 0;
                    }
                } else {
                    if (!answer) {
                        myPassage.textContent = '答对了！';
                        myPassage.style.color = "green";
                        accu[j] = 1;
                    } else {
                        myPassage.textContent = '答错了！';
                        myPassage.style.color = "red";
                        accu[j] = 0;
                    }
                }
                // 移除事件监听器，避免重复触发
                document.removeEventListener('keydown', handleKeyDown);

                // 箭头干扰
                myImgs[4].setAttribute('src', `images/${getRandomArrow()}.png`);
                setTimeout(() => {
                    myImgs[4].setAttribute('src', 'images/blank.png');

                }, 1000); // 假设干扰持续1000ms
            }
        };
        document.addEventListener('keydown', handleKeyDown);
    }, lastTime);
}






//i控制训练组数(12),j控制训练轮次(30)
//记录每组答题情况
let accu = new Array(30).fill(0);
let reactTime = new Array(30).fill(0);

// for(let i = 0; i < groupNum; i++){
//     let ques = getRandomImg1();
//     for(let j = 0; j < epochesNum; j++){
//         train(n,ques,j,imgLastTime1,accu);
//     }
// }


// let ques = getRandomImg1();
// train(n,ques,0,imgLastTime1,accu);
// 假设train函数已经被正确地修改为异步函数，并且接受必要的参数
async function performTraining() {


    let ques;
    for(let i=0;i < groupNum;i++){
        if(i<6){
            n=1;
            // 每次训练轮次前获取问题
            if(i<3){
                ques=getRandomImg1();
            }else{
                ques = getRandomImg2();
            }
        }else{
            n=2;
            if(i<9){
                ques=getRandomImg1();
            }else{
                ques = getRandomImg2();
            }
        }

        for (let j = 0; j < epochesNum; j++) {
            myPassage.textContent=`No.${i+1}-${j+1}`;
            myPassage.style.color = "white";
            // 等待train函数完成
            await new Promise((resolve) => {

                let p = getRandomPosition();
                myImgs[p].setAttribute('src', `images/${ques[j+1]}.png`);

                let imgLastTime;
                if(i===2||i===5||i===8||i===11){
                    imgLastTime = imgLastTime2;
                }else{
                    imgLastTime = imgLastTime1;
                }
                // 使用setTimeout代替忙等待
                setTimeout(() => {
                    let t1 = Date.now();//用于记录反应时间
                    myImgs[p].setAttribute('src', 'images/blank.png');
                    let answer;
                    if (ques[j+n] === ques[j]) {
                        answer = true;
                    } else {
                        answer = false;
                    }


                    const handleKeyDown = (event) => {
                        reactTime[j]=Date.now()-t1;

                        // 根据用户的按键判断答案的正确性
                        if ((event.key === 'f' || event.key === 'F') || (event.key === 'j' || event.key === 'J')) {

                            if (event.key === 'f' || event.key === 'F') {
                                if (answer) {
                                    myPassage.textContent = '答对了！';
                                    myPassage.style.color = "green";
                                    accu[j] = 1;
                                } else {
                                    myPassage.textContent = '答错了！';
                                    myPassage.style.color = "red";
                                    accu[j] = 0;
                                }
                            } else {
                                if (!answer) {
                                    myPassage.textContent = '答对了！';
                                    myPassage.style.color = "green";
                                    accu[j] = 1;
                                } else {
                                    myPassage.textContent = '答错了！';
                                    myPassage.style.color = "red";
                                    accu[j] = 0;
                                }
                            }
                            // 移除事件监听器，避免重复触发
                            document.removeEventListener('keydown', handleKeyDown);

                            // 箭头干扰
                            if(i===0||i===3||i===6||i===9){
                                myImgs[4].setAttribute('src', `images/center.png`);
                            }else if (i===1||i===4||i===7||i===10){
                                myImgs[4].setAttribute('src', `images/${getRandomArrow()}.png`);
                            }else{
                                myImgs[4].setAttribute('src', `images/${getRandomArrow()}.png`);
                            }

                            setTimeout(() => {
                                myImgs[4].setAttribute('src', 'images/blank.png');
                                resolve();
                            }, 1000); // 假设干扰持续1000ms
                        }
                    };
                    document.addEventListener('keydown', handleKeyDown);
                }, imgLastTime);

            });
        }
        //待补充
        //向数据库发送每一组的答题情况和每一小题的反应时间
    }


    if(window.confirm("恭喜你完成了训练！")){
        window.location.href='../N-back/index.html';
    }else{
        window.location.href='../N-back/index.html';
    }

}

// 调用performTraining函数开始训练
performTraining();

