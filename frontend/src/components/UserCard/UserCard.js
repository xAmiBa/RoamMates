import "./UserCard.css"

const UserCard = (props) => {

    /*
    Component to display UserCard on UserList view.
    Takes user in props.
    */
const goToUserDetail = () => {
    props.navigate("/userdetail")
}

const user = props.user
//TODO: Add link to the 'User Detail view"
    return(
        <div onClick={goToUserDetail} className="user-card shadow-effect">
            <span className="user-info primary-text-colour" data-cy="test-UserName">{user.username}</span>
            <div className="image-container">
                <img src="avatar.webp"/>
            </div>
            <div>
                <span className="user-info primary-text-colour" data-cy="test-age">{user.age}</span>
                <span className="user-info primary-text-colour" data-cy="test-gender">{user.gender}</span>
                <p data-cy="test-bio">{user.bio}</p>
            </div>
        </div>
    )
}

export default UserCard