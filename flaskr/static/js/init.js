$(document).ready(function(){
  $('.parallax').parallax();
});

$(document).ready(function(){
    $('.carousel').carousel();
  });
$(document).ready(function(){
    $('.dropdown-trigger').dropdown({ hover: false });
  });


 if ('serviceWorker' in navigator) {
  navigator.serviceWorker
    .register("../sw.js", {scope: '/'})
    .then(registration => {
      console.log("ServiceWorker running");
    })
    .catch(err => {
       console.log(err);
    })
}
