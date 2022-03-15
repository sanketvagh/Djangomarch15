
function editmodal(element) {
    // console.log(element.parentElement.parentElement.children);
    mfname=document.querySelector('#mfname')
    mlname=document.querySelector('#mlname')
    mrole=document.querySelector('#mrole')
    role=element.parentElement.parentElement.children[3].innerText

    mfname.value=element.parentElement.parentElement.children[1].innerText
    mlname.value=element.parentElement.parentElement.children[2].innerText
    let i=0
    while(i<mrole.childElementCount) {
        if(mrole.children[i].value==role){
            mrole.children[i].selected=true;
            console.log(i)
        }
        i++
    }

    savechange=document.getElementById('savechange');
    savechange.addEventListener('click',()=>{
        saveChanges(element);
    })
}
function saveChanges(element){
   
    mfname=document.querySelector('#mfname')
    mlname=document.querySelector('#mlname')
    mrole=document.querySelector('#mrole')

    element.parentElement.parentElement.children[3].innerText=  mrole.value
    element.parentElement.parentElement.children[1].innerText=mfname.value
    element.parentElement.parentElement.children[2].innerText=mlname.value;
    

}

