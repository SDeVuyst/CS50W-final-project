
function addfunds () {

    // Get amount and set up for converting to decimal in backend
    amount = document.getElementById('amount').value.replace(",", ".");
    console.log(amount)
    if (amount) {
        // Check if input is number
        if (isNaN(amount)) {
            console.error("User input must be a number!");
            modalmessage("Input must be a number.")

        // Check if input is positive
        } else if (Math.sign(amount) === -1) {

            console.error("User input is negative");
            // Show error on modal
            modalmessage("Input must be positive.")
            
        } else {

            // Fetch to add balance to user
            fetch(`/addfunds/${amount}`)
            .then(response => response.json())
            .then(message => {
                console.log(message);

                // Close the modal
                var myModalEl = document.getElementById('fundsModal');
                var modal = bootstrap.Modal.getInstance(myModalEl); // Returns a Bootstrap modal instance
                modal.hide()

                // Asynchronously add balance for user
                var balanceHTML = document.getElementById("balance");
                var balance = parseFloat(balanceHTML.innerHTML);
                balanceHTML.innerHTML = (balance + parseFloat(amount)).toFixed(2);
            })
        }

    // User did not input any value to add to their balance
    } else { 
        console.error("no value");

        // Show error on modal
        modalmessage("You must specify a value!");
        
    }
}


function hidemodalmessage () {
    document.getElementById("modalmessagediv").hidden = true;
}


function modalmessage (message) {
    document.getElementById("modalmessagediv").hidden= false;
    document.getElementById("modalmessage").innerHTML = message;
}