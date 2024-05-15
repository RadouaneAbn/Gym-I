const token = localStorage.getItem('access_token');

document.addEventListener("DOMContentLoaded", function () {
if (token) {
    fetch('http://0.0.0.0:5002/token_check', {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${token}`,
        }
    })
    .then(data => {
        if (data.ok) {
            window.location.href = '/user/gymes';
        } else {
            localStorage.removeItem('access_token');
            $('body').css('display', 'block');
        }
    })
} else {
    localStorage.removeItem('access_token');
    $('body').css('display', 'block');
    }})