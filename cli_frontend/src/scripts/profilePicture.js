document.addEventListener('DOMContentLoaded', async function () {
  const profilePicture = document.getElementById('profile_picture');

  fetch('http://0.0.0.0:5002/api/v1/users/', {
    method: 'GET',
    headers: {
      Authorization: `Bearer ${token}`
    }
  })
    .then(res => res.json())
    .then(data => {
      const profilePic = data.profile_pic;
      profilePicture.src = profilePic;
    });
});
