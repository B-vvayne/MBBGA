let operators = ["+","-","*"];
const startBtn = document.getElementById("start-btn");
const question = document.getElementById("question");
const controls = document.querySelector("controls-container");
const result = document.getElementById("result");
const submitBtn = document.getElementById("submit-btn");
const errorMessage = document.getElementById("error-msg");
let answerValue;
let operatorQuestion;

//random value generator
const randomValue = (min,max) => Math.floor(Math.random()*(max-min))+min;

const questionGenerator = () => {
    let [num1, num2] = [randomValue(1,20),randomValue(1,20)];

    let randomOperator = operators[Math.floor(Math.random()*operators.length)];

    if(randomOperator == "-" && num2>num1){
    [num1,num2] = [num2,num1];
    }

    //solve equation
    let solution = eval(`${num1}${randomOperator}${num2}`);
    
    //for placing the input at random position
    let randomVar = randomValue(1,5);
    
    if(randomVar == 1){
        answerValue = num1;
        question.innerHTML = `<input type="number" id ="inputValue" placeholder="?" \> ${randomOperator} ${num2} = ${solution}`;
    }else if(randomVar == 2) {
        answerValue = num2;
        question.innerHTML = `${num1} ${randomOperator} <input type="number" id ="inputValue" placeholder="?"\> = ${solution}`;
    }
    else if(randomVar == 3){
        answerValue = randomOperator;
        operatorQuestion = true;
        question.innerHTML = `${num1} <input type="text" id ="inputValue" placeholder="?"\> ${num2} = ${solution}`;
    } else{
        answerValue = solution;
        question.innerHTML = `${num1} ${randomOperator} ${num2} = <input type="number" id="inputValue" placeholder="?"\>`;
    }


//user input check
submitBtn.addEventListener("click",() => {
    
    errorMessage.classList.add("hide");
    let userInput = document.getElementById("inputValue").value;
    if (userInput){
        if(userInput == answerValue){
            stopGame(`Yippie!!<span>Correct</span> Answer`);
            startBtn.classList.remove('hide');
        }
        //if inputs operators other than +-*
        else if (operatorQuestion && !operators.includes(userInput)){
            errorMessage.classList.remove("hide");
            errorMessage.innerHTML = "please enter a valid operator";
        }
        //if user guessed wrong answer
        else{
            stopGame(`Opps!!<span>Wrong</span> Answer`);
            startBtn.innerHTML = "";
            startBtn.classList.add('hide');
        }
    }
        //if user input is empty
    else {
            errorMessage.classList.remove("hide");
            errorMessage.innerHTML = "input cannot be Empty";
        }
});

};
let exNum = 0;
let codeArr = [];
//start
startBtn.addEventListener("click", () => {
    exNum = exNum + 1;
    if (exNum > 5) {
        alert('记忆完成，开始回忆阶段');
        window.location.href = 'index_dual2.html';
    } else {
        codeArr.push(getCode(4));
        document.getElementById('checkCode').innerText = codeArr[codeArr.length-1];
        console.log(codeArr);
        // 存储数据
        localStorage.setItem('codeArr', JSON.stringify(codeArr));

        if (startBtn.innerText === "Next") {
            result.innerHTML = "";
        }
        operatorQuestion = false;
        answerValue = "";
        errorMessage.innerHTML = "";
        errorMessage.classList.add("hide");
        questionGenerator();
        startBtn.innerHTML = "";
        startBtn.classList.add('hide');
    }
    
});

const stopGame = (resultText) => {
    result.innerHTML = resultText;
    startBtn.innerText = "Next";  

};


function getCode(n){
    var arr = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'];
    var str = '';
    for (var i = 0;i<n;i++){
        var num = Math.round(Math.random()*(15-0)+0);
        str += arr[num];
    }
    return str;
}

