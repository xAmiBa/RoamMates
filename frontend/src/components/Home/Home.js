import "./Home.css";
import "../PrimaryButton/PrimaryButton";
import PrimaryButton from "../PrimaryButton/PrimaryButton";

const Home = ({ navigate }) => {
  /* Component to display non-authenticated home page.
    Contains navigation to login and signup page.
    */

  const navigateToLogin = () => {
    navigate("/login");
  };

  const navigateToSignUp = () => {
    navigate("/signup");
  };

  return (
    <div className="container">
      <h1 className="primary-heading" data-cy="head-content">Roam Mates</h1>
      <PrimaryButton text="Login" onClick={navigateToLogin} />
      <PrimaryButton text="Sign Up" onClick={navigateToSignUp} />
    </div>
  );
};
export default Home;
