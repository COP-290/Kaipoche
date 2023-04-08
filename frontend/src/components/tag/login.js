import JoditEditor from "jodit-react";
import { useRef, useState } from "react";
import { useNavigate } from "react-router-dom";



export default function Login() {

  const [username,setUsername] = useState('')
  const [email,setEmail] = useState('')
  const [password,setPassword] = useState('')

  let navigate = useNavigate();
  const to = async (id) => {
    let path = `/${id}`;
    navigate(path);
  //   await scroller.scrollTo("head", {
  //     duration: 1500,
  //     offset: 0,
  //   });
  };

  function api(Username,Email,Password){
    console.log(Username,Email,Password)
    fetch(`/login/`, {
        method: 'POST',
        body: JSON.stringify({
          'Email': Email,
          'Password': Password,
          'Username': Username,
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
    if(id === "email"){setEmail(value);}  
    if(id === "password"){setPassword(value);}  
    if(id === "username"){setUsername(value);}  
}   

    const editor = useRef(null);
    const [content, setContent] = useState('');
    return (
        <>
        <body>

<div class="row">
  <div class="page_title col-12 d-flex justify-content-center">
    Login
  </div>
</div>

<div class="row">
    <div class="col-12 d-flex justify-content-center mt-3">
        <div class="sign_up_box p-3">
            <form>
            <div class="mb-3">
                    <label for="exampleInputusername1" class="form-label label_title">Username</label>
                    <input type="username" class="form-control" id="username" aria-describedby="usernameHelp" onChange={(e) => handleInputChange(e)}></input>
                  </div>
                <div class="mb-3">
                  <label for="exampleInputEmail1" class="form-label label_title">Email address</label>
                  <input type="email" class="form-control" id="email" placeholder="name@example.com" aria-describedby="emailHelp" onChange={(e) => handleInputChange(e)}></input>
                  <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
                </div>
                <div class="mb-3 row d-flex flex-column">
                    <label for="inputPassword" class="col-sm-2 col-form-label label_title">Password</label>
                    <div class="col-12">
                      <input type="password" class="form-control" id="password" onChange={(e) => handleInputChange(e)}></input>
                    </div>
                  </div>
                <div class="mb-3 d-flex justify-content-center">
                  Are you new here?
                  <div class="px-1">
                    <a href="signup" class="link-primary">click here</a>
                  </div>
                </div>
                <div class="d-flex justify-content-center">
                    <button type="button" class="sign_up_btn btn btn-primary" onClick={()=>{api(username,email,password);to('profile')}}>Login</button>
                </div>
            </form>
        </div>
    </div>
    
</div>
</body>

        </>
);
}
