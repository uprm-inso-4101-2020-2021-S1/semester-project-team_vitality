import React from 'react';
import ReactDOM from 'react-dom';
import Header from '../Header';

//Test if the header renders without any failure
it("renders without crashing", () => {
    const header = document.createElement("header");
    ReactDOM.render(<Header></Header>, header)
});