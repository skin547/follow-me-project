import React from 'react'
import {Image,Carousel} from 'react-bootstrap'
import background from './assets/banner2.jpg'
import {Link, } from 'react-router-dom'
const Header = () =>{
  return(
          <div style={{backgroundImage: `url(${background}`,backgroundRepeat:"no-repeat",backgroundSize:"cover",height:"400px"}}>
            <br/><br/><br/><br/><br/><br/><br/>
              <Link to = "/"><p style={{textAlign:"center",color:"white",fontFamily:"Algerian",fontSize:75}}><strong>Follow Me</strong></p></Link>
               <div style={{fontFamily:"Microsoft YaHei",color:"white",textAlign:"center"}}><h3>跟著我，一起節省您寶貴的時間✌</h3></div>
          </div>

        // <Carousel controls={false}>
        //        <Carousel.Item>
        //           <Image 
        //               src={background} 
        //               fluid
        //           />  
        //                <Carousel.Caption style={ {top:"40%",fontFamily:"Algerian",fontSize:50}}>
        //                <Link to = "/" style={{color:"white"}}><strong>Follow Me</strong></Link>
        //                       <div style={{fontFamily:"Microsoft YaHei"}}><h3>跟著我，一起節省您寶貴的時間✌</h3></div>
        //               </Carousel.Caption>
                      
        //       </Carousel.Item> 
        //   </Carousel>
  )
}

export default Header;

