console.log('inside home js')


document.addEventListener("DOMContentLoaded", function () {
    const carouselItems = document.querySelectorAll(".carousel-item");
    let currentIndex = 0;
    let autoScrollInterval;
    const intervalTime = 10000; // Show time for each slide (10 seconds)

    // Show a specific slide by index
    function showSlide(index) {
        carouselItems.forEach((item, i) => {
            // Display the targeted slide with opacity and ensure it moves vertically with smooth transition
            if (i === index) {
                item.classList.add("opacity-100");
                item.classList.remove("opacity-0");
                item.style.transform = "translateY(0)";
            } else {
                item.classList.remove("opacity-100");
                item.classList.add("opacity-0");
                item.style.transform = "translateY(100%)";  // Move the non-active slides out of view
            }
        });
    }

    // Auto-scroll function
    function autoScroll() {
        autoScrollInterval = setInterval(nextSlide, intervalTime);
    }

    // Go to the next slide automatically
    function nextSlide() {
        currentIndex = (currentIndex < carouselItems.length - 1) ? currentIndex + 1 : 0;
        showSlide(currentIndex);
        resetAutoScroll();
    }

    // Reset auto-scroll when manually navigating
    function resetAutoScroll() {
        clearInterval(autoScrollInterval);
        autoScroll();
    }

    // Show the initial slide and start auto-scroll
    showSlide(currentIndex);
    autoScroll();
});

// document.addEventListener("DOMContentLoaded", function () {
//     const carouselItems = document.querySelectorAll(".carousel-item");
//     let currentIndex = 0;
//     let autoScrollInterval;
  
//     // Function to show a specific slide
//     function showSlide(index) {
//       // Hide all slides except the one with the given index
//       carouselItems.forEach((item, i) => {
//         item.style.opacity = i === index ? "1" : "0";
//       });
//     }
  
//     // Move to the previous slide
//     function prevSlide() {
//       currentIndex = (currentIndex > 0) ? currentIndex - 1 : carouselItems.length - 1;
//       showSlide(currentIndex);
//       resetAutoScroll();  // Reset the auto-scroll timer
//     }
  
//     // Move to the next slide
//     function nextSlide() {
//       currentIndex = (currentIndex < carouselItems.length - 1) ? currentIndex + 1 : 0;
//       showSlide(currentIndex);
//       resetAutoScroll();  // Reset the auto-scroll timer
//     }
  
//     // Auto-scroll function
//     function autoScroll() {
//       autoScrollInterval = setInterval(function () {
//         nextSlide();
//       }, 10000); // 5 seconds interval
//     }
  
//     // Reset auto-scroll timer whenever user manually interacts
//     function resetAutoScroll() {
//       clearInterval(autoScrollInterval); // Clear the existing interval
//       autoScroll(); // Restart the auto-scroll
//     }
  
//     // Event listeners for manual navigation
//     document.querySelector("[data-carousel-prev]").addEventListener("click", prevSlide);
//     document.querySelector("[data-carousel-next]").addEventListener("click", nextSlide);
  
//     // Initially show the first slide and start auto-scroll
//     showSlide(currentIndex);
//     autoScroll();
//   });


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
