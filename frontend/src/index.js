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
import GetDevices from "./Components/GetDevices";
import GetPackets from "./Components/GetPackets";
import Pricing from "./Components/Subs";

const routing = (
	<Router>
		<React.StrictMode>
			<Header />
			<Routes>
				<Route exact path="/" element={<App/>} />
				<Route exact path="/register" element={<Register/>} />
				<Route exact path="/login" element={<Login/>} />
				<Route exact path="/logout" element={<Logout/>} />
				<Route exact path="/devices" element={<GetDevices/>} />
				<Route exact path="/packets/:id" element={<GetPackets/>} />
				<Route exact path="/subs/" element={<Pricing/>} />
			</Routes>
			<Footer />
		</React.StrictMode>
	</Router>
);

ReactDOM.render(routing, document.getElementById('root'));


serviceWorker.unregister();