import {useState,useEffect} from 'react'

export default function Ans({value:value}){
    
    const [as,set_as] = useState(value);
    const [score,setScore] = useState(value[4]);
    // set_as(value);
    console.log(value[0])

    
    function inc(){
      fetch(`/${value[0]}/upans`).then((res) =>
      res.json().then((data) => {
        console.log(data);
        setScore(data)
      })
      );
    }

    function dec(){
      fetch(`/${value[0]}/downans`).then((res) =>
      res.json().then((data) => {
        console.log(data);
        setScore(data)
      })
      );
    }    

    useEffect(() => {
    
      fetch(`/${value[0]}/answers`).then((res) =>
      res.json().then((data) => {
        // console.log(data);
        set_as(data)
      })
      );
  
  },[score]);

    return(
<>
        {/* Answers */}
        <div class="row mt-3 d-flex flex-row">
          <div class="d-flex justify-content-end">
            <div  class="question_box col-xl-8 col-lg-8 col-md-11 col-sm-12 col-12 p-2 d-flex flex-column">
              <div class="row px-3 mt-1">
              <div class="like_box col-2 px-3 ms-3 mt-1">
                <div class="like">
                <svg onClick={()=>{console.log("cr");inc()}}  class="like" width="20" height="20" fill="currentColor" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" >
                  <path d="M313.4 32.9c26 5.2 42.9 30.5 37.7 56.5l-2.3 11.4c-5.3 26.7-15.1 52.1-28.8 75.2H464c26.5 0 48 21.5 48 48c0 18.5-10.5 34.6-25.9 42.6C497 275.4 504 288.9 504 304c0 23.4-16.8 42.9-38.9 47.1c4.4 7.3 6.9 15.8 6.9 24.9c0 21.3-13.9 39.4-33.1 45.6c.7 3.3 1.1 6.8 1.1 10.4c0 26.5-21.5 48-48 48H294.5c-19 0-37.5-5.6-53.3-16.1l-38.5-25.7C176 420.4 160 390.4 160 358.3V320 272 247.1c0-29.2 13.3-56.7 36-75l7.4-5.9c26.5-21.2 44.6-51 51.2-84.2l2.3-11.4c5.2-26 30.5-42.9 56.5-37.7zM32 192H96c17.7 0 32 14.3 32 32V448c0 17.7-14.3 32-32 32H32c-17.7 0-32-14.3-32-32V224c0-17.7 14.3-32 32-32z"/></svg>
                </div>
                <div class="like d-flex justify-content-center ">
                 {score}``
                </div>
                <div class="like">
                <svg onClick={()=>{console.log("cr");dec()}}   class="like" width="20" height="20" fill="currentColor" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
                <path d="M0 56v240c0 13.255 10.745 24 24 24h80c13.255 0 24-10.745 24-24V56c0-13.255-10.745-24-24-24H24C10.745 32 0 42.745 0 56zm40 200c0-13.255 10.745-24 24-24s24 10.745 24 24-10.745 24-24 24-24-10.745-24-24zm272 256c-20.183 0-29.485-39.293-33.931-57.795-5.206-21.666-10.589-44.07-25.393-58.902-32.469-32.524-49.503-73.967-89.117-113.111a11.98 11.98 0 0 1-3.558-8.521V59.901c0-6.541 5.243-11.878 11.783-11.998 15.831-.29 36.694-9.079 52.651-16.178C256.189 17.598 295.709.017 343.995 0h2.844c42.777 0 93.363.413 113.774 29.737 8.392 12.057 10.446 27.034 6.148 44.632 16.312 17.053 25.063 48.863 16.382 74.757 17.544 23.432 19.143 56.132 9.308 79.469l.11.11c11.893 11.949 19.523 31.259 19.439 49.197-.156 30.352-26.157 58.098-59.553 58.098H350.723C358.03 364.34 384 388.132 384 430.548 384 504 336 512 312 512z"/></svg>
                </div>
              </div>
                <div class="col-xl-10 col-lg-10 col-md-10 col-sm-10 col-10 px-2 d-flex justify-content-center">
                  <div class="answer_title_par col-11 p-1 d-flex justify-content-center flex-column" style ={{"font-size":"x-large", "color":"3A4D3A","cursor": "pointer"}}>
                    {value[5]?<div dangerouslySetInnerHTML={{__html:value[5].substring(1, value[5].length-1)}} />:<></>}
                  </div>
                </div>
              </div>
              <div class="row d-flex justify-content-end px-3 mb-1">
                <div  class="col-xl-2 col-lg-2 col-md-2 col-sm-12 col-12 mt-3 justify-content-center post_data_box">
                  <div class="row px-2 d-flex">
                    <div class="post_title">
                        Posted by :- 
                    </div>
                    <div class="user_p4" >
                        <div class="d-flex justify-content-start">
                            <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16">
                                <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/>
                                <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"/>
                            </svg>
                        </div>
                    </div>
                    <div class="row px-2 d-flex flex-column">
                        <div class="post_title">
                            Posted on :- 
                        </div>
                        <div class="user_pp d-flex float-end " style={{"font-size": "large","color": "E7E4DF"}}>
                          {value[2]}
                        </div>
                  </div>
                </div>
              </div>
            </div>
          </div> 
        </div>

      {/* question date and posted user */}
      
      </div>
      </>
    
    );
  }
