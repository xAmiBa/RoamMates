import "../app/App.css";
import "../UserDetail/UserDetail.css";
import mockUser from "../../constants/mockUser";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faEarthEurope } from "@fortawesome/free-solid-svg-icons";
import { faCakeCandles } from "@fortawesome/free-solid-svg-icons";
import { faCloudSunRain } from "@fortawesome/free-solid-svg-icons";
import { faUmbrellaBeach } from "@fortawesome/free-solid-svg-icons";
import { faVenusMars } from "@fortawesome/free-solid-svg-icons";
import {
  faGenderless,
  faVenus,
  faMars,
} from "@fortawesome/free-solid-svg-icons";

import { useState } from "react";

const UserDetail = ({ navigate }) => {
  /*
Component to store single user details. 
Displays user information and travel preferences. 
*/

  // State to store user details.
  const [user, setUser] = useState(mockUser);

  const preferences = [
    {
      icon: faCakeCandles,
      preferenceText: "Age",
      preferenceValue: 28,
    },
    {
      icon: faVenusMars,
      preferenceText: "Gender",
      preferenceValue: "Male",
    },
    {
      icon: faEarthEurope,
      preferenceText: "Travel Destination",
      preferenceValue: "Europe",
    },
    {
      icon: faCloudSunRain,
      preferenceText: "Time Of Travel",
      preferenceValue: "Spring",
    },
    {
      icon: faUmbrellaBeach,
      preferenceText: "Holiday Category",
      preferenceValue: "City Break",
    },
  ];

  // TODO: Write fetch function to get user data.
  return (
    <div className="profile-detail">
      <div className="profile-detail-container primary-background-colour">
        <div className="row">
          <h1 className="secondary-heading">Hi, I'm {user.userName}!</h1>
        </div>
        <div className="row">
          <div className="col">
            <div className="image-container-profile">
              <img src="avatar.webp" />
            </div>
          </div>
          <div className="col">
            <div className="row bio-container">
              {/* TODO: customizable component to accept / reject / none */}
            </div>
            <div className="row bio-container">{user.bio}</div>
          </div>
        </div>

        <div className="row preferences-container">
          {preferences.map((preference) => (
            <div className="icon-container">
              <span className="icon-wrapper">
                <FontAwesomeIcon icon={preference.icon} size="2xl" />
              </span>
              <br />
              <span className="preference-text">
                {preference.preferenceText}:
              </span>
              <br />
              <span className="preference-value">
                {preference.preferenceValue}
              </span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
export default UserDetail;
