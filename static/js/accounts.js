
/* REGISTERATION FORM JS */
var fname = document.getElementsByName("firstname")[0];
 var lname = document.getElementsByName('lastname')[0];
 var pswd1 = document.getElementsByName('password1')[0];
 var pswd2 = document.getElementsByName('password2')[0];
 fname.addEventListener('input', checkLength)
 lname.addEventListener('input', checkLength)
 pswd1.addEventListener('input',checkLength2)
 var uname = document.getElementsByName('username')[0];
 uname.addEventListener('input',checkLength)
 function checkLength(event){
    if (event.target.value.length > 2){
        event.target.style.border = 'none';
    }
    if (event.target.value.length < 3){
        event.target.style.border = '2px solid rgb(56, 55, 55)';
    }
 }
 function checkLength2(event){
    if (event.target.value.length > 7){
        event.target.style.border = 'none';
    }
    if (event.target.value.length < 8){
        event.target.style.border = '2px solid rgb(56, 55, 55)';
    }
    
 }
function validateForm(){
    var inputEle = document.getElementsByClassName('designform')
  console.log(inputEle)
  for (var i=0;i<inputEle.length-2; i++){
      var input = inputEle[i];
      console.log(input)
      if(input.value.length == 0){
          input.style.border = '2px solid rgb(56, 55, 55)';
          alert('All fields are required')
          return false;
      }
    }
    var arryaitems = [fname, lname, uname, pswd1];
    for (var i =0; i<arryaitems.length; i++){
        var item = arryaitems[i];
        if (item.value.length < 3 && i!=3){
          alert("The field marked in black should be atleast three characters long")
          item.style.border = '2px solid rgb(56, 55, 55)';
          return false;
        }
        if (item.value.length < 8 && i==3){
          alert('password should be atleast 8 characters long');
          item.style.border = '2px solid rgb(56, 55, 55)';
          return false;
        }
    }

    if (pswd1.value != pswd2.value){
        alert("password does not match");
        pswd2.style.border = '2px solid rgb(56, 55, 55)';
        return false;
    }
  }
/* REGISTERATION FORM JS ENDS */
/* Login page js would be handled by server side validation in django  */
/* forms css handling by js */

var headings = document.getElementsByClassName('target');

for(var i=0 ; i< headings.length; i++){
  var heading = headings[i];
  if (i==0){
    heading.addEventListener("click", curtainUp);
  }
  else {
    heading.addEventListener("click", curtainUp2);
  }
}
function curtainUp(event){
  var formHeading = event.target;
  //console.log(formHeading)
  var ele = event.target.parentElement;
  ele.classList.add('curtain');
  var sblng = ele.parentElement;
  var form = sblng.getElementsByClassName("formcontainer")[0];
  form.classList.add('formcontainer2');
  formHeading.classList.remove('form-heading');
  //console.log(sblng.nextSibling.nextSibling)
  var nextaccount = sblng.nextSibling.nextSibling
  var curtainnext = nextaccount.getElementsByClassName('curtain2')[0];
 // console.log(curtainnext)
  var secondFormHeading = curtainnext.getElementsByTagName('h1')[0];
 // console.log(secondFormHeading);
  secondFormHeading.classList.add('form-heading')
  curtainnext.classList.remove('curtain')
  var formnext = nextaccount.getElementsByClassName('formcontainer')[0];
  //console.log(formnext)
  formnext.classList.remove('formcontainer2')
}
function curtainUp2(event){
  var formHeading = event.target;
  var ele = event.target.parentElement;
  ele.classList.add('curtain');
  var sblng = ele.parentElement;
  var form = sblng.getElementsByClassName("formcontainer")[0];
  form.classList.add('formcontainer2');
  formHeading.classList.remove('form-heading');
  //console.log(sblng.previousSibling.previousSibling)
  var nextaccount = sblng.previousSibling.previousSibling
  var curtainnext = nextaccount.getElementsByClassName('curtain2')[0];
  //console.log(curtainnext)
  var secondFormHeading = curtainnext.getElementsByTagName('h1')[0];
 // console.log(secondFormHeading);
  secondFormHeading.classList.add('form-heading')
  curtainnext.classList.remove('curtain')
  var formnext = nextaccount.getElementsByClassName('formcontainer')[0];
  //console.log(formnext)
  formnext.classList.remove('formcontainer2')
}
function changeform(){
  document.getElementsByClassName('two')[0].style.display="none";
  document.getElementsByClassName('one')[0].style.display="block";
}
