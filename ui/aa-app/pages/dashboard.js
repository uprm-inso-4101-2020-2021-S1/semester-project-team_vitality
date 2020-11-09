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

    let cards = [];

    const cardCreator = (item, index) => {
        cards.push(<Paper elevation={3}>
            <Card className={classes.card}>
                <CardContent>
                    <Typography className={classes.title} color="textSecondary" gutterbottom>
                        Appointment #{index}
                    </Typography>
                    <Typography variant="h5" component="h2">
                        Jarana
            </Typography>
                    <Typography variant="body2" component="p">
                        Confirmation Number: {item.confirmation_number}
                    </Typography>

                </CardContent>
            </Card>
        </Paper>);
    };

    console.log(appointments.length);

    appointments.forEach(cardCreator);

    return (
        <div className={classes.root}>
            <h1>Appointments</h1>
            <Grid
                container
                spacing={2}
                direction="row"
                justify="flex-start"
                alignItems="flex-start"
            >
                {appointments.map(elem => (
                    <Grid xs={12} sm={6} md={3} key={appointments.indexOf(elem)}>
                        <CardHeader title="Business" subheader={`Confirmation Number: ${elem.confirmation_number}`} />
                        <CardContent>
                            <Typography variant="h5" gutterBottom>
                                Starts: {elem.start_time}
                            </Typography>
                            <Typography variant="h5">
                                Ends: {elem.end_time}
                            </Typography>
                        </CardContent>
                    </Grid>
                ))}
            </Grid>
        </div>
    );
}

export async function getServerSideProps(context) {
    const res = await axios.get(`http://backend:5000/appointments/user/${context.query.uid}`);

    const body = await res.data;

    const appointments = { appointments: body.businesses };

    return {
        props: appointments,
    };
}