import { useState } from "react";
import handleLogin from "../../services/auth";
import FormField from "../FormField/FormField";
import PrimaryButton from "../PrimaryButton/PrimaryButton";
import "./LoginPage.css";
import "../app/App.css";

const LoginPage = ({ navigate }) => {
  /* Component to display login page.
    Children: 
        - FormField component
        - Primary Button component
    */

  //Prevents from visiting loggin page when already logged it.
  if (window.localStorage.getItem("token")) {
    navigate("/");
  }
  // Sets up and inputs ValueState
  const [values, setValues] = useState({
    email: "",
    password: "",
  });

  //Sets up state for errors returned from api when credentials are invalid.
  const [authError, setAuthError] = useState("");

  // List of objects representing FormField
  const form = [
    {
      id: 1,
      name: "email",
      type: "email",
      label: "Email",
      required: true,
      errorMessage: "Email should be a valid email.",
    },
    {
      id: 2,
      name: "password",
      type: "password",
      label: "Password",
      required: true,
      //pattern: `^(?=.*[0-9])(?=.*[a-zA-Z])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,20}$`,
      errorMessage:
        "Password should be 8-20 characters and include at least 1 letter, 1 number and 1 special character!",
    },
  ];

  // Function that handles input value changes
  const onChange = (event) => {
    setValues({ ...values, [event.target.name]: event.target.value });
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    // Get Api Url from env var.
    const apiAuthUrl = process.env.REACT_APP_AUTH_API_URL;
    handleLogin(
      `${apiAuthUrl}`,
      values.email,
      values.password,
      setAuthError,
      navigate,
    );
  };

  return (
    <div className="primary-container primary-background-colour">
      <h1 className="primary-heading" data-cy="login-heading" id="login-title">
        Login
      </h1>
      {authError && <p className="auth-error">{authError}</p>}
      <form onSubmit={handleSubmit}>
        {form.map((input) => (
          <FormField
            key={input.id}
            {...input}
            value={values[input.name]}
            onChange={onChange}
          />
        ))}
        <div className="button-container">
          <PrimaryButton text="Login" id="login-login-button" />
        </div>
        <p>
          <a href="/users/signup" id="login-signup-redirect">
            Don't have an account? Go to Sign Up.
          </a>
        </p>
      </form>
    </div>
  );
};

export default LoginPage;
