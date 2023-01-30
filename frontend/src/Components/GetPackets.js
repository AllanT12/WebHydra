import React, { useEffect, useState } from 'react';
import '../App.css';
import Packets from './Packets';
import DeviceLoadingComponent from './DeviceLoading';
import axiosInstance from "../axios";
import {useParams} from "react-router-dom";

function GetPackets() {
	const PostLoading = DeviceLoadingComponent(Packets);
	const { id } = useParams();
	const [appState, setAppState] = useState({
		loading: false,
		packets: null,
	});

	useEffect(() => {
		console.log(id);
		axiosInstance.get('/packets/view/'+id).then((res) => {
			const allPosts = res.data;
			setAppState({ loading: false, packets: allPosts });
			console.log(res.data);
		});
	}, [setAppState]);
	return (
		<div className="App">
			<h1>Packets</h1>
			<PostLoading isLoading={appState.loading} devices={appState.packets} />
		</div>
	);
}
export default GetPackets;