import React, { useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import "antd/dist/antd.css";
import { Outlet } from 'react-router-dom';
import { BackTop, Layout } from 'antd';
import { Content, Footer } from 'antd/lib/layout/layout';
import axios from 'axios';
import Dashboard from './features/Dashboard';
import { useAppDispatch } from './app/hooks';
import { setInterceptionData } from './features/intercept/InterceptionDataSlice';
import { setConfigSettings } from './features/config-display/ConfigSettingsSlice';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';

export const ColorModeContext = React.createContext({ toggleColorMode: () => {} });
function App() {

  const [mode, setMode] = React.useState<'light' | 'dark'>('light');
  const colorMode = React.useMemo(() => ({
      toggleColorMode: () => {
        setMode((prevMode) => (prevMode === 'light' ? 'dark' : 'light'));
      },
    }),
    [],
  );

  const theme = React.useMemo(
    () =>
      createTheme({
        palette: {
          mode,
        },
      }),
    [mode],
  );


  const dispatch = useAppDispatch();

  /*
   * SHORT POLLING FOR INTERCEPTED MESSAGES (every 3 seconds)
   */
  useEffect(() => { 
    
    setInterval(() => {
      axios.get('http://10.8.0.4:7000/api/intercept/get')
      .then(
        (response) => {
          // console.log(response.data.data);
          dispatch(setInterceptionData(response.data.data));
        });
        },3000);
    
  }, []);
  
  return (
    <ColorModeContext.Provider value={colorMode}>
      <ThemeProvider theme={theme}>
        <Dashboard/>
      </ThemeProvider>
    </ColorModeContext.Provider>);
}

export default App;
