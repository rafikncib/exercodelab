// Returns a random integer from 1 to 1000:
        
let result = Math.floor(Math.random() * 1000) + 1;

const formGuess = document.getElementById('formGuess');
const numberInput = document.getElementById('number');
const formHelp = document.getElementById('formHelp');
const hint = document.getElementById('hint');
formGuess.addEventListener('submit',(even)=>{
    even.preventDefault();
    let gessNumber = Number.parseInt(numberInput.value);
    if(result===gessNumber){
        alert('You did it');
    }else {
        if(hint.checked){
            if(gessNumber < result){
                alert('Your guess is small!');
            }else{
                alert('Your guess is high!');
            }
        }else{
            alert("Try again!")
        }
    }
})


formHelp.addEventListener('submit',(even)=>{
    even.preventDefault();
    alert('The number is '+result);
})