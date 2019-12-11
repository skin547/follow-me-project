import {Table,Container,InputGroup,FormControl,Form,Button,Image} from 'react-bootstrap'
import React,{useState, useEffect} from 'react';
import mall from "./assets/mall.jpg"
import station from "./assets/station.jpg"
import playground from "./assets/playground.jpg"
import {Link, useParams} from 'react-router-dom'
import creatHistory from 'history/createBrowserHistory' 
const AddArea=()=>{
  const [name,setName] = useState();
  const [image_path,setImagePath] = useState();
  const history = creatHistory();
  const Upload = (e) => {
    e.preventDefault();
    const data = {"name":name,"image_path":image_path};
    fetch('/api/users', {
      method: 'POST',
      mode:'cors',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      }, 
      body: JSON.stringify(data),
    });
    history.goBack();
  }
  
  return(
    <Container>
      <Table responsive striped bordered hover 
              size="sm" variant="dark" borderless  
              style={{color:"white",marginTop:"7.5%",marginLeft:"7.5%",width:"40rem"}}>

        <thead>
          <tr>
            {/* <td>
              {name}
              {image_path}
            </td> */}
            <td colSpan="3" align="center">

              <InputGroup size="sm" className="mb-3" style={{width:"300px"}}>

                <InputGroup.Prepend>
                  <InputGroup.Text id="inputGroup-sizing-sm">名稱:</InputGroup.Text>
                </InputGroup.Prepend>

                <FormControl aria-label="Small" aria-describedby="inputGroup-sizing-sm"
                        onChange={ (e) => {setName(e.target.value)} }
                        style={{background:"#353a40",color:"white" }}/>
              </InputGroup>
            </td>
          </tr>

          <tr align="center" style={{fontSize:"12pt"}}>    

            <th>
              <Form.Check
                type="radio"
                label="商場"
                name="formHorizontalRadios"
                id="formHorizontalRadios1"
                onChange={(e) => { setImagePath("mall") }}
              />
            </th>

            <th>
              <Form.Check
                type="radio"
                label="遊樂園"
                name="formHorizontalRadios"
                id="formHorizontalRadios1"
                onChange={(e) => { setImagePath("playground")}}
              />
            </th>

            <th>
              <Form.Check
                type="radio"
                label="車站"
                name="formHorizontalRadios"
                id="formHorizontalRadios1"
                onChange={(e) => { setImagePath("station") }}
                
              />
            </th>

          </tr>

          <tr align="left" style={{fontSize:"12pt"}}>
            <th><Image src={mall} style={{height:"200px",height:"200px"}}></Image></th>
            <th><Image src={playground} style={{height:"200px",height:"200px"}}></Image></th>
            <th><Image src={station} style={{height:"200px",height:"200px"}}></Image></th>
          </tr>
        
          <td colSpan="3" align="center">
              <Button style={{color:"white",background:"#00AAAA"}} onClick= {Upload}>submit</Button>
          </td>
        </thead>
      </Table>
    </Container>
    )
  }
export default AddArea;