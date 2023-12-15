import "./App.css";
import UserList from "../UserList/UserList";
import Home from "../Home/Home";
import LoginPage from "../LoginPage/LoginPage";
import SignUp from "../SignUp/SignUp";
import React from "react";
import { useNavigate, Routes, Route } from "react-router-dom";
import UserDetail from "../UserDetail/UserDetail";

const App = () => {
  return (
    <div>
      <Routes>
        <Route path="/" element={<Home navigate={useNavigate()} />}></Route>
        <Route
          path="/login"
          element={<LoginPage navigate={useNavigate()} />}
        ></Route>
        <Route
          path="/signup"
          element={<SignUp navigate={useNavigate()} />}
        ></Route>
        <Route path="/home" element={<UserList navigate={useNavigate()} componentVersion='home'/>} 
        ></Route>
        <Route path="/matches" element={<UserList navigate={useNavigate()} componentVersion='matches'/>} 
        ></Route>
        <Route path="/requests" element={<UserList navigate={useNavigate()} componentVersion='requests'/>} 
        ></Route>
        {/* TODO: Add userID URL param */}
        <Route path="/userdetail" element={<UserDetail navigate={useNavigate()}/>} 
      ></Route>
      </Routes>
    </div>
  );
};

export default App;
