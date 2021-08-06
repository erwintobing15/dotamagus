// initialize hero draft counter
var radiantCounter = 0;
var direCounter = 0;

// pick a hero, display the hero on team draft
function pickHero(img) {
  radiantCounter += 1;

  // check if radiant draft not pick 5 hero yet
  if (radiantCounter <= 5) {
    console.log("Picked " + radiantCounter + " hero for radiant team.");
    // display picked hero
    document.getElementById("imgRadiant"+radiantCounter).src = img.src;
    // assign picked hero as input value
    document.getElementById("inputRadiant"+radiantCounter).value = img.alt;

    // make hero picked unclickable and change hero img become empty picture
    img.style.pointerEvents = "none";
    img.src = "../static/images/empty.png";
  }
  else {
    alert("Tidak dapat memilih hero lebih dari 5")
  }
}
