/**
 * Custom Hook to set preferences for User Detail page.
 * 
 * @param {userObj}  user
 * @param {function} setPrefAge
 * @param {function} setPrefGender
 * @param {function} setPrefDestination
 * @param {function} setPrefTime
 * @param {function} setPrefCat
 */
import { useEffect } from "react";

export const useSetPreferences = (
  user,
  setPrefAge,
  setPrefGender,
  setPrefDestination,
  setPrefTime,
  setPrefCat
) => {
  useEffect(() => {
    setPrefAge(user.profile.age);
    setPrefGender(user.profile.gender);
    setPrefDestination(user.preferences.continent);
    setPrefTime(user.preferences.season);
    setPrefCat(user.preferences.category);
  });
};
