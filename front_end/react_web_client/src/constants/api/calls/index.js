/**
 * Api calls main functions
 */

export const ApiGet = async (url) => {
	return await fetch(url)
	.then(response => response.json())
}