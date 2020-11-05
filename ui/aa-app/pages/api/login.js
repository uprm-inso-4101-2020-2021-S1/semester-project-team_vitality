import axios from 'axios'

const users = [{ id: 1 }, { id: 2 }, { id: 3 }]
export default async (req, res) => {
    if (req.method === "POST") {
        await axios.post('http://backend:5000/login', req.body)
            .then(function (res) { console.log("hit api then") })
            .catch(error => {
            });
        console.log("Survived api hit.");
        res.status(200).json(users);
    }
}