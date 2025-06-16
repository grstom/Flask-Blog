function Logon() {
    // get a user ID and session ID

    accountStatusMsg = document.getElementById("SignUpWarn")
    getUsername = document.getElementById("username").value;
    getPassword = document.getElementById("password").value;
    
    if (getUsername === "" || getPassword === "") {
        accountStatusMsg.innerHTML = "Username or password cannot be blank";
    } else {

        /////////////////////////////////                    

        // This always assumes that the
        // login is correct and
        // the function will run anyways, even if the user dosent exist. it will just fail at setting cookies
        // 
        // todo:
        // Tell user incorrect name/pw if the server returns so
        // ! Need to write function for displaying incorrect username and also on server to return that it is incorrect
        /////////////////////////////////


        accountStatusMsg.innerHTML = "Logging in...";
        accountStatusMsg.setAttribute("style", "visibility:visible")

        let username = document.getElementById("username").value;
        let password = document.getElementById("password").value;

        let xhr = new XMLHttpRequest();
        let submitUrl = "/logon";

        xhr.open("POST", submitUrl, true);
        xhr.setRequestHeader("Content-Type", "application/json");

        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                recievedLogon = JSON.parse(this.responseText);
                // console.log(recievedLogon.sessionid, recievedLogon.userid);
                
                sessionId = "sessionid=" + recievedLogon.sessionid;
                userId = "userid=" + recievedLogon.userid;
                accountUserStatus = recievedLogon.code;

                document.cookie = String(sessionId);
                document.cookie = String(userId);

                
                if (accountUserStatus === "200") {
                    window.location.replace("http://localhost:5000/")
                }
            }
        };

        let sentData = JSON.stringify({"username": username, "password": password});
        xhr.send(sentData);
    
    
    };
};


function Register() {

    // get a user ID and session ID

    accountStatusMsg = document.getElementById("SignUpWarn")
    getUsername = document.getElementById("username").value;
    getPassword = document.getElementById("password").value;
    getEmail = document.getElementById("email").value;
    
    if (getUsername === "" || getPassword === "" || getEmail == "") {
        accountStatusMsg.innerHTML = "Username, password, email cannot be blank";
    } else {

        accountStatusMsg.innerHTML = "Registering...";
        accountStatusMsg.setAttribute("style", "visibility:visible")

        // get a user ID and session ID

        let username = document.getElementById("username").value;
        let password = document.getElementById("password").value;
        let email = document.getElementById("email").value;


        let xhr = new XMLHttpRequest();
        let submitUrl = "/register";

        xhr.open("POST", submitUrl, true);
        xhr.setRequestHeader("Content-Type", "application/json");

        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                recievedLogon = JSON.parse(this.responseText);
                // console.log(recievedLogon.sessionid, recievedLogon.userid);
                
                sessionId = "sessionid=" + recievedLogon.sessionid;
                userId = "userid=" + recievedLogon.userid;
                accountServerStatus = recievedLogon.code;

                document.cookie = String(sessionId);
                document.cookie = String(userId);

                if (accountServerStatus === "500") {
                    accountStatusMsg.innerHTML = "The account username or email is already taken.";
                    accountStatusMsg.setAttribute("style", "visibility:visible")                    
                }
            
            }
        };

        let sentData = JSON.stringify({"username": username, "password": password, 'email': email});
        xhr.send(sentData);

    };
}