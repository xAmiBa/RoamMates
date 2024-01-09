import "./UserCard.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faGenderless,
  faVenus,
  faMars,
} from "@fortawesome/free-solid-svg-icons";
import Flip from "react-reveal/Flip";

const UserCard = (props) => {
  /*
    Component to display UserCard on UserList view.
    Takes user in props.
    */

  const user = props.user;

  const goToUserDetail = () => {
    // TODO: Change user id to reflect data from database.
    props.navigate(`/user/${user.user_id}`);
  };

  

  return (
    <Flip left>
      <div onClick={goToUserDetail} className="user-card">
        <div className="image-container">
          <img src={user.picture} />
          <div className="user-info-left" data-cy="test-UserName-and-age">
            {user.name} | {user.age}
          </div>
          <div className="user-info-right" data-cy="test-gender">
            {user.gender === "Male" ? (
              <FontAwesomeIcon icon={faMars} style={{}} />
            ) : user.gender === "Female" ? (
              <FontAwesomeIcon icon={faVenus} style={{}} />
            ) : (
              <FontAwesomeIcon icon={faGenderless} style={{}} />
            )}
          </div>
        </div>
      </div>
    </Flip>
  );
};

export default UserCard;
