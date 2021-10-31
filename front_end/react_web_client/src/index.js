import React from 'react';
import ReactDOM from 'react-dom';
import {MainPage} from './pages/index';
import { MuiThemeProvider } from '@material-ui/core';
import { theme } from './constants/theme';


ReactDOM.render(
  <React.StrictMode>
      <MuiThemeProvider theme={theme}>
        <MainPage/>
      </MuiThemeProvider>
  </React.StrictMode>,
  document.getElementById('root')
);
