import { useState } from 'react';
import { JsonText } from './JsonText'
import { SendButton } from './SendButton'
import {getAnonymizeData} from '../../../constants/api/calls/Anonymization/index'
import {SEND_BUTTON, TEXTBOX_LBL} from '../../../constants/texts/index'
import { makeStyles, useTheme } from '@material-ui/core';

const useStyles = makeStyles((theme) => ({
	content: {
		display: 'flex'
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
			setMessage(data)
		})
	}
	// return
	return (
		<>
			<form onSubmit = {submit}>
				<JsonText label={TEXTBOX_LBL} text={text} setText={setText}/>
				<SendButton name={SEND_BUTTON}/>
			</form>
			<div>
				{message}
			</div>
		</>
	);
}
