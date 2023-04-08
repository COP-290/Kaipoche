import { useState } from "react";

export default function Signup() {

  const [username,setUsername] = useState('')
  const [email,setEmail] = useState('')
  const [password,setPassword] = useState('')

  const handleInputChange = (e) => {
    const {id , value} = e.target;    
    if(id === "email"){setEmail(value);}  
    if(id === "password"){setPassword(value);}  
    if(id === "username"){setUsername(value);}  
}   

function api(Username,Email,Password){
  console.log(Username,Email,Password)
  fetch(`/register`, {
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

    return (
        <>
        <body>

<div class="row">
  <div class="page_title col-12 d-flex justify-content-center">
    Sign up
  </div>
</div>

<div class="row">
    <div class="col-12 d-flex justify-content-center mt-3">
        <div class="sign_up_box p-3">
            <form >
                <div class="mb-3">
                    <label for="exampleInputusername1" class="form-label label_title" >Username</label>
                    <input type="username" class="form-control" id="username" aria-describedby="usernameHelp" onChange={(e) => handleInputChange(e)}></input>
                  </div>
                <div class="mb-3">
                  <label for="exampleInputEmail1" class="form-label label_title">Email address</label>
                  <input type="email" class="form-control" id="email" placeholder="name@example.com" aria-describedby="emailHelp" onChange={(e) => handleInputChange(e)}></input>
                  <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
                </div>
                <div class="mb-3">
                  <label for="exampleInputPassword1" class="form-label label_title">Password</label>
                  <input type="password" class="form-control" id="password" onChange={(e) => handleInputChange(e)}></input>
                </div>
                <div class="mb-3 form-check">
                  <input type="checkbox" class="form-check-input" id="exampleCheck1"></input>
                  <label class="form-check-label" for="exampleCheck1">Remember me</label>
                </div>
                <div class="mb-3 d-flex justify-content-center">
                  Already have an account?
                  <div class="px-1">
                    <a href="login" class="link-primary">click here</a>
                  </div>
                </div>
                <div class="d-flex justify-content-center">
                    <button type="button" onClick={()=>api(username,email,password)} class="sign_up_btn btn btn-primary">Sign up</button>
                </div>
            </form>
        </div>
    </div>
    
</div>

</body>
        </>
);
}