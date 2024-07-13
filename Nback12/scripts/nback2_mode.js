let viewportWidth = window.innerWidth;
let viewportHeight = window.innerHeight;



document.addEventListener("DOMContentLoaded", ()=>{
    console.log('1',viewportWidth);
    console.log('1',window.outerWidth);
    let container = document.querySelector("div");
    container.style.width = '100%';
    container.style.height = '100%';
})

let myButtons= document.querySelectorAll('button');
for(let i = 0; i < myButtons.length; i++){
    myButtons[i].addEventListener('click', function(){
        sessionStorage.setItem('n',(i+1).toString());
        window.location.href = 'nback2_train.html';
    })
}