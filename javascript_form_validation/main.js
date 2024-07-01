// define validate inputs function

function validateInputs() {
    var isNameInputValid = true;
    var nameInput = document.getElementsByName('name')[0];
    var nameInputValue = nameInput.value;
    if (nameInputValue === "") {
        isNameInputValid = false;
    }
    var nameInvalidMessageElement = document.getElementsByName('nameInvalidMessage')[0];
    if (!isNameInputValid) {
        nameInvalidMessageElement.style.display = "";
        nameInvalidMessageElement.style.color = "red";
    }
}