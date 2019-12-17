import React ,{useState, useEffect} from 'react'
import {Row,Col,Table,Card,Button, Image} from 'react-bootstrap'
import BodyInfo from "./BodyInfo"
import BodyContent from "./BodyContent"
import mall from "./assets/mall.jpg"
import playground from "./assets/playground.jpg"
import station from "./assets/station.jpg"
import {Link, } from 'react-router-dom'
import Detail from "./Detail"
import {Route, Switch} from 'react-router-dom'

const TotalInfo = ({users}) =>{
  return(
    <div>
      <Link to ="/AddArea"><p style={{color:"#FF8C00",marginTop:"2%"}}>+新增一筆場域資料</p></Link>
      <div style={{marginTop:"2%"}}>
                  <Row>                   
                    {
                     <BigButt datas = {users}></BigButt>
                    }
                    {/* <Col align="center"><BodyInfo/></Col>
                    <Col align="center"><BodyContent/></Col>  */}
                  </Row>
       </div> 
    </div>
  )
}
const BigButt=({datas = []}) =>{ 
  var path = "/Detail/";
  return(
    
    datas.map( (data) =>
    
    <Col xs='12' sm='4' md ='4' style={{marginTop:"1%",marginBottom:"1%"}}>
      
      <Link to ={{pathname:path+data.id}}>
        <Image src={showImage(data.image_path)} style={{marginTop:"7.5%",marginLeft:"10%",height:"250px",width:"250px"}} roundedCircle thumbnail/>
        <p style={{color:"white",marginLeft:"40%",marginTop:"2%"}}>{data.name}</p>
      </Link>
    </Col>
    )
  )
  
}
const showImage =(status)=>{
  if(status==="mall"){
    return mall;
  }
  else if(status==="playground"){
    return playground;
  }
  else if(status==="station"){
    return station;
  }
};
export default TotalInfo;
export {showImage};