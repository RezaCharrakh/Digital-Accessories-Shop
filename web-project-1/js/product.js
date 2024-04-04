function openTab(evt, tabName) {
    // Declare all variables
    var i, tabcontent, tablinks;

    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tab-content");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }

    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("more-details-button");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(tabName).style.display = "block";
    if(evt) evt.currentTarget.className += " active";
    else document.querySelector('button.more-details-button').className += " active";

    // document.getElementById(tabName).style.display = "block";
    // evt.currentTarget.className += " active";
  }
  document.body.addEventListener('DOMContentLoaded', openTab(event, 'description-text-container'));


function openNav() {
  document.getElementById("side-bar-cart").style.width = "352px";
  document.getElementById("side-bar-cart").style.padding = "20px";
}

function closeNav() {
  document.getElementById("side-bar-cart").style.width = "0";
  document.getElementById("side-bar-cart").style.padding = "0";
}