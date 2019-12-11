import React from 'react'
import {Image,Carousel} from 'react-bootstrap'
import background from './assets/footer_background.png'
const Footer = () =>{
  return(
    <div style={{backgroundImage: `url(${background}`,backgroundRepeat:"no-repeat",backgroundSize:"cover",height:"300px"}}>
            <br/><br/>
            <div style={{fontSize:50,color:"white",textAlign:"center"}}>關於我們</div>
               <div style={{fontSize:15,color:"white",textAlign:"center"}}><br/>透過此網站，可以讓您輕易地得知個遊樂設施，或是您欲前往的區域之尖峰時段及人潮數，Follow Me 將會幫<br/></div>
               <div style={{fontSize:15,color:"white",textAlign:"center"}}>您分析各場域熱點，讓您更有效率的分配時間，再也不用跟別人擠 ~</div>
              <div style={{fontSize:15,color:"white",textAlign:"center"}}><br/><br/>64002 雲林縣斗六市大學路3段123號資訊管理系 © Design: follow me.</div>
          </div>
          // <Carousel controls={false} style={{background:"#444444"} }>
          //     <Carousel.Item> 
          //       <Image
          //           src = {background}/>
          //             <Carousel.Caption  style={{top:"10%",fontSize:50}}>
          //                   關於我們
          //                     <div style={{top:"40%",fontSize:15}}><br/><br/>透過此網站，可以讓您輕易地得知個遊樂設施，或是您欲前往的區域之尖峰時段及人潮數，Follow Me 將會幫<br/>您分析各場域熱點，讓您更有效率的分配時間，再也不用跟別人擠 ~</div>
          //                     <div style={{top:"40%",fontSize:15}}><br/><br/>64002 雲林縣斗六市大學路3段123號資訊管理系 © Design: follow me.</div>
          //             </Carousel.Caption>

          //     </Carousel.Item>
          // </Carousel>
  )
}

export default Footer;