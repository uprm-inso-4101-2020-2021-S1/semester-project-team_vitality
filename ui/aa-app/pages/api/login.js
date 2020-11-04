import axios from 'axios'

export default async (req, res) => {
    console.log("hit api")
    console.log(req.body);
    if(req.method === "POST") {
        await axios.post('http://backend:5000/login', req.body)
              .catch(error => {
                  console.log(error);
              });
        res.statusCode = 200;
    }
}