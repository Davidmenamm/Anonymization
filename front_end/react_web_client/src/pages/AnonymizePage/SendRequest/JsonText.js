import {Textbox} from '../../../common/UI/Textbox'

export const JsonText = ({text,setText}) => {
	return (
		<>
			<label>Enter your name:</label>
			<Textbox text={text} setText = {setText}/>
		</>
	);
}
