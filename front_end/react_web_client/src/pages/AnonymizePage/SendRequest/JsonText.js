import { makeStyles } from '@material-ui/core/styles';
import { TextField, useTheme } from '@material-ui/core';

const useStyles = makeStyles((theme) => ({
	defaultTextbox: {
	}
  }));

export const JsonText = ({label, text,setText}) => {
	const theme = useTheme()
	const classes = useStyles(theme);
	return (
		<>
			<label>{label}</label>
			<TextField value={text} onChange={e => setText(e.target.value)}/>
		</>
	);
}
