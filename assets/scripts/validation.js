function validate(){
    var res=true;
   var x=document.getElementById("sp");
    var sp2 = document.getElementById("sp2");
   if(x.value.length==0 || sp2.value.length == 0){
    res=false;
	alert("no filled will be empty");

	}
	return res;
}
