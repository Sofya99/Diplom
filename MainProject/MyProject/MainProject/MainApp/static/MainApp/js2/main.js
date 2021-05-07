    let menuElem = document.getElementById('.center');
    let titleElem = menuElem.querySelector('.test');

    titleElem.onclick = function() {menuElem.classList.toggle('open')};
