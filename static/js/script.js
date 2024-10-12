console.log('inside scripts.js')

// All department name show

document.getElementById("toggle-departments").addEventListener("click", function () {
    var departmentList = document.getElementById("departments-list");
    var chevronIcon = document.getElementById("chevron-icon");

    // Toggle the 'hidden' class to show or hide the list
    departmentList.classList.toggle("hidden");

    // Switch between 'fa-chevron-down' and 'fa-chevron-up'
    if (chevronIcon.classList.contains("fa-chevron-down")) {
        chevronIcon.classList.remove("fa-chevron-down");
        chevronIcon.classList.add("fa-chevron-up");
    } else {
        chevronIcon.classList.remove("fa-chevron-up");
        chevronIcon.classList.add("fa-chevron-down");
    }
});


// Search functionality

document.addEventListener("DOMContentLoaded", function () {
  const searchForm = document.getElementById("search-form");
  const searchInput = document.getElementById("search-input");
  const searchButton = document.getElementById("search-button");

  searchForm.addEventListener("submit", function (e) {
    e.preventDefault();
    const query = searchInput.value.trim();
    if (query) {
      // Redirect to search page with query parameter
      window.location.href = `/search?query=${encodeURIComponent(query)}`;
    } else {
      alert("Please enter a search term");
    }
  });

  searchButton.addEventListener("click", function () {
    searchForm.submit();
  });
});


// Voice and others search functionality
console.log('Print something')

document.addEventListener("DOMContentLoaded", function () {
  const voiceSearchBtn = document.getElementById('voice-search-btn');
  const searchQueryInput = document.getElementById('search-query');
  const searchForm = searchQueryInput.closest('form');  // Get the form element
  const voiceSearchPopup = document.getElementById('voice-search-popup');  // Get the popup element

  // Check if the browser supports speech recognition
  if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    const recognition = new SpeechRecognition();
    recognition.continuous = false;
    recognition.interimResults = false;
    recognition.lang = 'en-US';  // Set language

    voiceSearchBtn.addEventListener('click', function (event) {
      event.preventDefault();  // Prevent form submission when clicking mic button
      voiceSearchPopup.classList.remove('hidden');  // Show the popup
      recognition.start();  // Start listening to voice
    });

    recognition.onresult = function (event) {
      let speechResult = event.results[0][0].transcript;  // Get the recognized text
      // Capitalize the first letter
      speechResult = speechResult.charAt(0).toUpperCase() + speechResult.slice(1);
      searchQueryInput.value = speechResult;  // Put the result into the input field

      // Hide the popup after voice input is done
      voiceSearchPopup.classList.add('hidden');

      // Add a 2-second delay before submitting the form
      setTimeout(function() {
        searchForm.submit();  // Automatically submit the form
      }, 2000);  // 2000 milliseconds = 2 seconds
    };

    recognition.onspeechend = function () {
      recognition.stop();  // Stop recognition when speech ends
      voiceSearchPopup.classList.add('hidden');  // Hide the popup
    };

    recognition.onerror = function (event) {
      console.error('Speech recognition error: ' + event.error);
      voiceSearchPopup.classList.add('hidden');  // Hide the popup if there's an error
    };
  } else {
    console.warn('Speech recognition not supported in this browser.');
    voiceSearchBtn.disabled = true;  // Disable the mic button if not supported
  }
});