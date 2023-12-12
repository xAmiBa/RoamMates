import './Home.css'
import '../PrimaryButton/PrimaryButton'
import PrimaryButton from '../PrimaryButton/PrimaryButton'

const Home = ({navigate}) => {
    const navigateToLogin = () => {
        // TODO: Add navigation to login page
    }

    const navigateToSignUp = () => {
        // TODO: Add navigation to signup page
    }
    return (
    <div className="container">
        <h1 className='primary-heading'>Roam Mates</h1>
        <PrimaryButton text="Login" onClick={navigateToLogin}/>
        <PrimaryButton text="Sign Up" onClick={navigateToSignUp}/>
    </div>
    )
}
export default Home