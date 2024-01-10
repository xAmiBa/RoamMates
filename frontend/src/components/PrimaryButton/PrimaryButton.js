import "./PrimaryButton.css";

const PrimaryButton = ({ text, onClick, bg, disabled=false }) => {
  /*
    Generic Button component.

    @Props: 
        - text: button text
        - onClick: function that runs event when the button is clicked
        - bg: Custom background colour
        - disabled: boolean set to true if You want to diable button
    */
  const bgColour = bg ? bg : ""
  return (
    <button
      className="primary-button secondary-background-colour primary-text-colour"
      data-cy="button-text-content"
      onClick={onClick}
      style={{backgroundColor: bg}}
      disabled={disabled}
    >
      {text}{" "}
    </button>
  );
};

export default PrimaryButton;
