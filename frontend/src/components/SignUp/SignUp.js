import { useState } from "react";
import PrimaryButton from "../PrimaryButton/PrimaryButton";
import FormField from "../FormField/FormField";
import "../app/App.css";
import handleSignup from "../../services/signup";

const SignUp = ({ navigate }) => {
  /* Component to display Sign Up page.

    Children: 
        - FormField component
        - Primary Button component
    */

  // Sets up and inputs ValueState
  const [values, setValues] = useState({
    email: "",
    password: "",
    confirmPassword: "",
    username: "",
  });

  //Sets up state for errors returned from api when credentials are invalid.
  const [signupError, setSignupError] = useState("");

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
      pattern: `^(?=.*[0-9])(?=.*[a-zA-Z])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,20}$`,
      errorMessage:
        "Password should be 8-20 characters and include at least 1 letter, 1 number and 1 special character!",
    },
    {
      id: 3,
      name: "confirmPassword",
      type: "password",
      label: "Confirm Password",
      required: true,
      errorMessage: "Passwords don't match!",
      pattern: values.password,
    },
    {
      id: 4,
      name: "username",
      type: "text",
      label: "Username",
      required: true,
      errorMessage: "Username needs to be at least 6 characters long!",
      minLength: "6",
    },
  ];

  // Function that handles input value changes
  const onChange = (event) => {
    setValues({ ...values, [event.target.name]: event.target.value });
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    // Get Api Url from env var.
    const apiAddUserUrl = process.env.REACT_APP_ADD_USER_API_URL;
    handleSignup(
      `${apiAddUserUrl}`,
      values.username,
      values.email,
      values.password,
      setSignupError,
      navigate,
    );
  };

  return (
    <div className="primary-container primary-background-colour">
      <h1
        className="primary-heading"
        data-cy="signup-heading"
        id="signup-title"
      >
        Sign Up
      </h1>
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
          <PrimaryButton text="Sign Up" dataTestId="signup-signup-button"/>
        </div>
        <p>
          <a href="/users/login" id="signup-login-redirect">
            Already have an account? Go to Log In.
          </a>
        </p>
      </form>
    </div>
  );
};
export default SignUp;
