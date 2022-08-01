let map;
var listt = document.getElementById("latlng");
var selectedvalue = [listt.selectedIndex].text;

function initMap(listworkouts) {
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


    /*var list = (document.getElementById("latlng").value).split('Row');
    alert(list)
    alert(list[1]);
    for (let x in list){
        alert(list[x]);
        newStr=(list[x].split(',')[3]).replace(')','')
        alert(newStr);


    }*/



    const marker = new google.maps.Marker({
        // The below line is equivalent to writing:
        // position: new google.maps.LatLng(-34.397, 150.644)

        position: {lat: 31.25633741620895, lng: 34.79312240575529},
        map: map,
    });

    const infowindow = new google.maps.InfoWindow({
        content: "<p>Marker Location:" + marker.getPosition() + "</p>",
        content: "יוגה בפארק!"
    });

    google.maps.event.addListener(marker, "click", () => {
        infowindow.open(map, marker);
    });


    const marker2 = new google.maps.Marker({
        // The below line is equivalent to writing:
        // position: new google.maps.LatLng(-34.397, 150.644)
        position: {lat: 31.261863139060313, lng: 34.80714633017435},
        map: map,
    });
    const infowindow2 = new google.maps.InfoWindow({
        content: "<p>Marker Location2:" + marker2.getPosition() + "</p>",
        content: "שחייה מתחילים"

    });

    google.maps.event.addListener(marker2, "click", () => {
        infowindow2.open(map, marker2);
    });

    const marker3 = new google.maps.Marker({
        // The below line is equivalent to writing:
        // position: new google.maps.LatLng(-34.397, 150.644)
        position: {lat: 31.258223688076885, lng: 34.79483186740401},
        map: map,
    });
    const infowindow3 = new google.maps.InfoWindow({
        content: "<p>Marker Location3:" + marker3.getPosition() + "</p>",
        content: "תחילת ריצה 3 קילומטר"
    });

    google.maps.event.addListener(marker3, "click", () => {
        infowindow3.open(map, marker3);
    });


}


window.initMap = initMap;

