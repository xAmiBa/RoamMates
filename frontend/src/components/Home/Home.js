import "./Home.css";
import "../PrimaryButton/PrimaryButton";
import PrimaryButton from "../PrimaryButton/PrimaryButton";
import { descirpiotn } from "../../constants/description";

const Home = ({ navigate }) => {
  /* 
  Component to display non-authenticated home page.
  Contains navigation to login and signup page.
  */

  const navigateToLogin = () => {
    navigate("/login");
  };

  const navigateToSignUp = () => {
    navigate("/signup");
  };

  return (
    <div className="container primary-background-colour">
      <h1 className="primary-heading" data-cy="head-content" id="home-title">
        Roam Mates
      </h1>
      <p className="description" id="home-app-description">{descirpiotn}</p>
      <PrimaryButton text="Login" onClick={navigateToLogin} id="home-login-button"/>
      <PrimaryButton text="Sign Up" onClick={navigateToSignUp} id="home-signup-button"/>
    </div>
  );
};
export default Home;
