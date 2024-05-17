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
    console.log('valid');
    requestLogin();
  } else {
    console.log('fail');
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
  console.log('req');
  $('#err-signin').html('&nbsp;');
  $.ajax({
    type: 'post',
    url: 'http://0.0.0.0:5002/clients/login',
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
      console.log('Error:', xhr.responseText); // Handle unauthorized access or other errors
      if (xhr.status === 401) {
        console.log('Unauthorized - Token might be invalid or expired');
        // Redirect to login or show an error message
        //   window.location.href = '/login';
      }
    }
  });
}

function redirectToMeOrLogin () {
  const token = localStorage.getItem('_token');
  // console.log('tok:', token)
  if (token) {
    // function submitToken() {
    //     const form = document.createElement('form');
    //     form.method = 'GET';
    //     form.action = '/user/gymes';

    //     const hiddenField = document.createElement('input');
    //     hiddenField.type = 'hidden';
    //     hiddenField.name = 'authorization';
    //     hiddenField.value = `Bearer ${token}`
    //     form.append(hiddenField);

    //     document.body.appendChild(form);
    //     // console.log(form)
    //     form.submit();
    // }
    // submitToken()

    // fetch('/user/gymes', {
    //     method: 'GET',
    //     headers: {
    //       'Authorization': `Bearer ${token}`,
    //       'Content-Type': 'application/json'
    //     }
    //   })
    //   .then(res => res.json())
    //   .then(data => {
    //     console.log(data)
    //     const blobUrl = URL.createObjectURL(new Blob([data], { type: "text/html" }));
    //     const newWindow = window.location(blobUrl, "_blank");

    //   })

    // $.ajax({
    //     url: '/user/gymes',
    //     type: 'GET',
    //     Headers: {
    //         'Authorization': 'Bearer ' + token
    //     },
    //     success: function (data) {
    //         // window.location.href = '/me';
    //         // console.log('data:', data)
    //     },
    //     error: function (xhr, status, error) {
    //         console.log('Error:', xhr.responseText);  // Handle unauthorized access or other errors
    //         if (xhr.status === 401) {
    //           console.log('Unauthorized - Token might be invalid or expired');
    //           // Redirect to login or show an error message
    //         window.location.href = '/signin';
    //         }
    //       },
    // })
  } else {
    console.log('token not found');
    window.location.href = '/signin';
  }
}
