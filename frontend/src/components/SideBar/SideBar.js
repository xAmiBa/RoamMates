import React from "react";
import LogoAnimation from "../LogoAnimation/LogoAnimation";
import "./SideBar.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faHouse,
  faBell,
  faSuitcaseRolling,
  faGear,
  faRightFromBracket,
} from "@fortawesome/free-solid-svg-icons";
import logout from "../../services/logout";

const SideBar = ({ navigate }) => {
  /** 
  Siderbar component for navigation to Home, Matches, Requests, My Profile and Log Out pages.
  */
  const links = [
    {
      id: 1,
      text: "Home",
      onClick() {
        navigate("/");
      },
      icon: faHouse,
    },
    {
      id: 2,
      text: "Matches",
      onClick() {
        navigate("/matches");
      },
      icon: faSuitcaseRolling,
    },
    {
      id: 3,
      text: "Requests",
      onClick() {
        navigate("/requests");
      },
      icon: faBell,
    },
    {
      id: 4,
      text: "My Profile",
      onClick() {
        navigate("/myprofile");
      },
      icon: faGear,
    },
    {
      id: 5,
      text: "Log Out",
      onClick() {
        logout(navigate);
      },
      icon: faRightFromBracket,
    },
  ];

  return (
    <div className="side-bar" id="sidebar">
      <div className="logo">
        <LogoAnimation width="60px" />
        <div className="logo-text">Roam Mates</div>
      </div>
      {links.map((link) => (
        <div className="side-bar-link" key={link.id}>
          {/* <i className={link.icon}/> */}
          <a onClick={link.onClick} key={link.id}  data-cy="button-text-content">
            <FontAwesomeIcon key={link.id} icon={link.icon} style={{ marginRight: "15px" }}></FontAwesomeIcon>
            {link.text}
          </a>
        </div>
      ))}
    </div>
  );
};
export default SideBar;
