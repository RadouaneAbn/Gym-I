let userInfo;

function popUpPicture(user) {
    return `
    <div id="profile_pic_container"
    class="bg-gray-900 bg-opacity-50  w-full h-screen flex justify-center items-center">

        <div style="width: 500px; height: 600px;"
        class="bg-gray-100 p-4 border border-gray-900 rounded-md text-center relative flex flex-col justify-center items-center">

            <img class="border-2 border-red-500 absolute top-0 right-0 m-4 cursor-pointer" id="cancel-picture"
            src="/cli_frontend//images/exit.png" alt="exit" width="25px" height="25px">

            <h2 class="text-xl font-medium">Upload Your Profile Picture</h2>
            <div style="height: 300px; width: 300px; overflow: hidden;"
            class="rounded-full mt-10 mb-8 border-2 border-gray-500">            
                <img src="${user.profile_picture_original}"
                class="object-cover object-center"
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
    `
}

function popUpDelete() {
    return `
    <div id="profile_pic_container"
    class="bg-gray-900 bg-opacity-50  w-full h-screen flex justify-center items-center">

        <div style="width: 500px; height: 600px;"
        class="bg-gray-100 p-4 border border-gray-900 rounded-md text-center relative flex flex-col justify-center items-center">

        <img class="border-2 border-red-500 absolute top-0 right-0 m-4 cursor-pointer" id="cancel-picture"
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
    `
}

function PaymentPage() {
    return `
    <div class="items-center mt-8 sm:mt-14 text-[#202142]">
    <h1 class="text-4xl flex items-center justify-center underline text-indigo-900 mx-auto text-semibold mb-4">Payment</h1>
    
    <div class="mb-2 sm:mb-6">
    <label for="name"
    class="block mb-2 text-sm font-medium text-indigo-900 dark:text-white">Youy full name</label>
    <input type="text" id="name"
    class="bg-indigo-50 border border-indigo-300 text-indigo-900 text-sm rounded-lg focus:ring-indigo-500 focus:border-indigo-500 block w-full p-2.5 "
    placeholder="enter your full name" value="" required>
    </div>
    
    <div class="mb-2 sm:mb-6">
    <label for="account_number"
    class="block mb-2 text-sm font-medium text-indigo-900 dark:text-white">Account Number</label>
    <input type="text" id="account_number"
    class="bg-indigo-50 border border-indigo-300 text-indigo-900 text-sm rounded-lg focus:ring-indigo-500 focus:border-indigo-500 block w-full p-2.5 "
    placeholder="0000 0000 0000 0000" value="" required>
    </div>
    
    <div
        class="flex flex-col items-center w-full mb-2 space-x-0 space-y-2 sm:flex-row sm:space-x-4 sm:space-y-0 sm:mb-6">
        <div class="w-full">
            <label for="expiry"
                class="block mb-2 text-sm font-medium text-indigo-900 dark:text-white">Expiry</label>
            <input type="text" id="expiry"
                class="bg-indigo-50 border border-indigo-300 text-indigo-900 text-sm rounded-lg focus:ring-indigo-500 focus:border-indigo-500 block w-full p-2.5 "
                placeholder="MM/YY" value="" required>
        </div>
    
        <div class="w-full">
            <label for="cvv"
                class="block mb-2 text-sm font-medium text-indigo-900 dark:text-white">CVV</label>
            <input type="text" id="cvv"
                class="bg-indigo-50 border border-indigo-300 text-indigo-900 text-sm rounded-lg focus:ring-indigo-500 focus:border-indigo-500 block w-full p-2.5 "
                placeholder="000" value="" required>
        </div>
    
    </div>
    
    <div class="mb-2 sm:mb-6">
        <label for="password"
            class="block mb-2 text-sm font-medium text-indigo-900 dark:text-white">Password</label>
        <input type="password" id="passwor"d
            class="bg-indigo-50 border border-indigo-300 text-indigo-900 text-sm rounded-lg focus:ring-indigo-500 focus:border-indigo-500 block w-full p-2.5 "
            placeholder="Enter old password" required>
    </div>
    
    
    <div class="flex justify-end">
        <button type="submit"
            class="text-white bg-indigo-700  hover:bg-indigo-800 focus:ring-4 focus:outline-none focus:ring-indigo-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-indigo-600 dark:hover:bg-indigo-700 dark:focus:ring-indigo-800">Save</button>
    </div>
    
    </div>
    `;
}

function ProfilePage(user) {
    return `
<div class="p-2 md:p-4">
    <div class="w-full px-6 pb-8 mt-8 sm:max-w-xl sm:rounded-lg">
        <h2 class="pl-6 text-2xl font-bold sm:text-xl">Public Profile</h2>
    
        <div class="grid max-w-2xl mx-auto mt-8">
            <div class="flex flex-col items-center space-y-5 sm:flex-row sm:space-y-0">
    
                <img class="object-cover w-40 h-40 p-1 rounded-full ring-2 ring-indigo-300 dark:ring-indigo-500"
                    src="${user.profile_picture_original}"
                    alt="Bordered avatar">
    
                <div class="flex flex-col space-y-5 sm:ml-8">
                    <button id="change-picture"
                        class="py-3.5 px-7 text-base font-medium text-indigo-100 focus:outline-none bg-[#202142] rounded-lg border border-indigo-200 hover:bg-indigo-900 focus:z-10 focus:ring-4 focus:ring-indigo-200 ">
                        Change picture
                    </button>
                    <button type="button" id="delete-btn"
                        class="py-3.5 px-7 text-base font-medium text-indigo-900 focus:outline-none bg-white rounded-lg border border-indigo-200 hover:bg-indigo-100 hover:text-[#202142] focus:z-10 focus:ring-4 focus:ring-indigo-200 ">
                        Delete picture
                    </button>
                </div>
            </div>
    
            <div class="items-center mt-8 sm:mt-14 text-[#202142]">
    
                <div
                    class="flex flex-col items-center w-full mb-2 space-x-0 space-y-2 sm:flex-row sm:space-x-4 sm:space-y-0 sm:mb-6">
                    <div class="w-full">
                        <label for="first_name"
                            class="block mb-2 text-sm font-medium text-indigo-900 dark:text-white">Your
                            first name</label>
                        <input type="text" id="first_name"
                            class="bg-indigo-50 border border-indigo-300 text-indigo-900 text-sm rounded-lg focus:ring-indigo-500 focus:border-indigo-500 block w-full p-2.5 "
                            placeholder="Your first name" value="${user.first_name}" required readonly>
                    </div>
    
                    <div class="w-full">
                        <label for="last_name"
                            class="block mb-2 text-sm font-medium text-indigo-900 dark:text-white">Your
                            last name</label>
                        <input type="text" id="last_name"
                            class="bg-indigo-50 border border-indigo-300 text-indigo-900 text-sm rounded-lg focus:ring-indigo-500 focus:border-indigo-500 block w-full p-2.5 "
                            placeholder="Your last name" value="${user.last_name}" required readonly>
                    </div>
    
                </div>
                <div
                    class="flex flex-col items-center w-full mb-2 space-x-0 space-y-2 sm:flex-row sm:space-x-4 sm:space-y-0 sm:mb-6">
                    <div class="w-full">
                        <label for="city"
                            class="block mb-2 text-sm font-medium text-indigo-900 dark:text-white">Your
                            City</label>
                        <input type="text" id="city"
                            class="bg-indigo-50 border border-indigo-300 text-indigo-900 text-sm rounded-lg focus:ring-indigo-500 focus:border-indigo-500 block w-full p-2.5 "
                            placeholder="Entre your City" value="Marrakech" required>
                    </div>
    
                    <div class="w-full">
                        <label for="Mobile"
                            class="block mb-2 text-sm font-medium text-indigo-900 dark:text-white">Your
                            phone</label>
                        <input type="number" id="phone"
                            class="bg-indigo-50 border border-indigo-300 text-indigo-900 text-sm rounded-lg focus:ring-indigo-500 focus:border-indigo-500 block w-full p-2.5 "
                            placeholder="+212 ..." value="06000000" required>
                    </div>
    
                </div>
    
                <div class="mb-2 sm:mb-6">
                    <label for="addresse"
                        class="block mb-2 text-sm font-medium text-indigo-900 dark:text-white">Addresse</label>
                    <input type="text" id="addresse"
                        class="bg-indigo-50 border border-indigo-300 text-indigo-900 text-sm rounded-lg focus:ring-indigo-500 focus:border-indigo-500 block w-full p-2.5 "
                        placeholder="Enter your addresse" required>
                </div>
                
                <div class="flex justify-end">
                    <button type="submit"
                        class="text-white bg-indigo-700  hover:bg-indigo-800 focus:ring-4 focus:outline-none focus:ring-indigo-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-indigo-600 dark:hover:bg-indigo-700 dark:focus:ring-indigo-800">Save</button>
                </div>
    
            </div>
        </div>
    </div>
    </div>`;
}

function onceCall(callback) {
    let called = false;
  
    return (...args) => {
      if (!called) {
        called = true;
        return callback(...args);
      }
    };
}
  

let helpMain = ``;
let proMain = ``;
function changeMainContent(content) {
    // console.log("Changing main content...");
    $('#dynamicMain').empty()
    $('#dynamicMain').append(content)
    // document.getElementById('dynamicMain').innerHTML = content;
}

async function builtProfileInfoPage() {
    const result = await fetch('http://0.0.0.0:5002/token_check', {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${token}`,
        }
    })
    .then(res => res.json())
    .then(data => {
        userInfo = data.user;
        const pageContent = ProfilePage(data.user);
        appendToDiv(pageContent)
    })
}

function appendToDiv(content) {
    // document.getElementById('dynamicMain').innerHTML = content;
    $('#dynamicMain').empty()
    $('#dynamicMain').append(content)
    $('button#change-picture').on('click', changePicture)
    $('button#delete-btn').on('click', deletPicture)
}

function deletPicture() {
    console.log('del')
    $('div#popups').append(popUpDelete())
    $('#ignore').on('click', () => {
        $('div#popups').empty();
    })

    const ignore = document.getElementById('ignore-btn');
    const confirm = document.getElementById('confirm-btn');

    const deletePicAdv = onceCall(uploadPicture);
    
    
}

function uploadPicture(img) {
        console.log('update')
        const dataForm = new FormData();
        dataForm.append('file_upload', img)
        fetch('http://0.0.0.0:5002/update_picture/', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${token}`,
            },
            body: dataForm,
        })
        .then(data => {
            if (data.ok) {
                window.location.href = '/profile';
            }
        })
}

function changePicture() {
    console.log('change')
    $('div#popups').append(popUpPicture(userInfo))
    $('#cancel-picture').on('click', () => {
        $('div#popups').empty();
    })

    const inputFile = document.getElementById('input-file');
    const profilePicture = document.getElementById('profile-pic');

    inputFile.onchange = function () {
        profilePicture.src = URL.createObjectURL(inputFile.files[0])
    }

    const uploadPictureAdv = onceCall(uploadPicture);
    
    $('label#save-btn').on('click', () => {
        uploadPictureAdv(inputFile.files[0])
    })
}

// Add event listener to the 'payment' button after DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // console.log("DOM Loaded");
    let paymentButton = document.getElementById('payment');
    let paymentMenu = document.getElementById('payment_menu');
    let profileButton = document.getElementById('Profile');
    let profileMenu = document.getElementById('Profile_menu');
    let helpButton = document.getElementById('Help');
    let helpMenu = document.getElementById('help_menu');
    let proButton = document.getElementById('Pro');
    let proMenu = document.getElementById('pro_menu');
    // const changePicBtn = document.getElementById('change-picture');
    builtProfileInfoPage();

    // console.log(paymentButton);
    paymentButton.addEventListener('click', function(event) {
    //   console.log("Button clicked");
      changeMainContent(payementMain); // Call the function to change the content
    });
    paymentMenu.addEventListener('click', function(event) {
        // console.log("Button clicked");
        changeMainContent(payementMain); // Call the function to change the content
      });

    profileButton.addEventListener('click', function(event) {
    //   console.log("Button clicked");
      changeMainContent(profileMain); // Call the function to change the content
    });
    profileMenu.addEventListener('click', function(event) {
        // console.log("Button clicked");
        changeMainContent(profileMain); // Call the function to change the content

    helpButton.addEventListener('click', function(event) {
      console.log("Button clicked");
      changeMainContent(helpMain); // Call the function to change the content
    });
    helpMenu.addEventListener('click', function(event) {
        console.log("Button clicked");
        changeMainContent(helpMain); // Call the function to change the content
      });


    proButton.addEventListener('click', function(event) {
      console.log("Button clicked");
      changeMainContent(proMain); // Call the function to change the content
    });
    proMenu.addEventListener('click', function(event) {
        console.log("Button clicked");
        changeMainContent(proMain); // Call the function to change the content
      });
  })
})
