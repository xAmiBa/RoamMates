import UserDetail from "../UserDetail/UserDetail";
import "../Settings/Settings.css"
import { useGetSingleUser } from "../../services/getSingleUser";
import { useState, useEffect } from "react";
import PrimaryButton from "../PrimaryButton/PrimaryButton";
import FormField from "../FormField/FormField";

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

    const onChange = (event) => {
        setValues({ ...values, [event.target.name]: event.target.value });
    };

    // const handleSubmit = async (event) => {
    //     event.preventDefault();
    //     const apiSingleUserDataUrl = process.env.REACT_APP_PREFERENCES_FOR_USER_ID;
    //     useGetSingleUser(
    //         window.localStorage.getItem("token"),
            
    //     )
    // };
    return (
        <div className="settings-container">
            <UserDetail navigate={navigate} />
            <div className="settings-form-container">
                <h2>My Settings</h2> <br/>
                <div className="profile-settings-container">
                    {/* TODO:  */}
                    <form onSubmit={useEffect}>
                        <div className="profile-bio">
                            <label for="bio">Bio</label>
                            <input type="text" id="bio" name ="bio"></input>
                            <input type="submit" value="submit"></input>
                        </div> <br/>

                    </form>
                </div>

                <div className="preference-settings-container">
                <form onSubmit={ useEffect }>

                    <div className="preference-age">
                        <label for="age_slot">Age</label>
                        <select id="age_slot" name="age_slot">
                            <option value="current-preference">{values.preferences.age_slot}</option>
                            <option value="[18, 24]">18-24</option>
                            <option value="[25, 30]">25-30</option>
                            <option value="[30, 100]">30+</option>
                        </select>
                    </div><br/>

                    <div className="preference-gender">
                    <label for="gender">Gender</label>
                        <select id="gender" name="gender">
                            <option value="current-preference">{values.preferences.gender}</option>
                            <option value="male">Male</option>
                            <option value="female">Female</option>
                            <option value="other">Other</option>
                        </select>
                    </div><br/>

                    <div className="prefernce-continent">
                        <label for="continent">Continent</label>
                        <select id="continent" name="continent">
                            <option value="current-preference">{values.preferences.continent}</option>
                            <option value="Africa">Africa</option>
                            <option value="Antarctica">Antarctica</option>
                            <option value="Asia">Asia</option>
                            <option value="Europe">Europe</option>
                            <option value="North America">North America</option>
                            <option value="Oceania">Oceania</option>
                            <option value="South America">South America</option>
                        </select>
                    </div><br/>

                    <div className="preference-season">
                        <label for="season">Season</label>
                        <select id="season" name="season">
                            <option value="current-preference">{values.preferences.season}</option>
                            <option value="spring">Spring</option>
                            <option value="summer">Summer</option>
                            <option value="autumn">Autumn</option>
                            <option value="winter">Winter</option>
                        </select>
                    </div><br/>

                    <div className="preference-category">
                        <label for="category">Category</label>
                        <select id="category" name="category">
                            <option value="current-preference">{values.preferences.category}</option>
                            <option value="mountains">Mountains</option>
                            <option value="beach">Beach</option>
                            <option value="resort">Resort</option>
                            <option value="city">City</option>
                            <option value="nature">Nature</option>
                            <option value="sport">Sport</option>
                        </select>
                    </div><br/>
                    <div className="button-container">
                        <PrimaryButton text="Set up new preferences" id="set-up-button" />
                    </div>
                
                </form>
                </div>

            </div>
        </div>
    )
}
export default Settings;