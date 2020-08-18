var url=document.getElementById('videoUrl'),
form=document.getElementById('form');

console.log(url.value);

var val=function(e){

    function validate_url(e){

        if(url.value == false){

            alert('Inserte una url');
            e.preventDefault();
        }
    }

    validate_url(e);
}


form.addEventListener('submit',val);