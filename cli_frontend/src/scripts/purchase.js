document.addEventListener("DOMContentLoaded",  function() {
    const purchaseBtn = document.getElementById('purchase');
    const purchaseDate = document.getElementById('purchase-date');
    const purchaseMonthNumber = document.getElementById('month-number');
    const gymId = $('main.container').attr('id');

    purchaseBtn.addEventListener('click', () => { enrole(purchaseDate.value, purchaseMonthNumber.value, gymId, token) })
})

// async function enrole (date, n, gymId, token) {
//     // console.log(n.value)
//     const form = FormData();
//     form.a

// }

// async function enrole (date, n, gymId, token) {
//     const response = await fetch('http://0.0.0.0:5002/client/gyms/enrol', {
//         method: 'POST',
//         headers: {
//             'Authorization': `Bearer ${token}`,
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify({
//             'gym_id': gymId,
//             'date': date,
//             'months': n
//         })
//     })
//     const result = await response.json();
//     console.log(result)

// }