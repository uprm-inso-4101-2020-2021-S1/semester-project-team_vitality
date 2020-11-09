import React, { Component } from 'react';
import Box from '@material-ui/core/Box';
import Button from '@material-ui/core/Button';
import { Container } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Typography from '@material-ui/core/Typography';
import Grid from '@material-ui/core/Grid';

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
                    <Cards />
                </div>
                <div id='bbar'>
                    <BBar />
                </div>
            </React.Fragment>

        );
    }
}

const useStyles = makeStyles({
    title: {
        fontSize: 14,
    },
    pos: {
        marginBottom: 12,
    },
});

function Cards() {
    const classes = useStyles();

    return (
        <React.Fragment>
            <div id='main-grid'>
                <Container maxWidth='lg'>
                    <Grid container spacing={6}>
                        <Grid item xs={6}>
                            <Card className='card' variant="outlined">
                                <CardContent>
                                    <Typography variant="h5" component="h2">
                                        Get more time, every day
                                    </Typography>
                                    <hr />
                                    <Typography color="textSecondary" gutterBottom>
                                        <h4>Not only will ArrangeAll appointment booking software help you to protect your business; our innovative
                                        features will help you deliver an exceptional client experience.
                                        </h4>
                                    </Typography>
                                </CardContent>
                            </Card>
                        </Grid>
                        <Grid item xs={6}>
                            <Card className='card' variant="outlined">
                                <CardContent>
                                    <Typography variant="h5" component="h2">
                                        Organize better your appointments
                                    </Typography>
                                    <hr />
                                    <Typography color="textSecondary" gutterBottom>
                                        <h4>Not only will ArrangeAll appointment booking software help you to protect your business; our innovative
                                        features will help you deliver an exceptional client experience.
                                </h4>
                                    </Typography>
                                </CardContent>
                            </Card>
                        </Grid>
                    </Grid>
                </Container>
                {/* <br/>
                <br/> */}
                <Container id='mid-container' maxWidth='sm'>
                    <Grid item xs={12} alignItems="center">
                        <Card className='card' variant="outlined">
                            <CardContent>
                                <Typography variant="h5" component="h2">
                                    Keep track of your appointments
                                </Typography>
                                <hr />
                                <Typography color="textSecondary" gutterBottom>
                                    <h4>Not only will ArrangeAll appointment booking software help you to protect your business; our innovative
                                    features will help you deliver an exceptional client experience.
                                </h4>
                                </Typography>
                            </CardContent>
                        </Card>
                    </Grid>
                </Container>
            </div>
        </React.Fragment>
    );
}

function BBar() {
    return (
        <React.Fragment>
            <Container id='bbar-container' maxWidth='md'>
                <Grid item xs={12}>
                    <Card id='bbar-card' variant="outlined">
                        <CardContent>
                            <Typography gutterBottom>
                                <h4>Not only will ArrangeAll appointment booking software help you to protect your business; our innovative
                                features will help you deliver an exceptional client experience.
                                </h4>
                                <a href="/register" class="bbar-button">Get started</a>
                            </Typography>
                        </CardContent>
                    </Card>
                </Grid>
            </Container>
        </React.Fragment>
    );
}

export default Main;