import "./PrimaryButton.css";

const PrimaryButton = ({ text, onClick, bg }) => {
  /*
    Generic Button component.

    @Props: 
        - text: button text
        - onClick: function that runs event when the button is clicked
    */
  const bgColour = bg ? bg : ""
  return (
    <button
      className="primary-button secondary-background-colour primary-text-colour"
      data-cy="button-text-content"
      onClick={onClick}
      style={{backgroundColor: bg}}
    >
      {text}{" "}
    </button>
  );
};

export default PrimaryButton;
