require "em-websocket"
require "pp"
require "./judge"

connect=[]

EM::WebSocket.start({:host => "192.168.0.24" ,:port => 9999}) do|ws_conn|
		ws_conn.onopen do
				connect<<ws_conn
		end
		ws_conn.onmessage do|message|
          receiveFile=message.split(":",2)
          targetFile="Main."+receiveFile[0]
          File.open(targetFile,"w") do|file|
            file.print(receiveFile[1])
          end
          Thread.new{Judge(0,targetFile)}
          p targetFile
          ws_conn.send(message)
		end
end 
