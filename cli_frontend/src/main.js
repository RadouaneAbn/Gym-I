const amenityIds = []
const cityIds = []

document.addEventListener("DOMContentLoaded", function() {
  const decrementButtons = document.querySelectorAll("[data-hs-input-number-decrement]");
  const incrementButtons = document.querySelectorAll("[data-hs-input-number-increment]");
  // const inputFields = document.querySelectorAll("[data-hs-input-number-input]");
  // const buttons = document.querySelectorAll('.btn-gym_id');
  const filterBtn = document.getElementById('filter_btn');
  const cityBtns = document.querySelectorAll('.city_btn');
  const amenityBtns = document.querySelectorAll('.amenity_btn');
  const prevPage = document.getElementById('prev_holder');
  const nextPage = document.getElementById('next_holder');
  const curPage = document.getElementById('cur_holder');
  const nextBtn = document.getElementById('next_btn')
  const prevBtn = document.getElementById('prev_btn')

  prevPage.addEventListener('click', goPrevPage)
  prevBtn.addEventListener('click', goPrevPage)

  nextPage.addEventListener('click', goNextPage)
  nextBtn.addEventListener('click', goNextPage)

  function goNextPage() {
    const pageNumber = parseInt(nextPage.outerText, 10)
    fetchData(pageNumber);
    if (nextBtn.dataset.count === nextPage.outerText) {
      // console.log('hide');
      $('.next_vis').css('visibility', 'hidden');
    }
    if (curPage.outerText === "1") {
      // console.log('unhide');
      $('.prev_vis').css('visibility', 'visible');
    }
    prevPage.querySelector('span').textContent = curPage.outerText;
    curPage.querySelector('span').textContent = nextPage.outerText;
    nextPage.querySelector('span').textContent = pageNumber + 1
    // console.log(pageNumber)
  }

  function goPrevPage() {
    const pageNumber = parseInt(prevPage.outerText, 10)
    fetchData(pageNumber);
    if (pageNumber === 1) {
      $('.prev_vis').css('visibility', 'hidden');
    }
    if (curPage.outerText === nextBtn.dataset.count) {
      $('.next_vis').css('visibility', 'visible');
    }
    nextPage.querySelector('span').textContent = curPage.outerText;
    curPage.querySelector('span').textContent = prevPage.outerText;
    prevPage.querySelector('span').textContent = pageNumber - 1;
    // console.log(pageNumber)
  }

  filterBtn.addEventListener('click', () => {
    fetchData(1)
    .then(() => {
      // console.log(nextBtn.dataset.count);
      if (nextBtn.dataset.count === '1') {
        $('.next_vis').css('visibility', 'hidden');
      } else {
        $('.next_vis').css('visibility', 'visible');
      }
    });
  });

  cityBtns.forEach(btn => {
    btn.addEventListener('click', function () {
      // console.log(btn.id)
      const bx = btn.querySelector('input[type="checkbox"]')
      
      if (bx.checked) {
        // console.log('check')
        cityIds.push(btn.id);
      } else {
        // console.log('uncheck')
        const idx = cityIds.indexOf(btn.id);
        if (idx !== -1) {
          cityIds.splice(idx, 1)
        }
      }
    })
  })

  amenityBtns.forEach(btn => {
    btn.addEventListener('click', function () {
      // console.log(btn.id)
      const bx = btn.querySelector('input[type="checkbox"]')
      
      if (bx.checked) {
        // console.log('check')
        amenityIds.push(btn.id);
      } else {
        // console.log('uncheck')
        const idx = amenityIds.indexOf(btn.id);
        if (idx !== -1) {
          amenityIds.splice(idx, 1)
        }
      }
    })
  })


  // buttons.forEach(btn => {
  //   btn.addEventListener('click', function() {
  //     const urlItem = '/user/gymes/' + btn.id;
  //     window.location.href = urlItem
  //   })
  // })
  
  $(document).on('click', 'button.btn-gym_id', function () {
    window.location.href = '/user/gymes/' + $(this).attr('id')
  })
// decrement price filter
  decrementButtons.forEach(button => {
    button.addEventListener("click", function() {
      const input = this.parentElement.querySelector("[data-hs-input-number-input]");
      let value = parseInt(input.value);
      if (!isNaN(value) && value > 20) {
        input.value = value - 1;
      } else {
        input.value = 20; // Set to 20 if value is already 20 or NaN
      }
    });
  });
// increment the price filter
  incrementButtons.forEach(button => {
    button.addEventListener("click", function() {
      const input = this.parentElement.querySelector("[data-hs-input-number-input]");
      let value = parseInt(input.value);
      if (!isNaN(value) && value < 150) {
        input.value = value + 1;
      } else {
        input.value = 150; // Set to 150 if value is NaN
      }
    });
  });
});

function appendGym(gym) {
  const block = `
  <div class="relative flex w-full max-w-[26rem] flex-col rounded-xl bg-white bg-clip-border text-gray-700 shadow-lg">
          <div
            class="relative mx-4 mt-4 h-44 overflow-hidden text-white shadow-lg rounded-xl bg-blue-gray-500 bg-clip-border shadow-blue-gray-500/40">
            <img
              class="h-[100%] w-full"
              src="${gym.profile_picture}"
              alt="ui/ux review check" />
            <div
              class="absolute inset-0 w-full h-full to-bg-black-10 bg-gradient-to-tr from-transparent via-transparent to-black/60">
            </div>
            <button
              class="!absolute  top-4 right-4 h-8 max-h-[32px] w-8 max-w-[32px] select-none rounded-full text-center align-middle font-sans text-xs font-medium uppercase text-red-500 transition-all hover:bg-red-500/10 active:bg-red-500/30 disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
              type="button">
              <span class="absolute transform -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-6 h-6">
                  <path
                    d="M11.645 20.91l-.007-.003-.022-.012a15.247 15.247 0 01-.383-.218 25.18 25.18 0 01-4.244-3.17C4.688 15.36 2.25 12.174 2.25 8.25 2.25 5.322 4.714 3 7.688 3A5.5 5.5 0 0112 5.052 5.5 5.5 0 0116.313 3c2.973 0 5.437 2.322 5.437 5.25 0 3.925-2.438 7.111-4.739 9.256a25.175 25.175 0 01-4.244 3.17 15.247 15.247 0 01-.383.219l-.022.012-.007.004-.003.001a.752.752 0 01-.704 0l-.003-.001z">
                  </path>
                </svg>
              </span>
            </button>
          </div>
          <div class="p-6">
            <div class="flex items-center justify-between mb-3">
              <div>
              <h5 class="block h-14 overflow-hidden font-sans text-xl antialiased font-medium leading-snug tracking-normal text-blue-gray-900">
                ${gym.name}
              </h5>
              <p class="w-10 flex items-center justify-center font-semibold text-red-600 ">${gym.price_by_month}$</p>
            </div>
              <p
                class="flex items-center gap-1.5 font-sans text-base font-normal leading-relaxed text-blue-gray-900 antialiased">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"
                  class="-mt-0.5 h-5 w-5 text-yellow-700">
                  <path fill-rule="evenodd"
                    d="M10.788 3.21c.448-1.077 1.976-1.077 2.424 0l2.082 5.007 5.404.433c1.164.093 1.636 1.545.749 2.305l-4.117 3.527 1.257 5.273c.271 1.136-.964 2.033-1.96 1.425L12 18.354 7.373 21.18c-.996.608-2.231-.29-1.96-1.425l1.257-5.273-4.117-3.527c-.887-.76-.415-2.212.749-2.305l5.404-.433 2.082-5.006z"
                    clip-rule="evenodd"></path>
                </svg>
                5.0
              </p>
            </div>
            <p class="text-gray-700">City: ${gym.city_name}<p class="text-base h-8 text-blue-950"></p></p>
            <p class="block h-14 font-sans text-xs antialiased font-light leading-relaxed text-gray-700 overflow-hidden">
              ${gym.description}
            </p>
          </div>
          <div class="p-6 pt-3">
            <button id="${gym.id}"
              class="btn-gym_id block w-full overflow-hidden select-none rounded-lg bg-gray-900 py-3.5 px-7 text-center align-middle font-sans text-sm font-bold uppercase text-white shadow-md shadow-gray-900/10 transition-all hover:shadow-lg hover:shadow-gray-900/20 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
              type="button">
              Reserve
            </button>
          </div>
        </div> 
  `;

  $('div#gym_container').append(block)

  // data.forEach(gym => {
  //   $('div#gym_container').append(block)
  // })
}

async function filter(page) {
  const response = await fetch('http://0.0.0.0:5002/gym_filter/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      "amenity_ids": amenityIds,
      "city_ids": cityIds,
      "page": page
    })
  });

  const newData = await response.json()
  return newData;
}

async function fetchData (page) {
  const newData = await filter(page);
  // console.log(newData)
  const count = Object.keys(newData)[0]
  const gymes = Object.values(newData)[0]

  $('#next_btn').attr('data-count', String(count))

  $('div#gym_container').empty()
  for (gym of gymes) {
    appendGym(gym);
  }
}

async function pageCount() {
  const response = await fetch('http://0.0.0.0:5002/gym_filter/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      "amenity_ids": amenityIds,
      "city_ids": cityIds,
      "page": page
    })
  });
}