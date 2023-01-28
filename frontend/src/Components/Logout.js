import React, { useState, useEffect } from 'react';
import axiosInstance from '../axios';
import { useNavigate } from 'react-router-dom';

export default function SignUp() {
	const history = useNavigate();

	useEffect(() => {
		localStorage.removeItem('token');
		axiosInstance.defaults.headers['Authorization'] = null;
		history('/');
	});
	return <div>Logout</div>;
}