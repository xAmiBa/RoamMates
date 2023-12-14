import { useState } from "react"
import'./UserList.css'
import UserCard from "../UserCard/UserCard"
import users from "../../constants/userList"

const UserList = (props) => {
/*
Generic UserList component displaying list of users for home page, requests and matches routes.
Takes componentVersion in props ("home", "requests" or "matches") 

Children:
    - UserCard component
*/

// State that holds list of users.
// TODO: Change to empty list
    const [userList, setUserList] = useState(users)

// Variable to control version of the list of users. 
    const componentVersion = props.componentVersion
    
// Variable to set the page heading.
    let heading
    switch (componentVersion) {
        case 'home':
            heading="Find Your Roam Mates!"
            break;
        case 'requests':
            heading="Requests"
            break;
        default: 
            heading="My Matches"
            break;
    }

// TODO: Add API request to change state of the UserList.

    return(
        <div className="container primary-background-colour">
            <h1 className="primary-heading" data-cy="test-heading">{heading}</h1>
            <div className="user-list-container">
                {userList.map((user) => (
                    <UserCard user={user} navigate={props.navigate}></UserCard>
                ))}
                </div>
        </div>
    )
}

export default UserList