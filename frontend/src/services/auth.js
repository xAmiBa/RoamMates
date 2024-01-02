/** 
Function to handle auth via api.

Params:
    @param apiUrl string - api Endpoint.
    @param email string - email value.
    @param password string - password value.
    @param setAuthError - funct to change state of Error.
    @param navigate - navigation.
*/
const handleLogin = async (
    apiUrl, email, password, setAuthError, navigate
    ) => {

  let response = await fetch(apiUrl, {
    method: "post",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ email: email, password: password }),
  });

  if (response.status != 200) {
    setAuthError("Email or Password is wrong.");
  } else {
    const data = await response.json();
    window.localStorage.setItem("token", data.token);
    navigate("/");
  }
};

export default handleLogin;
