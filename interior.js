// popover
var popoverTriggerList = $('[data-bs-toggle="popover"]');
var popoverList = popoverTriggerList.map(function() {
  return new bootstrap.Popover($(this)[0]);
});


// slideBar
function openNav() {
  $("#Sidebar").css("width", "400px");
  $("#main").css("marginLeft", "400px");
}

function closeNav() {
  $("#Sidebar").css("width", "0");
  $("#main").css("marginLeft", "0");
}

//entering fade in 
// var enteringImage = document.getElementById("entering");
// enteringImage.addEventListener("load", function() {
//   enteringImage.style.opacity = "1";
// });

// music
var audio = $("#music")[0];
var playButton = $("#playButton");
var playIcon = $("#playIcon");

function play() {
  if (audio.paused) {
    audio.play();
    playIcon.removeClass("fa-circle-play");
    playIcon.addClass("fa-circle-pause");
  } else {
    audio.pause();
    playIcon.removeClass("fa-circle-pause");
    playIcon.addClass("fa-circle-play");
  }
}


//animations 
//rows
window.addEventListener("scroll", reveal);
function reveal(){
  var reveals = $(".row");
  for(var i=0; i<reveals.length; i++){
    var windowHeight=window.innerHeight;
    var revealTop=reveals[i].getBoundingClientRect().top;
    var revealpoint=150;

    if(revealTop<windowHeight-revealpoint)
    reveals[i].classList.add("active");
    else reveals[i].classList.remove("active");
  }

}

//counter 
var countDownDate = new Date("June 20, 2023 12:00:00").getTime();

var countdownfunction = setInterval(function() {

  var now = new Date().getTime();
  var distance = countDownDate - now;
  
  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);
  
  document.getElementById("demo").innerHTML = days + "d " + hours + "h "
  + minutes + "m " + seconds + "s ";
  
  if (distance < 0) {
    clearInterval(countdownfunction);
    document.getElementById("demo").innerHTML = "EXPIRED";
  }
}, 1000);

