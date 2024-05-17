let valid = 1;
let validEmail = 1;

$(document).ready(function () {
  start();
});

function onceCall (callback) {
  let called = false;

  return (...args) => {
    if (!called) {
      called = true;
      return callback(...args);
    }
  };
}

function start () {
  const firsNname = document.getElementById('first_name');
  const lastName = document.getElementById('last_name');
  const email = document.getElementById('email');
  const pwd = document.getElementById('pwd');
  const rPwd = document.getElementById('r-pwd');
  const submit = document.getElementById('submit');
  const fields = document.querySelectorAll('.field');
  const showPwd = document.getElementById('show-pwd');
  const phoneNumber = document.getElementById('phone-number');

  fields.forEach(field => {
    field.addEventListener('click', function () {
      field.style.border = '1px solid transparent';
    });
  });

  showPwd.addEventListener('click', function () {
    if (showPwd.checked) {
      pwd.type = rPwd.type = 'text';
    } else {
      pwd.type = rPwd.type = 'password';
    }
  });

  email.addEventListener('blur', function () {
    if (email.value && !validateEmail(email.value)) {
      $('p.err-email').text('Wrong email format');
    } else if (email.value) {
      $.ajax({
        type: 'POST',
        url: 'http://0.0.0.0:5002/emailcheck/',
        contentType: 'application/json',
        data: JSON.stringify({ email: email.value }),
        success: function (status) {
          if (status) {
            $('p.err-email').html('&nbsp;');
            validEmail = 1;
          } else {
            $('p.err-email').text('email already exists');
            email.style.border = '2px solid #F3755B';
            validEmail = 0;
          }
        }
      });
    } else { { $('p.err-email').html('&nbsp;'); } }
  });

  submit.addEventListener('click', function () {
    $('.err-pwd').html('&nbsp;');
    valid = validEmail;
    if (!valid) {
      $('p.err-pwd').text('email already exists');
      return;
    }
    [firsNname, lastName, email, pwd, rPwd, phoneNumber].forEach(field => {
      if (!field.value) {
        field.style.border = '2px solid #F3755B';
        valid *= 0;
      }
    });
    if (!valid) {
      $('.err-pwd').text('No empty fields are allowed');
      return;
    }

    validatPassword(pwd.value);

    if (rPwd) {
      if (rPwd.value !== pwd.value) {
        $('.err-pwd').text('Passwords are not identical.');
        rPwd.value = '';
        valid *= 0;
      }
    }

    if (valid) {
      popForProfilePic(firsNname.value, lastName.value, email.value, pwd.value);
    }
  });

  function validatPassword (pwd) {
    const lowerCase = /[a-z]/;
    const upperCase = /[A-Z]/;
    const number = /[0-9]/;
    const symbol = /[!@#$%^&*]/;
    valid = 0;

    if (pwd.length < 8) {
      $('.err-pwd').text('Use 8 characters or more for your password');
    } else if (!lowerCase.test(pwd)) {
      $('.err-pwd').text('Password should at least have one lowercase letter');
    } else if (!upperCase.test(pwd)) {
      $('.err-pwd').text('Password should at least have one uppercase letter');
    } else if (!number.test(pwd)) {
      $('.err-pwd').text('Password should at least have one number');
    } else if (!symbol.test(pwd)) {
      $('.err-pwd').text('Password should at least have one symbol');
    } else {
      valid = 1;
    }
  }

  function validateEmail (email) {
    const regex = /^[^@]+@[^@]+\.\w+$/;
    if (!regex.test(email)) {
      validEmail = 0;
      return false;
    }
    return true;
  }
}

function popForProfilePic (firstName, lastName, email, passWord) {
  const registerCon = document.getElementById('register-form-container');
  const profilePicture = document.getElementById('profile-pic');
  const profilePictureCon = document.getElementById('profile_pic_container');
  const inputFile = document.getElementById('input-file');
  const nextBtn = document.getElementById('next-btn');

  registerCon.style.display = 'none';
  profilePictureCon.style.display = 'flex';

  inputFile.onchange = function () {
    profilePicture.src = URL.createObjectURL(inputFile.files[0]);
  };

  const createClientOnce = onceCall(createClient);

  nextBtn.addEventListener('click', () => {
    createClientOnce(inputFile.files[0], firstName, lastName, email, passWord);
  });
}

function createClient (img, firstName, lastName, email, passWord) {
  console.log(firstName);
  const dataForm = new FormData();
  dataForm.append('first_name', firstName);
  dataForm.append('last_name', lastName);
  dataForm.append('email', email);
  dataForm.append('password', passWord);
  if (img) {
    $('label#next-btn').text('Uploading ...');
    dataForm.append('file_upload', img);
  }

  fetch('http://0.0.0.0:5002/clients/', {
    method: 'POST',
    body: dataForm
  })
    .then(data => {
      if (data.ok) {
        window.location.href = '/signin';
      }
    });
}
