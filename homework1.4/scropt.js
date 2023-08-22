
let randomTextColor = document.querySelector(".color")
let score = document.querySelector(".span")
let start = document.querySelector(".startGame")
let arrowColors = ["red", "blue", "green", 'yellow']
// let colors = ["rgb(255, 0, 0)", "rgb(0, 0, 255)", "rgb(0, 255, 0)", "rgb(255, 255, 0)"]


let buttons = document.querySelectorAll(".buttons")
let counter = 0

for (let i = 0; i < buttons.length; i++) {
  buttons[i].addEventListener("click", function colorButtons(e) {
    let colors = window.getComputedStyle(e.target).backgroundColor


    if (colors === "rgb(255, 0, 0)") {
      if (randomTextColor.innerHTML === "red") {
        score.innerHTML = ++counter
        randomButtonColor()
      } else {
        score.innerHTML = --counter
        randomButtonColor()
      }
    } else if (colors === "rgb(0, 0, 255)") {
      if (randomTextColor.innerHTML === "blue") {
        score.innerHTML = ++counter
        randomButtonColor()
      } else {
        score.innerHTML = --counter
        randomButtonColor()
      }
    }  else if (colors === "rgb(0, 255, 0)") {
      if (randomTextColor.innerHTML === "green") {
        score.innerHTML = ++counter
        randomButtonColor()
      } else {
        score.innerHTML = --counter
        randomButtonColor()
      }
    }  else if (colors === "rgb(255, 255, 0)") {
      if (randomTextColor.innerHTML === "yellow") {
        score.innerHTML = ++counter
        randomButtonColor()
      } else {
        score.innerHTML = --counter
        randomButtonColor()
      }
    } 
    
  })
}
function randomButtonColor() {
  let random = Math.floor(Math.random() * arrowColors.length)
  randomTextColor.innerHTML = arrowColors[random]
}
start.addEventListener("click", function startGame() {
  randomButtonColor()
  for (let i = 0; i < buttons.length; i++) {
    buttons[i].disabled = false;
  }
})








