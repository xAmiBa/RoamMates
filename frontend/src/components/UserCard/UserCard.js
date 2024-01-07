import "./UserCard.css"
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faGenderless, faVenus, faMars } from "@fortawesome/free-solid-svg-icons";

const UserCard = (props) => {

    /*
    Component to display UserCard on UserList view.
    Takes user in props.
    */
const goToUserDetail = () => {
    // TODO: Change user id to reflect data from database.
    props.navigate("/user/id/1")
}

const user = props.user
//TODO: Add link to the 'User Detail view"
    return(
        <div onClick={goToUserDetail} className="user-card">
            <div className="image-container">
                <img src="avatar.webp"/>
                <div className="user-info-left" data-cy="test-UserName-and-age" >
                {user.username} | {user.age}
                </div>
                <div className="user-info-right" data-cy="test-gender">
                    {user.gender === "Male" ? (
                        <FontAwesomeIcon icon={faMars} style={{ }}/>
                        ) : user.gender === "Female" ? (
                        <FontAwesomeIcon icon={faVenus} style={{ }}/>
                        ) : (
                        <FontAwesomeIcon icon={faGenderless} style={{ }}/>
                        )}
                </div>
            </div>
                {/* I'm deleting user bio as it will be too long to present on the card.
                It will be included in the profile */}
                {/* <p data-cy="test-bio">{user.bio}</p> */}
        </div>
    )
}

export default UserCard