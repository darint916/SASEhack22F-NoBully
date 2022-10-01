import React, { useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import "antd/dist/antd.css";
import { Outlet } from 'react-router-dom';
import { BackTop, Layout } from 'antd';
import { Content, Footer } from 'antd/lib/layout/layout';
import NavBar from './features/navbar/NavBar';
import axios from 'axios';

function App() {

  useEffect(() => {
    axios.get('http://localhost:5000/api/testing').then((res) => {
      console.log(res);
    });
  }, []);

  return (
    <Layout>
      <BackTop/>
      <Layout style={{minHeight: '100vh', marginLeft: 200}}>
        <NavBar/>
        <Content style={{padding: '0 50px'}}>
          <Outlet/> 
        </Content>
      </Layout>
        <Footer style={{ textAlign: 'center' }}>SASE Hack 2022 Fall : No Bully</Footer>
    </Layout>
  );
}

export default App;
