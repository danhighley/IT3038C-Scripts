var dns = require('dns');

function hostnameLookup(hostname) {    
    dns.lookup(hostname, function(err, addresses, family) {
        console.log(`address: %j family: IPv%s`, addresses, family)
    });
}

if (process.argv.length <= 2) {
    console.log("USAGE: " + __filename + " IPADDR")
} else if (process.argv.length = 0) {
    process.exit(-1)
}

//var hostname = process.argv[1];
var hostname = "Google.com";

console.log(`Checking IP of: ${hostname}`)
console.log(hostnameLookup(hostname));