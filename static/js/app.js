$('.welcomeCarusel').slick({
    dots: true,
    infinite: true,
    speed: 300,
    slidesToShow: 1,
    infinite: true,
    adaptiveHeight: true,
    arrows: false,
});
$('.categories').slick({
    infinite: true,
    speed: 3000,
    arrows: false,
    slidesToShow: 4,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 0,
    dots: false,
    responsive: [
        {
        breakpoint: 768,
        settings: {
            arrows: false,
            centerMode: true,
            centerPadding: '40px',
            slidesToShow: 3
            }
        },
        {
        breakpoint: 480,
        settings: {
            arrows: false,
            centerMode: true,
            centerPadding: '40px',
            slidesToShow: 1
            }
        }
    ]
});
$('.brandsBlock').slick({
    infinite: true,
    speed: 3000,
    arrows: false,
    slidesToShow: 4,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 0,
    dots: false,
    responsive: [
        {
        breakpoint: 768,
        settings: {
            arrows: false,
            centerMode: true,
            centerPadding: '40px',
            slidesToShow: 3
            }
        },
        {
        breakpoint: 480,
        settings: {
            arrows: false,
            centerMode: true,
            centerPadding: '40px',
            slidesToShow: 1
            }
        }
    ]
});
// gece gunduz
function toggleTheme() {
    const body = document.body;
    const themeCheckbox = document.querySelector('.theme-switch__checkbox');
    if (themeCheckbox.checked) {
        body.classList.add('body-dark'); // Qaranlıq rejimi aktivləşdir
        localStorage.setItem('theme', 'dark');
    } else {
        body.classList.remove('body-dark'); // Qaranlıq rejimi deaktivləşdir
        localStorage.setItem('theme', 'light');
    }
}
function loadTheme() {
    const body = document.body;
    const themeCheckbox = document.querySelector('.theme-switch__checkbox');
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        body.classList.add('body-dark');
        themeCheckbox.checked = true;
    } else {
        body.classList.remove('body-dark');
        themeCheckbox.checked = false;
    }
}
document.addEventListener('DOMContentLoaded', () => {
    loadTheme(); // Tema rejimini yüklə
    const themeCheckbox = document.querySelector('.theme-switch__checkbox');
    themeCheckbox.addEventListener('change', toggleTheme); // Tema dəyişikliklərini dinləyir
});