const username = "Regina"
 username? console.log(`Hello, ${username}!`):console.log('Hello!');
const userQuestion = "Will I get that promotion?"
 console.log(`You asked, ${userQuestion}`);
var randomNumber = Math.floor(Math.random()*9)
let eightBall = randomNumber
  console.log(`The mystics say, ${eightBall}`)
  switch (eightBall){
    case 1:
    console.log('It is almost certain');
    break;
    case 2:
    console.log('It\'s decidedly so');
    break;
    case 3:
    console.log('Reply hazy, try again');
    break;
    case 4:
    console.log("Don't count on it");
    break;
    case 5:
    console.log('My sources say no');
    break;
    case 6:
    console.log('Cannot predict now');
    break;
    case 7:
    console.log('Outlook not so good');
    break;
    case 8:
    console.log('All signs point to yes');
    break;
  default:
    console.log('Have tired for today');
    break;
    
  }