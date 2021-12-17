/* send request component */

/* imports */
import { useState } from 'react';
import { makeStyles, useTheme, TextField, Button } from '@material-ui/core';
import { SEND_BUTTON, TEXTBOX_LBL, UPLOAD_BUTTON } from '../../constants/texts/index'
import { urlAnonymizeData } from '../../constants/api/urls';

/* styles */
const useStyles = makeStyles((theme) => ({
	defaultButton: {
		backgroundColor: theme.palette.primary.main,
		borderColor: theme.palette.primary.main,
		color: theme.palette.contrast.white
	},
	defaultTextbox: {
		width: '40rem'
	},
	hideInput: {
		display: 'none'
	},
  }));

/* component */
export const SendRequest = () => {
	// hooks
	const theme = useTheme()
	const classes = useStyles(theme);
	const [text, setText] = useState('')
	// return
	return (
		<>
			{/* form */}
			<form action={urlAnonymizeData}
				enctype="multipart/form-data"
				method="post">
				<div>
					{/* textfield */}
					<p>{TEXTBOX_LBL}</p>
					<TextField name='config'
						className={classes.defaultTextbox}
						multiline={true}
						minRows={15}
						value={text}
						onChange={e => setText(e.target.value)}/>
					{/* upload button */}
					<Button className={classes.defaultButton}>
						<label>
							<input name='file'
								type="file"
								accept='.parquet'
								className={classes.hideInput}/>
							{UPLOAD_BUTTON}
						</label>
					</Button>
				</div>
				<div>
					{/* send button */}
					<Button name='sendButton'
						type='submit'
						className={classes.defaultButton}>
							{SEND_BUTTON}
					</Button>
				</div>
			</form>
		</>
	);
}


