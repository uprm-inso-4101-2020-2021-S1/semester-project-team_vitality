import axios from 'axios'

export default async (req, res) => {
    if (req.method === "POST") {
        await axios.post('http://backend:5000/login', req.body)
            .then(response => {
                console.log(response.data);
                return res.status(response.status).json(response.data);
            })
            .catch(error => {
                return res.status(500).json(error);
            });
    }
}