var http = require("http");
var fs = require("fs");
var os = require("os");
var ip = require('ip');

function round(value, decimals) {
    return Number(Math.round(value + 'e' + decimals) + 'e-' + decimals);
}
    
http.createServer(function(req, res) {

    if (req.url === "/") {
        fs.readFile("./public/index.html", "UTF-8", function(err, body) {
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(body);
        });
    }
        else if(req.url.match("/sysinfo")) {
            var myHostName = os.hostname();
            var totalMemMB = round(((os.totalmem()/1024)/1024),3);
            var freeMemMB = round(((os.freemem()/1024)/1024),3);
            var seconds = os.uptime();
            console.log(seconds);
            var d = Math.floor(seconds / (3600*24));
            var h = Math.floor(seconds % (3600*24) / 3600);
            var m = Math.floor(seconds % 3600 / 60);
            var s = Math.floor(seconds % 60);
            var noCPUs = os.cpus();
            var noLogicalCores = 0;
            noCPUs.forEach(element => {
                noLogicalCores++;
            });
            noLogicalCores = noLogicalCores/2; //hyperthreading tech doubles os.cpus count
            html = `
            <!DOCTYPE html>
            <html>
                <head>
                    <title>Node JS Response</Title>
                </head>
                <body>
                    <p>Hostname: ${myHostName}</p>
                    <p>IP: ${ip.address()}</p>
                    <p>Server Uptime: Days: ${d}, Hours: ${h}, Minutes: ${m}, Seconds: ${s}</p>             
                    <p>Total Memory: ${totalMemMB} MB</p>
                    <p>Free Memory: ${freeMemMB} MB</p>
                    <p>Number of CPUs: ${noLogicalCores}</p>
                </body>
            </html> `
            res.writeHead(200, {"Content-Type": "text/html"});
            res.end(html);
            }
            else {
            res.writeHead(404, {"Content-Type": "text/plain"});
            res.end(`404 File Not Found at ${req.url}`);
        }

}).listen(3000)

console.log("Server listening on port 3000");