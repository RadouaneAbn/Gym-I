// document.addEventListener("DOMContentLoaded", async function(){
//     document.getElementById("clientId").value = clientId;
//     console.log(clientId)
// })
// Set the value of the duration input field
document.addEventListener("DOMContentLoaded", function() {
    const clientId = document.getElementById('clientId');
    
    fetch('http://0.0.0.0:5002/users/', {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${token}`,
      }
    })
    .then(res => res.json())
    .then(data => {
      user = data.user_info.id;
      console.log(user)
      document.getElementById("clientId").value = user;
    })
})