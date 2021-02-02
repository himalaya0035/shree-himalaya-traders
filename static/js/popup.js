var parent = document.querySelector('.parent');
var btn = document.querySelector('#cart-icon');
var cross = document.querySelector('.cross');

btn.addEventListener('click',appear)

function appear(){
    parent.style.display="block"
    section.style.filter ="blur(10px)";
}

cross.addEventListener('click', disappear);

function disappear(){
    parent.style.display="none"
    section.style.filter="blur(0px)"
}
parent.addEventListener('click',disappearParent)

function disappearParent(event){
    if (event.target.className == 'parent-modal'){
        parent.style.display="none"
        section.style.filter="blur(0px)"
    }
}

document.getElementById("demo").innerText="content added dynamically"