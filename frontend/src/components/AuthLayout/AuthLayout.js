import { Navigate, Outlet } from "react-router";
import SideBar from "../SideBar/SideBar";

const AuthLayout = ({ navigate }) => {
  /*
  Component to set the layout for all authenticated views.
  If the user is not authenticated, navigates to **"users/home"**.
  
  @Children:
    - Sidebar 
   */

  const token = window.localStorage.getItem("token");

  return token ? (
    <>
      <SideBar navigate={navigate} />
      <Outlet />
    </>
  ) : (
    <Navigate to="/users/home" />
  );
};
export default AuthLayout;
