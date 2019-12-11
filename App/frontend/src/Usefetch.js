import {useState, useEffect} from 'react'

const useFetch = (url,option) => {
    const [response, setResponse] = useState(null);
    useEffect(  () => {
        fetch(url,option)
        .then(res => res.json())
        .then(json => setResponse(json))
        .catch(error => console.log(error))
        return response;
        // const fetchData = async() =>{
        //         const res = await fetch(url, option).catch(error => console.log(error));
        //         const json = await res.json();
        //         setResponse(json);
        //     }
        // fetchData();
        // return response;
    });
}

export default useFetch;