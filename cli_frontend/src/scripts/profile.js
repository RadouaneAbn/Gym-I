let userInfo;

function popUpPicture (user) {
  return `
    <div id="profile_pic_container"
    class="bg-gray-900 bg-opacity-50  w-full h-screen flex justify-center items-center">

        <div style="width: 500px; height: 600px;"
        class="bg-gray-100 p-4 border border-gray-900 rounded-md text-center relative flex flex-col justify-center items-center">

            <img class="border-2 border-red-500 absolute top-0 right-0 m-4 cursor-pointer" id="cancel-btn"
            src="/cli_frontend/images/exit.png" alt="exit" width="25px" height="25px">

            <h2 class="text-xl font-medium">Upload Your Profile Picture</h2>
            <div style="height: 300px; width: 300px; overflow: hidden;"
            class="rounded-full mt-10 mb-8 border-2 border-gray-500">
                <img src="${user.profile_picture_original}"
                class=""
                alt="profile picture"
                id="profile-pic" width="300px" height="300px">
            </div>
            <div class="mt-10 flex justify-between px-8 w-full">
                <label style="width: 160px; height: 50px;" for="input-file" class=" bg-blue-500 text-white font-bold py-3 px-5 rounded cursor-pointer hover:bg-blue-600 transition">Upload image</label>
                <label id="save-btn" style="width: 160px; height: 50px;"  class="bg-blue-500 text-white font-bold py-3 px-5 rounded cursor-pointer hover:bg-blue-600 transition">
                    Save
                </label>
            </div>

            <input type="file" accept="image/jpeg" id="input-file" style="display: none;">

        </div>
    </div>
    `;
}

function popUpDelete () {
  return `
    <div id="profile_pic_container"
    class="bg-gray-900 bg-opacity-50  w-full h-screen flex justify-center items-center">

        <div style="width: 500px; height: 300px;"
        class="bg-gray-100 p-4 border border-gray-900 rounded-md text-center relative flex flex-col justify-center items-center">
        <h2 class="mt-5 text-xl font-medium">Are you sure you want to delete the profile picture ?</h2>
        <img class="border-2 border-red-500 absolute top-0 right-0 m-4 cursor-pointer" id="cancel-btn"
        src="/cli_frontend//images/exit.png" alt="exit" width="25px" height="25px">

            <div class="mt-10 flex justify-between px-8 w-full">
                <button id="ignore-btn" style="width: 160px; height: 50px;" class=" bg-blue-500 text-white font-bold py-3 px-5 rounded cursor-pointer hover:bg-blue-600 transition">
                    Ignore
                </button>

                <button id="confirm-btn" style="width: 160px; height: 50px;" class="bg-blue-500 text-white font-bold py-3 px-5 rounded cursor-pointer hover:bg-blue-600 transition">
                    Delete
                </button>
            </div>
        </div>
    </div>
    `;
}

document.addEventListener('DOMContentLoaded', function () {
  builtProfileInfoPage();
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

const helpMain = '';
const proMain = '';

async function builtProfileInfoPage () {
  const result = await fetch('http://0.0.0.0:5002/token_check', {
    method: 'GET',
    headers: {
      Authorization: `Bearer ${token}`
    }
  })
    .then(res => res.json())
    .then(data => {
      userInfo = data.user;
      updateProfile(data.user);
    });
}

function updateProfile (user) {
  document.getElementById('profile_main_picture').src = user.profile_picture_original;
  document.getElementById('first_name').value = user.first_name;
  document.getElementById('last_name').value = user.last_name;

  $('button#change-picture').on('click', changePicture);
  $('button#delete-btn').on('click', deletPicture);
}

function deletPicture () {
  console.log('del');
  $('div#popups').append(popUpDelete());
  $('#cancel-btn').on('click', () => {
    $('div#popups').empty();
  });

  const ignore = document.getElementById('ignore-btn');
  const confirm = document.getElementById('confirm-btn');

  const deletePicAdv = onceCall(deletPictureRequest);

  ignore.addEventListener('click', () => {
    $('div#popups').empty();
  });

  confirm.addEventListener('click', () => {
    deletePicAdv();
  });
}

function deletPictureRequest () {
  console.log('delete');
  fetch(`http://0.0.0.0:5002/profile_picture/${userInfo.id}`, {
    method: 'DELETE'
  })
    .then(data => {
      if (data.ok) {
        window.location.href = '/profile';
      }
    });
}

function uploadPicture (img) {
  // console.log('update')
  $('label#save-btn').text('Uploading ...');
  const dataForm = new FormData();
  dataForm.append('file_upload', img);
  fetch('http://0.0.0.0:5002/profile_picture/', {
    method: 'PUT',
    headers: {
      Authorization: `Bearer ${token}`
    },
    body: dataForm
  })
    .then(data => {
      if (data.ok) {
        window.location.href = '/profile';
      }
    });
}

function changePicture () {
  console.log('change');
  $('div#popups').append(popUpPicture(userInfo));
  $('#cancel-btn').on('click', () => {
    $('div#popups').empty();
  });

  const inputFile = document.getElementById('input-file');
  const profilePicture = document.getElementById('profile-pic');
  let changed = false;
  inputFile.onchange = function () {
    changed = true;
    profilePicture.src = URL.createObjectURL(inputFile.files[0]);
  };

  const uploadPictureAdv = onceCall(uploadPicture);

  $('label#save-btn').on('click', () => {
    if (changed) {
      uploadPictureAdv(inputFile.files[0]);
    }
  });
}
