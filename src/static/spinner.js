const spinnerBox = document.getElementById('spinner-box'); 

if (spinnerBox) {
$.ajax({
    type: 'GET',
    url: '/',
    success: function(response){
        spinnerBox.classList.add('spinner')
    }
})
} 