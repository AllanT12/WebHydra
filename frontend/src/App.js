import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';

const useStyles = makeStyles((theme) => ({
  root: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    marginTop: theme.spacing(10),
  },
  title: {
    fontWeight: 700,
    marginBottom: theme.spacing(3),
  },
  button: {
    marginTop: theme.spacing(3),
  },
}));

function App() {
  const classes = useStyles();

  return (
    <Container className={classes.root}>
      <Typography variant="h4" className={classes.title}>
        Welcome to Hydra Web Edition
      </Typography>
      <Typography variant="body1">
        Hydra Web edition is a web application for my python based packet sniffer
      </Typography>
    </Container>
  );
}

export default App;