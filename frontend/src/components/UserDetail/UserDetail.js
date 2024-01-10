import "../app/App.css";
import "../UserDetail/UserDetail.css";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faEarthEurope } from "@fortawesome/free-solid-svg-icons";
import { faCakeCandles } from "@fortawesome/free-solid-svg-icons";
import { faCloudSunRain } from "@fortawesome/free-solid-svg-icons";
import { faUmbrellaBeach } from "@fortawesome/free-solid-svg-icons";
import { faVenusMars } from "@fortawesome/free-solid-svg-icons";

import { useState } from "react";

import useGetSingleUser from "../../services/getSingleUser";
import { useSetPreferences } from "../../hooks/useSetPreferences";

const UserDetail = ({ navigate }) => {
  /*
Component to store single user details. 
Displays user information and travel preferences. 
*/

  // State to store user details.
  const [user, setUser] = useState({
    preferences: {},
    profile: {},
    user_request_status: "",
  });
  const [error, setError] = useState(null);

  //States to hold preferences details
  const [prefAge, setPrefAge] = useState(0);
  const [prefGender, setPrefGender] = useState("");
  const [prefDestination, setPrefDestination] = useState("");
  const [prefTime, setPrefTime] = useState("");
  const [prefCat, setPrefCat] = useState("");

  //Get User data from service
  useGetSingleUser(window.localStorage.getItem("token"), setUser, setError);
  
  //Set preferences from custom hook
  useSetPreferences(
    user,
    setPrefAge,
    setPrefGender,
    setPrefDestination,
    setPrefTime,
    setPrefCat
  );
  const preferences = [
    {
      icon: faCakeCandles,
      preferenceText: "Age",
      preferenceValue: prefAge,
    },
    {
      icon: faVenusMars,
      preferenceText: "Gender",
      preferenceValue: prefGender,
    },
    {
      icon: faEarthEurope,
      preferenceText: "Travel Destination",
      preferenceValue: prefDestination,
    },
    {
      icon: faCloudSunRain,
      preferenceText: "Time Of Travel",
      preferenceValue: prefTime,
    },
    {
      icon: faUmbrellaBeach,
      preferenceText: "Holiday Category",
      preferenceValue: prefCat,
    },
  ];

  return (
    <div className="profile-detail">
      <div className="profile-detail-container primary-background-colour">
        <div className="row">
          <h1 className="secondary-heading">Hi, I'm {user.profile.name}!</h1>
        </div>
        <div className="row">
          <div className="col">
            <div className="image-container-profile">
              <img src={user.profile.picture} />
            </div>
          </div>
          <div className="col">
            <div className="row bio-container">
              {/* TODO: customizable component to accept / reject / none */}
            </div>
            <div className="row bio-container">{user.profile.bio}</div>
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
