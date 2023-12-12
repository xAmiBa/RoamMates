import './App.css';
import LoginForm from '../auth/LoginForm'
import SignUpForm from '../user/SignUpForm'
import Home from '../Home/Home'
import LoginPage from '../LoginPage/LoginPage';
import SignUp from '../SignUp/SignUp'
import React, { useState } from 'react';
import {
  useNavigate,
  Routes,
  Route,
} from "react-router-dom";

const App = () => {
    return (
      <div>
        <Routes>
          <Route path='/' element={<Home navigate={useNavigate()}/>}></Route>
          <Route path='/login' element={<LoginPage navigate={useNavigate()}/>}></Route>
          <Route path='/signup' element={<SignUp navigate={useNavigate()}/>}></Route>

        </Routes>
    </div>
    )
}

export default App;
