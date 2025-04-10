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