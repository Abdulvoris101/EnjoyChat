data = {
    isActive: false,
    
    isUserFollowersActive: false,
}


let allVideos = document.querySelectorAll('.video-css')
let arr = []

var first_video_num;

allVideos.forEach((event, i) => {
    let data_id = event.attributes.getNamedItem('data-id').value
    let myel = document.querySelector('#video' + data_id)
    var top = myel.getBoundingClientRect().top;
    arr.push(
        {
            'id': data_id,
            'height': parseInt(top)
        }
    )
    first_video_num = arr[0].id
    
})


let filteredVideos = []



window.addEventListener('scroll', function() {
    for (let i = 0; i < arr.length; i++) {
        let allVideos = arr[i]

        if(pageYOffset >= allVideos.height) {
            let filteredVideos = arr.filter(function (el) {
                return el.height + 250 < pageYOffset
            });
            videojs('video' + filteredVideos[i].id).pause()

        }
        
        else if(pageYOffset <= allVideos.height) {
            let filteredVideos = arr.filter(function (el) {
                return el.height + 250 >= pageYOffset
            });

            videojs('video' + filteredVideos[1].id).pause()

        }
    }
});


// let new_video = 


let toggleCreateModal = () => {
    data.isActive = !data.isActive
    let modal = document.querySelector('#create_modal')

    
    if (data.isActive == true) {
        modal.classList.add('is-active');
    }
    else {
        modal.classList.remove('is-active')
    }
    
}

let modalBtns = document.querySelectorAll('.open-modal')
let closeModal = document.querySelectorAll('.close-modal-l')


modalBtns.forEach(function (btn) {
    
    btn.onclick = function () {
        var modal = btn.getAttribute('data-modal');
        document.getElementById(modal).classList.add('is-active')
        document.getElementById('documentBody').classList.add('modal-open')
    }
})

closeModal.forEach((btn) => {
    btn.onclick = () => {
        console.log(btn);
        var modal = btn.getAttribute('data-id');
        modal = 'modal' + modal
        document.getElementById(modal).classList.remove('is-active')
        document.getElementById('documentBody').classList.remove('modal-open')
    }
})

// document.getElementById('open-following-modal').onclick = () => {
//     data.isMyFollowingActive = !data.isMyFollowingActive
//     let modal = document.querySelector('#my-profile-following')
//     if (data.isMyFollowingActive == true) {
//         modal.classList.add('is-active')
//     } else {
//         modal.classList.remove('is-active')
//     }
// }


// my_profile_modal_following 

// document.getElementById('close-myf-modal').onclick = () => {

// }

// let myoffcanvas = document.querySelector('#myoffcanvas')

//           myoffcanvas.addEventListener('touchstart', handleTouchStart, false)
//           myoffcanvas.addEventListener('touchmove', handleTouchMove, false)

//           let x1 = null;
//           let y1 = null;

//           function handleTouchStart(event) {
//               const firstTouch = event.touches[0]

//               x1 = firstTouch.clientX;
//               y1 = firstTouch.clientY;
//           }

//           function handleTouchMove(event) {
//               if (!x1 || !y1) {
//                   return false;
//               }
//               let x2 = event.touches[0].clientX;
//               let y2 = event.touches[0].clientY;
//               let xDiff = x2 - x1;
//               let yDiff = y2 - y1;

//               if (Math.abs(xDiff) < Math.abs(yDiff)) {

//                   if (yDiff > 0) {
//                       console.log('down');
//                   } else {
//                       console.log('top');
//                   }

//               } 

//           }


let verif = document.querySelector('#notif-verificated')
let isverif = document.querySelector('#openedVerifNotif')

if (isverif) {
    if (isverif.value == 'True') {
        function setTimeVerif() {
            verif.style.display = 'none'
        }
    
        setTimeout(setTimeVerif, 1000);
    }
}




function handleFormSubmit(event) {
    event.preventDefault();

}


$('.owl-carousel').owlCarousel({
    loop:false,
    margin:10,
    nav:true,
    responsive:{
        0:{
            items:2
        },
        600:{
            items:3
        },
        1000:{
            items:3
        }
    }
})