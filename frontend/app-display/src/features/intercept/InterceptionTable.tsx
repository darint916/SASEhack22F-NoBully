import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell, { tableCellClasses } from '@mui/material/TableCell';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Title from './Title';
import { useAppSelector } from '../../app/hooks';
import { SocialIcon } from 'react-social-icons';
import { styled } from '@mui/material/styles';
import { useTheme} from '@mui/material/styles';

const StyledTableCell = styled(TableCell)(({ theme }) => ({
    [`&.${tableCellClasses.head}`]: {
      backgroundColor: theme.palette.action.disabledBackground
    },
    [`&.${tableCellClasses.body}`]: {
      fontSize: 14,
      backgroundColor: theme.palette.action.hover
    },
}));

const StyledTableRow = styled(TableRow)(({ theme }) => ({
    '&:nth-of-type(odd)': {
        backgroundColor: theme.palette.action.hover
    },
    // hide last border
    '&:last-child td, &:last-child th': {
        border: 0,
    },
}));

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

function formatTime(timestamp: number) {
    const date = new Date(timestamp*1000);
    return date.toLocaleString();
}

export default function InterceptionTable() {
    const theme = useTheme();
    const interceptionData = useAppSelector((state) => state.interceptionData.data);
    const row = interceptionData["Http Interceptor"].intercepted.map((intercepted, index) => {
        return createData(index, intercepted.message, (new URL(intercepted.domain)).hostname, intercepted.reason, intercepted.timestamp, "Http Interceptor");
    }).filter((intercepted) => {
        if(intercepted.message.length < 1300) {
            return intercepted
        }
    });

    const row2 = interceptionData["Websocket Interceptor"].intercepted.map((intercepted, index) => {
        return createData(index, intercepted.message, (new URL(intercepted.domain)).hostname, intercepted.reason, intercepted.timestamp, "Websocket Interceptor");
    }).filter((intercepted) => {
        if(intercepted.message.length < 1300) {
            return intercepted
        }
    });
    const rows = row.concat(row2).sort((a, b) => b.timestamp - a.timestamp);
    
    return (
        <React.Fragment>
        <Title><span style={{fontSize:"35px", color:theme.palette.text.primary}}>Intercepted Data</span></Title>
        <Table size="small">
          <TableHead>
            <TableRow>
              <StyledTableCell><Title>Message</Title></StyledTableCell>
              <StyledTableCell align='right'><Title>App</Title></StyledTableCell>
              <StyledTableCell align="right"><Title>Domain</Title></StyledTableCell>
              <StyledTableCell align="right"><Title>Reason</Title></StyledTableCell>
              <StyledTableCell align="right"><Title>Time Stamp</Title></StyledTableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {rows.map((row) => (
              <TableRow key={row.timestamp}>
                <StyledTableCell style={{whiteSpace: "normal", wordWrap: "break-word"}}>{row.message}</StyledTableCell>
                <StyledTableCell style={{whiteSpace: "normal", wordWrap: "break-word"}} align="right"><SocialIcon url={row.domain}/></StyledTableCell>
                <StyledTableCell style={{whiteSpace: "normal", wordWrap: "break-word"}} align="right">{row.domain}</StyledTableCell>
                <StyledTableCell style={{whiteSpace: "normal", wordWrap: "break-word"}} align="right">{row.reason}</StyledTableCell>
                <StyledTableCell style={{whiteSpace: "normal", wordWrap: "break-word"}} align="right">{formatTime(row.timestamp)}</StyledTableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </React.Fragment>
    )
}