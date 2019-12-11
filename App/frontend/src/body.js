import React,{useState,useEffect}from 'react'
import {Row,Container} from 'react-bootstrap'
import {Route, Switch} from 'react-router-dom'
import TotalInfo from "./TotalInfo"
import Detail from "./Detail"
import AddArea from "./AddArea"
import AddFacil from './AddFacil'
import FacilDetail from './FacilDetail'
const Body =({users}) =>{
    const [data,setData] = useState();
    useEffect( ()=> { async function fetchData(){
        let url = '/api/users';
        let users = [];
        await fetch(url,{mode: 'cors'})
            .then(res => res.json())
            .then(json => json.forEach( (todo) => users.push(todo)))
            .then(json => setData(users))};
          fetchData();
        // setData(users);
        } ,[] );  
    return(
        <div style={{background :"#353a40"}}>
        <Container >
        
            {/* <br/><br/><br/> */}
            {/* <Switch> */}
                <Container fluid>
                    <Row  style={{background :"#353a40"}}>
                        <Route exact path='/' component={() => <TotalInfo users={data} />}  />
                        <Route path='/Info' component={() => <TotalInfo users={data} />} />
                        <Route path='/Detail/:id' component={Detail}/>
                        <Route path='/AddArea' component={AddArea}/>
                        <Route path='/AddFacil/:uid' component={AddFacil}/>
                        <Route path='/FacilDetail/:uid' component={FacilDetail}/>
                    </Row>
                </Container>
            {/* </Switch> */}
            <br/><br/><br/>
         </Container>
        </div>
    )
}  
export default Body;