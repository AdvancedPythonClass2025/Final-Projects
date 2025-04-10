function PlayPause(){
    const image = document.getElementById('play');
    const originalSrc = 'icons/play.png'; 
    const newSrc = 'icons/pause.png'; 


    if (image.src.includes(originalSrc)) {
        image.src = newSrc; 
    } else {
        image.src = originalSrc; 
    }
    
}

function like(){
    const image = document.getElementById('like');
    const originalSrc = 'icons/like.png'; 
    const newSrc = 'icons/like_clicked.png'; 


    if (image.src.includes(originalSrc)) {
        image.src = newSrc; 
    } else {
        image.src = originalSrc; 
    }
}

function dislike(){
    const image = document.getElementById('dislike');
    const originalSrc = 'icons/dislike.png'; 
    const newSrc = 'icons/dislike_clicked.png'; 


    if (image.src.includes(originalSrc)) {
        image.src = newSrc; 
    } else {
        image.src = originalSrc; 
    }
}