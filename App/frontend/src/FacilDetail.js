import {Table} from 'react-bootstrap'
import React,{useState, useEffect} from 'react';
import {useParams, withRouter} from 'react-router-dom'
import {Vid} from './Detail';
const FacilDetail=(props)=>{
  let {uid} = useParams();
  const [area, setArea] = useState();
  const [vid, setVid] = useState();

  useEffect(() => {
    async function fetchData() {
      let url = '/api/areas/' + uid;
      let temp;
      await fetch(url, { mode: 'cors' })
        .then(res => res.json())
        .then(json => temp = json)
      setArea(temp);
      console.log(temp);
      setVid(temp.video_id);
    };
    fetchData();

  }, []);

    return(
      <div>
        <h1 style={{ color: 'white', marginLeft: "46%", marginTop: "2.5%" }}>{area && area.name} </h1>
          {vid ?
          <Vid Vid={vid} />
          : <h1 style={{ color: 'white', marginLeft: "46%", marginTop: "2.5%" }}>Video loading....</h1>}
        {area && <FrameList frames={area.frames} />}
      </div>
    )
}


const FrameList = ({frames}) => {
  const [list, setList] = useState(frames);
  return(
    <Table responsive striped bordered hover size="sm" variant="dark" borderless style={{ color: "white", marginTop: "2%", marginLeft: "15%", width: "50rem" }}>
      <thead>
        <tr align="center" style={{ fontSize: "15pt" }}>
          <th>時間</th>
          <th>人數</th>
        </tr>
      </thead>
      <tbody>
        {

          list.map((frame) => {
            return (
              <tr align='center'>
                <td>{frame.time}</td>
                <td>{frame.number}</td>
              </tr>
            )
          })
        }
      </tbody>
    </Table>
  )
}


export default withRouter(FacilDetail);