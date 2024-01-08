import { useEffect } from "react";


/** 
Function to handle auth via api.

Params:
    @param apiUrl string - api Endpoint.

*/
const useGetUsers = (
    apiUrl, token, setUsers, setError
    ) => {
        console.log(apiUrl)
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
        }, [])
 
};

export default useGetUsers;
