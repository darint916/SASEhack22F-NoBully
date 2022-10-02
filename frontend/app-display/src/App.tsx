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


function App() {

  const dispatch = useAppDispatch();

  useEffect(() => {
    
    const interval = setInterval(() => {
      axios.get('http://10.8.0.4:7000/api/intercept/get')
      .then(
        (response) => {
          // console.log(response.data.data);
          dispatch(setInterceptionData(response.data.data));
        });
        },3000);
    
  }, []);
  

  return (
    <Dashboard/>
    // <Layout>
    //   <BackTop/>
    //   <Layout style={{minHeight: '100vh', marginLeft: 200}}>
    //     <NavBar/>
    //     <Content style={{padding: '0 50px'}}>
    //       <Outlet/> 
    //     </Content>
    //   </Layout>
    //     <Footer style={{ textAlign: 'center' }}>SASE Hack 2022 Fall : No Bully</Footer>
    // </Layout>
  );
}

export default App;
