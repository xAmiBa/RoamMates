import UserDetail from "../UserDetail/UserDetail";
import "../Settings/Settings.css"
import { useGetSingleUser } from "../../services/getSingleUser";
import { useState, useEffect } from "react";
import PrimaryButton from "../PrimaryButton/PrimaryButton";
import PreferencesForm from "../PreferencesForm/PreferencesForm";

const Settings = ({ navigate }) => {
    // Sets up and inputs ValueState
    const [values, setValues] = useState({
        preferences: {},
        profile: {},
        user_request_status: "",
    });
    const [setError, setAuthError] = useState("");
    const userId = window.localStorage.getItem("id")
    const token = window.localStorage.getItem("token")
        
    useEffect(() => {
        const apiUrl = process.env.REACT_APP_PROFILES_DETAIL_BASE_URL + userId;
    
        fetch(apiUrl, {
            headers: {
            Authorization: `Bearer ${token}`,
            },
        })
            .then((response) => response.json())
            .then((data) => setValues(data))
            .catch((error) => {
            setAuthError(error);
            });
        }, [userId]);

    
    return (
        <div className="settings-container">
            <UserDetail navigate={navigate} />
            <div className="settings-form-container">
                <h2>My Settings</h2> <br/>
                <div className="profile-settings-container">
                    {/* TODO:  */}
                </div>
                <PreferencesForm {...values} {...setValues}/>
                

            </div>
        </div>
    )
}
export default Settings;