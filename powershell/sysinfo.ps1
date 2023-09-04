function getIP{

    (get-netipaddress).ipv4address | Select-String "192*"

}
write-host(getIP)

$IP = getIP
Write-Host("This machine's IP is $IP")