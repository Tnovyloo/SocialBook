// REFRESHING WINDOW PAGE POSITION SET TO TOP

window.onbeforeunload = () => window.scrollTo(0, 0)

// CALCULATE HEIGHT FOR CONTAINER POSTS SECTION 

window.onload = () => {
    document.getElementById('container-posts-section').style.height = document.getElementById('posts-container').offsetHeight + document.getElementById('add-post').offsetHeight + 'px'
}

window.onresize = () => {
    if (innerWidth < 1150) {
        document.getElementById('container-posts-section').style.height = document.getElementById('posts-container').offsetHeight + document.getElementById('add-post').offsetHeight + 'px'
    }
    if (innerWidth > 1150) {
        document.getElementById('container-posts-section').style.height = document.getElementById('posts-container').offsetHeight + document.getElementById('add-post').offsetHeight + 'px'
    }
}

// REPORT AND DELETE OPTION

const reportButton = document.getElementsByClassName('post-options-button')
const postOptions = document.getElementsByClassName('post-options')
const reportText = document.getElementsByClassName('report')
const deleteText = document.getElementsByClassName('delete')
const allPosts = document.getElementsByClassName('post')

for (let z = 0; z < reportButton.length; z++) {
    reportButton[z].onclick = () => postOptions[z].style.display ='flex';
    reportText[z].addEventListener('click', () => {
    document.querySelector('#report-background').style.display = 'flex'
    document.getElementsByTagName('body')[0].style.overflowY = 'hidden'
    document.getElementsByTagName('body')[0].style.paddingRight = '17px'
    })
    deleteText[z].addEventListener('click', () => {
        document.getElementById('container-posts-section').style.height = document.getElementById('container-posts-section').style.height.split('').slice(0, -2).join('') - allPosts[z].offsetHeight + 'px'
        allPosts[z].style.display = 'none'
    })
}

document.querySelector('#report-background').addEventListener('click',
function() {
    document.querySelector('#report-background').style.display = 'none'
    document.getElementsByTagName('body')[0].style.overflowY = 'scroll'
    document.getElementsByTagName('body')[0].style.paddingRight = '0'
})

window.addEventListener('click', (event) => {
    if ([...reportButton].every(el => el !== event.target) && [...postOptions].every(el => el !== event.target)) {
        for (let i = 0; i < postOptions.length; i++) {
            postOptions[i].style.display = 'none'
        }
    }
})

// EDIT CAPTION OPTION

const changeCaptionForm = document.getElementsByClassName('change-caption-form')
const editText = document.getElementsByClassName('edit-caption')
const editTextarea = document.getElementsByClassName('change-caption-text')
const captionText = document.getElementsByClassName('caption-text')
const finishedEditing = document.getElementsByClassName('finished-editing')
const cancel= document.getElementsByClassName('cancel')
const caption = document.getElementsByClassName('caption')

// functionality of edit text

for (let i = 0; i < editText.length; i++) {
    editText[i].addEventListener('click', () => {
        if (caption[i].style.display === 'none') {
            caption[i].style.display = 'block'
        }
        captionText[i].style.display = 'none'
        changeCaptionForm[i].style.display = 'grid'
    })
}

// value of input = caption text

for (let i = 0; i < editTextarea.length; i++) {
    editTextarea[i].value = captionText[i].innerText
}

// count number of characters

let numOfCharactersLeft = document.getElementsByClassName('edit-num-of-characters-left')
let max = 500

for (let i = 0; i < numOfCharactersLeft.length; i++) {
    numOfCharactersLeft[i].innerText = max - document.getElementsByClassName('change-caption-text')[i].value.length
}

function calcChar(textarea) {
    for (let i = 0; i < numOfCharactersLeft.length; i++) {
        numOfCharactersLeft[i].innerText = max - textarea.value.length
    }
}

// finished editing and cancel buttons functionality

const changeCaptionForms = document.getElementsByClassName('change-caption-form')

for (let i = 0; i < changeCaptionForm.length; i++) {
    changeCaptionForms[i].addEventListener('submit', (event) => {
        event.preventDefault()
    })

    finishedEditing[i].addEventListener('click', () => {
        if (!editTextarea[i].value) {
            caption[i].style.display = 'none'
        }
        captionText[i].innerText = editTextarea[i].value
        captionText[i].style.display = 'block'
        changeCaptionForm[i].style.display = 'none'
    })

    cancel[i].addEventListener('click', () => {
        if(captionText[i].innerText === '') {
            caption[i].style.display = 'none'
        }
        captionText[i].style.display = 'block'
        changeCaptionForm[i].style.display = 'none'
    })
}

// SELECT SECTION IN POSTS SECTION

let posts = document.getElementById("posts")
let photos = document.getElementById("photos")
let about = document.getElementById("about")
let friends = document.getElementById('friends')
let underlines = document.getElementsByClassName('underline')
let postsSection = document.getElementById('container-posts-section')
let photosSection = document.getElementById('photos-section')
let aboutSection = document.getElementById('about-section')
let friendsSection = document.getElementById('friends-section')
let allFriends = document.getElementsByClassName('all-friends')

posts.style.color = 'var(--accept-button-color)'
underlines[0].style.display = 'block'
aboutSection.style.display = 'none'
photosSection.style.display = 'none'
friendsSection.style.display = 'none'

posts.addEventListener('click', () => {
    underlines[0].style.display = 'block'
    underlines[1].style.display = 'none'
    underlines[2].style.display = 'none'
    underlines[3].style.display = 'none'
    posts.style.color = 'var(--accept-button-color)'
    photos.style.color = 'var(--text-color)'
    about.style.color = 'var(--text-color)'
    friends.style.color = 'var(--text-color)'
    postsSection.style.display = 'block'
    document.getElementById('posts-container').style.display = 'block' 
    photosSection.style.display = 'none'
    aboutSection.style.display = 'none'
    friendsSection.style.display = 'none'
    for (let i = 0; i < document.getElementsByClassName('friend').length; i++) {
        document.getElementsByClassName('friend')[i].style.display = 'block'
    }
})

photos.addEventListener('click', () => {
    underlines[0].style.display = 'none';
    underlines[1].style.display = 'block';
    underlines[2].style.display = 'none';
    underlines[3].style.display = 'none';
    posts.style.color = 'var(--text-color)'
    photos.style.color = 'var(--accept-button-color)'
    about.style.color = 'var(--text-color)'
    friends.style.color = 'var(--text-color)'
    postsSection.style.display = 'none'
    document.getElementById('posts-container').style.display = 'none'
    photosSection.style.display = 'block'
    aboutSection.style.display = 'none'
    friendsSection.style.display = 'none'
    for (let i = 0; i < document.getElementsByClassName('friend').length; i++) {
        document.getElementsByClassName('friend')[i].style.display = 'block'
    }
})

about.addEventListener('click', () => {
    underlines[0].style.display = 'none';
    underlines[1].style.display = 'none'
    underlines[2].style.display = 'block';
    underlines[3].style.display = 'none';
    posts.style.color = 'var(--text-color)'
    photos.style.color = 'var(--text-color)'
    about.style.color = 'var(--accept-button-color)'
    friends.style.color = 'var(--text-color)'
    postsSection.style.display = 'none'
    document.getElementById('posts-container').style.display = 'none'
    photosSection.style.display = 'none'
    aboutSection.style.display = 'block'
    friendsSection.style.display = 'none'
    for (let i = 0; i < document.getElementsByClassName('friend').length; i++) {
        document.getElementsByClassName('friend')[i].style.display = 'block'
    }
})

// SEE ALL FRIENDS OPTION 

let friendsDirection = [friends, allFriends[0], allFriends[1]]

for (let i = 0; i < friendsDirection.length; i++) {
    friendsDirection[i].addEventListener('click', () => {
            underlines[0].style.display = 'none'
            underlines[1].style.display = 'none'
            underlines[2].style.display = 'none'
            underlines[3].style.display = 'block'
            posts.style.color = 'var(--text-color)'
            about.style.color = 'var(--text-color)'
            photos.style.color = 'var(--text-color)'
            friends.style.color = 'var(--accept-button-color)'
            postsSection.style.display = 'none'
            document.getElementById('posts-container').style.display = 'none'
            photosSection.style.display = 'none'
            aboutSection.style.display = 'none'
            friendsSection.style.display = 'block'
            document.getElementById('all-friends-section-underline').style.borderBottom = '3px solid var(--accept-button-color)'
            document.getElementById('family-members-section-underline').style.borderBottom = 'none'
            document.getElementById('same-city-section-underline').style.borderBottom = 'none'
            document.documentElement.scrollTop = 0
    })
}

// SEE ALL PHOTOS OPTION

document.getElementById('all-photos').addEventListener('click', () => {
    underlines[0].style.display = 'none'
    underlines[1].style.display = 'block'
    posts.style.color = 'var(--text-color)'
    photos.style.color = 'hsl(220, 60%, 35%)'
    postsSection.style.display = 'none'
    document.getElementById('posts-container').style.display = 'none'
    photosSection.style.display = 'block'
})

// SELECT SECTION IN FRIENDS SECTION

// all type of friends

let sameCityFriends = document.getElementsByClassName('same-city')
let familyFriends = document.getElementsByClassName('family')
let allFriendsInFriendsSection = document.getElementsByClassName('friend')

// underlines and border style

let allFriendsSectionUnderline = document.getElementById('all-friends-section-underline') // in friends section
let familyMembersSectionUnderline = document.getElementById('family-members-section-underline') 
let sameCitySectionUnderline = document.getElementById('same-city-section-underline')
let borderBottomOn = '3px solid var(--accept-button-color)'
let borderBottomOff = 'none'

allFriendsSectionUnderline.style.borderBottom = borderBottomOn

allFriendsSectionUnderline.addEventListener('click', () => {
    allFriendsSectionUnderline.style.borderBottom = borderBottomOn
    familyMembersSectionUnderline.style.borderBottom = borderBottomOff
    sameCitySectionUnderline.style.borderBottom = borderBottomOff
    for (let i = 0; i < allFriendsInFriendsSection.length; i++) {
        allFriendsInFriendsSection[i].style.display = 'block'
    }
})

familyMembersSectionUnderline.addEventListener('click', () => {
    allFriendsSectionUnderline.style.borderBottom = borderBottomOff
    familyMembersSectionUnderline.style.borderBottom = borderBottomOn
    sameCitySectionUnderline.style.borderBottom = borderBottomOff
    for (let i = 0; i < allFriendsInFriendsSection.length; i++) {
        allFriendsInFriendsSection[i].style.display = 'none'
    }
    for (let i = 0; i < familyFriends.length; i++) {
        familyFriends[i].style.display = 'block'
    }
})

sameCitySectionUnderline.addEventListener('click', () => {
    allFriendsSectionUnderline.style.borderBottom = borderBottomOff
    familyMembersSectionUnderline.style.borderBottom = borderBottomOff
    sameCitySectionUnderline.style.borderBottom = borderBottomOn
    for (let i = 0; i < allFriendsInFriendsSection.length; i++) {
        allFriendsInFriendsSection[i].style.display = 'none'
    }

    for (let i = 0; i < sameCityFriends.length; i++) {
        sameCityFriends[i].style.display = 'block'
    }
})

// ADD BIO POSTS SECTION

let addBioButton = document.getElementById('add-bio-submit')
let bioText = document.getElementById('user-input-text')
let bioForm = document.getElementById('bio-form')
let addBioText = document.getElementById('add-bio-text')
let saveBioTextButton = document.getElementById('bio-save')
let cancelBioTextButton = document.getElementById('bio-cancel')

if (bioText.innerText === '') {
    addBioButton.style.display = 'block'
    document.getElementById('user-input-info').style.borderBottom = 'none'
}

addBioButton.addEventListener('click', () => {
    bioForm.style.display = 'grid'
    bioForm.style.marginTop = '10px'
    addBioButton.style.display = 'none'
})

saveBioTextButton.addEventListener('click', () => {
    bioForm.style.display = 'none'
    if (addBioText.value !== '') {
        bioText.innerText = addBioText.value
        bioText.style.display = 'block'
        document.getElementById('user-input-info').style.borderBottom = '2px solid hsl(0, 0%, 86%)'
    }
    if (bioText.offsetHeight > 60) {
        bioText.style.maxHeight = '50px';
        bioText.style.fontSize = '1.5rem';
        document.getElementById('additional-info-posts-section').style.top = '1.5rem'
    } else if (bioText.offsetHeight > 50) {
        document.getElementById('additional-info-posts-section').style.top = '0.5rem'
    } else {
        document.getElementById('additional-info-posts-section').style.top = '1.8rem'
    }
})

cancelBioTextButton.addEventListener('click', () => {
    bioForm.style.display = 'none'
    if (bioText.innerText === '') {
        addBioButton.style.display = 'block'
    } else {
        bioText.style.display = 'block'
        document.getElementById('user-input-info').style.borderBottom = '2px solid hsl(0, 0%, 86%)'
    }
})

// remaining characters in bio

let charCount = (textarea) => {
    let currNumOfCharacters = textarea.value.length
    document.getElementById('num-of-characters-bio').innerText = currNumOfCharacters
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
let postsSectionUserInfo = [document.getElementById('live-place'), document.getElementById('from-place'), document.getElementById('hobby')]

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
        if (i === 0 || i === 1) {
            postsSectionUserInfo[i].innerText = newChanges[i].value
        } else if (i === 3) {
            postsSectionUserInfo[2].innerText = newChanges[i].value
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
    favouriteOption[i].addEventListener('click', () => favouriteHearts[i].style.color === 'red' ? favouriteHearts[i].style.color = 'var(--text-color)' : favouriteHearts[i].style.color = 'red')
    followOption[i].addEventListener('click', () => followText[i].innerText === 'Unfollow' ? followText[i].innerText = 'Follow' : followText[i].innerText = 'Unfollow')
    unfriendOption[i].addEventListener('click', () => {addFriendButton[i].style.display = 'block'; friendOptionsButton[i].style.opacity = 0})
    addFriendButton[i].addEventListener('click', () => addFriendButton[i].innerText === 'Cancel Request' ? addFriendButton[i].innerText = 'Add Friend' : addFriendButton[i].innerText = 'Cancel Request')
}