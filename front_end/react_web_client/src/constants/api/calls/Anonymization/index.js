/**
 * Define specific parameters and make the callings
 * For APIs
 * Any API related logic also
 */

import {ApiGet} from '../index'
import {urlAnonymizeData} from '../../urls'


export const getAnonymizeData = async () => {
	const call = 
		await ApiGet(urlAnonymizeData)
		.then(data =>{
			// Include any data preprocessing, before it is handled by react component
			return data.accuracy
		})
	return call
}