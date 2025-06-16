function SignUp() {
  accountStatusMsg = document.getElementById("SignUpWarn")
  getUsername = document.getElementById("username").value;
  getPassword = document.getElementById("password").value;
  
  if (getUsername === "" || getPassword === "") {
    accountStatusMsg.innerHTML = "Username or password cannot be blank";
  } else {
    accountStatusMsg.innerHTML = "Success";
  }
}