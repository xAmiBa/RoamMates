import { useState } from "react"
import'./UserList.css'
import UserCard from "../UserCard/UserCard"
import users from "../../constants/userList"
import SideBar from "../SideBar/SideBar"
import useGetUsers from "../../services/getusers"
import { useEffect } from "react"


const UserList = (props) => {
/*
Generic UserList component displaying list of users for home page, requests and matches routes.
Takes componentVersion in props ("home", "requests" or "matches") 

Children:
    - UserCard component
*/

// State that holds list of users.
// TODO: Change to empty list
    const [userList, setUserList] = useState([])
    const [error, setError] = useState(null)
    
    let apiUrl
// Variable to control version of the list of users. 
    const componentVersion = props.componentVersion
    
// Variable to set the page heading.
    let heading
    switch (componentVersion) {
        case 'home':
            heading="Find Your Roam Mates!"
            apiUrl=process.env.REACT_APP_USERS_PROFILES_URL
            break;
        case 'requests':
            heading="Requests"
            apiUrl=process.env.REACT_APP_REQUESTS_URL
            break;
        default: 
            heading="My Matches"
            apiUrl=process.env.REACT_APP_MATCHES_URL
            break;
    }
   useGetUsers(apiUrl, window.localStorage.getItem("token"), setUserList, setError, heading)

// TODO: Add API request to change state of the UserList.

    return(
        <>
        {error && <span>{error}</span>} 
        <div className="container primary-background-colour">
            <h1 className="primary-heading" id="page-header" data-cy="test-heading">{heading}</h1>
            <div id="home-user-list-container" className="user-list-container">
                {userList.map((user, index) => (
                    <UserCard key={index} user={user} navigate={props.navigate}></UserCard>
                ))}
                </div>
        </div>
        </>
    )
}

export default UserList