# Danny Highley

# This PowerShell script will tell you the volume of the hard
# drives on your system and how much space is used / free.

# Script is run from the Powershell command line ./drivespace.ps1

# Find host(computer) name and its IP address
$hostName = $env:COMPUTERNAME
$IP = ((ipconfig | findstr [0-9].\.)[0]).Split()[-1]

# Set initial drive letter array to null.
$drives = $Null

# Query Drives from win32 volume data and make an array of the drive letters.
if ($drives -eq $Null -Or $drives -lt 1) {
        $localVolumes = Get-WmiObject win32_volume
        $drives = @();
    foreach ($vol in $localVolumes) {
        if ($vol.DriveType -eq 3 -And $vol.DriveLetter -ne $null ) {
            $drives += $vol.DriveLetter[0];
        }
    }
}

# sort the array of drive letters.
$drives = $drives | Sort

#Display system name, IP address and how many drives were detected.
Write-Host ""
Write-Host "System" $hostName "residing at IP:"$IP "is showing" $drives.Length "drives."
Write-Host ""

# Move through each element of the array (drive letter) and extract Free and Used fields
# from PSDrive data. Calculate total disk volume from Free and Used fields. The output
# drive volume data in GB.
foreach ($d in $drives) {
    $disk = Get-PSDrive $d;
    $diskFree = [math]::round($disk.Free/1GB,2)
    $diskUsed = [math]::round($disk.Used/1GB,2)
    $diskTotal = [math]::round($diskFree + $diskUsed)
    Write-Host "Drive:" $d "has a total of"$diskTotal "GB ("$diskUsed "Used /"$diskFree "Free )"
}