$(document).ready(function () {
    start();
    emailSyntax();

    // [email, pwd].forEach(field => {
    //     field.addEventListener('click', function () {
    //         field.html('&nbsp;')
    //     })
    // })
});
let valid;
let email;
let pwd;
let submit;
let emailMsg;
let pwdMsg;
let emailValid = 0;

function start() {
    email = document.getElementById('email');
    pwd = document.getElementById('pwd');
    submit = document.getElementById('submit');
    emailMsg = document.getElementById('err-email')
    pwdMsg = document.getElementById('err-pwd')
    submit.addEventListener("click", login)
}

function emailSyntax() {
    email.addEventListener('blur', function (){
        const regexEmail = /^[^@]+@[^@]+\.\w+$/;
        if (email.value && !regexEmail.test(email.value)) {
            $('#err-email').text('Wrong email format')
            emailValid = 0;
        } else {
            $('#err-email').html('&nbsp;')
            emailValid = 1;
        }
    })
}


function login () {
    validate()
    if (valid) {
        console.log('run');
        requestLogin();
    } else {
        console.log('fail');
    }
}

function validate() {
    valid = emailValid;
    if (!email.value) {
        $('#err-email').text('Email field is empty')
        valid *= 0;
    }
    if (!pwd.value) {
        $('#err-pwd').text('Password field is empty')
        valid *= 0;
    }
}

function requestLogin() {
    $.ajax ({
        type: 'post',
        url: 'http://0.0.0.0:5002/clients/login',
        contentType: 'application/json',
        data: JSON.stringify({
            email: email.value,
            password: pwd.value
        }),
        success: function (user) {
            console.log(user)
        }
    })
}