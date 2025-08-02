// declaration of variables
const screen = document.getElementById('screen');
const soustractionButton = document.getElementById('soustractionButton');
const additionButton = document.getElementById('additionButton');

screen.textContent = 100;
let counter = screen.textContent;
console.log(counter);
soustractionButton.addEventListener('click',()=>{
    counter--;
    screen.textContent = counter;
});


additionButton.addEventListener('click',function(){
    counter++;
    screen.textContent = counter;
});
