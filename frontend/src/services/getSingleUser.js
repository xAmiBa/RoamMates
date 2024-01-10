import { useEffect } from "react";

/** 
Service to get a single user from API.

Params:
    @param token = Auth token
    @param setSingleUser = function to set a single users
    @param setError = functions to set list of errors
*/
const useGetSingleUser = (token, setSingleUser, setError, userId) => {
  useEffect(() => {
    const apiUrl = process.env.REACT_APP_PROFILES_DETAIL_BASE_URL + userId;

    fetch(apiUrl, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
      .then((response) => response.json())
      .then((data) => setSingleUser(data))
      .catch((error) => {
        setError(error);
      });
  }, [userId]);
};

export default useGetSingleUser;
