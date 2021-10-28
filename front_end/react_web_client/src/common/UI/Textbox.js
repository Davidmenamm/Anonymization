

export const Textbox = ({text,setText}) => {
	return (
		<>
			<input value={text} onChange={e => setText(e.target.value)} style={{marginLeft:'1.2rem'}}/>
		</>
	);
}
