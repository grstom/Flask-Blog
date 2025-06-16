function buttonPressed() {

    console.log('ok 1');
    let session = getCookie("sessionid");
    const text = document.getElementById("document").value;

    if (session !== "") {
        let xhr = new XMLHttpRequest();
        let postReq = "/post";

        xhr.open("POST", postReq, true);
        xhr.setRequestHeader("Content-Type", "application/json");

        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                console.log('ok 2');
                recievedStatusResponse = JSON.parse(this.responseText);

                postId = recievedStatusResponse.postid;
                console.log(postId);

                }
        }; 

    let SubmissionData = JSON.stringify({'postText': text, 'sessionId': session});
    xhr.send(SubmissionData);

    }

}