import React from "react";
import LogoAnimation from "../LogoAnimation/LogoAnimation";
import "./SideBar.css"
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faHouse, faBell, faSuitcaseRolling, faGear, faRightFromBracket } from "@fortawesome/free-solid-svg-icons";
// run: npm i --save @fortawesome/fontawesome-svg-core
// run: npm i --save @fortawesome/free-solid-svg-icons
// run: npm i --save @fortawesome/react-fontawesome@latest


const SideBar = ({navigate}) => {
    const links = [
        {
            id:1,
            text:"Home",
            url: "/",
            icon: faHouse
        },
        {
            id:2,
            text:"Matches",
            url: "/matches",
            icon: faSuitcaseRolling
        },
        {
            id:3,
            text:"Requests",
            url: "/requests",
            icon: faBell
        },
        {
            id:4,
            text:"My Profile",
            url: "/myprofile",
            icon: faGear
        },
        {
            id:5,
            text:"Log Out",
            url: "#",
            icon: faRightFromBracket
        },
    ]

    return (
        <div className="side-bar" id="sidebar">
                <div className="logo">
                    <LogoAnimation width="60px"/>
                    <div className="logo-text">
                        Roam Mates
                    </div>
                </div>
            {links.map((link) => (

                <div className="side-bar-link">
                    {/* <i className={link.icon}/> */}
                    <a href={link.url} data-cy="button-text-content">
                    <FontAwesomeIcon icon={link.icon} style={{ marginRight: '15px' }}/>

                        {link.text}
                    </a>
                </div>
            ))}
            </div>

    )
}
export default SideBar