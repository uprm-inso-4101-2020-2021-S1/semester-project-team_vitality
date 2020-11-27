import React, { Component } from 'react';
import {
    FaFacebook,
    FaInstagram,
    FaYoutube,
    FaTwitter,
    FaLinkedin
  } from 'react-icons/fa';

const style = {
    position: "relative",
    right: 0,
    bottom: 0,
    left: 0
}

const Footer = () => {
    return (
        <footer id='footer-container'>
            <div id='footer-wrap'>
                <div id='footer-links-container'>
                    <div id='footer-links-wrapper'>
                        <ul id='footer-link-items'>
                            <h1 id='footer-link-title'>About Us</h1>
                            <a href='/signin'>How it works</a>
                            <a href='/'>Testimonials</a>
                            <a href='/'>Careers</a>
                            <a href='/'>Investors</a>
                            <a href='/'>Terms of Service</a>
                        </ul>
                        <ul id='footer-link-items'>
                            <h1 id='footer-link-title'>Contact Us</h1>
                            <a href='/'>Contact</a>
                            <a href='/'>Support</a>
                            <a href='/'>Destinations</a>
                            <a href='/'>Sponsorships</a>
                        </ul>
                    </div>
                    <div id='footer-links-wrapper'>
                        <ul id='footer-link-items'>
                            <h1 id='footer-link-title'>App</h1>
                            <a href='/'>Marketplace</a>
                            <a href='/'>Mobile App</a>
                            <a href='/'>Desktop App</a>
                            <a href='/'>API/Developers</a>
                        </ul>
                        <ul id='footer-link-items'>
                            <h1 id='footer-link-title'>Social Media</h1>
                            <a href='/'>Instagram</a>
                            <a href='/'>Facebook</a>
                            <a href='/'>Youtube</a>
                            <a href='/'>Twitter</a>
                        </ul>
                    </div>
                </div>
                <hr/>
                <div id='social-media'>
                    <div id='social-media-wrap'>
                        <a id='social-logo' href='/'>
                            <strong>Arrange</strong>All&trade;
                        </a>
                        <div id='copyrights'>ArrangeAll © 2020 All rights reserved.</div>
                        
                        <div id='social-icons'>
                            <a id='social-icon-link' href='/' target='_blank' aria-label='Facebook'>
                                <FaFacebook />
                            </a>
                            <a id='social-icon-link' href='/' target='_blank' aria-label='Instagram'>
                                <FaInstagram />
                            </a>
                            <a  id='social-icon-link'
                                href='/'
                                target='_blank'
                                aria-label='Youtube'
                                rel=''
                            >
                                <FaYoutube />
                            </a>
                            <a  id='social-icon-link'
                                target='_blank'
                                aria-label='Twitter'
                                href='/'
                            >
                                <FaTwitter />
                            </a>
                            <a id='social-icon-link' href='/' target='_blank' aria-label='Linkedin'>
                                <FaLinkedin />
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </footer>
    )
}
export default Footer;