/** 
Function to handle preferences change.

Params:
    @param apiUrl string - api Endpoint.
    @param age_slot string - age_slot value.
    @param gender string - password value.
    @param continent - string - continent value.
    @param season - string - season value.
    @param category - string - category value.
    @param setFormError - funct to change state of Error.

*/

const setupPreferences = async (apiUrl, age_slot, gender, continent, season, category, setFormError) => {
    const token = window.localStorage.getItem("token")
    let response = await fetch(apiUrl, {
        method: "put",
        headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({
            age_slot: age_slot,
            gender: gender,
            continent: continent,
            season: season,
            category: category
        })
    });

    if (response.status != 200) {
        setFormError("Something went wrong!")
    } else {
        const data = await response.json();
        window.localStorage.setItem("token", data.token);
        window.localStorage.setItem("id", data.user_id)
    }
}

export default setupPreferences;