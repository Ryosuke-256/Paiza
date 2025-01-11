const http = require("http");

const server = http.createServer((_,res) => {
    res.writeHead(200,{
        "Content-Type":"text/html;charset = utf-8",
    });
    res.end("<h1>Hello World<h1>");
});

const port = 3000;
server.listen(port,function(){
    console.log("Node.js Server Started:" + port);
});