let map;
function initMap() {
    map = new google.maps.Map(document.getElementById("map2"), {
        zoom: 15,
        center: new google.maps.LatLng(31.2573952, 34.8028928),
        mapTypeId: "terrain",
    });

    // Create a <script> tag and set the USGS URL as the source.
    const script = document.createElement("script");

    // This example uses a local copy of the GeoJSON stored at
    // http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.geojsonp
    script.src =
        "https://developers.google.com/maps/documentation/javascript/examples/json/earthquake_GeoJSONP.js";
    document.getElementsByTagName("head")[0].appendChild(script);



    // google.maps.event.addListener(marker, 'ddd', mylatlng);


    const marker = new google.maps.Marker({

        // The below line is equivalent to writing:
        // position: new google.maps.LatLng(-34.397, 150.644)
        draggable: true,
        animation: google.maps.Animation.DROP,
        position: {lat: 31.2573952, lng: 34.8028928},
        map: map,
    });
    var lat1 = document.getElementById("lat").value;
    var lng2 = document.getElementById("lng").value;
    var mylatlng = new google.maps.LatLng(lat1, lng2);
    marker.setPosition(mylatlng);
    map.panTo(mylatlng);

    const infowindow = new google.maps.InfoWindow({
        content: "<p>Marker Location:" + marker.getPosition() + "</p>",
        content: document.getElementById("desc").value
    });

    google.maps.event.addListener(marker, "click", () => {
        infowindow.open(map, marker);
    });


    var latlng = new google.maps.LatLng(lat1, lng2);
    // This is making the Geocode request
    var geocoder = new google.maps.Geocoder();
    geocoder.geocode({ 'latLng': latlng },  (results, status) =>{
        if (status !== google.maps.GeocoderStatus.OK) {
            alert(status);
        }
        // This is checking to see if the Geoeode Status is OK before proceeding
        if (status == google.maps.GeocoderStatus.OK) {
            console.log(results);
            var address = (results[0].formatted_address);
            document.getElementById("add").value=address;

        }
    });



}

// Loop through the results array and place a marker for each
// set of coordinates.
const eqfeed_callback = function (results) {
    for (let i = 0; i < results.features.length; i++) {
        const coords = results.features[i].geometry.coordinates;
        const latLng = new google.maps.LatLng(coords[1], coords[0]);
        google.maps.event.addListener(map, 'click', function (event) {
            placeMarker(event.latLng);
        });
        new google.maps.Marker({
            position: latLng,
            map: map,
        });
    }
};

window.initMap = initMap;
window.eqfeed_callback = eqfeed_callback;

function placeMarker(location) {
    var marker = new google.maps.Marker({
        position: location,
        map: map,
    });
    var infowindow = new google.maps.InfoWindow({
        content: 'Latitude: ' + location.lat() + '<br>Longitude: ' + location.lng()
    });
    infowindow.open(map, marker);
}

