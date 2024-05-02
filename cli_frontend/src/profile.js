var payementMain = `
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
var profileMain = `<div class="p-2 md:p-4">
<div class="w-full px-6 pb-8 mt-8 sm:max-w-xl sm:rounded-lg">
    <h2 class="pl-6 text-2xl font-bold sm:text-xl">Public Profile</h2>

    <div class="grid max-w-2xl mx-auto mt-8">
        <div class="flex flex-col items-center space-y-5 sm:flex-row sm:space-y-0">

            <img class="object-cover w-40 h-40 p-1 rounded-full ring-2 ring-indigo-300 dark:ring-indigo-500"
                src="https://images.unsplash.com/photo-1633332755192-727a05c4013d?ixlib=rb-1.2.1&amp;ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&amp;auto=format&amp;fit=crop&amp;w=1480&amp;q=80"
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
                        placeholder="Your first name" value="Jane" required>
                </div>

                <div class="w-full">
                    <label for="last_name"
                        class="block mb-2 text-sm font-medium text-indigo-900 dark:text-white">Your
                        last name</label>
                    <input type="text" id="last_name"
                        class="bg-indigo-50 border border-indigo-300 text-indigo-900 text-sm rounded-lg focus:ring-indigo-500 focus:border-indigo-500 block w-full p-2.5 "
                        placeholder="Your last name" value="Ferguson" required>
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

            <div class="mb-2 sm:mb-6">
                <label for="email"
                    class="block mb-2 text-sm font-medium text-indigo-900 dark:text-white">Your
                    email</label>
                <input type="email" id="email"
                    class="bg-indigo-50 border border-indigo-300 text-indigo-900 text-sm rounded-lg focus:ring-indigo-500 focus:border-indigo-500 block w-full p-2.5 "
                    placeholder="your.email@mail.com" required>
            </div>

            <div class="mb-2 sm:mb-6">
                <label for="password"
                    class="block mb-2 text-sm font-medium text-indigo-900 dark:text-white">Password</label>
                <input type="password" id="passwor"d
                    class="bg-indigo-50 border border-indigo-300 text-indigo-900 text-sm rounded-lg focus:ring-indigo-500 focus:border-indigo-500 block w-full p-2.5 "
                    placeholder="Enter old password" required>
            </div>
            <div
                class="flex flex-col items-center w-full mb-2 space-x-0 space-y-2 sm:flex-row sm:space-x-4 sm:space-y-0 sm:mb-6">
                <div class="w-full">
                    <label for="New_password"
                        class="block mb-2 text-sm font-medium text-indigo-900 dark:text-white">Your
                        New password</label>
                    <input type="password" id="New_password"
                        class="bg-indigo-50 border border-indigo-300 text-indigo-900 text-sm rounded-lg focus:ring-indigo-500 focus:border-indigo-500 block w-full p-2.5 "
                        placeholder="Enter new password" value="" required>
                </div>

                <div class="w-full">
                    <label for="confirm_password"
                        class="block mb-2 text-sm font-medium text-indigo-900 dark:text-white">Your
                        Confirme New Password</label>
                    <input type="password" id="confirm_password"
                        class="bg-indigo-50 border border-indigo-300 text-indigo-900 text-sm rounded-lg focus:ring-indigo-500 focus:border-indigo-500 block w-full p-2.5 "
                        placeholder="Confirm your password" value="" required>
                </div>

            </div>
            
            <div class="flex justify-end">
                <button type="submit"
                    class="text-white bg-indigo-700  hover:bg-indigo-800 focus:ring-4 focus:outline-none focus:ring-indigo-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-indigo-600 dark:hover:bg-indigo-700 dark:focus:ring-indigo-800">Save</button>
            </div>

        </div>
    </div>
</div>
</div>`;
var helpMain = ``;
var proMain = ``;
function changeMainContent(Content) {
    console.log("Changing main content...");
    var newContent = Content;
    document.getElementById('dynamicMain').innerHTML = newContent;
  }
  
  // Add event listener to the 'payment' button after DOM is loaded
  document.addEventListener('DOMContentLoaded', function() {
    console.log("DOM Loaded");
    var paymentButton = document.getElementById('payment');
    var paymentMenu = document.getElementById('payment_menu');
    console.log(paymentButton);
    paymentButton.addEventListener('click', function(event) {
      console.log("Button clicked");
      changeMainContent(payementMain); // Call the function to change the content
    });
    paymentMenu.addEventListener('click', function(event) {
        console.log("Button clicked");
        changeMainContent(payementMain); // Call the function to change the content
      });

  });

  document.addEventListener('DOMContentLoaded', function() {
    console.log("DOM Loaded");
    var profileButton = document.getElementById('Profile');
    var profileMenu = document.getElementById('Profile_menu');
    console.log(profileButton);
    profileButton.addEventListener('click', function(event) {
      console.log("Button clicked");
      changeMainContent(profileMain); // Call the function to change the content
    });
    profileMenu.addEventListener('click', function(event) {
        console.log("Button clicked");
        changeMainContent(profileMain); // Call the function to change the content
      });
  });

  document.addEventListener('DOMContentLoaded', function() {
    console.log("DOM Loaded");
    var helpButton = document.getElementById('Help');
    var helpMenu = document.getElementById('help_menu');
    console.log(helpButton);
    helpButton.addEventListener('click', function(event) {
      console.log("Button clicked");
      changeMainContent(helpMain); // Call the function to change the content
    });
    helpMenu.addEventListener('click', function(event) {
        console.log("Button clicked");
        changeMainContent(helpMain); // Call the function to change the content
      });
  });

  document.addEventListener('DOMContentLoaded', function() {
    console.log("DOM Loaded");
    var proButton = document.getElementById('Pro');
    var proMenu = document.getElementById('pro_menu');
    console.log(proButton);
    proButton.addEventListener('click', function(event) {
      console.log("Button clicked");
      changeMainContent(proMain); // Call the function to change the content
    });
    proMenu.addEventListener('click', function(event) {
        console.log("Button clicked");
        changeMainContent(proMain); // Call the function to change the content
      });
  });