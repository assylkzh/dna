// slideBar
function openNav() {
  $("#Sidebar").css("width", "400px");
  $("#main").css("marginLeft", "400px");
}

function closeNav() {
  $("#Sidebar").css("width", "0");
  $("#main").css("marginLeft", "0");
}


//starting fade in 
var enteringImage = document.getElementById("start-img");
enteringImage.addEventListener("load", function() {
  enteringImage.style.opacity = "1";
});

//typing 
$(document).ready(function() {
  var textElement = $("h1");
  var text = "САРҚЫТҚА ҚОШ КЕЛДІҢІЗ!";
  var speed = 100;

  function typeWriter() {
    if (text.length > 0) {
      textElement.html(textElement.html() + text.charAt(0));
      text = text.slice(1);
      setTimeout(typeWriter, speed);
    }
  }

  typeWriter();
});


//mouseOver logo
function big(x) {
    x.style.height = "200px";
    x.style.width = "200px";
}
function normal(x) {
    x.style.height = "100px"
    x.style.width = "100px";
}

//keypress JQUERY 

$(document).ready(function() {
  $("#mark").keypress(function() {
    var text = "Сарқыт Жобасына баға бергеніңіз үшін алғыс білдіреміз!";
    var speed = 90;
    var index = 0;

    function typeWriter() {
      if (index < text.length) {
        var currentChar = text.charAt(index);
        $("#letter").text($("#letter").text() + currentChar);
        index++;
        setTimeout(typeWriter, speed);
      }
    }

    typeWriter();
  });
});

  //popups 
  function openPopupAssyl() {
    var popup = document.getElementById('popupAssyl');
    popup.style.display = 'block';
  }
  
  function closePopupAssyl() {
    var popup = document.getElementById('popupAssyl');
    popup.style.display = 'none';
  }

  function openPopupAssem() {
    var popup = document.getElementById('popupAssem');
    popup.style.display = 'block';
  }
  
  function closePopupAssem() {
    var popup = document.getElementById('popupAssem');
    popup.style.display = 'none';
  }

  function openPopupNurai() {
    var popup = document.getElementById('popupNurai');
    popup.style.display = 'block';
  }
  
  function closePopupNurai() {
    var popup = document.getElementById('popupNurai');
    popup.style.display = 'none';
  }

  function openPopupDilnaz() {
    var popup = document.getElementById('popupDilnaz');
    popup.style.display = 'block';
  }
  
  function closePopupDilnaz() {
    var popup = document.getElementById('popupDilnaz');
    popup.style.display = 'none';
  }

//Trigger a Button Click on Enter
var input = document.getElementById("myInput");
input.addEventListener("keypress", function(event) {
  if (event.key === "Enter") {
    event.preventDefault();
    document.getElementById("myBtn").click();
  }
});
