function toggle() {
 
  var blur = document.getElementById("blur");
  blur.classList.toggle("active");
  var popup = document.getElementById("popup");
  popup.classList.toggle("active");
}

function valid(){
	var a = document.form.Gender;
	for (i=0; i<a.length; i++)
	{

		if(a[i].checked==true)
			return true;
	}
	document.getElementById("msg").innerhtml="select only one option";

	return false; 
}