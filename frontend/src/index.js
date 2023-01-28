import React from 'react';
import ReactDOM from 'react-dom';
import * as serviceWorker from './serviceWorker';
import './index.css';
import { Route, BrowserRouter as Router, Routes } from 'react-router-dom';
import App from './App';
import Header from './Components/Header';
import Footer from './Components/Footer';
import Register from './Components/Register';
import Login from './Components/Login';
import Logout from './Components/Logout';

const routing = (
	<Router>
		<React.StrictMode>
			<Header />
			<Routes>
				<Route exact path="/" element={<App/>} />
				<Route exact path="/register" element={<Register/>} />
				<Route exact path="/login" element={<Login/>} />
				<Route exact path="/logout" element={<Logout/>} />
			</Routes>
			<Footer />
		</React.StrictMode>
	</Router>
);

ReactDOM.render(routing, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();