/**
 * Define specific parameters and make the callings
 * For APIs
 * Any API related logic also
 */
import {ApiPost} from '../index'
import {urlAnonymizeData} from '../../urls'


/**
 * Define API expected response
 */
const output = {
	message : 'string'
}



/**
 * @param
 * @returns Promise with result of API
 */
export const getAnonymizeData = async ({config, file}) => {
	// Body
	let body = new FormData()
	body.append('file', file)
	body.append('config', config)
	// Promise
	const call = 
		await ApiPost({url: urlAnonymizeData, body:body, receiveType:'file'})
		.then(data =>{
			// Include any data preprocessing, before it is handled by react component
			let results = {}
			// if (data){
			// 	for (const key in output) {
			// 		if (data[key] && typeof(data[key]) === output[key]){
			// 			results[key] = data[key]
			// 		}
			// 		else {
			// 			results = null
			// 			break
			// 		}
			// 	}
			// }
			// return
			return results
		})
	return call
}