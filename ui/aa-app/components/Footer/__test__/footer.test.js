import React from 'react';
import ReactDOM from 'react-dom';
import Footer from '../Footer';

//Test if the footer renders without any failure
it("renders without crashing", () => {
    const footer = document.createElement("footer");
    ReactDOM.render(<Footer></Footer>, footer)
});




