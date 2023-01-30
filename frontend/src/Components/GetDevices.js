import React, { useEffect, useState } from 'react';
import '../App.css';
import Devices from './Devices';
import DeviceLoadingComponent from './DeviceLoading';
import axiosInstance from "../axios";

function GetDevices() {
	const PostLoading = DeviceLoadingComponent(Devices);
	const [appState, setAppState] = useState({
		loading: false,
		devices: null,
	});

	useEffect(() => {
		axiosInstance.get('/devices/view').then((res) => {
			const allPosts = res.data;
			setAppState({ loading: false, devices: allPosts });
		});
	}, [setAppState]);
	return (
		<div className="App">
			<h1>Devices</h1>
			<PostLoading isLoading={appState.loading} devices={appState.devices} />
		</div>
	);
}
export default GetDevices;