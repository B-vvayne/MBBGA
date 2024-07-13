let viewport_height = window.innerHeight;

//为引导框设置自适应上边距----------------------------------------------------------------------------------------
let myDiv = document.querySelector('div');
document.addEventListener('DOMContentLoaded', () => {
    myDiv.style.marginTop = 0.3*viewport_height + 'px';
})

document.addEventListener('keydown', () => {
    //let mySpan = document.querySelector('span');
    //mySpan.textContent = `${event.key}`;
    if(event.key === ' '){
        window.location.href='nback2_train.html';

    }
})