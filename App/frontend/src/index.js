import React,{useState, useEffect} from 'react';
import ReactDOM from 'react-dom';
import './index.css'
import {BrowserRouter as Router} from 'react-router-dom';
import Header from './Header';
import Body from './body';
import Footer from './Footer';
import * as serviceWorker from './serviceWorker';

// function getTodosJson() {
//     let url = 'http://140.125.218.125:5000/api/areas';
//     let todos = [];
//     fetch(url,{mode: 'cors'})
//         .then(res => res.json())
//         .then(json => json.forEach( (todo) => todos.push(todo) ))
//     return todos;
// }


const App = () =>{

    return (
            <div style={{fontFamily:"微軟正黑體"}}>
                {/* {data && data[2].name} */}
                {/* {data && data.map( (item) => <h1>{item.name}</h1>)} */}
                <Router>
                        <Header/>
                        <Body/>
                        <Footer/>
                </Router>
            </div>
    )
}

ReactDOM.render(<App />, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA


    // let url = 'https://jsonplaceholder.typicode.com/todos/';
    // let datas =[];
    // fetch(url)
    //     .then(res => res.json())
    //     .then(json => json.forEach( (data) => datas.push(data) ))
    // return datas;
    
   
serviceWorker.unregister();