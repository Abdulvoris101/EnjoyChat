data =  {
    isMyFollowingActive:false,
    isMyFollowersActive:false,
}
function openCloseModal(btn_id, isActivity, modal_id, closed_btn_id) {

    document.getElementById(btn_id).onclick = () => {
        isActivity = !isActivity
        let modal = document.getElementById(modal_id)
        if (isActivity == true) {
            modal.classList.add('is-active')
        } else {
            modal.classList.remove('is-active')
        }
        console.log(modal_id);
    }
    document.getElementById(closed_btn_id).onclick = () => {
        let modal = document.getElementById(modal_id)
        modal.classList.remove('is-active')
    }

}



openCloseModal('open-following-modal', data.isMyFollowingActive, 'my-profile-following', 'close-myf-modal');
openCloseModal('open-followers-modal', data.isMyFollowersActive, 'my-profile-followers', 'close-myfw-modal');