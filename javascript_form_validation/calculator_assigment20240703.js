console.log('Calculator Assignment')

var result = null;
var currentNumber = 0;
var previousNumber = 0;
var operation = null;
var resultInputElement = document.getElementById('result'); //hmtl element for the result input
// to change the result in the html. input tag to type stuff, so you can click instead of type
function updateCalculation(buttonValue) {
    if (buttonValue === 'c') { // if press on C we delete everything 
        currentNumber = 0;
        previousNumber = 0;
        operation = null;// to nothing 
        resultInputElement.value = null;// clear out the input display 
    } else if (typeof buttonValue == 'number') {// type off syntax to check the value in console log. check if its a number
        if (currentNumber !== 0) {//if the number is 0 
            currentNumber += buttonValue.toString();//we make two numbers into strings
        } else {
            currentNumber = buttonValue.toString();
        }
        resultInputElement.value = currentNumber;//update the number 
    } else if (buttonValue === '.') {// if you press on a dot
        currentNumber = (currentNumber || 0).toString() + '.';
        resultInputElement.value = currentNumber;
    } else if (buttonValue == '+') {
        operation = '+';
        resultInputElement.value = '+';
        previousNumber = parseFloat(currentNumber || result);//previous number to the current number or the result
        currentNumber = 0;// so i can + several times several operations
    }
    else if (buttonValue == '*') {
        operation = '*';
        resultInputElement.value = '*';
        previousNumber = parseFloat(currentNumber || result);
        currentNumber = 0;
    }
    else if (buttonValue == '/') {
        operation = '/';
        resultInputElement.value = '/';
        previousNumber = parseFloat(currentNumber || result);
        currentNumber = 0;
    }
    else if (buttonValue == '-') {
        operation = '-';
        resultInputElement.value = '-';
        previousNumber = parseFloat(currentNumber || result);
        currentNumber = 0;
    }
    else if (buttonValue == '=') {
        currentNumber = parseFloat(currentNumber);
        if (operation === '+') {
            result = currentNumber + previousNumber;
            resultInputElement.value = result;//display show the result
        } else if (operation === '*') {
            result = currentNumber * previousNumber;
            resultInputElement.value = result;
        } else if (operation === '/') {
            if (currentNumber == 0) {
                result = 'division by zero';
                resultInputElement.value = result;
            } else {
                result = previousNumber / currentNumber;
                resultInputElement.value = result;
            }
        } else if (operation === '-') {
            result = previousNumber - currentNumber;
            resultInputElement.value = result;
        }
        currentNumber = 0;//after pressing = it resents to 0 
    }
}
