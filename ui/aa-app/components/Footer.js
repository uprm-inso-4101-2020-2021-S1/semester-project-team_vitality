import React, { Component } from 'react';

const style = {
    position: "relative",
    right: 0,
    bottom: 0,
    left: 0
}
const Footer = () => {
    return (
        <footer style={style} id="footer">
            <div>
                <p>
                    &copy; Copyright ArrangeAll 2020
            </p>
            </div>
        </footer>
    );
}
export default Footer;