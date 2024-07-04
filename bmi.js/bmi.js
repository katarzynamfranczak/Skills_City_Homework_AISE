console.log("bmi check if html is connected")

alert("Let's calculate your BMI!");

let userInputWeight = prompt("Enter your weight in kg: ");//input html
let userInputHeight = prompt("Enter your height in cm: ");

userInputWeight = parseFloat(userInputWeight);//change to deci.
userInputHeight = parseFloat(userInputHeight)/100;// cm need to be divided by 100 to move the "."

// let bmi = userInputWeight/Math.pow(userInputHeight, 2);

// alert("Your BMI is " + bmi);
alert("Your BMI is: " + userInputWeight/Math.pow(userInputHeight, 2));// calculation straight in alert

var bmi = userInputWeight/Math.pow(userInputHeight, 2);

bmi = Math.floor(bmi);// slims down the number to and int 

if (bmi <= 18) {
    alert("Your BMI is low, you should contact a doctor.")
}

   else if (bmi <= 25) {
        alert("Well done, your BMI is in recommented range!");
   }
        else {
            alert("You BMI seems to be high, contact your doctor.");
        }