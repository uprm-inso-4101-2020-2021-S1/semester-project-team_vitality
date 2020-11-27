import React from 'react';
import ReactDOM from 'react-dom';
import Main from '../Main';

//Test if the main component renders without any failure
it("renders without crashing", () => {
    const div = document.createElement("main");
    ReactDOM.render(<Main></Main>, div)
});