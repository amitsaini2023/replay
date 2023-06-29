let home_search=document.querySelector('.home_search')
let contribution=document.querySelector('#top_two')

// Get the current URL
var currentURL = window.location.href;

document.addEventListener('DOMContentLoaded', function() {
    var slides = document.querySelectorAll('.slide');
    var currentSlide = 0;
    var slideInterval = setInterval(nextSlide, 2500);

    slides[currentSlide].classList.add('active'); // Add active class to the first slide initially

    function nextSlide() {
    var previousSlide = currentSlide;
    currentSlide = (currentSlide + 1) % slides.length;

    slides[currentSlide].classList.add('active');
    slides[previousSlide].classList.remove('active');
    slides[previousSlide].style.animation = 'fade-out 0.35s ease-in-out forwards';
    slides[currentSlide].style.animation = 'slide-in 0.35s ease-in-out forwards';
    }


    let contribution = document.querySelector('#top_two');

    // Rest of the code for event listeners and redirection

    contribution.addEventListener('click', function() {
      
        // Redirect to the current search URL
        window.location.href = currentURL + "contribution";
    });
});


// Replace the path with '/search'
var searchUrl = currentURL.replace(/\/[^\/]*$/, '/search');


home_search.addEventListener('click',()=>{
    // Redirect to the current search URL
    window.location.href = searchUrl;
})



