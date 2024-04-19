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
  document.getElementById("aaa").style.backgroundColor = "rgba(0,0,0,0.5)";
}

function closeNav() {
  document.getElementById("side-bar-cart").style.width = "0";
  document.getElementById("side-bar-cart").style.padding = "0";
  document.getElementById("aaa").style.backgroundColor = "unset";
}

function openlogIn() {
  document.getElementById("login-conteiner").style.opacity = "1";
  document.getElementById("login-conteiner").style.pointerEvents = "all";
}

function changeColor(color1){
  let elements = document.getElementsByClassName("product-color-size")

  switch (color1.className) {
    case "product-color product-color-size product-color-border":
      document.getElementById("product-price-id").innerHTML = "$1999.00"

      for (let i = 0; i < elements.length; i++) {
        elements[i].style.width = "36px";
        elements[i].style.height = "36px";
        elements[i].style.border = "solid 0px";
      }

      document.getElementsByClassName("product-color")[0].style.width = "40px";
      document.getElementsByClassName("product-color")[0].style.height = "40px";
      document.getElementsByClassName("product-color")[0].style.border = "solid 2px";
      break;

      case "product-color1 product-color-size product-color-border":
      document.getElementById("product-price-id").innerHTML = "$1700.00"

      for (let i = 0; i < elements.length; i++) {
        elements[i].style.width = "36px";
        elements[i].style.height = "36px";
        elements[i].style.border = "solid 0px";
      }

      document.getElementsByClassName("product-color1")[0].style.width = "40px";
      document.getElementsByClassName("product-color1")[0].style.height = "40px";
      document.getElementsByClassName("product-color1")[0].style.border = "solid 2px";
      break;

      case "product-color2 product-color-size product-color-border":
      document.getElementById("product-price-id").innerHTML = "$1850.00"

      for (let i = 0; i < elements.length; i++) {
        elements[i].style.width = "36px";
        elements[i].style.height = "36px";
        elements[i].style.border = "solid 0px";
      }

      document.getElementsByClassName("product-color2")[0].style.width = "40px";
      document.getElementsByClassName("product-color2")[0].style.height = "40px";
      document.getElementsByClassName("product-color2")[0].style.border = "solid 2px";
      break;

      case "product-color3 product-color-size product-color-border":
      document.getElementById("product-price-id").innerHTML = "$1500.00"

      for (let i = 0; i < elements.length; i++) {
        elements[i].style.width = "36px";
        elements[i].style.height = "36px";
        elements[i].style.border = "solid 0px";
      }

      document.getElementsByClassName("product-color3")[0].style.width = "40px";
      document.getElementsByClassName("product-color3")[0].style.height = "40px";
      document.getElementsByClassName("product-color3")[0].style.border = "solid 2px";
      break;

    default:
      break;
  }
}

function addItemToCart() {
  let cartNumber = document.getElementsByClassName("item-numbers-cart")[0].innerHTML;
  document.getElementsByClassName("item-numbers-cart")[0].innerHTML = parseInt(cartNumber) + 1;
}

function removeItem(item) {
  document.getElementById(item).style.display = "none";
}