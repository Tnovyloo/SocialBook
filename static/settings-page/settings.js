// CALCULATING LENGTH OF SUBTITLES IN SETTINGS CONTENT TO SET WIDTH OF THEM

let submitButton = document.getElementsByClassName('submit-button')

// for basic info

let basicInfoToChange = document.getElementsByClassName('info-to-change-basic')
let elementLength = []

for (let i = 0; i < basicInfoToChange.length; i++) {
    elementLength.push(basicInfoToChange[i].offsetWidth)
}

for (let i = 0; i < basicInfoToChange.length; i++) {
    basicInfoToChange[i].style.width = `${Math.max(...elementLength) + 15}px`
}

submitButton[0].style.marginLeft = `${Math.max(...elementLength) + 20}px`

// for places info

let placeInfoToChange = document.getElementsByClassName('info-to-change-places')
elementLength = []

for (let i = 0; i < placeInfoToChange.length; i++) {
    elementLength.push(placeInfoToChange[i].offsetWidth)
}

for (let i = 0 ; i < placeInfoToChange.length; i++) {
    placeInfoToChange[i].style.width = `${Math.max(...elementLength) + 15}px`
}

submitButton[1].style.marginLeft = `${Math.max(...elementLength) + 20}px`

// for education / hobby info

let eduHobbyInfoToChange = document.getElementsByClassName('info-to-change-hobby-education')
elementLength = []

for (let i = 0; i < eduHobbyInfoToChange.length; i++) {
    elementLength.push(eduHobbyInfoToChange[i].offsetWidth)
}

for (let i = 0 ; i < eduHobbyInfoToChange.length; i++) {
    eduHobbyInfoToChange[i].style.width = `${Math.max(...elementLength) + 15}px`
}

submitButton[2].style.marginLeft = `${Math.max(...elementLength) + 20}px`

// for contact info

let contactInfoToChange = document.getElementsByClassName('info-to-change-contact')
elementLength = []

for (let i = 0; i < contactInfoToChange.length; i++) {
    elementLength.push(contactInfoToChange[i].offsetWidth)
}

for (let i = 0 ; i < contactInfoToChange.length; i++) {
    contactInfoToChange[i].style.width = `${Math.max(...elementLength) + 15}px`
}

submitButton[3].style.marginLeft = `${Math.max(...elementLength) + 20}px`

// for close people info

let peopleInfoToChange = document.getElementsByClassName('info-to-change-people')
elementLength = []

for (let i = 0; i < peopleInfoToChange.length; i++) {
    elementLength.push(peopleInfoToChange[i].offsetWidth)
}

for (let i = 0 ; i < peopleInfoToChange.length; i++) {
    peopleInfoToChange[i].style.width = `${Math.max(...elementLength) + 15}px`
}

submitButton[4].style.marginLeft = `${Math.max(...elementLength) + 20}px`

// for change password

let changePasswordInfo = document.getElementsByClassName('change-password-info')
elementLength = []

for (let i = 0; i < changePasswordInfo.length; i++) {
    elementLength.push(changePasswordInfo[i].offsetWidth)
}

for (let i = 0 ; i < changePasswordInfo.length; i++) {
    changePasswordInfo[i].style.width = `${Math.max(...elementLength) + 15}px`
}

submitButton[5].style.marginLeft = `${Math.max(...elementLength) + 20}px`

// DISPLAYING DIFFERENT PARTS OF PAGE AT ONE TIME

let basicInfo = document.getElementById('basic-info')
let places = document.getElementById('live-places')
let hobbyEducation = document.getElementById('hobby-education')
let contact = document.getElementById('contact')
let closePeople = document.getElementById('close-people')
let changePassword = document.getElementById('change-password')
let forms = document.getElementsByClassName('forms')
let activateForm = document.getElementsByClassName('activate-form')

basicInfo.style.display = 'block'
places.style.display = 'none'
hobbyEducation.style.display = 'none'
contact.style.display = 'none'
closePeople.style.display = 'none'
changePassword.style.display = 'none'
activateForm[0].style.borderLeft = '2px solid var(--border-clr)'
activateForm[0].style.fontWeight = 'bold'

for (let i = 0 ; i < forms.length; i++) {
    activateForm[i].addEventListener('click', () => {
        for (let j = 0; j < forms.length; j++) {
            forms[j].style.display = 'none'
            activateForm[j].style.borderLeft = 'none'
            activateForm[j].style.fontWeight = '400'
        }
        forms[i].style.display = 'block'
        activateForm[i].style.borderLeft = '2px solid var(--border-clr)'
        activateForm[i].style.fontWeight = 'bold'
    })
}

// COUNT NUMBER OF NOTIFICATIONS

let numOfNotifications = 0

let notificationNumber = document.getElementsByClassName('info-content')

for (let i = 0; i < notificationNumber.length; i++) {
    notificationNumber[i].style.fontWeight = 'bold'
}

for(let i = 0; i < notificationNumber.length; i++) {
    if (notificationNumber[i].style.fontWeight === 'bold') {
        numOfNotifications += 1 
    }
}

document.getElementById('notification-icon').innerText = numOfNotifications

// NOTIFICATIONS WINDOW

const notificationWindow = document.getElementById('info')
const notificationSign = document.getElementById('notification-open') 
const infoTexts = document.getElementsByClassName('info-text')
const infoContent = document.getElementsByClassName('info-content')
const circlesNotification = document.getElementsByClassName('circle-notification')
const confirmFriend = document.getElementsByClassName('confirm')
const removeFriend = document.getElementsByClassName('remove')
const acceptGroup = document.getElementsByClassName('accept')
const declineGroup = document.getElementsByClassName('decline')

// displaying window

notificationSign.addEventListener('click', () => {
    notificationWindow.style.display = 'block'
    document.getElementById('notification-icon').style.display = 'none'
    notificationSign.style.opacity = 0.7
})

// closing window

document.getElementById('close-notifications').addEventListener('click', () => {
    notificationWindow.style.display = 'none'
    document.getElementById('other-pages').style.display = 'none'
    notificationSign.style.opacity = 1
})

for (let i = 0; i < infoTexts.length; i++) {
    infoTexts[i].addEventListener('click', () => {
        circlesNotification[i].style.display = 'none'
        infoContent[i].style.fontWeight = 'normal'
        if (numOfNotifications > 0) {
        numOfNotifications -= 1
        }
    })
}

// prevent refreshing form in notifications

let userRequestForm = document.getElementsByClassName('user-request')

for (let i = 0; i < userRequestForm.length; i++) {
    userRequestForm[i].addEventListener('submit', (e) => {
        e.preventDefault()
    })
}

// confirm - remove friend invitation

for (let i = 0; i < confirmFriend.length; i++) {
    confirmFriend[i].addEventListener('click', () => {
        document.getElementsByClassName('after-confirm')[i].style.display = 'block'
        confirmFriend[i].style.opacity = '0'
        confirmFriend[i].style.pointerEvents = 'none'
        removeFriend[i].style.opacity = '0'
        removeFriend[i].style.pointerEvents = 'none'
    })
}

for (let i = 0; i < removeFriend.length; i++) {
    removeFriend[i].addEventListener('click', () => {
        document.getElementsByClassName('after-remove')[i].style.display = 'block'
        confirmFriend[i].style.opacity = '0'
        confirmFriend[i].style.pointerEvents = 'none'
        removeFriend[i].style.opacity = '0'
        removeFriend[i].style.pointerEvents = 'none'
    })
}

// accept - decline group invitation

for (let i = 0; i < acceptGroup.length; i++) {
    acceptGroup[i].addEventListener('click', () => {
        document.getElementsByClassName('after-accept')[i].style.display = 'block'
        acceptGroup[i].style.opacity = '0'
        acceptGroup[i].style.pointerEvents = 'none'
        declineGroup[i].style.opacity = '0'
        declineGroup[i].style.pointerEvents = 'none'
    })
}

for (let i = 0; i < declineGroup.length; i++) {
    declineGroup[i].addEventListener('click', () => {
        document.getElementsByClassName('after-decline')[i].style.display = 'block'
        acceptGroup[i].style.opacity = '0'
        acceptGroup[i].style.pointerEvents = 'none'
        declineGroup[i].style.opacity = '0'
        declineGroup[i].style.pointerEvents = 'none'
    })
}

// OTHER PAGES WINDOW

let openPagesWindow = document.getElementById('photo-wrapper-onclick')
let otherPagesWindow = document.getElementById('other-pages')

openPagesWindow.onclick = () => {
    otherPagesWindow.style.display = 'block'
    document.getElementById('info').style.display = 'none'
    if (document.getElementById('notification-open').style.opacity !== 1) {
        document.getElementById('notification-open').style.opacity = 1
    }
}

window.addEventListener('click', (event) => {
    if (event.target !== openPagesWindow) {
        otherPagesWindow.style.display = 'none'
    }
})

// APPEARING WINDOW WITH OPTION TO CHANGE PROFILE 

let changeProfileWindow = document.getElementById('change-profile-image-window')
let changeProfileButton = document.getElementById('change-profile-image-button')
let chooseImageLabel = document.getElementById('choose-image-label')
let chooseImageInput = document.getElementById('choose-image')
let imagePlaceholder = document.getElementById('image-placeholder')

let changeProfileWindowItems = [
    changeProfileWindow,
    chooseImageLabel,
    chooseImageInput,
    changeProfileButton,
    document.getElementById('image-wrapper'),
    document.getElementById('change-profile-title'),
    imagePlaceholder]

changeProfileButton.onclick = () => {
    changeProfileWindow.style.display = 'flex';
    document.getElementById('black-background').style.display = 'block'
}

// DISPLAY IMAGE AFTER CHOOSE

let imageWrapper = document.getElementById('image-wrapper')

let showImage = (event) => {
    imageWrapper.style.backgroundImage = `url(${URL.createObjectURL(event.target.files[0])})`
}

// CLOSE WINDOW

window.onclick = function(event) {
    if (changeProfileWindowItems.every(el => el !== event.target)) {
        changeProfileWindow.style.display = 'none'
        document.getElementById('black-background').style.display = 'none'
        imageWrapper.style.backgroundImage = 'none'
    };
}