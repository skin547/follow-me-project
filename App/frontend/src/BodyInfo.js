import React from 'react'
import {Row,Card,ListGroup,ListGroupItem} from 'react-bootstrap'
import background from "./assets/info.JPG"
import red from './assets/r.png'
import green from './assets/g.png'
import yellow from './assets/y.png'
import black from './assets/b.png'
import purple from './assets/p.png'
const BodyInfo = () =>{
    return(
            <div>
                <Showinfo/>
            </div>
    )
}

const Showinfo = ({content}) => {
    return(
            
            <Card style={{ background:"#2d2c32",width: '21rem'}}>
                <Card.Img style = {{height:'10rem'}}variant="top" src={background} />
                <ListGroup className="list-group-flush" >
                    <ListGroupItem style = {{background:"#2d2c32",marginLeft:'7rem',height:'3rem'}}>
                        <Row><img src={purple} style={{height:"1.5rem",width:"1.5rem"}} alt="purple"/>
                        <RowContent text="紫燈 (擁擠)"/> 
                        </Row>
                    </ListGroupItem>
                    <ListGroupItem style = {{background:"#2d2c32",marginLeft:'7rem',height:'3rem'}}>
                        <Row><img src={red} style={{height:"1.5rem",width:"1.5rem"}} alt="red"/>
                        <RowContent text="紅燈 (人多)"/>
                        </Row>
                    </ListGroupItem>
                    <ListGroupItem style = {{background:"#2d2c32",marginLeft:'7rem',height:'3rem'}}>
                        <Row><img src={yellow} style={{height:"1.5rem",width:"1.5rem"}} alt="yellow"/>
                        <RowContent text="黃燈 (適中)"/>
                        </Row>
                    </ListGroupItem>
                    <ListGroupItem style = {{background:"#2d2c32",marginLeft:'7rem',height:'3rem'}}>
                        <Row><img src={green} style={{height:"1.5rem",width:"1.5rem"}}alt="green"/>
                        <RowContent text="綠燈 (人少)"/>
                        </Row>
                    </ListGroupItem>
                    <ListGroupItem style = {{background:"#2d2c32",marginLeft:'7rem',height:'3rem'}}>
                        <Row><img src={black} style={{height:"1.5rem",width:"1.5rem"}}alt="black"/>
                        <RowContent text="灰燈 (尚未開放)"/>
                        </Row>
                    </ListGroupItem>
                </ListGroup>
                
            </Card>
    )
}
const RowContent = ({text}) =>{
    return(
        <Row>
            <p className="text-white" style={{fontSize:20,marginLeft:"1rem"}}> {text}</p>
        </Row>
    )
}
export default BodyInfo