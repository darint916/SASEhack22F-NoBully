import * as React from 'react';
import { styled, ThemeProvider } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import Box from '@mui/material/Box';
import MuiAppBar, { AppBarProps as MuiAppBarProps } from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import IconButton from '@mui/material/IconButton';
import Container from '@mui/material/Container';
import Grid from '@mui/material/Grid';
import Paper from '@mui/material/Paper';
import Link from '@mui/material/Link';
import { useTheme} from '@mui/material/styles';
import Brightness4Icon from '@mui/icons-material/Brightness4';
import Brightness7Icon from '@mui/icons-material/Brightness7';
import InterceptionTable from './intercept/InterceptionTable';
import ConfigDomains from './config-display/ConfigDomains';
import ConfigWords from './config-display/ConfigWords';
import { ColorModeContext } from '../App';

/*
* FOOTER FORMAT
 */
function Copyright(props: any) {
    const theme = useTheme();
    return (
        <Typography variant="body2" color={theme.palette.text.secondary} align="center" {...props}>
        {'Copyright © '}
        <Link color="inherit" href="https://en.wikipedia.org/wiki/Political_geography_of_Nineteen_Eighty-Four#Oceania">
            Ingsoc
        </Link>{' '}
        1984
        {'.'}
        </Typography>
    );
}

/*
* TOP APPBAR FORMAT
*/
interface AppBarProps extends MuiAppBarProps {
  open?: boolean;
}
const AppBar = styled(MuiAppBar, {
  shouldForwardProp: (prop) => prop !== 'open',
})<AppBarProps>(({ theme, open }) => ({
  zIndex: theme.zIndex.drawer + 1,
  transition: theme.transitions.create(['width', 'margin'], {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.leavingScreen,
  })
}));

/*
* DASHBOARD GRID SETUP
*/
function DashboardContent() {
    const colorMode = React.useContext(ColorModeContext);
    const theme = useTheme();
    return (
        <ThemeProvider theme={theme}>
        <Box  sx={{ display: 'flex' }}>
            <CssBaseline />
            <AppBar position="absolute" >
            <Toolbar color={theme.palette.background.default}>
                <Typography
                component="h1"
                variant="h5"
                color='inherit'
                noWrap
                sx={{ flexGrow: 1 }}
                >
                Dashboard
                </Typography>
                {theme.palette.mode} mode
                <IconButton sx={{ ml: 1 }} onClick={colorMode.toggleColorMode} color="inherit">
                    {theme.palette.mode === 'dark' ? <Brightness7Icon /> : <Brightness4Icon />}
                </IconButton>
            </Toolbar>
            </AppBar>
            
            <Box
            component="main"
            sx={{
                backgroundColor: theme.palette.action.hover,
                flexGrow: 1,
                height: '100vh',
                overflow: 'auto',
            }}
            >
            <Toolbar />
            <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
                <Grid container spacing={3}>
                {/*TRACKED DOMAINS*/}
                <Grid item xs={6} md={6} lg={6}>
                    <Paper
                    sx={{
                        p: 2,
                        display: 'flex',
                        flexDirection: 'column',
                        minHeight: 240,
                    }}
                    >
                    
                    <ConfigDomains/>
                    </Paper>
                </Grid>

                {/* blocked words */}
                <Grid item xs={6} md={6} lg={6}>
                    <Paper
                    sx={{
                        p: 2,
                        display: 'flex',
                        flexDirection: 'column',
                        minHeight: 240,
                    }}
                    >
                    <ConfigWords/>
                    </Paper>
                </Grid>

                {/* Interceptions */}
                <Grid item xs={12}>
                    <Paper sx={{ p: 2, display: 'flex', flexDirection: 'column' }}>
                    <InterceptionTable />
                    </Paper>
                </Grid>
                </Grid>
                <Copyright sx={{ pt: 4 }} />
            </Container>
            </Box>
        </Box>
        </ThemeProvider>
    );
}

export default function Dashboard() {
  return <DashboardContent />;
}