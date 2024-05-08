document.addEventListener("DOMContentLoaded", async function() {
    const profilePicture = document.getElementById('profile_picture');

    getUserInfo(profilePicture);
})

function getUserInfo(profilePicture) {

    fetch('http://0.0.0.0:5002/users/', {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${token}`,
      }
    })
    .then(res => res.json())
    .then(data => {
      user = data.user_info;
      profilePicture.src = user.profile_picture;
      profilePicture.display = true;
    })
  }