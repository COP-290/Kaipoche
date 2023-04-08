import { useEffect,useState,useRef } from "react";
import "highlight.js/styles/github.css";
import hljs from "highlight.js";
import JoditEditor from "jodit-react";
import Ans from "./ans";
import { useNavigate, useParams } from "react-router-dom";
// import Ans from './ans'

export default function Par_ques() {
  
  let navigate = useNavigate();
  const to = async (id) => {
    let path = `/${id}`;
    navigate(path);
  //   await scroller.scrollTo("head", {
  //     duration: 1500,
  //     offset: 0,
  //   });
  };

  const editor = useRef(null);
  const [content,setContent] = useState('');
  const [data,setdata] = useState(0);
  const [ans,setans] = useState(0);
  const [score,setScore] = useState(0);
  const { id } = useParams(); 

  useEffect(()=>{
    hljs.highlightAll();
  });

  useEffect(() => {
    
    fetch(`/${id}/answer`).then((res) =>
    res.json().then((data) => {
      // console.log(data);
      setdata(data)
    })
    );
    
    fetch(`/${id}/answers`).then((res) =>
    res.json().then((data) => {
      // console.log(data);
      setans(data)
    })
    );

},[score]);

  function inc(){
    fetch(`/${id}/upscore`).then((res) =>
    res.json().then((data) => {
      console.log(data);
      setScore(data)
    })
    );
  }

  function dec(){
    fetch(`/${id}/downscore`).then((res) =>
    res.json().then((data) => {
      console.log(data);
      setScore(data)
    })
    );
  }

function api(id,Answer){
  fetch(`/${id}/new_ans`, {
      method: 'POST',
      body: JSON.stringify({
        'Answer':Answer,
      }),
      headers: {
        'Content-type': 'application/json; charset=UTF-8',
      }
      })
      .then(function(response){ 
      return response.json()})
      .then(function(data)
      {console.log(data)
    }).catch(error => console.error('Error:', error)); 

}

    return (
        <>
        <body >

  <div class="row d-flex flex-row">
      <div class="row">
          <div class="question_title col-xl-9 col-lg-9 col-md-9 col-sm-12 col-12 px-5 d-flex justify-content-start">
              {data?data[0][4]:""}
          </div>
          <div class ="col-xl-3 col-lg-3 col-md-3 col-sm-12 col-12 px-4 py-2 d-flex justify-content-end">
              <button type="button" class=" ask_btn btn btn-success" onClick={()=>to('new_question')}>
                Ask question
              </button>
          </div>
      </div>

      <div class="row mt-3">
        <div class="d-flex justify-content-center">
          <div class="question_box col-xl-8 col-lg-8 col-md-11 col-sm-12 col-12 p-2 d-flex flex-column">

            <div class="row like_box+answer">
              <div class="like_box col-2 px-3 ms-3 mt-1">
                <div class="like">
                <svg onClick={()=>{console.log("cr");inc()}}  class="like" width="20" height="20" fill="currentColor" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" >
                  <path d="M313.4 32.9c26 5.2 42.9 30.5 37.7 56.5l-2.3 11.4c-5.3 26.7-15.1 52.1-28.8 75.2H464c26.5 0 48 21.5 48 48c0 18.5-10.5 34.6-25.9 42.6C497 275.4 504 288.9 504 304c0 23.4-16.8 42.9-38.9 47.1c4.4 7.3 6.9 15.8 6.9 24.9c0 21.3-13.9 39.4-33.1 45.6c.7 3.3 1.1 6.8 1.1 10.4c0 26.5-21.5 48-48 48H294.5c-19 0-37.5-5.6-53.3-16.1l-38.5-25.7C176 420.4 160 390.4 160 358.3V320 272 247.1c0-29.2 13.3-56.7 36-75l7.4-5.9c26.5-21.2 44.6-51 51.2-84.2l2.3-11.4c5.2-26 30.5-42.9 56.5-37.7zM32 192H96c17.7 0 32 14.3 32 32V448c0 17.7-14.3 32-32 32H32c-17.7 0-32-14.3-32-32V224c0-17.7 14.3-32 32-32z"/></svg>
                </div>
                <div class="like_no d-flex justify-content-center ">
                 {data?data[0][3]:""}
                </div>
                <div class="like">
                <svg onClick={()=>{console.log("cr");dec()}}   class="like" width="20" height="20" fill="currentColor" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
                <path d="M0 56v240c0 13.255 10.745 24 24 24h80c13.255 0 24-10.745 24-24V56c0-13.255-10.745-24-24-24H24C10.745 32 0 42.745 0 56zm40 200c0-13.255 10.745-24 24-24s24 10.745 24 24-10.745 24-24 24-24-10.745-24-24zm272 256c-20.183 0-29.485-39.293-33.931-57.795-5.206-21.666-10.589-44.07-25.393-58.902-32.469-32.524-49.503-73.967-89.117-113.111a11.98 11.98 0 0 1-3.558-8.521V59.901c0-6.541 5.243-11.878 11.783-11.998 15.831-.29 36.694-9.079 52.651-16.178C256.189 17.598 295.709.017 343.995 0h2.844c42.777 0 93.363.413 113.774 29.737 8.392 12.057 10.446 27.034 6.148 44.632 16.312 17.053 25.063 48.863 16.382 74.757 17.544 23.432 19.143 56.132 9.308 79.469l.11.11c11.893 11.949 19.523 31.259 19.439 49.197-.156 30.352-26.157 58.098-59.553 58.098H350.723C358.03 364.34 384 388.132 384 430.548 384 504 336 512 312 512z"/></svg>
                </div>
              </div>
              <div class="col-10 px-2 d-flex justify-content-center">
                <div class="answer_title_par col-11 p-1 d-flex justify-content-center flex-column" style ={{"font-size":"x-large", "color":"3A4D3A","cursor": "pointer"}}>
                  {data?<div dangerouslySetInnerHTML={{__html:data[0][5]}} />:<></>}
                </div>
              </div> 
            </div>  
            
            <div class="row tag+post_data_box d-flex justify-content-end flex-row">
              <div class="col-xl-10 col-lg-10 col-md-10 col-sm-12 col-12 mt-3">
                <div class="d-flex tag_box_par flex-row flex-wrap justify-content-start px-3">
                    {data[1]?  Object.entries(data[1]).map(([key,value])=>
                    <>
                        <div class=" justify-content-center">
                        <a class="num_button py-2 px-3" >
                          {value[0]}
                        </a>
                      </div>
                    </>
                      
                    ):<></>}
                    </div>
                </div>
                <div  class="col-xl-2 col-lg-2 col-md-2 col-sm-12 col-12 mt-3 me-3 post_data_box mb-1">
                    <div class="row px-2 d-flex">
                        <div class="post_title">
                            Posted by :- 
                        </div>
                        <div class="user_p" >
                            <div class="d-flex justify-content-start">
                                <svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16">
                                    <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/>
                                    <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"/>
                                </svg>
                              </div>
                        </div>
                      </div>
                    <div class="row px-2 d-flex flex-column">
                        <div class="post_title">
                            Posted on :- 
                        </div>
                        <div class="user_p3 d-flex float-end ">
                            {data?data[0][2]:""}
                        </div>
                    </div>
                </div>
            <div/>

          </div>
        </div>  
      </div>
  </div>
      {/* tags  */}
      <div class="row py-2 d-flex flex-row ">
        

      </div>

          
      </div>
  
      <hr style={{"border": "solid 0.75px !important"}} />
      {/* {% endfor %} */}
      <div class="row">
      
        <div class="col-6 no_answer d-flex justify-content-end">
          {/* {{m}} Answer */}100 answers
        </div>

        {/* sorting box */}
        <div class="col-6 px-3 d-flex justify-content-start">
          <div class="dropdown col-4 px-4 ">
            <button  class="sorting_box btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
              Sorting
            </button>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="#">Newest</a></li>
              <li><a class="dropdown-item" href="#">Active</a></li>
              <li><a class="dropdown-item" href="#">Score</a></li>
            </ul>
          </div>
        </div>

      {ans?  Object.entries(ans).map(([key,value])=>
<Ans value={value} />
      ):<></>}
    </div>
    <hr style={{"border": "solid 0.75px !important"}} />
    <div class="row d-flex justify-content-center mt-2">
      <div class="col-xl-8 col-lg-8 col-md-9 col-sm-10 col-12  d-flex justify-content-center" style={{"font-size": "x-large","color":"3A4D3A !important"}}>
        Submit your answer
      </div>
      <div class="col-10 my-3 d-flex justify-content-center">
      <div class="d-flex flex-row q_title">
        <span class="input-group-text d-flex justify-content-center par_question_span_body">Answer</span>

        <div class="q_title">

        <JoditEditor
        
			ref={editor}
			value={content}
			onBlur={newContent => {setContent(newContent)}} // preferred to use only this option to update the content for performance reasons
      // onChange={newcontent=>{console.log(newcontent)}}
      
    />
        </div>
      </div>
      </div>
      <div class="d-flex justify-content-center mb-3">
        <div class="col-4 d-flex justify-content-center column-gap-1">
          <div class="px-1">
            <button type="submit" class="p-1 btn btn-outline-primary" onClick={()=>{api(data[0][0],content)}}>Submit</button>
          </div>
          <div class="px-1">
            <button type="button" class="p-1 btn btn-outline-danger">Cancel</button>
          </div>
        </div>
      </div>
    </div>
</body>

        </>
    );
}