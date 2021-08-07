// initialize hero draft counter and picked slot
var radiantCounter = 1;
var direCounter = 1;

var teamPicking = "radiant";

// pick a hero, display the hero on team draft,
// and make hero picked unavailable to pick again
function pickHero(img) {

  // check if radiant draft not pick 5 hero yet
  if (radiantCounter <= 5 || direCounter <= 5) {

    // check if radiant time to pick then pick for radiant
    // if dire time to pick then pick for dire team
    // default pick for radiant team
    if (teamPicking == "radiant")
    {
      console.log("Picked " + radiantCounter + " hero for radiant team.");
      console.log("Radiant slot available : " + (5-radiantCounter));

      // display picked hero
      document.getElementById("radiantHero"+radiantCounter).src = img.src;
      document.getElementById("radiantHero"+radiantCounter).alt = img.alt;
      // set picked hero as input value
      document.getElementById("inputRadiant"+radiantCounter).value = img.alt;

      radiantCounter += 1;
    }
    else if (teamPicking == "dire")
    {
      console.log("Picked " + direCounter + " hero for radiant team.");
      console.log("Radiant slot available : " + (5-direCounter));

      // display picked hero
      document.getElementById("direHero"+direCounter).src = img.src;
      document.getElementById("direHero"+direCounter).alt = img.alt;
      // set picked hero as input value
      document.getElementById("inputDire"+direCounter).value = img.alt;

      direCounter += 1;
    }

    // make hero picked unclickable and change hero img become empty picture
    img.style.pointerEvents = "none";
    img.src = "../static/images/empty.png";
  }
  else {
    alert("Tidak dapat memilih hero lebih dari 5 untuk setiap tim.")
  }
}

function setRadiantToPick() {
  teamPicking = "radiant";
}

function setDireToPick() {
  teamPicking = "dire";
}
