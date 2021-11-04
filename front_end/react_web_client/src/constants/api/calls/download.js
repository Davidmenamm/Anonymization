/* Handle download */

// Download function
export const download = ( {response, file_name, type='attachment'} ) => {
	response.blob().then(blob =>{
		if( type === 'attachment'){
			// blob url
			const url = window.URL.createObjectURL(blob);
			console.log(url)
			// new link element not visible
			const a = document.createElement('a');
			a.style.display = 'none';
			a.href = 'data:application/octet-stream;' + url;
			// filename
			a.download = file_name;
			// target
			a.target = '_blank'
			// append link
			document.body.appendChild(a);
			// click link
			a.click();
			// remove from document
			document.body.removeChild(a);
			window.URL.revokeObjectURL(url);
		}
	})
  }