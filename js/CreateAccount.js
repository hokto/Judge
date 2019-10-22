$(function(){
	$("#createBtn").on("click",function(){
		name=document.getElementById("accountName").value;
		console.log(name);
		document.location.href="../HTML/Home.html";
	});
});

