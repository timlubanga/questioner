/*
var formlet=document.querySelector("h1");
formlet.style.color="red";

var linked=document.getElementsByTagName("a");
console.log(linked);

for(i=0; i<linked.length;i++){
    linked[i].style.color="yellow";
}

var input=document.querySelector('input[type="password"]');
input.placeholder="ugali";

var par=document.querySelectorAll(".container");


items=document.querySelector(".form");
items.children[3].placeholder="kenya"

var username=document.querySelector('input[name="username"]');
console.log(username.placeholder);

wrap=document.querySelectorAll(".container");
console.log(wrap);



//clearning the input fields
var table=document.querySelector(".form");
function addinput(){
 selection=document.querySelectorAll(".cls1"+","+".cls2");
 var fields=[selection[0],selection[1]];
 fields.forEach(function(current, index){
     current.value="";
 });
 selection[0].focus();
};


formless=document.querySelector('button[type="submit"]').addEventListener('click',addinput);
console.log(formless);


var button=document.querySelector('button[type="submit"]').addEventListener('click',buttonclicked);

function buttonclicked(){
    blank=true;
    pass=true;
    while (blank){
    x=prompt("please enter username"); 
    if(x){
        var y=document.querySelector('input[type="text"]');
        y.value=x;   
        blank=false;

        while (pass){
        w=prompt("please enter password"); 
        if(w){
            var z=document.querySelector('input[type="password"]');
            z.value=w;   
            pass=false;
    } 
    } 
}    
    
}

    
submit=document.querySelector('button[type="submit"]').addEventListener('click',filled_pasted);


function filled(){
       var username=prompt("please enter username");
       var password=prompt("please enter password");
       ch=document.querySelector('input[type="text"]');
       ch.value=username;
       ch1=document.querySelector('input[type="password"]');
       ch1.value=password;
      console.log("your username is:"+username +"and your password is:"+password);
   }

   function submitted(e){
       username=document.querySelector('input[type="text"]').value;
       password=document.querySelector('input[type="password"]').value;
       console.log("your username is:"+username +" and your password is:"+password);
       console.log(e.target.textContent);


   }
    
   

function filled_pasted(){
    var items=document.querySelector("input");
    items.style.backgroundColor="green";
    console.log(items);


}



form=document.querySelector('button[type="submit"]').addEventListener('click',submitted_);

function submitted_(e){
    username=document.querySelector('input[type="text"]').value;
    password=document.querySelector('input[type="password"]').value;
    if (username=="timlubanga" && password=="smartjoker"){
        alert("successfully logged in");
        }
    else {
        alert("wrong signup credetials");
    }

}


var numbers=[34,56,78,90];

for(i=0;i<numbers.length;i++){
    console.log(numbers[i]);
}




var june=["mark", "jacob","allan"];

for(i=0;i<june.length;i++){
    console.log(june[i])

};

june.forEach(function(current, i){
    console.log("my name is",current+ "I am at index"+",", i.toString());
});



//testing isNaN()


function testing(){
    var x=parseFloat(prompt("please enter a number"));

    console.log(x);
   
    
}
testing();

*/



var ar=[23,56,8,9];

 ar.splice(1,1)
console.log(ar);
var sum=0
ar.forEach(function(current){
sum=sum+current;
});
console.log(sum);