import {
    DesktopOutlined,
    FileOutlined,
    PieChartOutlined,
    TeamOutlined,
    UserOutlined,
    SettingOutlined,
  } from '@ant-design/icons';
  import type { MenuProps } from 'antd';
  import SettingsLineIcon from 'remixicon-react/SettingsLineIcon';
  import { Breadcrumb, Layout, Menu } from 'antd';
  import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import ConfigDisplay from '../config-display/ConfigDisplay';
  
  const { Header, Content, Footer, Sider } = Layout;
  
  type MenuItem = Required<MenuProps>['items'][number];
  
  function getItem(
    label: React.ReactNode,
    key: React.Key,
    onClick? : () => void,
    icon?: React.ReactNode,
    children?: MenuItem[],
  ): MenuItem {
    return {
      key,
      icon,
      onClick,
      children,
      label,
    } as MenuItem;
  }
  
  function NavBar() {
    const navigate = useNavigate();
    
    const items: MenuItem[] = [
      getItem('User Settings', 'config',() => navigate('config'), <SettingOutlined />),
      getItem('Block Modules', 'sub2', () => navigate('config'),<TeamOutlined />),
      getItem('Blocked Messages', 'sub3', () => navigate('config'),<UserOutlined />),
    ];
    return (
        <Sider style={{overflow: 'auto',
        height: '100vh',
        position: 'fixed',
        left: 0,
        top: 0,
        bottom: 0,}}>
          <div className="logo" />
          <Menu theme="dark" defaultSelectedKeys={['config']} mode="inline" items={items} />
        </Sider>
    );
  };
  export default NavBar;