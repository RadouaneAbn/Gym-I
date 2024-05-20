function gymItem (gym) {
  return `
    <div class="search_item" id="${gym.id}">
              <div class="relative flex items-start py-1 px-3 dark:hover:bg-neutral-700 ">
                  <label for="hs-dropdown-item-checkbox-delete-cities" class="ms-3.5">
                    <span class="mx-2 block text-sm text-left font-medium text-white">${gym.name}</span>
                  </label>

                  <svg
              class="mx-2 absolute left-0 top-1/2 -translate-y-1/2"
              xmlns="http://www.w3.org/2000/svg"
              width="20"
              height="20"
              viewBox="0 0 24 24"
              stroke-width="1"
              stroke="white"
              fill="none"
              stroke-linecap="round"
              stroke-linejoin="round"
            >
              <path stroke="none" d="M0 0h24v24H0z" fill="none" />
              <path d="M10 10m-7 0a7 7 0 1 0 14 0a7 7 0 1 0 -14 0" />
              <path d="M21 21l-6 -6" />
            </svg>

                </div>
              </div>
    `;
}

function debounce (callback, delay = 1000) {
  let timeout;

  return (...args) => {
    clearTimeout(timeout);
    timeout = setTimeout(() => {
      callback(...args);
    }, delay);
  };
}

let searchContainer;
let searchBar;
let searchText = '';

document.addEventListener('DOMContentLoaded', function () {
  searchContainer = $('div#search_container');
  searchBar = $('input#search_bar');

  searchBar.on('keydown', function (event) {
    if (event.keyCode === 13) {
      // console.log(searchText);
      searchContainer.css('visibility', 'hidden');
      scrollUp();
      loadPage(1)
        .then(() => {
          // console.log(nextBtn.dataset.count);
          if (nextBtn.dataset.count === '1') {
            $('.next_vis').css('visibility', 'hidden');
            $('.prev_vis').css('visibility', 'hidden');
            curPage.querySelector('span').textContent = '1';
          } else {
            $('.next_vis').css('visibility', 'visible');
          }
        });
    }
  });

  const delayedFetchData = debounce(fetchData, 250);

  searchBar.on('blur', function () {
    setTimeout(function () {
      searchContainer.css('visibility', 'hidden');
    }, 200);
  });

  searchBar.on('focus', function () {
    if (searchBar.val()) {
      searchContainer.css('visibility', 'visible');
    }
  });

  searchBar.on('input', function () {
    searchText = searchBar.val();
    if (!searchText) {
      searchContainer.empty();
      searchContainer.css('visibility', 'hidden');
    } else {
      delayedFetchData(searchText);
      choiceGym();
    }
  });
});

function choiceGym () {
  $('body').on('click', 'div.search_item', function () {
    window.location.href = '/user/gymes/' + $(this).attr('id');
  });
}

// style="visibility: hidden;
async function fetchData (name) {
  let searchResult = '';
  const response = await fetch('http://0.0.0.0:5002/api/v1/gym_search/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      name
    })
  });
  const result = await response.json();
  for (gym of result) {
    searchResult += gymItem(gym);
  }
  if (searchResult) {
    searchContainer.empty();
    searchContainer.css('visibility', 'visible');
    searchContainer.append(searchResult);
  }
}
