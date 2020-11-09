import React, { Component } from 'react'

class Header extends Component {

    render() {
        return (
            <header id="header">
                <div id='border-top'></div>
                <div className="center">
                    {/* LOGO */}
                    <div id="logo">
                        <span id="brand">
                            <strong>Arrange</strong>All&trade;
                        </span>
                    </div>

                    {/* MENU */}
                    <nav id="menu">
                        <ul>
                            <li>
                                <a href="/">Home</a>
                            </li>
                            <li>
                                <a href="/register">Register</a>
                            </li>
                            <li>
                                <a href="/signin">Sign In</a>
                            </li>
                            <li>
                                <a href="/profile">Profile</a>
                            </li>
                        </ul>
                    </nav>
                </div>
            </header>
        );
    }
}

export default Header;