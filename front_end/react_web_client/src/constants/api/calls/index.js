/**
 * Api calls main functions
 */

import { download } from "./download"

// GET
export const ApiGet = async (url) => {
	return await fetch(url)
	.then(response => response.json())
}


// // POST
// export const ApiPost = async ({url, body = {}, receiveType = 'json', options = {} }) => {
// 	return await fetch(url, {
//         method: "post",
//         body
//     })
// 	.then(response => {
// 		//buffer to fill with all data from server
// 		let pdfContentBuffer = new Int8Array();
	
// 		// response.body is a readableStream 
// 		const reader = response.body.getReader();
	
// 		//function to retreive the next chunk from the stream
// 		function handleChunk({ done, chunk })  {
// 			console.log('chunk')
// 			console.log(chunk)
// 			if (done) {
// 				//everything has been loaded, call `download()` to save gthe file as pdf and name it "my-file.pdf"
// 				download(pdfContentBuffer, `my-file.csv`, 'text/csv')
// 				return;
// 			}
		
// 			// concat already loaded data with the loaded chunk
// 			pdfContentBuffer = Int8Array.from([...pdfContentBuffer, ...chunk]);
		
// 			// retreive next chunk
// 			reader.read().then(({done,chunk}) => handleChunk({done,chunk}))
// 		}
	
// 		//retreive first chunk
// 		reader.read().then(handleChunk)
// 	})
// 	.catch(err => console.error(err))
// }



// // POST
// export const ApiPost = async ({url, body = {}, receiveType = 'json', options = {} }) => {
// 	return await fetch(url, {
//         method: "post",
//         body
//     })
// 	.then(response => {
// 		let data = response
// 		if(receiveType === 'json'){
// 			data = response.json()
// 		}
// 		else if(receiveType === 'file'){
// 			// get data from header
// 			const header = headerObject(response.headers)
// 			const file_name = header['content-disposition']['filename']
// 			const type = header['content-disposition']['attachment']
// 			// download
// 			data = download({response, file_name, type})
// 		}
// 		return data
// 	})
// }



// POST
export const ApiPost = async ({url, body = {}, receiveType = 'json', options = {} }) => {
	return await fetch(url, {
        method: "post",
        body
    })
	.then(response => response.blob()).then( response => {
		let data = response
		if(receiveType === 'json'){
			data = response.json()
		}
		else if(receiveType === 'file'){
			const blob = new Blob([response], {type: "octet/stream"})
			// blob url
			const url = window.URL.createObjectURL(blob)
			console.log(url)
			// new link element not visible
			const a = document.createElement('a')
			a.style.display = 'none';
			a.href = url
			// filename
			a.download = 'david.csv'
			// target
			a.target = '_blank'
			// append link
			document.body.appendChild(a)
			// click link
			a.click()
			// remove from document
			document.body.removeChild(a)
			window.URL.revokeObjectURL(url)
		}
		return data
	})
}



// Get header as object
const headerObject = (header_iterator) => {
	// iterate header elements
	const root = {}
	for (const [elem, value] of header_iterator.entries()) {
		console.log(elem)
		console.log(value)
		// build content
		root[elem] = {}
		// parse content
		const value_parsed = value.replace(/\s+/g, '').split(';')
		console.log(value_parsed)
		// add params
		for (const param of value_parsed){
			console.log(param)
			// split params
			const keyValParam = param.split('=')
			// normal params
			if( keyValParam.length === 2){
				root[elem][keyValParam[0]] = keyValParam[1]
			}
			// no '=' in param (ej inline)
			else {
				root[elem][keyValParam[0]] = keyValParam[0]
			}
		}
	}	
	// return
	return root
}