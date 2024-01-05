import animationData from './logo_earth.json';
import React from 'react';
import Lottie from 'react-lottie';
//  run: npm i react-lottie


const LogoAnimation = ({ width }) => {

    const defaultOptions = {
        loop: true,
        autoplay: true,
        animationData: animationData,
        rendererSettings: {
          preserveAspectRatio: "xMidYMid slice"
        }}

    return (
        <div className="logo-animation">
            <Lottie
            options={defaultOptions}
            width={width}
            ></Lottie>
        </div>
    )
}

export default LogoAnimation;