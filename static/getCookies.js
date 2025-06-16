//Get cookies here
function getCookie(name) {
    let cookies = document.cookie.split('; ');
    for (let cookie of cookies) {
        let [key, value] = cookie.split('=');
        if (key === name) {
            return decodeURIComponent(value);
        }
    }
    return "";
}



//This works for the navbar when getting a user ID
//It should've been put somewhere else, but oh well
function getUser() {
    let user = getCookie("userid")
    console.log('ok 1');

    if (user !== "") {
        console.log('ok 2')
        let xhrRequest = new XMLHttpRequest();
        let lookupUrl = '/lookup';
        
        xhrRequest.open("POST", lookupUrl, true);
        xhrRequest.setRequestHeader("Content-Type", "application/json");

        console.log('ok 3');
        xhrRequest.onreadystatechange = function () {
            if (xhrRequest.readyState === 4 && xhrRequest.status === 200) {
                recievedUserInfo = JSON.parse(this.responseText);
                
                username = recievedUserInfo.userId;
                document.getElementById("username").innerHTML = username;

                // if we're on the homepage, just hide the register and sign up
                const signup = document.getElementById("signup");
                const signin = document.getElementById("signin");

                signup.remove();
                signin.remove();

            }
        };

        let getInformation = JSON.stringify({"userId": user});
        xhrRequest.send(getInformation);

    } else {
        console.log('User not found or is not logged on');

        //remove the 'My blog' button
        const myblog = document.getElementById('blog');
        const postButton = document.getElementById('post');
        myblog.remove();
        postButton.remove();

    };
}