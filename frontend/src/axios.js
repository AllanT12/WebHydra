import axios from 'axios';

const baseURL = 'http://192.168.1.241:8000';

const axiosInstance = axios.create({
	baseURL: baseURL,
	timeout: 5000,
	headers: {
		Authorization: localStorage.getItem('token')
			? 'Token ' + localStorage.getItem('token')
			: null,
		'Content-Type': 'application/json',
		accept: 'application/json',
	},
});


export default axiosInstance;

