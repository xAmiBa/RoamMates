import "./App.css";
import UserList from "../UserList/UserList";
import Home from "../Home/Home";
import LoginPage from "../LoginPage/LoginPage";
import SignUp from "../SignUp/SignUp";
import React from "react";
import { useNavigate, Routes, Route } from "react-router-dom";
import UserDetail from "../UserDetail/UserDetail";

import AuthLayout from "../AuthLayout/AuthLayout";
import Settings from "../Settings/Settings";

const App = () => {
  return (
    <div>
      <Routes>
        <Route
          path="/users/home"
          element={<Home navigate={useNavigate()} />}
        ></Route>
        <Route
          path="users/login"
          element={<LoginPage navigate={useNavigate()} />}
        ></Route>
        <Route
          path="users/signup"
          element={<SignUp navigate={useNavigate()} />}
        ></Route>

        <Route path="/" element={<AuthLayout navigate={useNavigate()} />}>
          <Route
            path=""
            element={
              <UserList navigate={useNavigate()} componentVersion="home" />
            }
          ></Route>
          <Route
            path="/matches"
            element={
              <UserList navigate={useNavigate()} componentVersion="matches" />
            }
          ></Route>
          <Route
            path="/requests"
            element={
              <UserList navigate={useNavigate()} componentVersion="requests" />
            }
          ></Route>
          {/* TODO: Add userID URL param */}
          <Route
            path="/user/id/:id"
            element={<UserDetail navigate={useNavigate()} />}
          ></Route>
          <Route
            path="/myprofile"
            element={<Settings navigate={useNavigate()} />}
          ></Route>
        </Route>
      </Routes>
    </div>
  );
};

export default App;
