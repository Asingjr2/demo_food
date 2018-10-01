function initMap() {
  var display = new google.maps.DirectionsRenderer;
  var service = new google.maps.DirectionsService;
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom:15,
    center: {lat: 33.73, lng: -84.24},
    mapTypeControl: false
  });  
  display.setMap(map);
  display.setPanel(document.getElementById("right-panel"));

  var firstEvent = new google.maps.Marker({
    position: {lat: 33.733, lng: -84.24},
    map: map,
    title: 'Food Festival'
  });


  var control = document.getElementById("floating-panel");
  control.style.display = "block";

  map.controls[google.maps.ControlPosition.TOP_LEFT].push(control);

  var onChange = function(){
    calculateAndDisplay(service, display);
  }; 
  // document.getElementById("get-route").addEventListener("click", onChange)
  document.getElementById("start").addEventListener("change", onChange);
  document.getElementById("end").addEventListener("change", onChange);
}  

function calculateAndDisplay(service, display){
var start = document.getElementById("start").value;
var end = document.getElementById("end").value;
console.log(start.length);
console.log(end.length);
console.log("fetching route")
  service.route({
    origin: start, 
    destination: end,
    travelMode: "DRIVING"
  }, function(response, status){
    if (status === "OK"){
      display.setDirections(response);
    } else {
      window.alert("directions cannot be found " + status);
    }
  });
}
