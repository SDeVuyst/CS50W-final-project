function addfunds () {
    console.log("Adding funds...");
    // Get amount and check for integer
    amount = parseInt(document.getElementById('amount').value);

    // Check for empty input
    // TODO: check for negative input
    if (amount) {
        console.log(amount)
        
        // Fetch to add balance to user
        fetch(`/addfunds/${amount}`)
        .then(response => response.json())
        .then(message => {
            console.log(message)
        })

        // Close the modal
        var modal = document.getElementById('fundsModal');
        modal.style.display = "none";

    } else {
        console.error("no value")
    }
}