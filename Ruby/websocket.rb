require "em-websocket"
require "pp"
require "./judge"
require "socket"
require "json"
connect=[]

ipAddress=Socket.getifaddrs.select{|x|
  x.name=="en0" and x.addr.ipv4?
}.first.addr.ip_address
EM::WebSocket.start({:host => ipAddress ,:port => 9999}) do|ws_conn|
		ws_conn.onopen do
				connect<<ws_conn
		end
		ws_conn.onmessage do|message|
          receiveFile=message.split(":",2)
          if receiveFile[0]=="NewAccount"
            File.open("UserInfo.json") do|file|
              userInfo=JSON.load(file)
            end
            userInfo.push(receiveFile[1])
            File.open("UserInfo.json","w") do|file|
              JSON.dump(userInfo,file)
            end
          end
          targetFile="Main."+receiveFile[0]
          File.open(targetFile,"w") do|file|
            file.print(receiveFile[1])
          end
          result=[]
          Thread.new{
            result=Judge(0,targetFile)
            ws_conn.send(result.join(":"))
          }
	end
end 
