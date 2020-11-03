import axios from 'axios';

const BASE_URI = 'http://backend:5000/';

const client = axios.create({
    baseURL: BASE_URI,
    json:true
})

class APIClient {

    constructor() {

    }

    login() {
        client.post('/login', {
            username: "test",
            password: "test"
          
        })
        .then(function (response) {
          console.log(response);
        })
        .catch(function (error) {
          console.log(error)
        });
        
    }
}

export default APIClient;