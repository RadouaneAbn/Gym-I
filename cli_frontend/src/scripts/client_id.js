document.addEventListener("DOMContentLoaded", function() {
    fetch('http://0.0.0.0:5002/token_check/', {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${token}`,
      }
    })
    .then(res => res.json())
    .then(data => {
      const user = data.user.id;
      // console.log(user)
      document.getElementById("clientId").value = user;
    })
})