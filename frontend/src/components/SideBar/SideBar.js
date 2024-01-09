import React from "react";
import PrimaryButton from "../PrimaryButton/PrimaryButton";
import "./SideBar.css";
import logout from "../../services/logout";

/*
Siderbar component for navigation to Home, Matches, Requests, My Profile and Log Out pages.
*/

const SideBar = ({ navigate }) => {
  const links = [
    {
      id: 1,
      text: "Home",
      onClick() {
        navigate("/");
      },
    },
    {
      id: 2,
      text: "Matches",
      onClick() {
        navigate("/matches");
      },
    },
    {
      id: 3,
      text: "Requests",
      onClick() {
        navigate("/requests");
      },
    },
    {
      id: 4,
      text: "My Profile",
      onClick() {
        navigate("/myprofile");
      },
    },
    {
      id: 5,
      text: "Log Out",
      onClick() {
        logout(navigate);
      },
    },
  ];

  return (
    <div className="side-bar primary-background-colour" id="sidebar">
      {links.map((link) => (
        <PrimaryButton key={link.id} text={link.text} onClick={link.onClick} />
      ))}
    </div>
  );
};
export default SideBar;
