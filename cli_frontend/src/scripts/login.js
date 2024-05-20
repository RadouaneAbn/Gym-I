$(document).ready(function () {
  start();
  emailSyntax();
});
let valid;
let email;
let pwd;
let submit;
let emailMsg;
let pwdMsg;
let emailValid = 0;

function start () {
  email = document.getElementById('email');
  pwd = document.getElementById('pwd');
  submit = document.getElementById('submit');
  emailMsg = document.getElementById('err-email');
  pwdMsg = document.getElementById('err-pwd');

  submit.addEventListener('click', login);

  email.addEventListener('keydown', function (event) {
    if (event.keyCode === 13) {
      login();
    }
  });

  pwd.addEventListener('keydown', function (event) {
    if (event.keyCode === 13) {
      login();
    }
  });
}

function emailSyntax () {
  email.addEventListener('blur', function () {
    const regexEmail = /^[^@]+@[^@]+\.\w+$/;
    if (email.value && !regexEmail.test(email.value)) {
      $('#err-email').text('Wrong email format');
      emailValid = 0;
    } else {
      $('#err-email').html('&nbsp;');
      emailValid = 1;
    }
  });
}

function login () {
  emailValid = 1;
  validate();
  if (valid) {
    // console.log('valid');
    requestLogin();
  } else {
    // console.log('fail');
  }
}

function validate () {
  valid = emailValid;
  if (!email.value) {
    $('#err-email').text('Email field is empty');
    valid *= 0;
  }
  if (!pwd.value) {
    $('#err-pwd').text('Password field is empty');
    valid *= 0;
  }
}

function requestLogin () {
  // console.log('req');
  $('#err-signin').html('&nbsp;');
  $.ajax({
    type: 'post',
    url: 'http://0.0.0.0:5002/api/v1/clients/login',
    // url: '/token',
    contentType: 'application/json',
    data: JSON.stringify({
      email: email.value,
      password: pwd.value
    }),
    success: function (token) {
      // console.log('/' + user.id)
      localStorage.setItem('access_token', token.access_token);
      localStorage.setItem('token_type', 'Bearer');
      window.location.href = '/user/gymes';
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
      console.error('Error:', xhr.responseText); // Handle unauthorized access or other errors
      if (xhr.status === 401) {
        console.error('Unauthorized - Token might be invalid or expired');
      }
    }
  });
}