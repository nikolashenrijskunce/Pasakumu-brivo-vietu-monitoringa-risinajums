// Atrod meklersanas elementu pec id
const searchInput = document.getElementById("searchInput");

// funkcijas, kas veic meklesanu, kad kko ievada meklesana
searchInput.addEventListener("keyup", function ()
{
    // Parveido meklesana ievadito vertibu uz mazajiem burtiem
    const value = this.value.toLowerCase();

    // Atrod visus cards, kas veido notikumu sarakstu
    const cards = document.querySelectorAll(".event-card");

    // No katra card iegust taja esoso tekstu un to padara par neredzamu, ja neatbilst ierakstitajam meklesana
    cards.forEach(card => {
        const text = card.innerText.toLowerCase();
        if (text.includes(value))
        {
            card.style.display = "";
        }
        else
        {
            card.style.display = "none";
        }
    });
});