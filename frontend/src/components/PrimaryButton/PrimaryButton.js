import './PrimaryButton.css'

const PrimaryButton = ({text, onClick} ) => {
    return(
        <button
        className='primary-button secondary-background-colour primary-text-colour'
        onClick={onClick} >{text} </button> 
        )
    }

    export default PrimaryButton