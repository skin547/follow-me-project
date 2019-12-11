import React,{useState, useEffect} from 'react';
import {Row,Button,Card,ListGroup,ListGroupItem} from 'react-bootstrap'
import head from "./assets/mall.jpg"
import red from './assets/r.png'
import green from './assets/g.png'
import yellow from './assets/y.png'
import black from './assets/b.png'
import purple from './assets/p.png'
import {Link, } from 'react-router-dom'
const BodyContent = ({users}) =>{
    const [data,setData] = useState();
    useEffect( () => { async function fetchData(){
        let url = 'http://172.20.10.2:5000/api/areas';
        let users = [];
        await fetch(url,{mode: 'cors'})
            .then(res => res.json())
            .then(json => json.forEach((todo) => users.push(todo)))
        setData(users);};
        fetchData();
        } ,[] );
    return(
        <div>
                <Content users={data}/> 
        </div>     
    )
}
const light =(status)=>{
    if(status==="gray"){
      return black;
    }
    else if(status==="green"){
      return green;
    }
    else if(status==="yellow"){
      return yellow;
    }
    else if(status==="red"){
      return red;
    }
    else if(status==="purple"){
      return purple;
    }
  };
const Content = ({users}) => {
    
    return(
            <Card style={{ background:"#2d2c32",width: '21rem'}}>
                <Card.Img style={{height:'10rem'}} variant="top" src={head} />
                    <ListGroup>
                    <ListGroupItem style = {{background:"#2d2c32",marginLeft:'8.5rem',height:'3rem'}}>
                        <RowContent text="Mall"/> 
                    </ListGroupItem>
                    <ListGroupItem style = {{background:"#2d2c32",marginLeft:'8rem',height:'3rem'}}>
                        <Row>
                        <RowContent text="結帳台1"/>
                        <img src={light(users && users[0].status)} style={{height:"1.5rem",width:"1.5rem",marginLeft:"1rem"}}/>
                        </Row>
                    </ListGroupItem>
                    <ListGroupItem style = {{background:"#2d2c32",marginLeft:'8rem',height:'3rem'}}>
                        <Row>
                        <RowContent text="結帳台2"/>
                        <img src={light(users && users[1].status)} style={{height:"1.5rem",width:"1.5rem",marginLeft:"1rem"}} alt="yellow"/>
                        </Row>
                    </ListGroupItem>
                    <ListGroupItem style = {{background:"#2d2c32",marginLeft:'8rem',height:'3rem'}}>
                        <Row>
                        <RowContent text="結帳台3"/>
                        <img src={light(users && users[2].status)} style={{height:"1.5rem",width:"1.5rem",marginLeft:"1rem"}}alt="green"/>
                        </Row>
                    </ListGroupItem>
                    <ListGroupItem style = {{background:"#2d2c32",marginLeft:'6rem',height:'3rem'}}>
                        <Row>
                        <Link to ={"/Detail"}>
                            <Button variant="flat"  style={{fontSize:16,background:"#7744FF",color:"white",height:"2.5rem",marginTop:"-0.5rem"}} >點擊以看更多</Button>
                        </Link>
                        </Row>
                    </ListGroupItem>
                </ListGroup>
            </Card>
    )
}
const RowContent = ({text}) =>{
    return(
        <Row>
            <p className="text-white" style={{fontSize:20}}> {text}</p>
        </Row>
    )
}


export default BodyContent