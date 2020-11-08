import React, { Component } from 'react';
import Box from '@material-ui/core/Box';
import Button from '@material-ui/core/Button';
import { Container } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Typography from '@material-ui/core/Typography';

class Main extends Component {
    render() {
        return (
            <React.Fragment>
                <div id="slider" class="slider-big">
                    <h1>Welcome to ArrangeAll!</h1>
                    <Container maxWidth='md'>
                        <Box>
                            <h3>ArrangeAll is an easy to use web application for business administrators to manage their business appointments
                            and flow of clients during work hours. The benefit of using our product is that it facilitate clients in setting
                            an appointment for a desired service at their time and place of preference.
                            </h3>
                        </Box>
                    </Container>
                </div>
                <div>
                    <Container maxWidth='xs'>
                        <div id='card'>
                            <OutlinedCard />
                        </div>
                    </Container>
                </div>
            </React.Fragment>

        );
    }
}

const useStyles = makeStyles({
    root: {
        minWidth: 275,
    },
    bullet: {
        display: 'inline-block',
        margin: '0 2px',
        transform: 'scale(0.8)',
    },
    title: {
        fontSize: 14,
    },
    pos: {
        marginBottom: 12,
    },
});

function OutlinedCard() {
    const classes = useStyles();
    const bull = <span className={classes.bullet}>•</span>;

    return (
        <React.Fragment>
            <div>
                <Card className={classes.root} variant="outlined">
                    <CardContent>
                        <Typography variant="h5" component="h2">
                            Get more time, every day
                        </Typography>
                        <hr />
                        <Typography variant="body2" component="p">
                            <h4>Not only will ArrangeAll appointment booking software help you to protect your business; our innovative
                            features will help you deliver an exceptional client experience.
                            </h4>
                        </Typography>
                    </CardContent>
                </Card>
            </div>
            <div>
                <Card className={classes.root} variant="outlined">
                    <CardContent>
                        <Typography variant="h5" component="h2">
                            Organize better your appointments
                        </Typography>
                        <hr />
                        <Typography variant="body2" component="p">
                            <h4>Not only will ArrangeAll appointment booking software help you to protect your business; our innovative
                            features will help you deliver an exceptional client experience.
                            </h4>
                        </Typography>
                    </CardContent>
                </Card>
            </div>
            <div>
                <Card className={classes.root} variant="outlined">
                    <CardContent>
                        <Typography variant="h5" component="h2">
                            Keep track of your appointments
                        </Typography>
                        <hr />
                        <Typography variant="body2" component="p">
                            <h4>Not only will ArrangeAll appointment booking software help you to protect your business; our innovative
                            features will help you deliver an exceptional client experience.
                            </h4>
                        </Typography>
                    </CardContent>
                </Card>
            </div>
            <div>
                <Card className={classes.root} variant="outlined">
                    <CardContent>
                        <Typography variant="body2" component="p">
                            <h4>Not only will ArrangeAll appointment booking software help you to protect your business; our innovative
                            features will help you deliver an exceptional client experience.
                            </h4>
                            <a href="/register" class="btn-white">Get started</a>
                        </Typography>
                    </CardContent>
                </Card>
            </div>
        </React.Fragment>
    );
}

export default Main;