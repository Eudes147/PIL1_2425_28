
 function toggleMenu() {
      document.getElementById('mobile-menu').classList.toggle('hidden');
}
 
 // Fonction pour afficher ou masquer la section "Informations sur le véhicule"
function toggleVehicleSection(show) {
    const section = document.getElementById("vehicle-section");
    section.classList.toggle("hidden", !show);
    }

  // Initialisation de la carte avec Leaflet.js
  const map = L.map('map').setView([6.3703, 2.3912], 13); // Coordonnées par défaut (Cotonou)

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
  }).addTo(map);

  let marker;

  // Événement lors d'un clic sur la carte
  map.on('click', function (e) {
    const { lat, lng } = e.latlng;

    if (marker) {
      marker.setLatLng([lat, lng]);
    } else {
      marker = L.marker([lat, lng]).addTo(map);
    }

    // Remplir les champs cachés avec les coordonnées choisies
    document.getElementById('latitude').value = lat;
    document.getElementById('longitude').value = lng;
  });

document.getElementById('photo').addEventListener('change', function (e) {
  const file = e.target.files[0];
  const preview = document.getElementById('photo-preview');
  if (file) {
    const reader = new FileReader();
    reader.onload = function (evt) {
      preview.src = evt.target.result;
      preview.classList.remove('hidden');
    };
    reader.readAsDataURL(file);
  } else {
    preview.src = '';
    preview.classList.add('hidden');
  }
});