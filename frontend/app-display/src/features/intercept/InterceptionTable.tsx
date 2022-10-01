import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Title from './Title';
import { useAppSelector } from '../../app/hooks';

function createData(
    id: number,
    message: string,
    domain: string,
    reason: string,
    timestamp: number,
    interceptor: string,
) {
    return { id, message, domain, reason, timestamp, interceptor };
}

function preventDefault(event: React.MouseEvent) {
    event.preventDefault();
}

function formatTime(timestamp: number) {
    const date = new Date(timestamp*1000);
    return date.toString();
}

export default function InterceptionTable() {
    const interceptionData = useAppSelector((state) => state.interceptionData.data);

    const row = interceptionData["Http Interceptor"].intercepted.map((intercepted, index) => {
        return createData(index, intercepted.message, intercepted.domain, intercepted.reason, intercepted.timestamp, "Http Interceptor");
    });
    const row2 = interceptionData["Websocket Interceptor"].intercepted.map((intercepted, index) => {
        return createData(index, intercepted.message, intercepted.domain, intercepted.reason, intercepted.timestamp, "Websocket Interceptor");
    });
    const rows = row.concat(row2).sort((a, b) => b.timestamp - a.timestamp);

    
    return (
        <React.Fragment>
        <Title>Intercepted Data</Title>
        <Table size="small">
          <TableHead>
            <TableRow>
              <TableCell>Message</TableCell>
              <TableCell>Domain</TableCell>
              <TableCell>Reason</TableCell>
              <TableCell>Time Stamp</TableCell>
              <TableCell align="right">Interceptor Type</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {rows.map((row) => (
              <TableRow key={row.id}>
                <TableCell>{row.message}</TableCell>
                <TableCell>{row.domain}</TableCell>
                <TableCell>{row.reason}</TableCell>
                <TableCell>{formatTime(row.timestamp)}</TableCell>
                <TableCell align="right">{row.interceptor}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
        {/* <Link color="primary" href="#" onClick={preventDefault} sx={{ mt: 3 }}>
          Refresh
        </Link> */}
      </React.Fragment>
    )
}