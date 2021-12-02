import { useState } from 'react';
import {getAnonymizeData} from '../../constants/api/calls/Anonymization/anonymizeData'
import { makeStyles, useTheme, TextField, Button, FormControl, InputLabel, Input  } from '@material-ui/core';
import {SEND_BUTTON, TEXTBOX_LBL, UPLOAD_BUTTON, RESPONSE} from '../../constants/texts/index'
import { urlAnonymizeData } from '../../constants/api/urls';

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
	},
	hideInput: {
		display: 'none'
	},
  }));

export const SendRequest = () => {
	// hooks
	const theme = useTheme()
	const classes = useStyles(theme);
	const [text, setText] = useState('')
	const [message, setMessage] = useState('')
	// handle submit
	const submit = (event) => {
		// prevent default behaviour (reloading)
		event.preventDefault();
		// send data to api
		const config = event.target.jsonText.value
		const file = event.target.uploadFile.files[0]
		// call and response
		getAnonymizeData({config, file})
		.then(data => {
			if(data){
				setMessage(data.message)
			}
		})
	}
	// return
	return (
		<>
			{/* <form action={urlAnonymizeData} enctype="multipart/form-data" method="post">
				<input name="file" type="file" accept='.parquet'/>
				<TextField name='config' className={classes.defaultTextbox} multiline={true} minRows={15} value={text} onChange={e => setText(e.target.value)}/>
				<input type="submit"/>
			</form> */}
			<form action={urlAnonymizeData} enctype="multipart/form-data" method="post">
				<div>
					<p>{TEXTBOX_LBL}</p>
					<TextField name='config' className={classes.defaultTextbox} multiline={true} minRows={15} value={text} onChange={e => setText(e.target.value)}/>
					<Button className={classes.defaultButton}>
						<label>
							<input name='file' type="file" accept='.parquet' className={classes.hideInput}/>
							{UPLOAD_BUTTON}
						</label>
					</Button>
				</div>
				<div>
					<Button name='sendButton' type='submit' className={classes.defaultButton}> {SEND_BUTTON} </Button>
				</div>
			</form>
		</>
	);
}