import { Outlet, Navigate } from "react-router";

const NonAuthLayout = () => {
  /**
   * Component to set Non Auth Layout pages.
   * At the moment it checks if user is authenticated and redirects
   * to ***Auth Home page*** when token is present.
   */
  const token = window.localStorage.getItem("token");

  return token ? <Navigate to="/" /> : <Outlet />;
};
export default NonAuthLayout;
