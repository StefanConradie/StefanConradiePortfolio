// Konami code easter egg: ↑ ↑ ↓ ↓ ← → ← → B A
(function () {
  var input = "";
  var key = "38384040373937396665";
  document.addEventListener("keydown", function (e) {
    input += "" + e.keyCode;
    if (input === key) {
      window.location.href = "/happy";
      return;
    }
    if (!key.indexOf(input)) return;
    input = "" + e.keyCode;
  });
})();
