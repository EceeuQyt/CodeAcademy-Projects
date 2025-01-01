// All valid credit card numbers
const valid1 = [4, 5, 3, 9, 6, 7, 7, 9, 0, 8, 0, 1, 6, 8, 0, 8];
const valid2 = [5, 5, 3, 5, 7, 6, 6, 7, 6, 8, 7, 5, 1, 4, 3, 9];
const valid3 = [3, 7, 1, 6, 1, 2, 0, 1, 9, 9, 8, 5, 2, 3, 6];
const valid4 = [6, 0, 1, 1, 1, 4, 4, 3, 4, 0, 6, 8, 2, 9, 0, 5];
const valid5 = [4, 5, 3, 9, 4, 0, 4, 9, 6, 7, 8, 6, 9, 6, 6, 6];
const valid6 = [4, 4, 8, 5, 3, 0, 4, 1, 7, 4, 5, 9, 8, 4, 3, 5];
// All invalid credit card numbers
const invalid1 = [4, 5, 3, 2, 7, 7, 8, 7, 7, 1, 0, 9, 1, 7, 9, 5];
const invalid2 = [5, 7, 9, 5, 5, 9, 3, 3, 9, 2, 1, 3, 4, 6, 4, 3];
const invalid3 = [3, 7, 5, 7, 9, 6, 0, 8, 4, 4, 5, 9, 9, 1, 4];
const invalid4 = [6, 0, 1, 1, 1, 2, 7, 9, 6, 1, 7, 7, 7, 9, 3, 5];
const invalid5 = [5, 3, 8, 2, 0, 1, 9, 7, 7, 2, 8, 8, 3, 8, 5, 4];

// Can be either valid or invalid
const mystery1 = [3, 4, 4, 8, 0, 1, 9, 6, 8, 3, 0, 5, 4, 1, 4];
const mystery2 = [5, 4, 6, 6, 1, 0, 0, 8, 6, 1, 6, 2, 0, 2, 3, 9];
const mystery3 = [6, 0, 1, 1, 3, 7, 7, 0, 2, 0, 9, 6, 2, 6, 5, 6, 2, 0, 3];
const mystery4 = [4, 9, 2, 9, 8, 7, 7, 1, 6, 9, 2, 1, 7, 0, 9, 3];
const mystery5 = [4, 9, 1, 3, 5, 4, 0, 4, 6, 3, 0, 7, 2, 5, 2, 3];

// An array of all the arrays above
//Possibly used to loop through all arrays w/ find invalidCards.
const batch = [valid1, valid2, valid3, valid4, valid5, invalid1, invalid2, invalid3, invalid4, invalid5, mystery1, mystery2, mystery3, mystery4, mystery5];


// Add your functions below:
/** Function One */
const validateCred = (creditArr) => {
//Readable variables, Locally Scope
let luhn = [];
let creditCard = [];
//Original Credit card
  for(let i = 0; i < creditArr.length; i++){
    creditCard.push(creditArr[i]);
  }
//console.log(creditCard);

/** Uses Luhn algorithm:
  * Reversing card, then remove #0 index.
  * For loop that iterators every other element by 1 using the 'i+=num' increment. Basically, starting from 0 index, skips one element iterating the next and so on.
  * Double the digits by mutiplying 2
  * If nums are greater then 9 after doubling, subtract 9 from its value, else keep single digit*/
  //let firstE = creditCard.pop();
  //console.log(firstE);
  let modifiedCred = creditCard.reverse()//.slice(1);
  console.log(modifiedCred);
  for(var i = 0; i < modifiedCred.length; i+=2){
     if(modifiedCred[i]*2 > 9){
       modifiedCred[i] = (modifiedCred[i]*2) - 9;
       luhn.push(modifiedCred[i]);
     }else{
       luhn.push(modifiedCred[i]*2)
     }
     //console.log(luhn) for proccess
  }
//console.log(luhn)
/* Next, Supposedly adds dropped nums to luhn Array by seperating original Credit card by oddOne and evenOne.*/
  var oddOnes = [];
  var evenOnes = [];
    for(var i=0; i<modifiedCred.length; i++){
      (i % 2 == 0 ? evenOnes : oddOnes).push(modifiedCred[i]);
      //console.log(evenOnes, oddOnes) for entire proccess  
    }
    //Using .concat(), merges luhn with dropped numbers.
    //Stored in a variable since it doesn't mutate.
    var finalLuhn = luhn.concat(oddOnes);
    //console.log(evenOnes, oddOnes);
    console.log(finalLuhn); 

/* Finds sum result of all nums using .reduce() method.*/
let sum = finalLuhn.reduce((a, b) => a + b, 0);
console.log(sum);

/**Ternary Operator, aka if/else shortcut
 * If sum variable, divided by 10, has remaider of zero then true--valid, else false--invalid. */
return  sum % 10 === 0 /** firstE */? true : false;
};



/** Function Two */
const findInvalidCards = (setOfCredCards) => {
  let invalidCards = [];
  let validCards = [];
  for(let i=0; i < batch.length; i++){
    let valid = validateCred(setOfCredCards[i]);
    (valid !== true ? invalidCards : validCards).push(setOfCredCards[i])
    /** 
    if(valid !== true){
      invalidCards.push(setOfCredCards[i]);
    }else{
      validCards.push(setOfCredCards[i]);
    }*/
  }
  //console.log(validCards);
  return invalidCards;
};

/** Function Three */
//make a switch case w/ for loop
 function idInvalidCardCompanies(setOfCc){
    let companies = [];
     let amex = 0;
     let visa = 0;
     let masterCard = 0;
     let discover = 0;
     let noCompanies = 0;
    for (let i = 0; i < setOfCc.length; i++) {
       if(setOfCc[i][0]=== 3){
         if(amex === 0){
           companies.push('Amex[AE]');
         }
         amex++;
       }
       else if(setOfCc[i][0] === 4){
         if(visa === 0){
           companies.push('Visa');
         }
         visa++;
       }
       else if(setOfCc[i][0] === 5){
         if(masterCard === 0){
           companies.push('MasterCard');
         }
         masterCard++;
       }
       else if(setOfCc[i][0] === 6){
         if(discover ===  0){
           companies.push('Discover');
         }
         discover++;
       }
       else{
         if(noCompanies === 0){
           companies.push('N/a');
         }
         noCompanies++;
        }
      }
    //console.log(visa, masterCard, amex, discover)
    //console.log(results);
    return companies;
  }; 
  



/**Reference test to check if function worked properly
  Function #1 :
   *console.log(validateCred(valid2));
   *console.log(validateCred(invalid3));
   *console.log(validateCred(batch[5]));---true
   *console.log(validateCred(batch[2]));---false
  Function #2 :
   *console.log(findInvalidCards(batch));
  Function #3 :
   *const results = findInvalidCards(batch)
   *console.log(idInvalidCardCompanies(results));
*/
