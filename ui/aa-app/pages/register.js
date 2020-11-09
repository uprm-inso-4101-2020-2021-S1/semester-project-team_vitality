import React from 'react';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Typography from '@material-ui/core/Typography';
import Grid from '@material-ui/core/Grid';


export default function OutlinedCard() {
    return (
        <div id='registergrid'>
            <Grid container spacing={6}>
                <Grid item xs={6}>
                    <Card className='card' variant="outlined">
                        <CardContent>
                            <Typography variant="h5" component="h2">
                                Register as Customer
                            </Typography>
                            <hr/>
                            <br/>
                            <Typography color="textSecondary" gutterBottom>
                                Lorem Ipsum is simply dummy text of the printing 
                                and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s
                            </Typography>
                        </CardContent>
                        <CardActions>
                            <a href="/registerc" class="btn-white">Get started</a>
                        </CardActions>
                    </Card>
                </Grid>
                <Grid item xs={6}>
                <Card className='card' variant="outlined">
                        <CardContent>
                            <Typography variant="h5" component="h2">
                                Register as Business
                            </Typography>
                            <hr/>
                            <br/>
                            <Typography color="textSecondary" gutterBottom>
                                Lorem Ipsum is simply dummy text of the printing 
                                and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s
                            </Typography>
                        </CardContent>
                        <CardActions>
                            <a href="/registerb" class="btn-white">Get started</a>
                        </CardActions>
                    </Card>
                </Grid>
            </Grid>
        </div>
    );
}