import { useState } from "react"
import'./UserList.css'
import UserCard from "../UserCard/UserCard"

const UserList = (props) => {
    /*
    1. Create setting values to control which version of UserList we want to display (/home, /request and /matches).
    2. Create the state to store UserList. 
    3. useEffect to get UserList from API, relevent to the version we want to display.
    4. Render users as list of UserCard components.
    */
    const [users, setUsers] = useState([])

    const componentVersion = props.componentVersion
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

    return(
        <div className="container primary-background-colour">
            <h1 className="primary-heading">{heading}</h1>
            <div className="user-list-container">
                <UserCard/>
                <UserCard/>
                <UserCard/>
                <UserCard/>
                <UserCard/>
                <UserCard/>
                <UserCard/>
                <UserCard/>
                <UserCard/>
            </div>
        </div>
    )
}

export default UserList