import { useState, useEffect } from 'react';
import { JsonText } from './JsonText'
import { SendButton } from './SendButton'
import {getAnonymizeData} from '../../../constants/api/calls/Anonymization/index'

export const SendRequest = () => {
	// hooks
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
				<JsonText text={text} setText={setText}/>
				<SendButton/>
			</form>
			<div>
				{message}
			</div>
		</>
	);
}
