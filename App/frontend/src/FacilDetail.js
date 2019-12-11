import {Table,Container,InputGroup,FormControl,Form,Button} from 'react-bootstrap'
import React,{useState, useEffect} from 'react';
import {Link, useParams, withRouter} from 'react-router-dom'
const FacilDetail=(props)=>{
  let {uid} = useParams();
  var url = "http://localhost:5000/api/video/"+uid;
  // var url = "/api/video/"+Vid;
  // console.log(url);
    return(
            <div className="embed-responsive embed-responsive-16by9" style={{marginTop:"5%",marginLeft:"12.5%",width:"900px",height:"650px"}}>
                <iframe title="Embeds Page" className="embed-responsive-item" src={url}
                allowfullscreen></iframe>
            </div>
    )
}
export default withRouter(FacilDetail);