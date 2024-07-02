let userInput = prompt ("What's your name?");
if (userInput.trim() == null || userInput.trim() == ""){ //function .trim to remove spaces for the start and the end of the string
    userInput = "Mystery Person"
        alert(userInput + ", finally you've ve arrived! Just on time to see what this web can do.");
}else {
    alert("Hello, " + userInput + "! Let's find out what this web does!");
    }
var number = [-5, -2,-6,0,10];
var largest = number[0];
alert("There is a list made out of " + number.length + " numbers.");
alert("The code should allow us to see the largest number from the list.");

for (var a =0; a<number.length; a++){
    if (number[a]> largest){
    largest = number[a];    
    }
}     
console.log("The largest number is: " + largest);
alert("The largest number is " + largest + " ! YAY!");
alert("Dear " + userInput + ", Farewell! I hope you've had fun with loops in js!")