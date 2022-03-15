let dt=document.getElementById('dt1')
let today = new Date().toLocaleDateString()
dt.innerHTML=today


console.log("file joined");

function ValidateEmailAddress(emailString) {
    // check for @ sign
    var atSymbol = emailString.indexOf("@");
    if(atSymbol < 1) return false;
    
    var dot = emailString.indexOf(".");
    if(dot <= atSymbol + 2) return false;
    
    // check that the dot is not at the end
    if (dot === emailString.length - 1) return false;
    
    return true;
}


function validateForm(){

    console.log("function called");

    let mobile=document.form1.mobile;
    let wmobile=document.form1.wmobile;
    let email=document.form1.email.value;
   

    console.log(mobile,wmobile,email);

    if(mobile.value.length != 10){
        alert("Please Enter valid mobile number")
        return false;
    }

    if(wmobile.value.length != 10){
        alert("Please Enter valid wmobile number")
        return false;
    }

    if(!ValidateEmailAddress(email)){
        alert("Please enter valid email id")
        return false;
    }
    return true;
}