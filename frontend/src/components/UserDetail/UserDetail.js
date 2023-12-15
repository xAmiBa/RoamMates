import "../app/App.css"
import "../UserDetail/UserDetail.css"

const UserDetail = ({navigate}) => {
    return(
        <div className="container primary-background-colour ">
            <div className="row">
                <div className="col">
                    <div className="image-container">
                        <img src="avatar.webp"/>
                    </div>
                </div>
                <div className="col">
                    Bio
                </div>
            </div>
            <div className="row">
                Preferences
            </div>
        </div>
        
    )
}
export default UserDetail