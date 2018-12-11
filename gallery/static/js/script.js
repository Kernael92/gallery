//Get the modal
var modal = document.getElementById('myModal');

// Get the image and insert it inside the modal - use its "alt" text as a caption
var img = document.getElementById('myImg');
var modalImg = document.getElementById("image.id");
var captionText = document.getElementById("caption");
img.onclick = function(){
  modal.style.display = "block";
  modalImg.src = this.src;
  captionText.innerHTML = this.div.caption;
}

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() { 
  modal.style.display = "none";
}

$('#clip_board').attr('data-clipboard-image', $(".copy_image").img())
window.onload = function(){
    var client = new ZeroClipboard(document.getElementsByClassName("copy-image") );
    client.on( "ready", function( readyEvent ) {
      client.on( "aftercopy", function( event ) {
        alert("Copied.." );
      });
    });
  }
