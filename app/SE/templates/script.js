function openCourse(evt, courseName){

   var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for(i = 0; i < tabcontent.length; i++){
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");

    for(i = 0; i < tablinks.length; i++){
        tablinks[i].className = tablinks[i].className.replace("active", "");
    }
    document.getElementById(courseName).style.display = "block";
    evt.currentTarget.className += " active";
}

function test(){
    console.log("anything");
}

var courseNum = 2;
function addCourse(){
    var txt;
    var person = prompt("Please enter your name:", "Harry Potter");
    if (person == null || person == "") {
        txt = "User cancelled the prompt.";
    } else {
        txt = "Hello " + person + "! How are you today?";
    }
}


// Get the element with id="defaultOpen" and click on it
document.getElementById("default").click();