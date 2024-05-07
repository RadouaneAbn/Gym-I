const token = localStorage.getItem('access_token');
if (!token) {
    window.location.href = '/signin';
} else {
    fetch('http://0.0.0.0:5002/token_check', {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${token}`,
        }
    })
    .then(data => {
        // console.log(data.status) // 200
        if (data.status === 401) {
            window.location.href = '/signin';
        }
    })
}
