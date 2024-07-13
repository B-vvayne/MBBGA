let viewportWidth = window.innerWidth;
let viewportHeight = window.innerHeight;



document.addEventListener("DOMContentLoaded", ()=>{
    console.log('1',viewportWidth);
    console.log('1',window.outerWidth);
    let container = document.querySelector("div");
    container.style.width = '100%';
    container.style.height = '100%';
})

sessionStorage.setItem('lastTime','800');
sessionStorage.setItem('trainNum','0');
sessionStorage.setItem('corrNum','0');

let myButtons= document.querySelectorAll('button');
for(let i = 0; i < myButtons.length; i++){
    myButtons[i].addEventListener('click', function(){
        sessionStorage.setItem('length',(i+5).toString());
        window.location.href = 'nback_train.html';
    })
}
