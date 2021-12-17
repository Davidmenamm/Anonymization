/* Main Theme */

/* imports */
 import { createMuiTheme } from '@material-ui/core';
 import { Colors } from './colors';

 /* theme */
export const theme = createMuiTheme({
	palette: {
	  primary: {
		main: Colors.principal,
	  },
	  secondary: {
		main: Colors.secondary,
	  },
	  contrast: {
		background: Colors.background,
		dark: Colors.dark,
		white: Colors.white,
	  },
	  specific: {
		topMenu: Colors.topMenu,
	  },
	  events: {
		success: Colors.success,
		error: Colors.error,
		warning: Colors.warning,
		important: Colors.important,
	  },
	},
	styles: {
	  borderRadius: '',
	  border: {
		backgroundColor: 'white',
		borderColor: '#ccc',
		borderRadius: '',
		borderStyle: 'solid',
		borderWidth: '1px',
		boxShadow: '0 0.125rem 0.25rem rgba(0, 0, 0, 0.075)',
	  },
	},
	overrides: {
	  MuiRadio: {
		root: {
		  color: Colors.principal,
		  '&$checked': {
			color: Colors.principal,
		  },
		},
		checked: {},
	  },
	},
  });


