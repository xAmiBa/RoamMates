/** 
Function to handle new user creation via api.

Params:
    @param apiUrl string - api Endpoint.
    @param username string - username value.
    @param email string - email value.
    @param password string - password value.
    @param setSignupError - funct to change state of Error.
    @param navigate - navigation.
*/

const handleSignup = async (
  apiUrl,
  username,
  email,
  password,
  setSignupError,
  navigate,
) => {
  let response = await fetch(apiUrl, {
    method: "post",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      email: email,
      username: username,
      password: password,
    }),
  });

  if (response.status !== 200) {
    setSignupError("Email already exists.");
  } else {
    const data = await response.json();
    navigate("../users/login");
  }
};

export default handleSignup;
