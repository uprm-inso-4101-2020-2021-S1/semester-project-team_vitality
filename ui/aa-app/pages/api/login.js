import axios from 'axios'

export default async (req, res) => {
    if (req.method === "POST") {
        await axios.post('http://backend:5000/login', req.body)
            .then(response => {
                return res.status(response.status).json(response.data);
            })
            .catch(error => {
                return res.status(500).json(error);
            });
        console.log("Survived api hit.");
    }
}