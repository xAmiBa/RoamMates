import PrimaryButton from "../PrimaryButton/PrimaryButton"
import setupPreferences from "../../services/setupPreferences";
import { useState } from "react";
import "../PreferencesForm/PreferencesFrom.css";


// Form works only when user chooses all preferences,
// otherwise useState should replace values with fetchedValues but it shows undefined.
// I think it might be async problem

const PreferencesForm = (fetchedValues) => {
    console.log("FETCHED VALUES", fetchedValues.preferences)

    // Sets up and inputs ValueState
    const [values, setValues] = useState({
        age_slot: fetchedValues.preferences.age_slot,
        gender: fetchedValues.preferences.gender,
        continent: fetchedValues.preferences.continent,
        season: fetchedValues.preferences.season,
        category: fetchedValues.preferences.category,
      });

    const [formError, setFormError] = useState("");

    const onChange = (event) => {
        console.log("CHANGE:", event.target.value, event.target.name)
        setValues({
          ...values,
          [event.target.name]: event.target.value === "" ? fetchedValues.preferences[event.target.name] : event.target.value,        });
      };

    const handleSubmit = async (event) => {
        event.preventDefault();
        console.log("SUBMITED VALUES", values)
        const apiPreferencesSetupUrl = process.env.REACT_APP_PREFERENCES_SETUP;
        setupPreferences(
            `${apiPreferencesSetupUrl}`,
            values.age_slot,
            values.gender,
            values.continent,
            values.season,
            values.category,
            setFormError,
        );
    };

    return (
        <div className="preference-settings-container">
                <form onSubmit={ handleSubmit }>

                    <div className="preference-age">
                        <label for="age_slot">Age</label>
                        <select 
                            id="age_slot" 
                            name="age_slot" 
                            onChange={onChange}
                            value={values.age_slot || fetchedValues.preferences.age_slot}
                        >
                            <option value="[18, 24]">18-24</option>
                            <option value="[25, 30]">25-30</option>
                            <option value="[30, 100]">30+</option>
                        </select>
                    </div>

                    <div className="preference-field-container">
                    <label for="gender">Gender</label>
                        <select 
                            id="gender" 
                            name="gender"
                            onChange={onChange}
                            value={values.gender || fetchedValues.preferences.gender}
                            >
                            <option value="male">Male</option>
                            <option value="female">Female</option>
                            <option value="other">Other</option>
                        </select>
                    </div><br/>

                    <div className="preference-field-container">
                        <label for="continent">Continent</label>
                        <select
                            id="continent" 
                            name="continent"
                            value={values.continent || fetchedValues.preferences.continent}
                            onChange={onChange}
                        >
                            <option value="Africa">Africa</option>
                            <option value="Antarctica">Antarctica</option>
                            <option value="Asia">Asia</option>
                            <option value="Europe">Europe</option>
                            <option value="North America">North America</option>
                            <option value="Oceania">Oceania</option>
                            <option value="South America">South America</option>
                        </select>
                    </div><br/>

                    <div className="preference-field-container">
                        <label for="season">Season</label>
                        <select 
                            id="season" 
                            name="season"
                            value={values.season || fetchedValues.preferences.season}
                            onChange={onChange}
                            >
                            <option value="spring">Spring</option>
                            <option value="summer">Summer</option>
                            <option value="autumn">Autumn</option>
                            <option value="winter">Winter</option>
                        </select>
                    </div><br/>

                    <div className="preference-field-container">
                        <label for="category">Category</label>
                        <select 
                            id="category" 
                            name="category"
                            value={values.category || fetchedValues.preferences.category}
                            onChange={onChange}
                        >
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