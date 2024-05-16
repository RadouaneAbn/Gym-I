const historicPage = `
    <div class="flex-1 mx-auto w-full h-1/4">
          you can find all your historic gym subsctiption here.
          <p>all suscribtion still active are shown in the table with active status</p>
        </div>
        <div class="flex flex-col">
          <div class="overflow-x-auto sm:-mx-6 lg:-mx-8">
            <div class="inline-block min-w-full py-2 sm:px-6 lg:px-8">
              <div class="overflow-hidden">
                <table
                  class="min-w-full text-center text-sm font-light text-surface dark:text-white">
                  <thead
                    class="border-b border-zinc-200 bg-[#332D2D] font-medium text-white dark:border-white/10">
                    <tr>
                      <th scope="col" class=" px-6 py-4">Gym Name</th>
                      <th scope="col" class=" px-6 py-4">Start at</th>
                      <th scope="col" class=" px-6 py-4">End at</th>
                      <th scope="col" class=" px-6 py-4">Status</th>
                    </tr>
                  </thead>
                  <tbody class="bg-gray-50">
                    <tr class="border-b border-neutral-600 dark:border-white/10">
                      <td class="whitespace-nowrap  px-6 py-4 font-medium">1</td>
                      <td class="whitespace-nowrap  px-6 py-4">Mark</td>
                      <td class="whitespace-nowrap  px-6 py-4">Otto</td>
                      <td class="whitespace-nowrap  px-6 py-4">@mdo</td>
                    </tr>
                    <tr class="border-b border-neutral-600 dark:border-white/10">
                      <td class="whitespace-nowrap  px-6 py-4 font-medium">2</td>
                      <td class="whitespace-nowrap  px-6 py-4 ">Jacob</td>
                      <td class="whitespace-nowrap  px-6 py-4">Thornton</td>
                      <td class="whitespace-nowrap  px-6 py-4">@fat</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
    `;


function ProfilePage(user) {
    return `<div class="p-2 md:p-4">
    <div class="w-full px-6 pb-8 mt-8 sm:max-w-xl sm:rounded-lg">
        <h2 class="pl-6 text-2xl font-bold sm:text-xl">Public Profile</h2>
    
        <div class="grid max-w-2xl mx-auto mt-8">
            <div class="flex flex-col items-center space-y-5 sm:flex-row sm:space-y-0">
    
                <img class="object-cover w-40 h-40 p-1 rounded-full ring-2 ring-indigo-300 dark:ring-indigo-500"
                    src="${user.profile_picture}&amp;ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&amp;auto=format&amp;fit=crop&amp;w=1480&amp;q=80"
                    alt="Bordered avatar">
    
                <div class="flex flex-col space-y-5 sm:ml-8">
                    <button type="button"
                        class="py-3.5 px-7 text-base font-medium text-indigo-100 focus:outline-none bg-[#202142] rounded-lg border border-indigo-200 hover:bg-indigo-900 focus:z-10 focus:ring-4 focus:ring-indigo-200 ">
                        Change picture
                    </button>
                    <button type="button"
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
                            placeholder="Your first name" value="${user.first_name}" required>
                    </div>
    
                    <div class="w-full">
                        <label for="last_name"
                            class="block mb-2 text-sm font-medium text-indigo-900 dark:text-white">Your
                            last name</label>
                        <input type="text" id="last_name"
                            class="bg-indigo-50 border border-indigo-300 text-indigo-900 text-sm rounded-lg focus:ring-indigo-500 focus:border-indigo-500 block w-full p-2.5 "
                            placeholder="Your last name" value="${user.last_name}" required>
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
        const pageContent = ProfilePage(data.user);
        appendToDiv(pageContent)
    })
}

function appendToDiv(content) {
    // document.getElementById('dynamicMain').innerHTML = content;
    $('#dynamicMain').empty()
    $('#dynamicMain').append(content)
}

// Add event listener to the 'payment' button after DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // console.log("DOM Loaded");
    let historicButton = document.getElementById('historic');
    let historicMenu = document.getElementById('historic_menu');
    let profileButton = document.getElementById('Profile');
    let profileMenu = document.getElementById('Profile_menu');
    let helpButton = document.getElementById('Help');
    let helpMenu = document.getElementById('help_menu');
    let proButton = document.getElementById('Pro');
    let proMenu = document.getElementById('pro_menu');
    
    
    builtProfileInfoPage();


    // console.log(paymentButton);
    historicButton.addEventListener('click', function(event) {
    //   console.log("Button clicked");
        changeMainContent(historicPage); // Call the function to change the content
    });
    historicMenu.addEventListener('click', function(event) {
        // console.log("Button clicked");
        changeMainContent(historicPage); // Call the function to change the content
      });

    // console.log("DOM Loaded");
    // console.log(profileButton);
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
