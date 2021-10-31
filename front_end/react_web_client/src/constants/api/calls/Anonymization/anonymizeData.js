/**
 * Define specific parameters and make the callings
 * For APIs
 * Any API related logic also
 */
import {ApiGet} from '../index'
import {urlAnonymizeData} from '../../urls'

/**
 * Define API expected input
 */
const input = {}


/**
 * Define API expected output
 */
const output = {
	message : 'string'
}



/**
 * @param
 * @returns Promise with result of API
 */
export const getAnonymizeData = async () => {
	const call = 
		await ApiGet(urlAnonymizeData)
		.then(data =>{
			// Include any data preprocessing, before it is handled by react component
			let results = {}
			if (data){
				for (const key in output) {
					if (data[key] && typeof(data[key]) === output[key]){
						results[key] = data[key]
					}
					else {
						results = null
						break
					}
				}
			}
			// return
			return results
		})
	return call
}