var textbox = document.getElementsByClassName('textbox')[0];
textbox.onkeyup = function () {
  //here goes the python code
  if (this.value.length != 0) {
    $.ajax({
      type: 'GET',
      url: '/count/',
      data: {
        text: this.value,
      },
      success: function (json) {
        //success code goes here
        if (json.success) {
          document.getElementById('numOfWords').innerHTML = json.words;
          document.getElementById('numOfSentences').innerHTML = json.sentences;
          document.getElementById('numOfCharacters').innerHTML =
            json.characters;
          document.getElementById('numOfLines').innerHTML = json.lines;
          document.getElementById('numOfParagraphs').innerHTML =
            json.paragraphs;
          document.getElementById('readingTime').innerHTML = json.read_speed;
          document.getElementById('freq_word').innerHTML = json.most_occur;
        }
      },
    });
  } else {
    document.getElementById('numOfWords').innerHTML = 0;
    document.getElementById('numOfSentences').innerHTML = 0;
    document.getElementById('numOfCharacters').innerHTML = 0;
    document.getElementById('numOfParagraphs').innerHTML = 0;
    document.getElementById('numOfLines').innerHTML = 0;
    document.getElementById('readingTime').innerHTML = 0;
    document.getElementById('freq_word').innerHTML = '---';
  }
};
