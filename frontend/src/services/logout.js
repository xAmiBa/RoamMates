const logout = (navigate) => {
  window.localStorage.removeItem("token");
  navigate("/users/home");
};

export default logout;
