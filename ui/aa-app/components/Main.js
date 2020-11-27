import React, { Component } from 'react';
import { Container } from '@material-ui/core';
import Grid from '@material-ui/core/Grid';

//Components
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';

class Main extends Component {
    render() {
        return (
            <React.Fragment>
                <Grid container id='slider' spacing={3}>
                    <Grid item xs={8}>
                        <Container maxWidth='sm'>
                            <h1>Welcome to ArrangeAll!</h1>
                            <h3>ArrangeAll is an easy to use web application for business administrators to manage their business appointments
                            and flow of clients during work hours. The benefit of using our product is that it facilitate clients in setting
                            an appointment for a desired service at their time and place of preference.
                            </h3>
                        </Container>
                    </Grid>
                    <Grid item xs={4}>
                        <img id='appointment' src='/schedule.svg' alt="" height='200' width='200'></img>
                    </Grid>
                </Grid>
                <Grid container id='middle-bar' spacing={3}>
                    <Grid item xs={8}>
                        <Container maxWidth='sm'>
                            <h1>Login to your account at any time</h1>
                            <h3>We have you covered no matter where you are located. All you need is an internet connection and a smartphone
                            or computer.
                            </h3>
                        </Container>
                    </Grid>
                    <Grid item xs={4}>
                        <img src='/productivity.png' height='200' width='200'></img>
                    </Grid>
                </Grid>
                {/* Services */}
                <Grid container id='services'>
                    <div id='services-bar'>
                        <h1>Our Services</h1>
                    </div>
                    <div id='services-wrapper'>
                        <Card id='services-card'>
                            <CardActionArea>
                                <CardMedia id='services-image' image='/image1.jpg' />
                                <CardContent>
                                    <h2>Organization</h2>
                                    <p>
                                        Reduce your waiting times and organize better your appointments.
                                    </p>
                                </CardContent>
                            </CardActionArea>
                        </Card>
                        <Card id='services-card'>
                            <CardActionArea>
                                <CardMedia id='services-image' image='/image3.jpg' />
                                <CardContent>
                                    <h2>Virtual Offices</h2>
                                    <p>
                                        You can access our platform online anywhere in the world.
                                    </p>
                                </CardContent>
                            </CardActionArea>
                        </Card>
                        <Card id='services-card'>
                            <CardActionArea>
                                <CardMedia id='services-image' image='/image5.jpg' />
                                <CardContent>
                                    <h2>Flexible Benefits</h2>
                                    <p>
                                        Cancel, change or delay appointments if its necessary.
                                    </p>
                                </CardContent>
                            </CardActionArea>
                        </Card>
                    </div>
                </Grid>
                {/* End Services */}
                <Grid container id='bc-container'>
                    <div id='bc-bar'>
                        <h1>Our Product</h1>
                    </div>
                    <div id='bc-wrapper'>
                        <Card id='bc-card'>
                            <CardActionArea>
                                <CardMedia id='bc-image' image='/AA.jpg' />
                                <CardContent>
                                    <p>
                                        Not only will ArrangeAll appointment booking software help you to protect your business; our innovative
                                        features will help you deliver an exceptional client experience.
                                    </p>
                                </CardContent>
                            </CardActionArea>
                            <CardActions>
                                <a href="/register" id='bc-btn'>Get started</a>
                            </CardActions>
                        </Card>
                    </div>
                </Grid>
            </React.Fragment>
        );
    }
}

export default Main;