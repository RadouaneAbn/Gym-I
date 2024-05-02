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
    emailValid = 1;
    validate()
    if (valid) {
        console.log('valid');
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
    console.log('req')
    $('#err-signin').html('&nbsp;');

    

    $.ajax ({
        type: 'post',
        // url: 'http://0.0.0.0:5002/clients/login',
        url: '/token',
        contentType: 'application/json',
        data: JSON.stringify({
            email: email.value,
            password: pwd.value
        }),
        success: function (token) {
            // console.log('/' + user.id)
            sessionStorage.setItem('_token', token.access_token)
            // window.location.href = '/me';
            redirectToMeOrLogin();
            // console.log(localStorage.getItem('_token'));
            // window.location.href = '/me';
        },
        statusCode: {
            404: function () {
                $('#err-signin').text('Email doesn\'t exist');
            },
            401: function () {
                $('#err-signin').text('Incorrect password');
            }
        },
        error: function (xhr, status, error) {
            console.log('Error:', xhr.responseText);  // Handle unauthorized access or other errors
            if (xhr.status === 401) {
              console.log('Unauthorized - Token might be invalid or expired');
              // Redirect to login or show an error message
            //   window.location.href = '/login';
            }
          },
    })
}


function redirectToMeOrLogin() {
    const token = sessionStorage.getItem('_token');
    // console.log('tok:', token)
    if (token) {
        $.ajax({
            url: '/me',
            type: 'GET',
            Headers: {
                'Authorization': 'Bearer ' + token
            },
            success: function (data) {
                // window.location.href = '/me'; 
                console.log('data:', data)
            },
            error: function (xhr, status, error) {
                console.log('Error:', xhr.responseText);  // Handle unauthorized access or other errors
                if (xhr.status === 401) {
                  console.log('Unauthorized - Token might be invalid or expired');
                  // Redirect to login or show an error message
                window.location.href = '/signin'; 
                }
              },
        })
    } else {
        console.log('token not found')
        window.location.href = '/signin'; 
    }
}