import { useEffect } from "react";
import { useParams } from "react-router";

/** 
Service to get a single user from API.

Params:
    @param apiUrl = string - api Endpoint
    @param token = Auth token
    @param setSingleUser = function to set a single users
    @param setError = functions to set list of errors
    // @param heading = string - determines the type of view for our user list 
*/
const useGetSingleUser = (token, setSingleUser, setError) => {
    const userId = useParams();

    useEffect(() => {
    // const token = window.localStorage.getItem("token")
    if (!userId) {
      setError("UserID is required");
    }

    const apiUrl = process.env.REACT_APP_PROFILES_DETAIL_BASE_URL + userId.id;
    //"/profiles/%{userId}>"

    fetch(apiUrl, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
      .then((response) => response.json())
      .then((data) => console.log(data))
      
      .catch((error) => {
        setError(error);
      });
  }, []);
};

export default useGetSingleUser;
