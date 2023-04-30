// SOURCE: https://www.codewars.com/kata/529b418d533b76924600085d/train/javascript

function toUnderscore(string) {
    if(typeof string !== 'string') return string.toString();
    
    let lettersArray = [string[0]];
    for(let i = 1; i < string.length; i++){
        if(string.charCodeAt(i) >= 97 && string.charCodeAt(i) <= 122 || string.charCodeAt(i) >= 48 && string.charCodeAt(i) <= 57){
            lettersArray.push(string[i]);
        }else{
            lettersArray.push("_");
            lettersArray.push(string[i]);
        }
    }
    let unitedLettersArray = lettersArray.join("").toLowerCase();
    return unitedLettersArray;
  }

  console.log(toUnderscore("MoviesAndBooks"));