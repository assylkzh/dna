let quotes = [
    {
      text: "Үш-ақ нәрсе адамның қасиеті: Ыстық қайрат, Нұрлы ақыл, Жылы жүрек.",
      author: "Абай Құнанбаев",
      photo: "abai.jpg"
    },
    {
      text: "Кітап аяулы досы бола бастаған шақтан былай ғана әрбір жан өзін интеллигент бола бастадым деп санауына болады.",
      author: "Мұхтар Әуезов",
      photo: "auezov.jpg"
    },
    {
      text: "Ең зиянды адам - мінезі тайғақ, екі сөйлейтін адам. Мейірім, ынсап, ақ пейіл, адал еңбек - осы төртеуі кімнің бойында болса - сол шын адам болады.",
      author: "Шәкәрім Құдайбердіұлы",
      photo: "shakarim.jpg"
    },
    {
        text: "Бақыттың мәні — парасаттылықта, әркімнің өз алдында игілікті мақсат қоя білуінде... адамның өз мінез-құлқын , іс-әрекетін ерікті түрде өзгертіп, игілікке бағаттап отыруында.",
        author: "Әл-Фараби",
        photo: "al-farabi.jpg"
      },
      {
        text: "Ерлік, қайрат үнемі ірі жұмыста көріне бермей, күндегі уақ-түйек жұмыста да көрінуі керек.",
        author: "Жүсіпбек Аймауытов",
        photo: "aimautov.jpg"
      },
  ];
  
  function getRandomIndex(max) {
    return Math.floor(Math.random() * max);
  }
  
  function generateRandomQuote() {
    let randomIndex = getRandomIndex(quotes.length);
    let quote = quotes[randomIndex];
  
    let quoteTextElement = document.getElementById("quote-text");
    quoteTextElement.textContent = quote.text;
  
    let quoteAuthorElement = document.getElementById("quote-author");
    quoteAuthorElement.textContent = quote.author;
  
    let quotePhotoElement = document.getElementById("quote-photo");
    quotePhotoElement.setAttribute("src", quote.photo);
  }
  
  generateRandomQuote();



  var i = 0;
    function move() {
      if (i == 0) {
        i = 1;
        var elem = document.getElementById("myBar");
        var width = 10;
        var id = setInterval(frame, 10);
        function frame() {
          if (width >= 100) {
            clearInterval(id);
            i = 0;
          } else {
            width++;
            elem.style.width = width + "%";
            elem.innerHTML = width  + "%";
          }
        }
      }
    }