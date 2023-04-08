import JoditEditor from "jodit-react";
import { useRef, useState, useEffect } from "react";
import Select from 'react-select';

export default function New_ques() {

    const [tags,setTags] = useState([])
    const [taglist,setTaglist] = useState([])
    const [title,setTitle] = useState([])
    const [content,setContent] = useState('');

    function api(Title,Body,Tags){
      console.log(Title,Body,Tags)
      fetch(`/ask/question`, {
          method: 'POST',
          body: JSON.stringify({
            'Body':Body,
            'Title':Title,
            'Tag':Tags
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

    const handleInputChange = (e) => {
      const {id , value} = e.target;
      
      if(id === "title"){setTitle(value);}

      
  }    

  useEffect(() => {
    fetch('/tag/list').then((res) =>
        res.json().then((data) => {
            // console.log(data);
            const p = Object.values(data)
            const q = JSON.stringify(p)
            const s = JSON.parse(q)
            // console.log(s)
            // console.log(s)
            // console.log(colourOptions)
            setTags(s)
          })
          );
        }, []); 
        
        const colourOptions = [
          { value: 'chocolate', label: 'Chocolate' },
          { value: 'strawberry', label: 'Strawberry' },
          { value: 'vanilla', label: 'Vanilla' }
        ]
        
      // console.log(colourOptions)
    const editor = useRef(null);
    return (
        <>
        <body>
    <div class="row">
      <div class="page_title p-1 d-flex justify-content-center">
          Ask any Questions
      </div>
    </div>

    <form class="row mx-5 my-4" method="POST" action="/ask/question">
    <div class="title col-12" style={{"font-size": "35px"}}>
    <div class="mb-3  d-flex flex-row" >
        <span class="d-flex justify-content-center input-group-text new_question_span" id="basic-addon1">Title</span>
        <input type="text" class="form-control q_title"  placeholder="Enter title.." aria-label="Title" aria-describedby="basic-addon1" id="title" onChange={(e) => handleInputChange(e)} ></input>
    </div>
  </div>

    <div class="tag col-12 d-flex flex-row mb-3" style={{"zIndex":"99"}}>
    {/* <div class="input-group my-3" > */}
        <span class="d-flex justify-content-center input-group-text new_question_span" id="basic-addon1">Tag</span>
        {/* <input type="text" class="form-control"  placeholder="Enter tags.." aria-label="Tag" aria-describedby="basic-addon1"></input> */}


    <div class="q_title">
    {tags?<Select
    // defaultValue={[colourOptions[2], colourOptions[3]]}
    isMulti
    // name="colors"
    options={tags}
    className="basic-multi-select"
    classNamePrefix="select"
    onChange={newcontent=>{console.log(newcontent);setTaglist(newcontent)}}
  />:<></>}
    </div>

{/* </div> */}
  </div>


  <div class="col-12 mb-3">
  <div class="d-flex justify-content-start ">
        <span class="d-flex justify-content-center input-group-text new_question_span">Body</span>

        <div class="q_title">
        <JoditEditor
        
			ref={editor}
			value={content}
			onBlur={newContent => setContent(newContent)} // preferred to use only this option to update the content for performance reasons
      onChange={newcontent=>{}}
      
    />
        </div>
      </div>
  </div>
      
      <div class="d-flex justify-content-center ">
        <div class="col-4 d-flex justify-content-center column-gap-1">
          <div class="px-1">
            <button type="button" class="p-1 btn btn-outline-primary" onClick={()=>{api(title,content,taglist)}}>Submit</button>
          </div>
          <div class="px-1">
            <button type="button" class="p-1 btn btn-outline-danger">Cancel</button>
          </div>
        </div>
      </div>




    </form>

    
      

</body>

        </>
    );
}