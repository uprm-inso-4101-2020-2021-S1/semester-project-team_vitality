import React from 'react';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Grid from '@material-ui/core/Grid';


export default function OutlinedCard() {
    return (
        <React.Fragment>
            <Grid container id='register-bg'>
            <Grid container>
                <div className='register-title'>
                    <h1>Register</h1>
                </div>
            </Grid>
            <Grid container>
                <div id='register-wrapper'>
                    <Card id='register-card'>
                        <CardActionArea>
                            <CardMedia id='register-image' image='/customer.png' />
                            <CardContent>
                                <h2 className='register-divs'>Register as Customer</h2>
                            </CardContent>
                        </CardActionArea>
                        <CardActions>
                            <a href="/registerc" className="register-btn">Register</a>
                        </CardActions>
                    </Card>
                    <Card id='register-card'>
                        <CardActionArea>
                            <CardMedia id='register-image' image='/business-portfolio.png' />
                            <CardContent>
                                <h2 className='register-divs'>Register as Business</h2>
                            </CardContent>
                        </CardActionArea>
                        <CardActions>
                            <a href="/registerc" className="register-btn">Register</a>
                        </CardActions>
                    </Card>
                </div>
            </Grid>
            </Grid>
        </React.Fragment>
    );
}