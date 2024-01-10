import { Outlet } from "react-router";
import SideBar from "../SideBar/SideBar";

const AuthLayout = ({ navigate }) => {
  /*
  Component to set the layout for all authenticated views.
  
  @Children:
    - Sidebar 
   */

  return (
    <>
      <SideBar navigate={navigate} />
      <Outlet />
    </>
  );
};
export default AuthLayout;
