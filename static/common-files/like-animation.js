const likes = document.getElementsByClassName('fa-thumbs-up')
const numOfLikes = document.getElementsByClassName('num-of-likes')
const lastPersonToLike = document.getElementsByClassName('last-person-like')

for (let i = 0; i < likes.length; i++) {
    likes[i].addEventListener('click', () => {
        likes[i].classList.toggle('animation-like');
        if (likes[i].classList[2] === 'animation-like') {
            numOfLikes[i].innerText = parseInt(numOfLikes[i].innerText) + 1
            lastPersonToLike[i].innerText = 'you'
        } else {
            numOfLikes[i].innerText = parseInt(numOfLikes[i].innerText) - 1
            lastPersonToLike[i].innerText = 'name'
        }
    })
}