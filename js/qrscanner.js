/*
To start scanning for a qrCode use the scanQrCode(element, callback) function
- element is a htmlelement that you want to put the qr scanner under
- callback is a function that returns the qr code after it has been read
  - Example function exampleCallback(code){...}

Have to include both scripts
    <script src="qrscanner.js"></script>
    <script src="libs/jsQR.js"></script>

Using https://github.com/cozmo/jsQR library for reading qr codes from image data

*/

scanQrCode = (function(element, callback){
  var canvas;
  var canvasElement;
  var video;
  var qrInput;
  var qrConfirm;
  var qrContainer;
  var qrButtonDiv;
  var qrConfirmed = false;
  var qrCallback = null;

  function confirmQr(){
    qrConfirmed = true;
    qrCallback(qrInput.value)
    qrContainer.parentNode.parentNode.removeChild(qrContainer.parentNode)
    video.srcObject.getTracks().forEach(track => track.stop())
    video.srcObjec = ""
  }

  function enterQrId(){
    qrInput.disabled = false;
    qrInput.focus();
    qrInput.style.background = '#deee';
  }

  function tick() {
    if (qrConfirmed){
      return
    }
    if (video.readyState === video.HAVE_ENOUGH_DATA) {
      canvasElement.hidden = false;

      canvasElement.height = video.videoHeight;
      canvasElement.width = video.videoWidth;
      qrInput.style.width = canvasElement.width + 'px';
      qrButtonDiv.style.width = canvasElement.width + 'px';
      qrContainer.style.height = canvasElement.height + 'px';
      qrButtonDiv.scrollIntoView();
      canvas.drawImage(video, 0, 0, canvasElement.width, canvasElement.height);
      var imageData = canvas.getImageData(0, 0, canvasElement.width, canvasElement.height);
      var code = jsQR(imageData.data, imageData.width, imageData.height, {
        inversionAttempts: "dontInvert",
      });
      if (code) {
          qrInput.value = code.data
          qrInput.size = code.data.length
          qrConfirm.style.visibility = 'visible'
      }
    }
    requestAnimationFrame(tick);
  }

  function setup(element){
    var textStuff = '<div>'
      +'<div id="qrcontainer" style="position:relative;width:100%;height:400px">'
        +'<canvas width="100%" height="400px" id="qrcanvas" style="display:block;"></canvas>'
        +'<textarea disabled id="qrinput" style="position:absolute;left:10px;top:150px;width:80%;height:200px;font-size:50pt;font-weight:bold;border:none;color:black;"></textarea>'
      +'</div>'
      +'<div id="qrButtonDiv">'
        +'<input id="qrconfirm" value="Confirm Code" type="button" style="visibility:hidden;">'
        +'<input id="qrenterid" value="Enter Id Manually" type="button" style="float:right;">'
      +'</div></div>'
    var template = document.createElement('template');
    template.innerHTML = textStuff.trim();
    element.parentNode.insertBefore(template.content.firstChild, element.nextSibling)

    qrContainer = document.getElementById('qrcontainer')
    qrButtonDiv = document.getElementById('qrButtonDiv')
    qrInput = document.getElementById('qrinput')
    canvasElement = document.getElementById('qrcanvas')
    qrConfirm = document.getElementById('qrconfirm')

    qrConfirm.addEventListener('click', confirmQr)
    document.getElementById('qrenterid', enterQrId)

    qrInput.style.background = 'transparent'

    video = document.createElement("video");
    canvas = canvasElement.getContext("2d");
  }


  function start(element, callback){
    setup(element)
    qrCallback = callback;
    //Use facingMode: environment to attemt to get the front camera on phones
    navigator.mediaDevices.getUserMedia({ video: { facingMode: "environment" } }).then(function(stream) {
      video.srcObject = stream;
      video.setAttribute("playsinline", true); // required to tell iOS safari we don't want fullscreen
      video.play();
      requestAnimationFrame(tick);
    });
  }
  start(element, callback);

});