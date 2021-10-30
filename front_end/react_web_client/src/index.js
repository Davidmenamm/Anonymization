import React from 'react';
import ReactDOM from 'react-dom';
import {AnonymizePage} from './pages/AnonymizePage';
import { MuiThemeProvider } from '@material-ui/core';
import { theme } from './constants/theme';


ReactDOM.render(
  <React.StrictMode>
      <MuiThemeProvider theme={theme}>
        <AnonymizePage/>
      </MuiThemeProvider>
  </React.StrictMode>,
  document.getElementById('root')
);
