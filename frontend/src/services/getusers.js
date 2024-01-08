import { useEffect } from "react";

/** 
Service to get list of users from API.

Params:
    @param apiUrl = string - api Endpoint
    @param token = Auth token
    @param setUsers = functions to set list of users
    @param setError = functions to set list of errors
    @param heading = string - determines the type of view for our user list 
*/
const useGetUsers = (
    apiUrl, token, setUsers, setError, heading
    ) => {
        useEffect(()=>{
            // const token = window.localStorage.getItem("token")
            fetch(apiUrl,
            {
                headers: {
                    'Authorization': `Bearer ${token}`
                }
            })
            .then(response => response.json())
            .then(data => setUsers(data.users))
            .catch((error) => {
                setError(error)
            })
        }, [heading])
 
};

export default useGetUsers;
