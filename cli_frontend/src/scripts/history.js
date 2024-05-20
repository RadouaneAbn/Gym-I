// javascript function needed.
document.addEventListener("DOMContentLoaded", function() {
    getHistory()
});

function getHistory() {
    fetch("http://0.0.0.0:5002/api/v1/clients/history/", {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${token}`,
        }
    })
    .then(res => res.json())
    .then(data => {
        for (let payment of data) {
            $('#history_table').append(paymentContent(payment));
        }
    })
    }

function paymentContent(payment) {
    return `
    <tr class="border-b bg-gray-50 border-neutral-500 dark:border-white/10">
    <td class="whitespace-nowrap font-semibold text-black  px-6 py-4">${payment.gym_name}</td>
    <td class="whitespace-nowrap font-semibold text-black px-6 py-4">${payment.from_date}</td>
    <td class="whitespace-nowrap font-semibold text-black px-6 py-4">${payment.to_date}</td>
    <td class="whitespace-nowrap font-semibold text-black px-6 py-4">
    <h4 style="color: ${payment.isactive ? 'green' : 'red'}">${payment.isactive ? 'Active' : 'Inactive'}</h4>
    </td>
    </tr>`;
}