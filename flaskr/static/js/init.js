$(document).ready(function(){
  $('.parallax').parallax();
});

$(document).ready(function(){
    $('.carousel').carousel();
  });
$(document).ready(function(){
    $('.dropdown-trigger').dropdown({ hover: false });
  });


(function() {
  if('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
      navigator.serviceWorker.register('/sw.js')
               .then(function(registration) {
               console.log('Service Worker Registered');
               return registration;
      })
      .catch(function(err) {
        console.error('Unable to register service worker.', err);
      });
      navigator.serviceWorker.ready.then(function(registration) {
        console.log('Service Worker Ready');
      });
    });
  }
})();
