import './PrimaryButton.css'

const PrimaryButton = ({text, onClick} ) => {
    /*
    Generic Button component.
    It takes props: 
        - text: button text
        - onClick: function that runs event when the button is clicked
    */
   
    return(
        <button
        className='primary-button secondary-background-colour primary-text-colour'
        data-cy="button-text-content"
        onClick={onClick} >{text} </button> 
        )
    }

    export default PrimaryButton