import React, { Component } from 'react';
import Box from '@material-ui/core/Box';
import Button from '@material-ui/core/Button';
import { Container } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Typography from '@material-ui/core/Typography';
import Grid from '@material-ui/core/Grid';


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
                        <img src='/productivity.png' alt="me" height='200' width='200'></img>
                    </Grid>
                </Grid> 
                <Grid container id='services-container'>

                </Grid>
                <Grid container id='bc-container'>

                </Grid>
            </React.Fragment>
        );
    }
}

export default Main;