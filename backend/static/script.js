const searchInput = document.getElementById("searchInput");

searchInput.addEventListener("keyup", function () {

    const value = this.value.toLowerCase();

    const cards = document.querySelectorAll(".event-card");

    cards.forEach(card => {

        const text = card.innerText.toLowerCase();

        if (text.includes(value)) {
            card.style.display = "";
        } else {
            card.style.display = "none";
        }

    });

});