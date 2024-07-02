

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
