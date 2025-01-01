let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below:
//Function 1a, 1b, 1c
function generateTarget() {
  return Math.ceil(Math.random()*10);
};

function computerChoice() {
  return Math.floor(Math.random()*10);
};

function userChoice (userInput){
  if(userInput > 0 && userInput < 10) {
    return userInput;
   }
  return 'Incorrect, NAN between 0-9.'
};


//Function 2
var compareGuesses = (user, computer, targetAim) => {
  const targerAim = generateTarget()
  const userDifference = Math.abs(targetAim - userChoice(5));
  const computerDifference = Math.abs(targetAim - computerChoice());
  return userDifference <= computerDifference; 
/*Longer version:
 if (userDifference <= computerdiffernce){
    return true;
  }else if(userDifference > computerDifference){
    return false;
  }
*/
};

//Function 3
//Delcare Increment or Decrement for Goblal Variables
let updateScore = (winner) => {
  if (winner === "human"){
    humanScore++
  }else if (winner === "computer"){
    computerScore++
  }
};

//Function 4
var advanceRound = () => {
   currentRoundNumber++;
};

//Verification: 
console.log(generateTarget())
console.log(userChoice(5))
console.log(computerChoice())
console.log(compareGuesses())

updateScore('human');
console.log(humanScore);

updateScore('computer');
console.log(computerScore);

console.log(advanceRound());