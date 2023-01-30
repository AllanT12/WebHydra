import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';
import {CardActions} from "@material-ui/core";
import Button from "@material-ui/core/Button";
import axiosInstance from "../axios";

const useStyles = makeStyles((theme) => ({
	cardMedia: {
		paddingTop: '56.25%', // 16:9
	},
	link: {
		margin: theme.spacing(1, 1.5),
	},
	cardHeader: {
		backgroundColor:
			theme.palette.type === 'light'
				? theme.palette.grey[200]
				: theme.palette.grey[700],
	},
	postTitle: {
		fontSize: '16px',
		textAlign: 'left',
	},
	postText: {
		display: 'flex',
		justifyContent: 'left',
		alignItems: 'baseline',
		fontSize: '12px',
		textAlign: 'left',
		marginBottom: theme.spacing(2),
	},
}));

const Devices = (props) => {
	const { devices } = props;
	const classes = useStyles();
	const navigateToPage = (nr) => {
  	window.location.assign("/packets/"+nr.toString());
		console.log(nr);
  };
	const del = (nr) => {
  	axiosInstance.delete('/devices/delete/'+nr.toString()).then((res) => {
		  window.location.reload();
		});
  };
	if (devices === null|| devices.length === 0) {return <p>Can not find any devices, sorry</p>;}else {
		return (
			<React.Fragment>
				<Container maxWidth="md" component="main">
					<Grid container spacing={5} alignItems="flex-end">
						{devices.map((device) => {
							return (
								<Grid item key={device.deivceid} xs={12} md={4}>
									<Card className={classes.card}>
										<CardContent className={classes.cardContent}>
											<Typography
												gutterBottom
												variant="h6"
												component="h2"
												className={classes.postTitle}
											>
												{device.devicename}
											</Typography>
										</CardContent>
										<CardActions>
                    						<Button onClick={() => navigateToPage(device.deivceid)} size="small">Read Packets</Button>
                    						<Button onClick={() => del(device.deivceid)} size="small" variant="outlined" color="error">Delete</Button>
                  						</CardActions>
									</Card>
								</Grid>
							);
						})}
					</Grid>
				</Container>
			</React.Fragment>
		);
	}
};
export default Devices;