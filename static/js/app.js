
let modelBox = document.getElementById("modelBox");

modelBox.onmousemove = function () {
    modelBox.style.display = "block";
  
}
function closeModel(){
  modelBox.style.display = "none";
}


// Set the target date and time for the countdown
const targetDate = new Date("2023-12-31T23:59:59").getTime();

// Update the countdown every second
const countdown = setInterval(function() {
    // Get the current date and time
    const currentDate = new Date().getTime();

    // Calculate the remaining time in milliseconds
    const remainingTime = targetDate - currentDate;

    // Check if the countdown has reached zero
    if (remainingTime <= 0) {
        clearInterval(countdown); // Stop the countdown
        document.getElementById("countdown").innerHTML = "Countdown expired!";
    } else {
        // Calculate the remaining days, hours, minutes, and seconds
        const days = Math.floor(remainingTime / (1000 * 60 * 60 * 24));
        const hours = Math.floor((remainingTime % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((remainingTime % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((remainingTime % (1000 * 60)) / 1000);

        // Display the countdown in the HTML element
        document.getElementById("countdown").innerHTML = `
            ${days}d:${hours}h:${minutes}m:${seconds}s
        `;
    }
}, 1000); // Update every 1000 milliseconds (1 second)


const myForm = document.getElementById("myForm");

// Add a submit event listener to the form
myForm.addEventListener("submit", function (event) {
    // Prevent the default form submission behavior
    event.preventDefault();

    // Your custom code here (e.g., handle form data, make an AJAX request)
});
