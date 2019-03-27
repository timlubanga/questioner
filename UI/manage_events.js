

var table1=document.querySelector("tbody");
/*
console.log(table1)

var newele=document.createElement("tr");
var newtb1=document.createElement("td");
var newtb2=document.createElement("td");
var newtb3=document.createElement("td");
var newtb4=document.createElement("td");
var newtb5=document.createElement("td");
var newtb6=document.createElement("td");
var newtb7=document.createElement("td");
*/

var a=prompt("please enter event name");
var b=prompt("please enter event date");
var c=prompt("please enter event descr")
var d=prompt("please enter event location");
var f=prompt("please enter event tag")

/*

var img_sourcing=document.createElement("img");
img_sourcing.src="./img/event_1.jpg";
img_sourcing.width="150px";
img_sourcing.height="100px";

var btr=document.createElement("button");
btr.className="icon2";
btr.type="button";
btr.name="button";

var del=document.createTextNode("Delete");
btr.appendChild(del);

var btr2=document.createElement("button");
btr2.className="icon1";
btr2.type="button";
btr2.name="button";



var edit=document.createTextNode("Edit");
btr2.appendChild(edit);



var txtnode1=document.createTextNode(a);
var txtnode2=document.createTextNode(b);
var txtnode3=document.createTextNode(c);
var txtnode4=document.createTextNode(d);
var txtnode6=document.createTextNode(f);

newtb1.appendChild(txtnode1);
newtb2.appendChild(txtnode2);
newtb3.appendChild(txtnode3);
newtb4.appendChild(txtnode4);
newtb5.appendChild(img_sourcing);
newtb6.appendChild(txtnode6);
newtb7.appendChild(btr2);
newtb7.appendChild(btr);

newele.appendChild(newtb1);
newele.appendChild(newtb2);
newele.appendChild(newtb3);
newele.appendChild(newtb4);
newele.appendChild(newtb5);
newele.appendChild(newtb6);
newele.appendChild(newtb7);

table1.appendChild(newele);



table1.addEventListener('click',delete_record);
table1.addEventListener('click',edit_record);

function delete_record(e){
    if(e.target.classList.contains('icon2')){
        if (confirm("are you sure you want to delete this record?")){
        item=e.target.parentElement.parentElement;
        table1.removeChild(item);
        alert("record deleted successfully!");
        }
       
    }
}

function edit_record(e){
    if (e.target.classList.contains('icon1')){
        console.log(e.target);

    }
}



//using addadjacement html to add a block of html

var htmlcode='<tr> <td>C</td><td>12</td><td>A</td><td>i</td><td><img src="./img/event_1.jpg" width="150" height="100"></img> </td><td>#T</td><td><button class="icon1" type="button" name="button">Edit</button><button class="icon2" type="button" name="button">Delete</button></td></tr>'
var newhtmlcode=htmlcode.replace("C",a);
var newhtmlcode=newhtmlcode.replace("12",b);
var newhtmlcode=newhtmlcode.replace("A",c);
var newhtmlcode=newhtmlcode.replace("i",d);
var newhtmlcode=newhtmlcode.replace("T",f);

table1.insertAdjacentHTML("beforeend", newhtmlcode);

*/
