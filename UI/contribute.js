var budgetController=(function(){
    var Person=function(id,firstname,lastname,amount){
        this.id=id;
        this.firstname=firstname;
        this.lastname=lastname;
        this.amount=amount;
    }

    var data={names:[],
        total:0
    };
    return {
        //create a new item
        newperson:function(firstname,lastname,amount){
            if (data["names"].length>0){
            var id=data.names[data["names"].length-1].id+1;
            }
            else{
                var id=0;
            }
            var newcoder=new Person(id,firstname,lastname,amount);
            data["names"].push(newcoder);
            return newcoder;

            

        
             },
    // loop through data to calculate sum
     getdata:function(){
        var sum=0;
        data["names"].forEach(function(current){
            sum=sum+current.amount;
            data.total=sum;
        });
        return data;
    },
    // delete selected item by id
    removeclicked:function(id){
        data["names"].forEach(function(current,index){
            if(id==current.id){
                data["names"].splice(index,1);
            }

        });
        return data["names"];

    },
// calculate the sum of the remaining item after delete
    updatedtotol:function(data){
        var sum=0;
        data.forEach(function(current){
            sum=sum+current.amount;
        });
        return sum;

    }


    }
})();

var UIcontroller=(function(){
    var tb=document.querySelector("tbody");
    return { 
            getinputs:function(){
                return {
                    firstname:document.querySelector('input[name="firstname"]').value,
                    lastname:document.querySelector('input[name="lastname"]').value,
                    total:document.querySelector("#total"),
                    table:document.querySelector("tbody"),
                    amount:parseFloat(document.querySelector('input[name="amount"]').value)}},

            additemul:function(obj){
                    var html='<tr><td>first</td> <td>last</td><td>amount</td><td><button class="icon2" id="any" type="button" name="button">Delete</button></td></td>'
                    var newhtml=html.replace("first",obj.firstname);
                    var newhtml=newhtml.replace("last",obj.lastname);
                    var newhtml=newhtml.replace("amount",obj.amount);
                    var newhtml=newhtml.replace("any",obj.id);
                    tb.insertAdjacentHTML("beforeend",newhtml);

                },
            clearfields:function(){
                selection=document.querySelectorAll(".cls1"+","+".cls2"+","+".cls3");
                var fields=[selection[0],selection[1],selection[2]];
                fields.forEach(function(current){
                current.value="";
                });
                selection[0].focus();
            },
            deleteitem:function(e,value){
                if(e.target.classList.contains("icon2")){
                    item=e.target.parentElement.parentElement;
                    value.removeChild(item);
                }
                return e.target.id;

            }

           
            
               
            }
    
} 

)();


var AppController=(function(uitr,bgtctr){
    
    var removeitem=function(e){
        //get inputs
        value=uitr.getinputs();
        //delete table element
        var rem=uitr.deleteitem(e,value.table);
        // delete data by id in the data structure
       var removing= bgtctr.removeclicked(rem);
        // update the new total by summing the remaining amount
        var removed= bgtctr.updatedtotol(removing);
        //post the new total in the ui
       var newdata=uitr.getinputs();

       newdata.total.textContent=removed;

    }


var additem=function(){
    //get inputs from the ul
    var newitem=uitr.getinputs();
//add a new item to data structure and return the item
if(!isNaN(newitem.amount) && newitem.firstname!="" && newitem.lastname!=''){
    var dataset=bgtctr.newperson(newitem.firstname,newitem.lastname,newitem.amount);
    
    //add item to the ui
    uitr.additemul(dataset);
}

//clear fields
uitr.clearfields();
//calculate total
var data=bgtctr.getdata();
console.log(data);
//display total to the ui
newitem.total.textContent=data.total;

    };

var btn=document.querySelector('button[type="submit"]').addEventListener('click',additem);
var btn1=document.querySelector('tbody').addEventListener('click',removeitem);
 
})(UIcontroller,budgetController);


