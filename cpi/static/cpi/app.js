const navSlide = () => {
	const burger = document.querySelector('.burger');
	const nav = document.querySelector('.menu-dropdown');
	const navLinks = document.querySelectorAll('.nav-links li')

	burger.addEventListener('click', () => {
		nav.classList.toggle('menu-dropdown-active');
	});

	navLinks.forEach((link, index) => {
		link.style.animation = 'navLinkFade 0.5s ease forwards ${ index / 7 }s'
	});
}

navSlide();