import "./Home.css";
import "../PrimaryButton/PrimaryButton";
import PrimaryButton from "../PrimaryButton/PrimaryButton";
import LogoAnimation from "../LogoAnimation/LogoAnimation";
import { descirpiotn, motto } from "../../constants/description";

const Home = ({ navigate }) => {
  /* 
  Component to display non-authenticated home page.
  Contains navigation to login and signup page.
  */

  const navigateToLogin = () => {
    navigate("/users/login");
  };

  const navigateToSignUp = () => {
    navigate("/users/signup");
  };

  return (
    <div className="container primary-background-colour">
      <LogoAnimation width="40%"/>
      <h1 className="primary-heading" data-cy="head-content" id="home-title">
        <spac className="first-word">Roam</spac>
        <br/>
        <spac className="second-word">mates.</spac>
      </h1>
      <p className="description" id="home-app-description">
        <spac>{motto} </spac> <br/>
        <spac>{descirpiotn}</spac>
      </p>
      <div className="primary-button-container">
        <PrimaryButton text="Login" onClick={navigateToLogin} id="home-login-button"/>
        <PrimaryButton text="Sign Up" onClick={navigateToSignUp} id="home-signup-button"/>
      </div>
    </div>
  );
};
export default Home;
