import React from "react";
import LogoAnimation from "../LogoAnimation/LogoAnimation";
import "./SideBar.css"

const SideBar = ({navigate}) => {
    const links = [
        {
            id:1,
            text:"Home",
            url: "/",
            icon: ""
        },
        {
            id:2,
            text:"Matches",
            url: "/matches",
            icon: ""
        },
        {
            id:3,
            text:"Requests",
            url: "/requests",
            icon: ""
        },
        {
            id:4,
            text:"My Profile",
            url: "/",
            icon: "/myprofile"
        },
        {
            id:5,
            text:"Log Out",
            url: "#",
            icon: ""
        },
    ]

    return (
        <div className="side-bar" id="sidebar">
                <div className="logo-image">
                    <LogoAnimation width="60px"/>
                    <div className="logo-text">
                        Roam Mates
                    </div>
                </div>
            {links.map((link) => (
                    <a href={link.url}>
                        {link.text}
                    </a>
            ))}
            </div>

    )
}
export default SideBar