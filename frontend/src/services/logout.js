const logout = (navigate) => {
  window.localStorage.removeItem("token");
  window.localStorage.removeItem("id");
  navigate("/users/home");
};

export default logout;
