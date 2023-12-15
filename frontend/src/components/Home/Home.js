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
    navigate("/users/login");
  };

  const navigateToSignUp = () => {
    navigate("/users/signup");
  };

  return (
    <div className="container primary-background-colour">
      <h1 className="primary-heading" data-cy="head-content">
        Roam Mates
      </h1>
      <p className="description">{descirpiotn}</p>
      <PrimaryButton text="Login" onClick={navigateToLogin} />
      <PrimaryButton text="Sign Up" onClick={navigateToSignUp} />
    </div>
  );
};
export default Home;
