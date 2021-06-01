
function scrollIntoView(eleID) {
  var e = document.getElementById(eleID);
  if (!!e && e.scrollIntoView) {
      e.scrollIntoView();
  }
}
function goToLastNode() {
  scrollIntoView("chatbox")
  sscroll('info')
  let elem = document.getElementById('chatlogs');
  elem.scrollTop = elem.scrollHeight;
}

function sscroll(id) {
  // (A) SCROLL PARAMETERS
  var speed = 10, // Less = faster
      step = 30, // Less = smoother but slower
      click = 0;
 
  // (B) GET CURRENT Y POSITION + TARGET Y POSITION
  var fromY = self.pageYOffset ? self.pageYOffset : document.body.scrollTop ;
  var target = document.getElementById(id);
  var toY = target.offsetTop;
  while (target.offsetParent && target.offsetParent != document.body) {
    target = target.offsetParent;
    toY += target.offsetTop;
  }
 
  // (C) SCROLL ANIMATION - DOWNWARDS
  if (fromY < toY) {
    for (var i=fromY; i<=toY; i+=step) {
      if (i+step > toY) {
        setTimeout("window.scrollTo(0, " + toY + ")", click * speed);
      } else {
        setTimeout("window.scrollTo(0, " + i + ")", click * speed);
      }
      click++;
    }
  }

  // (D) SCROLL ANIMATION - UPWARDS
  else {
    for (var i=fromY; i>=toY; i-=step) {
      if (i-step < toY) {
        setTimeout("window.scrollTo(0, " + toY + ")", click * speed);
      } else {
        setTimeout("window.scrollTo(0, " + i + ")", click * speed);
      }
      click++;
    }
  }
}
/*
1 -- extract zip to device// preferrably to desktop locatiom
2 -- open cmd
3 -- type cd desktop\software_test
4 -- type env\Scripts\activate.bat
5 -- type python app.py

*/
