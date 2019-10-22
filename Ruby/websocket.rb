require "em-websocket"
require "pp"
require "./judge"
require "socket"
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
