console.log('hello from spinner')

const spinnerBox = document.getElementById('spinner-box') 


$.ajax({
    type: 'GET',
    url: '/',
    success: function(response){
        spinnerBox.classList.add('spinner')
    }
})