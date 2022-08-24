// CALCULATING LENGTH OF SUBTITLES IN SETTINGS CONTENT TO SET WIDTH OF THEM

let submitButton = document.getElementsByClassName('submit-button')

// for basic info

let basicInfoToChange = document.getElementsByClassName('info-to-change-basic')
let elementLength = []

for (let i = 0; i < basicInfoToChange.length; i++) {
    elementLength.push(basicInfoToChange[i].offsetWidth)
}

for (let i = 0; i < basicInfoToChange.length; i++) {
    basicInfoToChange[i].style.width = `${Math.max(...elementLength) + 10}px`
}

submitButton[0].style.marginLeft = `${Math.max(...elementLength) + 15}px`

// for places info

let placeInfoToChange = document.getElementsByClassName('info-to-change-places')
elementLength = []

for (let i = 0; i < placeInfoToChange.length; i++) {
    elementLength.push(placeInfoToChange[i].offsetWidth)
}

for (let i = 0 ; i < placeInfoToChange.length; i++) {
    placeInfoToChange[i].style.width = `${Math.max(...elementLength) + 10}px`
}

submitButton[1].style.marginLeft = `${Math.max(...elementLength) + 15}px`

// for education / hobby info

let eduHobbyInfoToChange = document.getElementsByClassName('info-to-change-hobby-education')
elementLength = []

for (let i = 0; i < eduHobbyInfoToChange.length; i++) {
    elementLength.push(eduHobbyInfoToChange[i].offsetWidth)
}

for (let i = 0 ; i < eduHobbyInfoToChange.length; i++) {
    eduHobbyInfoToChange[i].style.width = `${Math.max(...elementLength) + 10}px`
}

submitButton[2].style.marginLeft = `${Math.max(...elementLength) + 15}px`

// for contact info

let contactInfoToChange = document.getElementsByClassName('info-to-change-contact')
elementLength = []

for (let i = 0; i < contactInfoToChange.length; i++) {
    elementLength.push(contactInfoToChange[i].offsetWidth)
}

for (let i = 0 ; i < contactInfoToChange.length; i++) {
    contactInfoToChange[i].style.width = `${Math.max(...elementLength) + 10}px`
}

submitButton[3].style.marginLeft = `${Math.max(...elementLength) + 15}px`

// for close people info

let peopleInfoToChange = document.getElementsByClassName('info-to-change-people')
elementLength = []

for (let i = 0; i < peopleInfoToChange.length; i++) {
    elementLength.push(peopleInfoToChange[i].offsetWidth)
}

for (let i = 0 ; i < peopleInfoToChange.length; i++) {
    peopleInfoToChange[i].style.width = `${Math.max(...elementLength) + 10}px`
}

submitButton[4].style.marginLeft = `${Math.max(...elementLength) + 15}px`

// DISPLAYING DIFFERENT PARTS OF PAGE AT ONE TIME

let basicInfo = document.getElementById('basic-info')
let places = document.getElementById('live-places')
let hobbyEducation = document.getElementById('hobby-education')
let contact = document.getElementById('contact')
let closePeople = document.getElementById('close-people')
let forms = document.getElementsByClassName('forms')
let activateForm = document.getElementsByClassName('activate-form')

basicInfo.style.display = 'block'
places.style.display = 'none'
hobbyEducation.style.display = 'none'
contact.style.display = 'none'
closePeople.style.display = 'none'
activateForm[0].style.borderLeft = '2px solid black'
activateForm[0].style.fontWeight = 'bold'

for (let i = 0 ; i < forms.length; i++) {
    activateForm[i].addEventListener('click', () => {
        for (let j = 0; j < forms.length; j++) {
            forms[j].style.display = 'none'
            activateForm[j].style.borderLeft = 'none'
            activateForm[j].style.fontWeight = '400'
        }
        forms[i].style.display = 'block'
        activateForm[i].style.borderLeft = '2px solid black'
        activateForm[i].style.fontWeight = 'bold'
    })
}