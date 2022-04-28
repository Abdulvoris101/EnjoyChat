const user_id = JSON.parse(document.getElementById('user_id').textContent)
const message_username = JSON.parse(document.getElementById('message_username').textContent)
const room_name = JSON.parse(document.getElementById('room_name').textContent)

(window.location.protocol === 'https:' ? 'wss' : 'ws') + '://'

let socket = new WebSocket(
    'ws://'
    + window.location.host
    + '/chat/'
    + user_id
    + '/'
)

window.onload = () => {
    var objDiv = document.querySelector(".chat_msg_box");
    objDiv.scrollTop = objDiv.scrollHeight;
}



document.querySelector('.form_msg_send').addEventListener('submit', function (e) {
    e.preventDefault()
    let messageInputDom = document.querySelector('#msg_send_inp');
    let message = messageInputDom.value;

    if (message !== '') {
        socket.send(JSON.stringify({
            'message': message,
            'username': message_username,
            'img_src': '',
        }))
    }

    

    messageInputDom.value = ''

    var objDiv = document.querySelector(".chat_msg_box");
    objDiv.scrollTop = objDiv.scrollHeight - 120;
    console.log(objDiv.scrollHeight);

})

socket.onopen = function (e) {
    console.log('Connection Established', e);
}



socket.onmessage = function (e) {
    let data = JSON.parse(e.data)
    console.log(data);

    if (data.username == message_username) {
        if (data.message != '') {
            document.querySelector('.chat_msg_box').innerHTML += `
                <div class="chat_msg_r chat_msg_m mt-1">
                    ${data.message}
                </div>
            `
        }
        if (data.img_src != '' ) {
            console.log('my data');
            document.querySelector('.chat_msg_box').innerHTML += `
            <img class="chat_msg_r_img chat_msg_m_img mt-2" src="${data.img_src}" />
        `
        }
    } else {
        if (data.message != '') {
            document.querySelector('.chat_msg_box').innerHTML += `
                <div class="chat_msg_l chat_msg_m mt-1">
                    ${data.message}
                </div>
            `
        }
        if (data.img_src != '') {
            document.querySelector('.chat_msg_box').innerHTML += `
            <img class="chat_msg_l_img chat_msg_m_img mt-2" src="${data.img_src}" />
            `
        }
    }
    

}


let imgU = document.getElementById('img_input_msg')
let chatRight = document.querySelector('.chat_msg_r')

imgU.onchange = event => {
    var file = event.target.files[0]
    if (file) {
        
        handleImageUpload(event)

        console.log('on');
        document.getElementById(file.name).src = URL.createObjectURL(file)
    }
}

socket.onerror = function (e) {
    console.log('Error', e);
}
socket.onclose = function (e) {
    console.log('Connection Lost', e);
}

const handleImageUpload = event => {
    const files = event.target.files
    const formData = new FormData()
    const csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value;
    formData.append('image', files[0])
    formData.append('sender', message_username)
    formData.append('room_name', room_name)


    fetch('http://localhost:8000/chat/img/image_upload/', {
      method: 'POST',
      headers: {
        'X-CSRFToken': csrf_token
      },
      body: formData
    })

    

    .then(response => response.json())

    .then(data => {
        img_src = data['image_src']
        console.log(message_username);
        socket.send(JSON.stringify({
            'img_src': img_src,
            'username': message_username,
            'message': ''
        }))

    })
    .catch(error => {
      console.log(error)
    })

  }
  


