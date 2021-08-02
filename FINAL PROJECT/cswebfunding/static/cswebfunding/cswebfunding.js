document.addEventListener('DOMContentLoaded', function () {

    // Image preview on newlising.html
    formFile.onchange = evt => {
        const [file] = formFile.files
        if (file) {
            output.src = URL.createObjectURL(file)
            output.hidden = false;
        }
    };
})


function addfunds () {

    // Get amount and set up for converting to decimal in backend
    amount = document.getElementById('amount').value.replace(",", ".");
    amount = parseFloat(amount);
    amount = parseFloat((amount.toFixed(2)));

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
                var balance = parseFloat(balanceHTML.innerHTML.replace('$', ''));
                var newbal = balance + amount;
                balanceHTML.innerHTML = `$${newbal}`;
            })
        }

    // User did not input any value to add to their balance
    } else { 
        console.error("no value");

        // Show error on modal
        modalmessage("You must specify a value!");
        
    }
};


function hidemodalmessage () {
    document.getElementById("modalmessagediv").hidden = true;
};


function modalmessage (message) {
    document.getElementById("modalmessagediv").hidden= false;
    document.getElementById("modalmessage").innerHTML = message;
};


function setdatelisting () {
    // Date to specify must be later than todays date for newlisting
    // Slightly edited from https://www.codegrepper.com/code-examples/html/datetime-local+min+today
    var today = new Date();
    var dd = today.getDate(); // Project must be open for at least a day
    var mm = today.getMonth()+1; //January is 0 so need to add 1 to make it 1!
    var yyyy = today.getFullYear();

    if(dd<10){
        dd='0'+dd
    } 
    if(mm<10){
        mm='0'+mm
    } 

    mindate = yyyy+'-'+mm+'-'+dd;
    maxdate = yyyy+5 +'-'+mm+'-'+dd;

    var element = document.getElementById("datefield");
    element.setAttribute("min", mindate);
    element.setAttribute("max", maxdate);

    console.log(`set min to ${mindate} and maxdate to ${maxdate}`)

};
