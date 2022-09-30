import { useAppSelector, useAppDispatch } from '../../app/hooks';
import React, { useState } from 'react';
import { Breadcrumb } from 'antd';
function ConfigDisplay () {
    return (<>
        <Breadcrumb style={{ margin: '16px 0' }}>
        <Breadcrumb.Item>App</Breadcrumb.Item>
        <Breadcrumb.Item>ConfigDisplay</Breadcrumb.Item>
        </Breadcrumb>
        <div className="site-layout-content" style={{margin: '0 50px'}}>
            agh
        </div>
        </>
        );
}
export default ConfigDisplay;