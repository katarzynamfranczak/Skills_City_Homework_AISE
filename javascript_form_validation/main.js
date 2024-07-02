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
   
    var isEmailInputValid = true;
    var emailInput = document.getElementsByName('email')[0];
    var emailInputValue = emailInput.value;
    if (emailInputValue == ""){
        isEmailInputValid = false;
    }
    var emailInvalidMessageElement = document.getElementsByName('emailInvalidMessage')[0];
    if (!isEmailInputValid){
        emailInvalidMessageElement.style.display="";
        emailInvalidMessageElement.style.color ="red";
    }

    var isContactNumberValid = true;
    var contactNumberInput = document.getElementsByName('contactNumber')[0];
    var contactNumberValue = contactNumberInput.value;
    if (contactNumberValue ==""){
        isContactNumberValid = false;
    }
    var contactNumberInvalidMessageElement = document.getElementsByName('contactNumberInvalidMessage')[0];
    if (!isContactNumberValid){
        contactNumberInvalidMessageElement.style.display="";
        contactNumberInvalidMessageElement.style.color ="red";
    }

    var isCityValid = true;
    var cityInput = document.getElementsByName('city')[0];
    var cityValue = cityInput.value;
    if (cityValue ==""){
        isCityValid = false;
    }

    var cityInvalidMessageElement = document.getElementsByName('cityInvalidMessage')[0];
    if (!isCityValid){
        cityInvalidMessageElement.style.display="";
        cityInvalidMessageElement.style.color ="red";
    }

    var isDescriptionValid = true;
    var descriptionInput = document.getElementsByName('city')[0]; //scans the html, it searches for tags that have the name called city
    var descriptionValue = descriptionInput.value;
    if (descriptionValue ==""){
        isDescriptionValid = false;
    }

    var descriptionInvalidMessageElement = document.getElementsByName('descriptionInvalidMessage')[0];
    if (!isDescriptionValid){
        descriptionInvalidMessageElement.style.display="";
        descriptionInvalidMessageElement.style.color ="red";
    }

}