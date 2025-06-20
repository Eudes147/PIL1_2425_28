const bounds = L.latLngBounds(
      [4.9, 0.3],    // sud-ouest
      [8.0, 4.4]     // nord-est
    );

    const map = L.map('map', {
      center: [6.4178, 2.3400],  // Centre sur campus
      zoom: 15,                  // Zoom initial sur campus
      maxZoom: 18,               // Permet zoomer jusqu’à 18
      maxBounds: bounds,
      maxBoundsViscosity: 1.0
});


    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    // Cercle autour du campus d'Abomey-Calavi
    const campusCoords = [6.4178, 2.3400];
    L.circle(campusCoords, {
      radius: 1000,  // 1 km
      color: 'blue',
      fillColor: '#add8e6',
      fillOpacity: 0.3,
      interactive: false
    }).addTo(map).bindPopup("Campus UAC");

    let startMarker = null;
    let endMarker = null;
    let isSelectingStart = true;

    map.on('click', function(e) {
      if (isSelectingStart) {
        if (startMarker) startMarker.setLatLng(e.latlng);
        else startMarker = L.marker(e.latlng, { draggable: true }).addTo(map).bindPopup("Départ").openPopup();

        document.getElementById("start_lat").value = e.latlng.lat;
        document.getElementById("start_lng").value = e.latlng.lng;

        isSelectingStart = false;
        alert("Point de départ sélectionné. Cliquez maintenant pour choisir le point d'arrivée.");
      } else {
        if (endMarker) endMarker.setLatLng(e.latlng);
        else endMarker = L.marker(e.latlng, { draggable: true }).addTo(map).bindPopup("Arrivée").openPopup();

        document.getElementById("end_lat").value = e.latlng.lat;
        document.getElementById("end_lng").value = e.latlng.lng;

        isSelectingStart = true;
        alert("Trajet sélectionné. Vous pouvez maintenant valider.");
      }
    });