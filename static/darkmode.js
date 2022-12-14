let darkMode = localStorage.getItem('darkMode')
let darkModeToggle = document.getElementById('dark-mode-toggle')

let enableDarkMode = () => {
    // add class of dark-mode to our file
    document.body.classList.add('dark-mode')
    // change darkMode in local to enabled
    localStorage.setItem('darkMode', 'enabled')
    // change icon of darkMode toggle to sun
    darkModeToggle.classList.remove('fa-moon')
    darkModeToggle.classList.add('fa-sun')
    document.getElementById('hover-dark-mode').innerText = 'Lightmode'
}

let disableDarkMode = () => {
    // remove class of dark-mode from our file
    document.body.classList.remove('dark-mode')
    // change dark-mode in local to disabled
    localStorage.setItem('darkMode', 'disabled')
    // change icon of darkMode toggle to moon
    darkModeToggle.classList.remove('fa-sun')
    darkModeToggle.classList.add('fa-moon')
    document.getElementById('hover-dark-mode').innerText = 'Darkmode'
}

// check what is value of darkMode in our local when load the page

if (darkMode === 'enabled') {
    enableDarkMode()
}

darkModeToggle.addEventListener('click', () => {
    // get current value of darkMode
    darkMode = localStorage.getItem('darkMode')
    if (darkMode === 'enabled') {
        disableDarkMode()
    } else {
        enableDarkMode()
    }
})