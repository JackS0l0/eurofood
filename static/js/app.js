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
    const themeCheckboxes = document.querySelectorAll('.theme-switch__checkbox');
    const isChecked = this.checked;
    themeCheckboxes.forEach(checkbox => {
        checkbox.checked = isChecked;
    });
    if (isChecked) {
        body.classList.add('body-dark');
        localStorage.setItem('theme', 'dark');
    } else {
        body.classList.remove('body-dark');
        localStorage.setItem('theme', 'light');
    }
}
function loadTheme() {
    const body = document.body;
    const themeCheckboxes = document.querySelectorAll('.theme-switch__checkbox');
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        body.classList.add('body-dark');
        themeCheckboxes.forEach(checkbox => checkbox.checked = true);
    } else {
        body.classList.remove('body-dark');
        themeCheckboxes.forEach(checkbox => checkbox.checked = false);
    }
}
document.addEventListener('DOMContentLoaded', () => {
    loadTheme();
    const themeCheckboxes = document.querySelectorAll('.theme-switch__checkbox');
    themeCheckboxes.forEach(checkbox => {
        checkbox.addEventListener('change', toggleTheme);
    });
});