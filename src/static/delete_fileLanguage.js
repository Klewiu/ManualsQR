document.addEventListener('DOMContentLoaded', function() {
  var fileInputs = [
    {
      file: document.querySelector("input[name='file']"),
      fileLanguage: document.querySelector("input[name='fileLanguage']"),
      fileCheckbox: document.querySelector("input[name='file-clear']"),
    },
    {
      file: document.querySelector("input[name='file2']"),
      fileLanguage: document.querySelector("input[name='file2Language']"),
      fileCheckbox: document.querySelector("input[name='file2-clear']"),
    },
    {
      file: document.querySelector("input[name='file3']"),
      fileLanguage: document.querySelector("input[name='file3Language']"),
      fileCheckbox: document.querySelector("input[name='file3-clear']"),
    },
    {
      file: document.querySelector("input[name='file4']"),
      fileLanguage: document.querySelector("input[name='file4Language']"),
      fileCheckbox: document.querySelector("input[name='file4-clear']"),
    },
  ];

  fileInputs.forEach(function(input) {
    if (input.fileCheckbox !== null) { // Add a null check for fileCheckbox
      input.fileLanguage.dataset.value = input.fileLanguage.value;
      input.fileCheckbox.addEventListener("click", function() {
        if (input.fileCheckbox.checked) {
          input.fileLanguage.value = "";
        } else {
          input.fileLanguage.value = input.fileLanguage.dataset.value;
        }
      });
    }
  });
});