import React, { useState, useEffect, useCallback, useRef } from 'react';
import { useRouter } from 'next/router';

// Material-UI
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';

// Styling (Login Page based on Material-UI template)
const useStyles = makeStyles((theme) => ({
    paper: {
        marginTop: theme.spacing(8),
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
    },
    avatar: {
        margin: theme.spacing(1),
        backgroundColor: theme.palette.secondary.main,
    },
    form: {
        width: '100%', // Fix IE 11 issue.
        marginTop: theme.spacing(1),
    },
    submit: {
        margin: theme.spacing(3, 0, 2),
    },
}));


export default function SignIn() {
    const form = useRef(null);
    const router = useRouter();

    const handleSubmit = useCallback((e) => {
        e.preventDefault();
        const formData = new FormData(form.current);
        const req = {};
        formData.forEach((value, key) => req[key] = value);
        console.log(req);

        fetch('api/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(req),
        }).then(res => {
            console.log(res);
            if (res.status === 200) router.push('/profile');
        })
    }, []);

    useEffect(() => {
        router.prefetch('/profile');
    }, [])

    const classes = useStyles();
    // Login Component (Default)
    return (
        <Container className='registerbc-padding' component="main" maxWidth="xs">
            <CssBaseline />
            <div className={classes.paper}>
                <Typography component="h1" variant="h5">
                    Register
                </Typography>
                <form ref={form} className={classes.form} onSubmit={handleSubmit}>
                    <TextField
                        variant="outlined"
                        margin="normal"
                        required
                        fullWidth
                        id="businessname"
                        label="Business Name"
                        name="businessname"
                        autoFocus
                    />
                    <TextField
                        variant="outlined"
                        margin="normal"
                        required
                        fullWidth
                        id="address"
                        label="Address"
                        name="address"
                        autoFocus
                    />
                    <TextField
                        variant="outlined"
                        margin="normal"
                        required
                        fullWidth
                        id="city"
                        label="City"
                        name="city"
                        autoFocus
                    />
                    <TextField
                        variant="outlined"
                        margin="normal"
                        required
                        fullWidth
                        id="zipcode"
                        label="Zip Code"
                        name="zipcode"
                        autoFocus
                    />
                    <TextField
                        variant="outlined"
                        margin="normal"
                        required
                        fullWidth
                        id="businessemail"
                        label="Business Email"
                        type='email'
                        name="businessemail"
                        autoFocus
                    />
                    <TextField
                        variant="outlined"
                        margin="normal"
                        required
                        fullWidth
                        id="maxcapacity"
                        label="Max Capacity"
                        name="maxcapacity"
                        autoFocus
                    />
                    <TextField
                        variant="outlined"
                        margin="normal"
                        required
                        fullWidth
                        name="ownerid"
                        label="Owner ID"
                        id="ownerid"
                    />
                    <Button
                        type="submit"
                        fullWidth
                        variant="contained"
                        color="primary"
                        className={classes.submit}
                        className='green-blue-btn'
                    >
                        Sign Up
                    </Button>
                </form>
            </div>
        </Container>
    );

}