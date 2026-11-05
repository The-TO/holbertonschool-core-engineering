const socket = new WebSocket("ws://localhost:8000/ws");

const form = document.getElementById("message-form");
const input = document.getElementById("message-input");
const messages = document.getElementById("messages");

function addMessage(text) {
    const item = document.createElement("li");
    item.textContent = text;
    messages.appendChild(item);
}

socket.onmessage = (event) => {
    addMessage(event.data);
};

form.addEventListener("submit", (event) => {
    event.preventDefault();
    if (input.value === "") {
        return;
    }
    socket.send(input.value);
    input.value = "";
});