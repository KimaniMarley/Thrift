window.onload = function(
    ) {
// Function to create the popup table content
function createPopupTableContent(markers) {
    let tableContent = "<table><thead><tr><th>Name</th><th>Type</th></tr></thead><tbody>";
    for (const marker of markers) {
        tableContent += `<tr><td>${marker.getPopup().getContent()}</td><td>${marker.options.icon.options.icon}</td></tr>`;
    }
    tableContent += "</tbody></table>";
    return tableContent;
}

// Function to handle map click
map_304a31f02f75758aecbf8bca8e890e7e.on('click', function(e) {
    // Calculate the buffer zone
    const buffer = turf.buffer(e.latlng, 5, { units: 'kilometers' });

    // Get markers within the buffer zone
    const markersInBuffer = [];
    health_group.eachLayer(marker => {
        if (turf.booleanPointInPolygon(marker.getLatLng(), buffer)) {
            markersInBuffer.push(marker);
        }
    });
    school_group.eachLayer(marker => {
        if (turf.booleanPointInPolygon(marker.getLatLng(), buffer)) {
            markersInBuffer.push(marker);
        }
    });

    // Update the popup table content
    const popupTable = document.getElementById('popup-table');
    popupTable.innerHTML = createPopupTableContent(markersInBuffer);
    popupTable.style.display = 'block'; // Show the popup table
});
};