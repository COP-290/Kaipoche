// import { useEffect } from "react";
import { useNavigate } from "react-router-dom";

export default function Navbar() {

  let navigate = useNavigate();
  const to = async (id) => {
    let path = `/${id}`;
    navigate(path);
  //   await scroller.scrollTo("head", {
  //     duration: 1500,
  //     offset: 0,
  //   });
  };

    function redirect(){
      fetch('/checkuser').then((res) =>
          res.json().then((data) => {
              console.log(data);
              if(data===true){
                to('profile')
              }
              else{
                to('signup')
              }
              // setNumber(parseInt(data))
          })
      );
    }


  return (
      <>
<nav class="navbar navbar-expand-lg navbar-light ">
        <div class="container-fluid mx-3 d-flex justify-content-between" >
          <a class="navbar-brand site_icon px-5"  href="/main" style={{"fontSize":"50px"}}>askQ</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item mx-3 d-flex justify-content-center">
                <a class="nav-link px-3 mx-1" aria-current="page" href="/about">About</a>
              </li>
              <li class="nav-item mx-3 d-flex justify-content-center">
                <a class="nav-link  px-3 mx-1" href="/tag">Tag</a>
              </li>
              <li class="nav-item mx-3 d-flex justify-content-center">
                <a class="nav-link  px-3 mx-1" href="/question">Question</a>
              </li>
            </ul> 
            
            <form class="d-flex mx-2 mb-3">
              <input class="form-control me-2" type="search" placeholder="Search..." aria-label="Search"></input>
              <button type="button" class="nav_search_btn btn btn-success">Search</button>
            </form>
            <div class="col-xl-1 col-lg-1 col-md-12 user_ppp d-flex justify-content-center " >
                <div class="d-flex justify-content-center" >

                  <svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16" onClick={()=>{redirect()}} >
                      <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/>
                      <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"/>
                  </svg>

                </div>
            </div>
          </div>
        </div>
    </nav>
        </>
    );
}