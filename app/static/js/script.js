document.getElementById("submit-btn").addEventListener("click", async () => {
    const userInput = document.getElementById("user-input").value;
    const outputDiv = document.getElementById("output");

    const response = await fetch("/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: userInput }),
    });

    const data = await response.json();
    if (data.response) {
        outputDiv.innerHTML = `<pre>${data.response}</pre>`;
    } else {
        outputDiv.innerHTML = "<p>Error processing your request.</p>";
    }
});
