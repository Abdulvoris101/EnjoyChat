data = {
    IsPostActive: false,
    allPosts: {
        url: `http:${window.location.host}/api/all_posts/`,
        response: [],
    }
}
let posts_data = [];

fetch(data.allPosts.url)
    .then(res => {
        res.json().then(data => {
            posts_data = data
            
        })
    })



// console.log(posts_data);

let modal_view = document.querySelectorAll('.modal-view')

modal_view.forEach(function (modals) {
    modals.classList.remove('textarea')
    modals.classList.add('input')
})


let modalExpBtns = document.querySelectorAll('.open-exp_modal')
let closeModal = document.querySelectorAll('.modal-close-explore')

function httpGet(url)
{
    fetch(url).then(function(response) {
        return response.json();
    })
    .then((response) => {
        console.log(response);

    }).catch(function(error) {
        console.log(error);
    });
}

modalExpBtns.forEach(function (btn) {
    btn.onclick = function () {
        
        var modal = btn.getAttribute('data-post');
        var post_id = btn.getAttribute('data-id')
        let videoEl = document.querySelector('#video' + post_id)
        
        if (videoEl) {
            let getVideoJs = videojs('video' + post_id)
            getVideoJs.play()
        }

        let prev_to = document.querySelector('.prev_to' + post_id)
        let prev_to_int = parseInt(prev_to.getAttribute('data-prev_id'))
        prev_to.dataset.prev_to_int = prev_to_int - 1

        let next_to = document.querySelector('.next_to' + post_id)
        let next_to_int = parseInt(next_to.getAttribute('data-next_id'))
        next_to.dataset.next_to_int = next_to_int + 1

        let url = 'http://' + window.location.host + '/public/' + '?post=' + post_id
        httpGet(url)

        document.getElementById(modal).classList.add('is-active')
        document.getElementById('documentBody').classList.add('modal-open')
    }
})


function prev_to_post(event) {
    let currentIntId = parseInt(event)
    let currentStrId = event
    let getNextoId = currentIntId + 1
    let modal_id = 'exp_modal' + getNextoId
    let currentDom = document.getElementById('exp_modal' + currentIntId)
    let dom = document.getElementById(modal_id)

    let videoEl = document.querySelector('#video' + currentStrId)
    

    if (videoEl) {
        let getVideoJs = videojs('video' + currentStrId)
        getVideoJs.pause()
    }

    


    for (let i = getNextoId; i < posts_data[0].id; i++) {
        dom = document.getElementById('exp_modal' + i)
        if (dom != null) {
            let newdom = document.getElementById('exp_modal' + i)
            let prevVideoEl = document.querySelector('#video' + i)

            if (prevVideoEl) {
                videojs('video' + i).play()
            }
            newdom.classList.add('is-active')
            currentDom.classList.remove('is-active')
            break;
        }

    }

}

function next_to_post(event) {
    let currentIntId = parseInt(event)
    let currentStrId = event
    let getPrevtoId = currentIntId - 1
    let modal_id = 'exp_modal' + getPrevtoId
    let currentDom = document.getElementById('exp_modal' + currentIntId)
    let dom = document.getElementById(modal_id)

    
    let videoEl = document.querySelector('#video' + currentStrId)

    
    

    if (videoEl) {
        let getVideoJs = videojs('video' + currentStrId)
        getVideoJs.pause()
    }

    for (let i = getPrevtoId; i > 0; i--) {
        dom = document.getElementById('exp_modal' + i)
        if (dom != null) {
            var last_id = i;
            let nextVideoEl = document.querySelector('#video' + i)

            if (nextVideoEl) {
                videojs('video' + i).play()
            }

            let newdom = document.getElementById('exp_modal' + i)
            newdom.classList.add('is-active')
            currentDom.classList.remove('is-active')
            break;
        }

    }
}

closeModal.forEach((btn) => {
    btn.onclick = () => {
        let modal_id = btn.getAttribute('data-id');
        let modal = 'exp_modal' + modal_id

        let videoEl = document.querySelector('#video' + modal_id)

        if (videoEl) {
            let getVideoJs = videojs('video' + modal_id)
            getVideoJs.pause()
        }

        document.getElementById(modal).classList.remove('is-active')
        document.getElementById('documentBody').classList.remove('modal-open')
    }
})



let modalLikeBtns = document.querySelectorAll('.open-modal')
let closeLikeModal = document.querySelectorAll('.close-modal-l')


modalLikeBtns.forEach(function (btn) {
    btn.onclick = function () {
        var modal = btn.getAttribute('data-modal');
        document.getElementById(modal).classList.add('is-active')
        document.getElementById('documentBody').classList.add('modal-open')
    }
})

closeLikeModal.forEach((btn) => {
    btn.onclick = () => {
        console.log(btn);
        var modal = btn.getAttribute('data-id');
        modal = 'modal' + modal
        document.getElementById(modal).classList.remove('is-active')
        document.getElementById('documentBody').classList.remove('modal-open')
    }
})
