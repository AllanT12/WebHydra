import React from 'react';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import CssBaseline from '@material-ui/core/CssBaseline';
import { makeStyles } from '@material-ui/core/styles';
import { NavLink } from 'react-router-dom';
import Link from '@material-ui/core/Link';
import Button from '@material-ui/core/Button';
import axiosInstance from "../axios";

const useStyles = makeStyles((theme) => ({
	appBar: {
		borderBottom: `1px solid ${theme.palette.divider}`,
	},
	link: {
		margin: theme.spacing(1, 1.5),
	},
	toolbarTitle: {
		flexGrow: 1,
	},
}));

function Header() {
	const classes = useStyles();
	const del = () => {
  	axiosInstance.delete('/user/delete/').then((res) => {
		  localStorage.removeItem('token');
		  axiosInstance.defaults.headers['Authorization'] = null;
		  window.location.assign("/");
		  window.location.reload();
		});
  };
	if(axiosInstance.defaults.headers.Authorization){
		return (
		<React.Fragment>
			<CssBaseline />
			<AppBar
				position="static"
				color="default"
				elevation={0}
				className={classes.appBar}
			>
				<Toolbar className={classes.toolbar}>
					<Typography
						variant="h6"
						color="inherit"
						noWrap
						className={classes.toolbarTitle}
					>
						<Link
							component={NavLink}
							to="/"
							underline="none"
							color="textPrimary"
						>
							Hydra WebEdition
						</Link>
					</Typography>
					<Button
							href="#"
							color="primary"
							variant="outlined"
							className={classes.link}
							component={NavLink}
							to="/subs"
						>
							Subscriptions
						</Button>
					<Button
						href="#"
						color="primary"
						variant="outlined"
						className={classes.link}
						component={NavLink}
						to="/devices"
					>
						My Devices
					</Button>
					<Button
						href="#"
						color="primary"
						variant="outlined"
						className={classes.link}
						component={NavLink}
						to="/logout"
					>
						Logout
					</Button>
					<Button
						href="#"
						color="error"
						variant="contained"
						className={classes.link}
						component={NavLink}
						onClick={() => del}
					>
						Delete Account
					</Button>
				</Toolbar>
			</AppBar>
		</React.Fragment>
	);
}else {
		return (
			<React.Fragment>
				<CssBaseline/>
				<AppBar
					position="static"
					color="default"
					elevation={0}
					className={classes.appBar}
				>
					<Toolbar className={classes.toolbar}>
						<Typography
							variant="h6"
							color="inherit"
							noWrap
							className={classes.toolbarTitle}
						>
							<Link
								component={NavLink}
								to="/"
								underline="none"
								color="textPrimary"
							>
								Hydra WebEdition
							</Link>
						</Typography>
						<nav>
							<Link
								color="textPrimary"
								href="#"
								className={classes.link}
								component={NavLink}
								to="/register"
							>
								Register
							</Link>
						</nav>
						<Button
							href="#"
							color="primary"
							variant="outlined"
							className={classes.link}
							component={NavLink}
							to="/login"
						>
							Login
						</Button>
						<Button
							href="#"
							color="primary"
							variant="outlined"
							className={classes.link}
							component={NavLink}
							to="/subs"
						>
							Subscriptions
						</Button>
					</Toolbar>
				</AppBar>
			</React.Fragment>
		);
	}
}

export default Header;