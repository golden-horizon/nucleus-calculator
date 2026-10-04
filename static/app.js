const form = document.querySelector("#calculator-form");
const result = document.querySelector("#result");

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  result.classList.remove("error");
  result.textContent = "Calculating…";

  const formData = new FormData(form);
  const payload = Object.fromEntries(formData.entries());

  try {
    const response = await fetch("/api/calculate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.error || "Calculation failed.");
    }
    result.textContent = `Result: ${data.result}`;
  } catch (error) {
    result.classList.add("error");
    result.textContent = `Error: ${error.message}`;
  }
});
