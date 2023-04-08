import { useState,useEffect } from "react"
import { useNavigate } from "react-router-dom";

export default function Profile() {

  let navigate = useNavigate();
  const to = async (id) => {
    let path = `/${id}`;
    navigate(path);
  //   await scroller.scrollTo("head", {
  //     duration: 1500,
  //     offset: 0,
  //   });
  };

  const [text,setText] = useState(true)
  const [btn,setBtn] = useState(true)
  const [date,setDate] = useState('')
  const [detail,setDetail] = useState([])
  console.log(detail)
  function edit_save(props) {
    const isDisabled = props.isDisabled;
    return (
      <>
        { isDisabled ? "Edit" : "Save" }
      </>
    );
  }

  function logout(){
    to('login')
    fetch(`/logout`, {
        // method: 'POST',
        // body: JSON.stringify({
        //   'Email': Email,
        //   'Password': Password,
        //   'Username': Username,
        // }),
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

  useEffect(() => {
    fetch('/user').then((res) =>
        res.json().then((data) => {
          console.log(data)
          setDate(data['date'])
          setDetail(data['detail'])
          console.log(detail);
        })
    );
}, []);  

  useEffect(() => {
    // document.title = `You clicked ${} times`;
  },[Text]);

    return (
        <>
        <body>
        <div class="d-flex flex-column justify-content-center mt-3">

<div class="row user_pp_profile d-flex justify-content-center ">
  <div class="d-flex justify-content-center" >
      <img src={detail?detail[9]:""} width="200px" style={{"border-radius":"50%"}}></img>
  </div>
</div>

<div class="row d-flex justify-content-center mt-3">

  <div class="username d-flex justify-content-center col-5" style={{"font-size": "35px"}}>
    <div class="input-group mb-3" >
        <span class="input-group-text profile_span" id="basic-addon1">Username</span>
        <input type="text" disabled={text} class="form-control"  placeholder={detail?detail[1]:""} aria-label="Username" aria-describedby="basic-addon1"></input>
    </div>
  </div>

  <div class="user ID d-flex justify-content-center col-5" style={{"font-size": "35px"}}>
    <div class="input-group mb-3">
        <span class="input-group-text profile_span" id="basic-addon1">User ID</span>
        <input type="text" disabled class="form-control" placeholder={detail?detail[0]:""} aria-label="User ID" aria-describedby="basic-addon1"></input>
    </div>
  </div>

  <div class="joindate d-flex justify-content-center col-5" style={{"font-size": "35px"}}>
  <div class="input-group mb-3">
        <span class="input-group-text profile_span" id="basic-addon1">Join Date</span>
        <input type="text" disabled class="form-control" placeholder={detail?detail[3]:""} aria-label="User ID" aria-describedby="basic-addon1"></input>
    </div>
  </div>


<div class="Reputation d-flex justify-content-center col-5" style={{"font-size": "35px"}}>
    <div class="input-group mb-3">
        <span class="input-group-text profile_span" id="basic-addon1">Reputation</span>
        <input type="text" disabled class="form-control" placeholder={detail?detail[6]:""} aria-label="Reputation" aria-describedby="basic-addon1"></input>
    </div>
  </div>

  <div class="Up Vote d-flex justify-content-center col-5" style={{"font-size": "35px"}}>
    <div class="input-group mb-3">
        <span class="input-group-text profile_span" id="basic-addon1">Up Vote</span>
        <input type="text" disabled class="form-control" placeholder={detail?detail[7]:""} aria-label="Up Vote" aria-describedby="basic-addon1"></input>
    </div>
  </div>
  <div class="Down Vote d-flex justify-content-center col-5" style={{"font-size": "35px"}}>
    <div class="input-group mb-3">
        <span class="input-group-text profile_span" id="basic-addon1">Down Vote</span>
        <input type="text" disabled class="form-control" placeholder={detail?detail[8]:""} aria-label="Down Vote" aria-describedby="basic-addon1"></input>
    </div>
  </div>
</div>
<hr/>

<div class="aboutme_row row d-flex justify-content-center">
  <div class="col-8">
    <div class="input-group">
      <span class="input-group-text profile_span">About me</span>
      <textarea disabled={text} name="content" class="form-control q_body" aria-label="Body" placeholder={'Think more - code less, or think less - code more? Love a clean program, where you can tell each functions meaning, each class\'s responsibilities, each variable\'s purpose'}></textarea>
    </div>
  </div>
  <div class="d-flex justify-content-center mt-3">
        <button type="button" class="btn btn-success" onClick={()=>{setText(Text => !Text)}}>
          {edit_save({isDisabled:text})}
        </button>
  </div>
    

</div>

<hr/>

<div class="settings_row row">
  <div class="d-flex flex-column justify-content-center"> 
    <div class="d-flex justify-content-center mb-3">
      <button type="button" class="btn btn-outline-danger" onClick={()=>logout()}>Logout</button>
    </div>

    {/* <div class="d-flex justify-content-center mb-3">
      <button type="button" class="btn btn-outline-danger">Delele Profile</button>
    </div> */}
    
  </div>
</div>
</div>

</body>
        </>
    )
}