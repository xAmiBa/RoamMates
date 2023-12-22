import { useState } from "react";
import "./FormField.css";

const FormField = (props) => {
  /*
    Reusable form field component.

    @props
        - input details: name, id, event handlers, etc..
    */

  const { id, label, onChange, errorMessage, ...inputProps } = props;

  const [focused, setFocused] = useState(false);
  const [isValid, setIsValid] = useState(true);

  // function to set input to focused afet it has been clicked but not filled.
  const handleFocus = (event) => {
    setFocused(true);
  };

  return (
    <div className="form-control">
      <label className="form-label" data-cy="form-label">
        {label}
      </label>
      <input
        {...inputProps}
        onChange={onChange}
        onBlur={handleFocus}
        // onFocus={()=> setFocused(true)}
        focused={focused.toString()}
      ></input>
      {focused === true && errorMessage && <span>{errorMessage}</span>}
    </div>
  );
};
export default FormField;
