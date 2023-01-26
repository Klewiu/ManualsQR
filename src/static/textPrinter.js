var i=0, text;
    text='ATS ASSEMBLE QR: Witaj ! Nie masz żadnych zleceń. Dodaj zlecenie aby odkryć kolejne funkcje ! Użyj przycisku + w menu.'

    function typing() {
      if (i<text.length){
        document.getElementById("text").innerHTML += text.charAt(i);
        i++;
        setTimeout(typing, 50);
        }
    }
    typing()