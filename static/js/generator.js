const promptInput = document.getElementById("creative_prompt");
const charCount = document.getElementById("charCount");
const lyricsForm = document.getElementById("lyricsForm");

promptInput.addEventListener("input", function () {

    const length = this.value.length;

    charCount.textContent = `${length} / 3000`;

});


lyricsForm.addEventListener("submit", function (event) {

    const prompt = promptInput.value.trim();

    if (prompt.length < 20) {

        event.preventDefault();

        alert("Please enter at least 20 characters describing your song.");

        promptInput.focus();

        return;

    }

});

function copyLyrics() {

    const lyrics = document.getElementById(
        "generatedLyrics"
    );

    navigator.clipboard.writeText(lyrics.value)
        .then(() => {
            alert("Lyrics copied successfully!");
        });

}


function downloadLyrics() {

    const lyrics = document.getElementById(
        "generatedLyrics"
    ).value;

    const blob = new Blob(
        [lyrics],
        { type: "text/plain;charset=utf-8" }
    );

    const url = URL.createObjectURL(blob);

    const link = document.createElement("a");

    link.href = url;
    link.download = "MelodyVerse_Lyrics.txt";

    link.click();

    URL.revokeObjectURL(url);

}

lyricsForm.addEventListener("submit", function () {

    const button = document.getElementById("generateBtn");

    const text = document.getElementById("generateText");

    button.disabled = true;

    text.innerHTML = "Creating your masterpiece...";

});