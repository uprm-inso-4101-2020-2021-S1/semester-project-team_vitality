import axios from 'axios'
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Paper from '@material-ui/core/Paper';
import Typography from '@material-ui/core/Typography';
import Grid from '@material-ui/core/Grid';
import { CardHeader } from '@material-ui/core';




const useStyles = makeStyles(theme => ({
    root: {
        flexGrow: 1,
        padding: theme.spacing(2)
    },
    card: {
        minWidth: 275,
    },
    title: {
        fontSize: 14,
    },
    pos: {
        marginBottom: 12,
    },
}))


export default function Dashboard({ appointments }) {
    const classes = useStyles();

    console.log(appointments.length);

    return (
        <div className={classes.root}>
            <Typography variant="h2" align="center">
                Appointments
            </Typography>
            <br />
            <Grid
                container
                spacing={2}
                direction="row"
                justify="flex-start"
                alignItems="flex-start"
            >
                {appointments.map(elem => (
                    <Grid item spacing={3} xs={12} sm={6} md={3} key={appointments.indexOf(elem)}>
                        <Paper elevation={3}>
                            <CardHeader title={elem.business_name} subheader={`Confirmation Number: ${elem.confirmation_number}`} />
                            <CardContent>
                                <Typography variant="p" gutterBottom>
                                    Starts: {elem.start_time} <br />
                                    Ends: {elem.end_time}
                                </Typography>
                            </CardContent>
                        </Paper>
                    </Grid>
                ))}
            </Grid>
        </div>
    );
}

export async function getServerSideProps(context) {
    const res = await axios.get(`http://backend:5000/appointments/user/${context.query.uid}`);

    const body = await res.data;

    const appointments = { appointments: body.appointments };

    return {
        props: appointments,
    };
}