$(function(){
    var ws = new WebSocket('ws://192.168.11.17:9999/'); 
    var sendText=null;
    var reader=new FileReader();
    var sendFile=document.getElementById("selectFile"); var type=null;
    var name=null;
      function fileChange(e){
              var target=e.target;
              var file=target.files[0];
              name=file.name;
              reader.readAsText(file);
      }
      sendFile.addEventListener("change",fileChange,false);
      $("#sendFile").on("click",function(){
          ws.send(name.split(".")[1]+":"+reader.result);
          ws.onclose=function(event){
                  console.log(event);
          }
          document.location.href="../HTML/test.html"
      });
      ws.onmessage = function(message){
          var result=message.data.split(":")
          for(var i=0;i<result.length-1;i++){
              var message_li = $('<li>').text(result[i]);
              $("#msg-area").append(message_li);
          }
          var Result=$('<li>').text("Result:"+result[result.length-1]);
          $("#msg-area").append(Result);
      };
  });

