import { useState } from "react";
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

  // Sets up and inputs ValueState
  const [values, setValues] = useState({
    email: "",
    password: "",
  });

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
  ];

  // Function that handles input value changes
  const onChange = (event) => {
    setValues({ ...values, [event.target.name]: event.target.value });
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    // TODO: Send data to the backend.
  };

  return (
    <div className="container primary-background-colour">
      <h1 className="primary-heading" data-cy="login-heading">
        Login
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
          <PrimaryButton text="Login" />
        </div>
        <p>
          <a href="/users/signup" id="login-signup-redirect">Don't have an account? Go to Sign Up.</a>
        </p>
      </form>
    </div>
  );
};

export default LoginPage;
