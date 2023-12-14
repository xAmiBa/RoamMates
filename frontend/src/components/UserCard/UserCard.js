import "./UserCard.css"

const UserCard = () => {
    return(
        <div className="user-card shadow-effect">
            <div className="image-container">
                <img src="avatar.webp"/>
            </div>
            <div>
                <span className="user-info primary-text-colour">User Name</span>
                <span className="user-info primary-text-colour">Age</span>
                <span className="user-info primary-text-colour">Gender</span>
                <p>Bio</p>
            </div>
        </div>
    )
}

export default UserCard