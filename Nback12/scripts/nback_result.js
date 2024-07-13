let myPassage = document.querySelectorAll('p');

//获取视口高度
let viewport_height = window.innerHeight;


document.addEventListener("DOMContentLoaded", () => {
    // 获取页面的URL中的查询字符串部分
    let queryString = window.location.search;
    // 创建一个URLSearchParams对象
    let params = new URLSearchParams(queryString);
    // 从查询字符串中获取result和reactTime的值
    let result = params.get('result');
    let reactTime = params.get('reactTime');

    myPassage[0].style.marginTop = viewport_height*0.45 + 'px';

    myPassage[0].textContent = `${result}!反应时间为${reactTime*0.001}秒！`;
    myPassage[1].textContent = "按下任意按键继续";
})

document.addEventListener('keydown', () => {
    window.location.href='nback_train.html';
})