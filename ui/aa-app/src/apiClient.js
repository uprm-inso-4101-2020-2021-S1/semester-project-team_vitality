import axios from 'axios';

export function login(username, password) {
  axios.post('http//backend:5000/login', {username, password})
}