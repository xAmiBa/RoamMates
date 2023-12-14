import "./UserCard.css"

const UserCard = (props) => {

    /*
    Component to display UserCard on UserList view.
    Takes user in props.
    */
   
const user = props.user
//TODO: Add link to the 'User Detail view"
    return(
        <div className="user-card shadow-effect">
            <span className="user-info primary-text-colour">{user.username}</span>
            <div className="image-container">
                <img src="avatar.webp"/>
            </div>
            <div>
                <span className="user-info primary-text-colour">{user.age}</span>
                <span className="user-info primary-text-colour">{user.gender}</span>
                <p>{user.bio}</p>
            </div>
        </div>
    )
}

export default UserCard