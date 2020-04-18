$(function(){
	var accountJson=[];
	$("#createBtn").on("click",function(){
		name=document.getElementById("accountName").value;
		accountJson.push({name: name});
		console.log(accountJson);
		document.location.href="../HTML/Home.html";
	});
});
