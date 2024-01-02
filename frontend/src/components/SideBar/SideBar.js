import React from "react";
import PrimaryButton from "../PrimaryButton/PrimaryButton";
import "./SideBar.css"


const SideBar = ({navigate}) => {
    const links = [
        {
            id:1,
            text:"Home",
            onClick(){
                navigate("/")
            }
        },
        {
            id:2,
            text:"Matches",
            onClick(){
                navigate("/matches")
            }
        },
        {
            id:3,
            text:"Requests",
            onClick(){
                navigate("/requests")
            }
        },
        {
            id:4,
            text:"My Profile",
            onClick(){
                navigate("/myprofile")
            }
        },
        {
            id:5,
            text:"Log Out",
            onClick(){
                navigate("#")
            }
        },
    ]

    return (
        <div className="side-bar primary-background-colour" id="sidebar">
            {links.map((link) => (
                <PrimaryButton 
                key={link.id}
                text={link.text}
                onClick={link.onClick}/>
            ))}

        </div>
    )
}
export default SideBar