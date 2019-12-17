import {Table,Container,InputGroup,FormControl,Form,Button} from 'react-bootstrap'
import React,{useState, useEffect} from 'react';
import {Link, useParams, withRouter} from 'react-router-dom'
import creatHistory from 'history/createBrowserHistory' 
const AddFacil=(props)=>{
  const [name,setName] = useState();
  const [capacity,setCapacity] = useState();
  const [source,setsource] = useState();
  let {uid} = useParams();
  const history = creatHistory();
  const Upload = (e) => {
    e.preventDefault();
    const data = {"user_id":uid,"name":name,"capacity":capacity,"source":source};
    fetch('/api/areas', {
      method: 'POST',
      mode:'cors',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      }, 
      body: JSON.stringify(data),
    });
    props.history.push('/Detail/'+uid);
  }
  return(
    <Container>
      <Form onSubmit={Upload}>
        <Table responsive striped bordered hover size="sm" variant="dark" borderless  style={{color:"white",marginTop:"7.5%",marginLeft:"15%",width:"50rem"}}>
        <thead>

            <td colSpan="3" align="center">
              <h1 style={{ color: "white" }}>新增區域</h1>
            </td>
          <tr>
              <td colSpan="3" align="center"><InputGroup size="sm" className="mb-3" style={{width:"300px"}}>
              <InputGroup.Prepend>
              <InputGroup.Text id="inputGroup-sizing-sm">名稱:</InputGroup.Text>
              </InputGroup.Prepend>
              <FormControl aria-label="Small" 
                onChange={ (e) => {setName(e.target.value)} }
                aria-describedby="inputGroup-sizing-sm" style={{background:"#353a40",color:"white"}}/>
              </InputGroup>
              </td>
          </tr>
          <tr>
            <td colSpan="3" align="center">
              <InputGroup size="sm" className="mb-3" style={{width:"300px"}}>
              <InputGroup.Prepend>
                <InputGroup.Text id="inputGroup-sizing-sm">人數上限:</InputGroup.Text>
              </InputGroup.Prepend>
              <FormControl aria-label="Small" 
                onChange={ (e) => {setCapacity(e.target.value)} }
                aria-describedby="inputGroup-sizing-sm" style={{background:"#353a40",color:"white"}}/>
              </InputGroup>
            </td>
          </tr>
          <tr>
            <td colSpan="3" align="center">
              <InputGroup size="sm" className="mb-3" style={{width:"300px"}}>
              <InputGroup.Prepend>
                <InputGroup.Text id="inputGroup-sizing-sm">IP位置:</InputGroup.Text>
              </InputGroup.Prepend>
              <FormControl aria-label="Small" 
                onChange={ (e) => {setsource(e.target.value)} }
                aria-describedby="inputGroup-sizing-sm" style={{background:"#353a40",color:"white"}}/>
              </InputGroup>
              </td>
          </tr>
          <tr>
            <td colSpan="3" align="center">
                <Button style={{color:"white",background:"#00AAAA"}} type='submit' >submit</Button>
            </td>
          </tr>
        </thead>
    </Table>
    </Form>
  </Container>
)
}
export default withRouter(AddFacil);