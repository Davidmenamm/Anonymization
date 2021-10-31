import { useState } from 'react';
import {getAnonymizeData} from '../../constants/api/calls/Anonymization/anonymizeData'
import { makeStyles, useTheme, TextField, Button  } from '@material-ui/core';
import {SEND_BUTTON, TEXTBOX_LBL, UPLOAD_BUTTON, RESPONSE} from '../../constants/texts/index'

const useStyles = makeStyles((theme) => ({
	uploadButton: {
		marginLeft:"10rem"
	},
	defaultButton: {
		backgroundColor: theme.palette.primary.main,
		borderColor: theme.palette.primary.main,
		color: theme.palette.contrast.white
	},
	defaultTextbox: {
		width: '40rem'
	},
	response:{
		marginTop: '5rem'
	}
  }));

export const SendRequest = () => {
	// hooks
	const theme = useTheme()
	const classes = useStyles(theme);
	const [text, setText] = useState('')
	const [message, setMessage] = useState('')
	// handle submit
	const submit = (e) => {
		e.preventDefault();
		getAnonymizeData()
		.then(data => {
			if(data){
				setMessage(data.message)
			}
		})
	}
	// return
	return (
		<>
			<form onSubmit = {submit}>
				<div>
					<label>{TEXTBOX_LBL}</label>
					<TextField className={classes.defaultTextbox} multiline={true} minRows={15} value={text} onChange={e => setText(e.target.value)}/>
					<Button className={classes.defaultButton}> {UPLOAD_BUTTON} </Button>
				</div>
				<div>
					<Button type={'submit'} className={classes.defaultButton}> {SEND_BUTTON} </Button>
				</div>
			</form>
			<div className = {classes.response}>
				<label> {RESPONSE} </label>
				{message}
			</div>
		</>
	);
}
