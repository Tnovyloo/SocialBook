// REFRESHING WINDOW PAGE POSITION SET TO TOP

window.onbeforeunload = () => window.scrollTo(0, 0)

// Settings posts wrapper to appropriate height

let additionalHeight = document.getElementById('posts-container').offsetHeight + document.getElementById('add-post').offsetHeight + 35
document.getElementById('additional-info-posts-section').style.height = `${additionalHeight}px`

// REPORT WINDOW

const reportButton = document.getElementsByClassName('post-options-button')
const postOptions = document.getElementsByClassName('post-options')
const reportText = document.getElementsByClassName('report')


for (let z = 0; z < reportButton.length; z++) {
    reportButton[z].onclick = () => postOptions[z].style.display ='flex';
    reportText[z].addEventListener('click', () => {
    postOptions[z].style.display = 'none'
    document.querySelector('#report-background').style.display = 'flex'
    document.getElementsByTagName('body')[0].style.overflowY = 'hidden'
    document.getElementsByTagName('body')[0].style.paddingRight = '17px'
})
}

window.onclick = function(event) {
    if ([...postOptions].every(el => el !== event.target) && [...reportButton].every(el => el !== event.target)) {
        for (let i = 0; i < postOptions.length; i++) {
            postOptions[i].style.display = 'none'
        }
    }
}

document.querySelector('#report-background').addEventListener('click',
function() {
    document.querySelector('#report-background').style.display = 'none'
    document.getElementsByTagName('body')[0].style.overflowY = 'scroll'
    document.getElementsByTagName('body')[0].style.paddingRight = '0'
})

// LIKE ANIMATION

const likesList = document.getElementsByClassName('fa-thumbs-up')

for (let i = 0; i < likesList.length; i++) {
    likesList[i].addEventListener('click', () => likesList[i].classList.toggle('animation-like'))
}

// SECTIONS SELECT ANIMATIONS

let posts = document.getElementById("posts")
let photos = document.getElementById("photos")
let about = document.getElementById("about")
let friends = document.getElementById('friends')
let underlines = document.getElementsByClassName('underline')
let postsSection = document.getElementById('container-posts-section')
let photosSection = document.getElementById('photos-section')
let aboutSection = document.getElementById('about-section')
let friendsSection = document.getElementById('friends-section')
let allFriends = document.getElementsByClassName('all')

posts.style.color = 'blue'
underlines[0].style.display = 'block'
aboutSection.style.display = 'none'
photosSection.style.display = 'none'
friendsSection.style.display = 'none'

posts.addEventListener('click', () => {
    underlines[0].style.display = 'block'
    underlines[1].style.display = 'none'
    underlines[2].style.display = 'none'
    underlines[3].style.display = 'none'
    posts.style.color = 'hsl(220, 60%, 35%)'
    photos.style.color = 'black'
    about.style.color = 'black'
    friends.style.color = 'black'
    postsSection.style.display = 'block'
    document.getElementById('posts-container').style.display = 'block'
    photosSection.style.display = 'none'
    aboutSection.style.display = 'none'
    friendsSection.style.display = 'none'
})

photos.addEventListener('click', () => {
    underlines[0].style.display = 'none';
    underlines[1].style.display = 'block';
    underlines[2].style.display = 'none';
    underlines[3].style.display = 'none';
    posts.style.color = 'black'
    photos.style.color = 'hsl(220, 60%, 35%)'
    about.style.color = 'black'
    friends.style.color = 'black'
    postsSection.style.display = 'none'
    document.getElementById('posts-container').style.display = 'none'
    photosSection.style.display = 'block'
    aboutSection.style.display = 'none'
    friendsSection.style.display = 'none'
})

about.addEventListener('click', () => {
    underlines[0].style.display = 'none';
    underlines[1].style.display = 'none'
    underlines[2].style.display = 'block';
    underlines[3].style.display = 'none';
    posts.style.color = 'black'
    photos.style.color = 'black'
    about.style.color = 'hsl(220, 60%, 35%)'
    friends.style.color = 'black'
    postsSection.style.display = 'none'
    document.getElementById('posts-container').style.display = 'none'
    photosSection.style.display = 'none'
    aboutSection.style.display = 'block'
    friendsSection.style.display = 'none'
})

let friendsDirection = [friends, allFriends[0], allFriends[1]]

for (let i = 0; i < friendsDirection.length; i++) {
    friendsDirection[i].addEventListener('click', () => {
            underlines[0].style.display = 'none'
            underlines[1].style.display = 'none'
            underlines[2].style.display = 'none'
            underlines[3].style.display = 'block'
            posts.style.color = 'black'
            photos.style.color = 'black'
            about.style.color = 'black'
            friends.style.color = 'hsl(220, 60%, 35%)'
            postsSection.style.display = 'none'
            document.getElementById('posts-container').style.display = 'none'
            photosSection.style.display = 'none'
            aboutSection.style.display = 'none'
            friendsSection.style.display = 'block'
            document.documentElement.scrollTop = 0
    })
}

// input in about section

let saveButton = document.getElementsByClassName('save')
let closeButton = document.getElementsByClassName('close')
let changeDiv = document.getElementsByClassName('change-value')
let currValue = document.getElementsByClassName('current-value')
let newChanges = document.getElementsByClassName('new-changes')
let openWindow = document.getElementsByClassName('open-window')
let leftIcons = document.getElementsByClassName('left')
let personalInfo = document.getElementsByClassName('personal-info')

for (let i = 0; i < newChanges.length; i++) {
    openWindow[i].addEventListener('click', () => {
        changeDiv[i].style.display = 'block'
        leftIcons[i].style.display = 'none';
        personalInfo[i].style.opacity = '0'
        openWindow[i].style.display ='none'
        for (let j = 0; j < openWindow.length; j++) {
            if (j !== i) {
                openWindow[j].style.pointerEvents = 'none'
            }
        }
    })
}

for (let i = 0; i < saveButton.length; i++) {
    saveButton[i].addEventListener('click', () => {
        currValue[i].innerText = newChanges[i].value;
        changeDiv[i].style.display = 'none';
        leftIcons[i].style.display = 'inline-block'
        personalInfo[i].style.opacity = '1'
        openWindow[i].style.display = 'inline-block'
        for (let j = 0; j < openWindow.length; j++) {
            if (j !== i) {
                openWindow[j].style.pointerEvents = 'auto'
            }
        }
    })
    closeButton[i].addEventListener('click', () => {
        changeDiv[i].style.display = 'none';
        leftIcons[i].style.display = 'inline-block'
        personalInfo[i].style.opacity = '1'
        openWindow[i].style.display = 'inline-block'
        for (let j = 0; j < openWindow.length; j++) {
            if (j !== i) {
                openWindow[j].style.pointerEvents = 'auto'
            }
        }
    })

    if (i === 6) {
        saveButton[i].addEventListener('click', () => currValue[i].innerText = document.getElementsByTagName('select')[0].value !== 'Select your option' ? document.getElementsByTagName('select')[0].value : '')
    }
}

// FRIENDS ABOUT SECTION - FRIENDS LIST OPTIONS

let friendOptionsButton = [...document.getElementsByClassName('friend-options-on')]
let friendOptionsWindow = [...document.getElementsByClassName('friend-options-window')]
let favouriteOption = document.getElementsByClassName('favourite')
let followOption = document.getElementsByClassName('follow-option')
let followText = document.getElementsByClassName('follow-text')
let unfriendOption = document.getElementsByClassName('unfriend')
let favouriteHearts = document.getElementsByClassName('fas fa-heart')
let addFriendButton = document.getElementsByClassName('add-friend')

for (let i = 0; i < friendOptionsButton.length; i++) {
    friendOptionsButton[i].onclick = function() {
        friendOptionsWindow[i].style.display = 'flex'
    }
     window.onclick = function(event) {
         if (friendOptionsButton.every(el => el !== event.target) && friendOptionsWindow.every(el => el !== event.target)) {
             for (let i = 0; i < friendOptionsWindow.length; i++) {
                 friendOptionsWindow[i].style.display = 'none'
             }
         }
     }
    favouriteOption[i].addEventListener('click', () => favouriteHearts[i].style.color === 'red' ? favouriteHearts[i].style.color = 'black' : favouriteHearts[i].style.color = 'red')
    followOption[i].addEventListener('click', () => followText[i].innerText === 'Unfollow' ? followText[i].innerText = 'Follow' : followText[i].innerText = 'Unfollow')
    unfriendOption[i].addEventListener('click', () => addFriendButton[i].style.display = 'block')
    addFriendButton[i].addEventListener('click', () => addFriendButton[i].innerText === 'Cancel Request' ? addFriendButton[i].innerText = 'Add Friend' : addFriendButton[i].innerText = 'Cancel Request')
}