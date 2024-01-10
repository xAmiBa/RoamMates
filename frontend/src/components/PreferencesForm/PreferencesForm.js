import PrimaryButton from "../PrimaryButton/PrimaryButton"
import setupPreferences from "../../services/setupPreferences";
import { useState } from "react";

const PreferencesForm = (fetchedValues) => {

    

    // Sets up and inputs ValueState
    const [values, setValues] = useState({
        age_slot: "",
        gender: "",
        continent: "",
        season: "",
        category: "",
    });

    const onChange = (event) => {
        setValues({ ...values, [event.target.name]: event.target.value });
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        const apiPreferencesSetup = process.env.REACT_APP_PREFERENCES_SETUP;
    };

    return (
        <div className="preference-settings-container">
                <form onSubmit={ handleSubmit }>

                    <div className="preference-age">
                        <label for="age_slot">Age</label>
                        <select id="age_slot" name="age_slot">
                            <option value="current-preference">{fetchedValues.preferences.age_slot}</option>
                            <option value="[18, 24]">18-24</option>
                            <option value="[25, 30]">25-30</option>
                            <option value="[30, 100]">30+</option>
                        </select>
                    </div><br/>

                    <div className="preference-gender">
                    <label for="gender">Gender</label>
                        <select id="gender" name="gender">
                            <option value="current-preference">{fetchedValues.preferences.gender}</option>
                            <option value="male">Male</option>
                            <option value="female">Female</option>
                            <option value="other">Other</option>
                        </select>
                    </div><br/>

                    <div className="prefernce-continent">
                        <label for="continent">Continent</label>
                        <select id="continent" name="continent">
                            <option value="current-preference">{fetchedValues.preferences.continent}</option>
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
                            <option value="current-preference">{fetchedValues.preferences.season}</option>
                            <option value="spring">Spring</option>
                            <option value="summer">Summer</option>
                            <option value="autumn">Autumn</option>
                            <option value="winter">Winter</option>
                        </select>
                    </div><br/>

                    <div className="preference-category">
                        <label for="category">Category</label>
                        <select id="category" name="category">
                            <option value="current-preference">{fetchedValues.preferences.category}</option>
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
    )
}

export default PreferencesForm;