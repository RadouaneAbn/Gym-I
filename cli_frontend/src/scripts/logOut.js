document.addEventListener('DOMContentLoaded', async function () {
  const logOutBtn = document.getElementById('logout-btn');

  logOutBtn.onclick = function () {
    localStorage.removeItem('access_token');
    window.location.href = '/signin';
  };
});
