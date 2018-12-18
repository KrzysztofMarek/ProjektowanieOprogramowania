jQuery.validator.addMethod("validateOfferName", function (value, element) {
    var regex = new RegExp("^[a-zA-ZżźćńółęąśŻŹĆĄŚĘŁÓŃ-\\s]+$");

    if (regex.test(value)) {
        return true;
    }
    return false;
}, "Nazwa dania może zawierać jedynie litery, białe znaki oraz myślniki");

jQuery.validator.addMethod("validateOfferNameBigLetter", function (value, element) {
    var regex = new RegExp("^[A-ZŻŹĆĄŚĘŁÓŃ]");

    if (regex.test(value)) {
        return true;
    }
    return false;
}, "Nazwa dania z dużej litery");

jQuery.validator.addMethod("validatePrice", function (value, element) {
    var regex = new RegExp("^\\d{1,3}\\,?\\d{1,2}?$");
    var isComa = value.includes(',');

    if (isComa) {
        if (regex.test(value)) {
            return true;
        }
    } else if (value.length > 0 && value.length < 4) {
        return true;
    }
    return false;
}, "Cena w formacie 000,00");

jQuery.validator.addMethod("validateDescription", function (value, element) {
    var forbidden = ['#', '$', '^', '%', '&', '*', '!', '@'];
    return forbidden.every(function (f) { return !value.includes(f) });
}, "Pole nie może zawierać znaków specjalnych");