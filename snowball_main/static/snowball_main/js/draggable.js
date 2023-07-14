var elements = document.getElementsByClassName("snowball-window");
for (var i = 0; i < elements.length; i++) {
  var titleBar = elements[i].getElementsByClassName("title-bar")[0];
  dragElement(titleBar, elements[i]);
}

var docIcon = document.getElementById("docIcon");
if (docIcon != null) {
  docIcon.addEventListener("click", function () {
    window.location.href = "https://docs.snowballtools.xyz";
  });
  dragElement(docIcon, docIcon);
}

function dragElement(titleBar, elmnt) {
  var pos1 = 0,
    pos2 = 0,
    pos3 = 0,
    pos4 = 0;

  titleBar.onmousedown = dragMouseDown;

  function dragMouseDown(e) {
    e = e || window.event;
    e.preventDefault();

    pos3 = e.clientX;
    pos4 = e.clientY;

    document.onmouseup = closeDragElement;
    document.onmousemove = elementDrag;
  }

  function elementDrag(e) {
    e = e || window.event;
    e.preventDefault();

    pos1 = pos3 - e.clientX;
    pos2 = pos4 - e.clientY;
    pos3 = e.clientX;
    pos4 = e.clientY;

    elmnt.style.top = elmnt.offsetTop - pos2 + "px";
    elmnt.style.left = elmnt.offsetLeft - pos1 + "px";
  }

  function closeDragElement() {
    document.onmouseup = null;
    document.onmousemove = null;
  }
}
