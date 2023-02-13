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
      input.fileLanguage.dataset.value = input.fileLanguage.value;
      input.fileCheckbox.addEventListener("click", function() {
        if (input.fileCheckbox.checked) {
          input.fileLanguage.value = "";
        } else {
          input.fileLanguage.value = input.fileLanguage.dataset.value;
        }
      });
    });
  });  


//   document.addEventListener('DOMContentLoaded', function() {
//     var file = document.querySelector("input[name='file']");
//     var fileLanguage = document.querySelector("input[name='fileLanguage']");
//     var fileCheckbox = document.querySelector("input[name='file-clear']");
//     var file2 = document.querySelector("input[name='file2']");
//     var file2Language = document.querySelector("input[name='file2Language']");
//     var file2Checkbox = document.querySelector("input[name='file2-clear']");
//     var file3 = document.querySelector("input[name='file3']");
//     var file3Language = document.querySelector("input[name='file3Language']");
//     var file3Checkbox = document.querySelector("input[name='file3-clear']");
//     var file4 = document.querySelector("input[name='file4']");
//     var file4Language = document.querySelector("input[name='file4Language']");
//     var file4Checkbox = document.querySelector("input[name='file4-clear']");

//     fileLanguage.dataset.value = fileLanguage.value;
//     file2Language.dataset.value = file2Language.value;
//     file3Language.dataset.value = file3Language.value;
//     file4Language.dataset.value = file4Language.value;


//     fileCheckbox.addEventListener("click", function() {
//       if (fileCheckbox.checked) {
//         fileLanguage.value = "";
//       } else {
//         fileLanguage.value = fileLanguage.dataset.value;
//       }
//     });

//     file2Checkbox.addEventListener("click", function() {
//       if (file2Checkbox.checked) {
//         file2Language.value = "";
//       } else {
//         file2Language.value = file2Language.dataset.value;
//       }
//     });

//     file3Checkbox.addEventListener("click", function() {
//       if (file3Checkbox.checked) {
//         file3Language.value = "";
//       } else {
//         file3Language.value = file3Language.dataset.value;
//       }
//     });
//     file4Checkbox.addEventListener("click", function() {
//       if (file4Checkbox.checked) {
//         file4Language.value = "";
//       } else {
//         file4Language.value = file4Language.dataset.value;
//       }
//     });
//   });  
