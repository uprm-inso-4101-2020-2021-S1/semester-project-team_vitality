import React from 'react'
import { Router, useRouter } from 'next/router'

const Header = () => {
    const router = useRouter();

    if (router.pathname.includes("dashboard")) {
        return (
            <header id="header">
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
                                <a href={router.pathname}>Home</a>
                            </li>
                            <li>
                                <a href="/profile">Profile</a>
                            </li>
                            <li>
                                <a href="/">Logout</a>
                            </li>
                        </ul>
                    </nav>
                </div>
            </header>
        )
    }

    else {
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
                        </ul>
                    </nav>
                </div>
            </header>
        );
    }

}

export default Header;