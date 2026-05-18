// MEKLESANAS FUNKCIJA
document.addEventListener("DOMContentLoaded", function () {

// Atrod meklersanas elementu pec id
    const searchInput = document.getElementById("searchInput");

// funkcijas, kas veic meklesanu, kad kko ievada meklesana
    searchInput.addEventListener("keyup", function () {
        // Parveido meklesana ievadito vertibu uz mazajiem burtiem
        const value = this.value.toLowerCase();

        // Atrod visus cards, kas veido notikumu sarakstu
        const rows = document.querySelectorAll(".event-row");

        // No katra card iegust taja esoso tekstu un to padara par neredzamu, ja neatbilst ierakstitajam meklesana
        rows.forEach(row => {
            const text = row.innerText.toLowerCase();
            if (text.includes(value)) {
                row.style.display = "";
            } else {
                row.style.display = "none";
            }
        });
    });
});



// KOLONNU KARTOSANAS FUNKCIJA
function sortTable(columnIndex) {

    const table = document.querySelector("table tbody");
    const rows = Array.from(table.querySelectorAll("tr"));
    const sortedRows = rows.sort((a, b) => {

        let aText = a.children[columnIndex].innerText.trim();
        let bText = b.children[columnIndex].innerText.trim();

        // Remove euro symbol and commas
        aText = aText.replace("€", "").replace(",", "");
        bText = bText.replace("€", "").replace(",", "");

        // Numeric sorting
        if (!isNaN(aText) && !isNaN(bText))
        {
            return Number(aText) - Number(bText);
        }

        if (columnIndex === 1)
        {
            const aDate = new Date(aText);
            const bDate = new Date(bText);
            return aDate - bDate;
        }

        // Text sorting
        return aText.localeCompare(bText);
    });
    // Re-add rows
    rows.forEach(row => row.remove());
    sortedRows.forEach(row => {table.appendChild(row);});
}