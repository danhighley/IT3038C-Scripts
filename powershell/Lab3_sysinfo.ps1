# Function to get system IP address
function getIP{
    (get-netipaddress).ipv4address | Select-String "192*"
}

# Function to get local user
function getUSER{
    ($env:UserName)
}

# function to get hostname
function getHostName{
    (Get-WmiObject -Class Win32_Computersystem).Name
}

# Funciton to get PowerShell Version
function getPSVersion{
    ($HOST).Version.Major
}

# Function to get Today's Date
function getDate{
    (get-Date -UFormat "%A, %B%e, %Y")
}

$IP = getIP
$USER = getUSER
$HOSTNAME = getHostName
$PSVERSION = getPSVersion
$TODAY = getDate

$BODY = ("This machine's IP is $IP. User is $USER. Hostname is $HOSTNAME. PowerShell Version $PSVERSION. Today's Date is $TODAY.")

write-host($BODY)
Send-MailMessage -To "leonardf@ucmail.uc.edu" -From "highleydan@gmail.com" -Subject "IT3038C Windows SysInfo" -Body $BODY -SmtpServer smtp.gmail.com -port 587 -UseSSL -Credential (Get-Credential)
