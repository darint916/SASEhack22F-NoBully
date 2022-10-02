import * as React from 'react';
import Typography from '@mui/material/Typography';
import { useTheme} from '@mui/material/styles';
interface TitleProps {
    children?: React.ReactNode;
  }
  
  export default function Title(props: TitleProps) {
    const theme = useTheme();
    return (
      <Typography component="h2" variant="h6" color={theme.palette.text.primary} gutterBottom>
        {props.children}
      </Typography>
    );
  }