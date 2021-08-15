document.addEventListener('DOMContentLoaded', function () {

    // dynamically change preview on input of new listing
    var titleform = document.getElementById("titleform");
    var descriptionform = document.getElementById("descriptionform");
    var goalform = document.getElementById("goalform");
    var dateform = document.getElementById("dateform");

        // Title
        titleform.oninput = evt => {
            var title = document.getElementById("newlistingtitle");
            title.innerHTML = titleform.value;
        }

        // Description
        descriptionform.oninput = evt => {
            var description = document.getElementById("newlistingdescription");
            description.innerHTML = descriptionform.value;
        }

        // Goal
        goalform.oninput = evt => {
            var goal = document.getElementById("newlistinggoal");
            goal.innerHTML = goalform.value;
        }

        // Date
        dateform.oninput = evt => {
            var date = document.getElementById("newlistingdate");

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
            date.innerHTML = `${mindate} - ${dateform.value}`;
        }

        // Photo
        formFile.onchange = evt => {
            const [file] = formFile.files
            if (file) {
                output.src = URL.createObjectURL(file)
            }
        };  
    
    // This if for donation modal, to check if user confirms the donation
    var clicked
});


function addfunds () {

    // Get amount and set up for converting to decimal in backend
    amount = document.getElementById('amount').value.replace(",", ".");
    amount = parseFloat(amount);
    amount = parseFloat((amount.toFixed(2)));

    if (amount) {
        
        // Check if input is positive
        if (Math.sign(amount) === -1) {

            console.error("User input is negative");
            // Show error on modal
            modalmessage("Input must be positive.")

            
        } else if (amount > 100000) {
            console.error("User input is larger than 100000")
            modalmessage("Input must be smaller than 100000")
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
                var balance = parseFloat(balanceHTML.innerHTML.replace('$', '').replace('Current balance: ', ''));
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

    var element = document.getElementById("dateform");
    element.setAttribute("min", mindate);
    element.setAttribute("max", maxdate);

    console.log(`set min to ${mindate} and maxdate to ${maxdate}`)

};

function checkexceedsgoal (goal, donated) {

    // user clicked confirmation button, and wants to donate extra
    if (clicked == 'confirm') {
        console.log("confirmed")
        clicked = 'not confirmed'
        return true;
    }

    const togo = goal - donated;

    donateinput = document.getElementById('donateamount').value;
    var donatemodalmessagediv = document.getElementById("donatemodalmessagediv")
    var donatemodalmessage = document.getElementById("donatemodalmessage")

    // Listing already reached its goal
    if (togo < 0) {

        donatemodalmessagediv.hidden = false;
        donatemodalmessage.innerHTML = "Listing has already completed it's goal. Are you sure you want to donate extra?";

        return false;

    // User wants to donate more than listings goal
    } else if (donateinput > togo) {

        donatemodalmessagediv.hidden = false;
        donatemodalmessage.innerHTML = "You will exceed the requested goal. Are you sure you want to donate extra?";

        return false;
    
    // Normal donation, form can be submitted
    } else {
        return true;
    }

}


function submitcommentform () {
    var form = document.getElementById("commentform");

    // Comment cannot be empty
    if (form.checkValidity()) {
        form.submit();
    } else {
        // Comment is empty, display error
        console.error('Comment cannot be empty');
        document.getElementById("emptycommentalert").hidden = false;
    }
}