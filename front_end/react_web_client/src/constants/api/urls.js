/**
 * All endpoints
 */

// Host:
// local
const baseProtocolAndHost = 'http://localhost'
const basePort = 4557
const localBaseUrl = `${baseProtocolAndHost}:${basePort}`
// production
const prodBaseUrl = process.env.REACT_APP_BACKEND_URL
// active base url
const baseUrl = prodBaseUrl || localBaseUrl

// Categories:
// anonymization
export const urlAnonymizeData = `${baseUrl}/endpoints/data_science/anonymization/`