// REPORT WINDOW

const reportButton = document.getElementsByClassName('fa-ellipsis')
const postOptions = document.getElementsByClassName('post-options') 
const closeSign = document.getElementsByClassName('close-sign')
const reportText = document.getElementsByClassName('report')

for (let z = 0; z < reportButton.length; z++) {
    reportButton[z].addEventListener('click', () => postOptions[z].style.display ='block')
    closeSign[z].addEventListener('click', () => postOptions[z].style.display = 'none')
    reportText[z].addEventListener('click', () => document.querySelector('#report-background').style.display = 'flex')
}

document.querySelector('#report-background').addEventListener('click',
function() {
    document.querySelector('#report-background').style.display = 'none'
})

// MESSAGE NOTIFICATION COUNTER

let numOfMessages = 0
let allMessages = document.getElementsByClassName('message')

for (let i = 0; i < allMessages.length; i++) {
    allMessages[i].style.fontWeight = 'bold'
}

for (let i = 0; i < allMessages.length; i++) {
    if (allMessages[i].style.fontWeight === 'bold') numOfMessages += 1
}

document.getElementById('notification').textContent = numOfMessages

// MESSAGE WINDOW AT INDEX.HTML

const circlesMessage = document.getElementsByClassName('circle-message')
const messagesContent = document.getElementsByClassName('message-content')

document.getElementById('message-icon').addEventListener('click',
function() {
    document.querySelector('#notification').style.display = 'none'
    document.querySelector('#messages').style.display = 'block'
    document.querySelector('#message-icon').style.color = 'gray'
})

document.querySelector('#close-messages').addEventListener('click',
function() {
    document.querySelector('#messages').style.display = 'none'
    document.querySelector('#message-icon').style.color = "black"
})

for (let i = 0; i < allMessages.length; i++) {
    allMessages[i].addEventListener('click', () => {
        allMessages[i].style.fontWeight = 'normal'
        messagesContent[i].style.color = 'black'
        circlesMessage[i].style.display = 'none'
        if (numOfMessages > 0) {
        numOfMessages -= 1
        }
    })
}

// COUNT NUMBER OF NOTIFICATIONS

let numOfNotifications = 0
// 
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

// NOTIFICATIONS WINDOW AT INDEX.HTML

const notificationSign = document.getElementById('notification-open') 
const infoTexts = document.getElementsByClassName('info-text')
const infoContent = document.getElementsByClassName('info-content')
const circlesNotification = document.getElementsByClassName('circle-notification')

// displaying window

notificationSign.addEventListener('click', () => {
    document.getElementById('info').style.display = 'block'
    document.getElementById('notification-icon').style.display = 'none'
    notificationSign.style.color = 'gray'
})

// closing window

document.getElementById('close-notifications').addEventListener('click', () => {
    document.querySelector('#info').style.display = 'none'
    notificationSign.style.color = "black"
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

// LIKE ANIMATION

const likesList = document.getElementsByClassName('fa-thumbs-up')

for (let i = 0; i < likesList.length; i++) {
    likesList[i].addEventListener('click', () => likesList[i].classList.toggle('animation-like'))
}
