var count =0;
// var loader = document.querySelector(".loader") // the loader object stores the reference of the div element with class loade
// //console.log(loader); // for debugging purposes
// window.addEventListener("load",vanish); // when the windows loads vanish function is executed
//  function vanish() {  // this fn adds the class disappear to the div element 
//      loader.classList.add("disappear"); // the disapppear class make the preloader disappear
//  }
/* thankyou jquery for existing */
 $(document).on('click','ul li',function(){
     $(this).addClass('iactive').siblings().removeClass('iactive')
 })
 /* above code is used for toggling the active links */
/* for toggling betwwen veiw cart and hide cart */
 function changeCommand() {
     var ele = document.getElementById("changetext");
     if (count==0){
        ele.innerHTML='Hide cart';
        count=1;
     }
     else {
        ele.innerHTML='View cart';
        count=0;
    }
     
 }
 /* toggling cart ends */

 /* Js for cart */
  
 /* js for cart ends */
