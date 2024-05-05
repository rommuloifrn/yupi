var ex = /^.*(youtu\.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=)([^#\&\?]*).*|([^#\&\?]{11})/;

function parseUrlAndSubmit(formId) {
    form = document.getElementById(formId);
    user_input = form.elements['video_id'].value;
    video_id = parseUrl(user_input);
    
    if(video_id == null) {
        //....
    } else {
        form.video_id.value = video_id;
        form.submit();
    }

    
}

function parseUrl(url) { // this regex and code was taken form 
    match = url.match(ex);
    if (match[2] && match[2].length == 11) {
        return match[2];
    } else if (match[3] && match[3].length == 11) {
        return match[3];
    }
    else {
        console.log("deu bsta!");
        console.log(match);
        return null;
    }
}