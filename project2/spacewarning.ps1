# Danny Highley

# This PowerShell script will tell you the volume of the hard
# drives on your system and how much space is used / free.

# Script is run from the Powershell command line ./spacewaring.ps1

# Find host(computer) name and its IP address
$hostName = $env:COMPUTERNAME
$IP = ((ipconfig | findstr [0-9].\.)[0]).Split()[-1]
 
# Set initial drive letter array to null.
$drives = $Null

# The minimum disk size to raise the warning.
# Currently set to 20GB.
# Change the GB number to change the warning threshold.
$minSize = 20GB
$minSize = [math]::Round($minSize/1GB,2)

# Initialize warning flag.
$Warn = $Null

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
    
    # Set flag if warning needs to be sent.
    if ($diskFree -lt $minSize) {
        $Warn = 1
    }
}

Write-Host ""

# Check to see if Warning flag set.
# Then move through each element of the drive letter array
# and send a warning to the screen if below minSize.
if ($Warn -eq 1) {
    foreach ($d in $drives) {
        $disk = Get-PSDrive $d;
        $diskFree = [math]::round($disk.Free/1GB,2)
        if ($diskFree -lt $minSize) {
            Write-Host "Warning > Drive:" $d "has less than" $minSize"GB space available."
            
            # Store warning text into an array in case of multiple warnings
            # to use in window pop up.
            $WarnText = ('Warning > Drive: ' + $d + ' has less than ' + $minSize + 'GB space available.')
            $WarnArray += @($WarnText)
        } 
    }
    # Send pop up warning to screen with warnings.
    # Used for autorunning the script at startup.
    # Powershell window will not be visable.
    $wsh = New-Object -ComObject Wscript.Shell
    $wsh.Popup($WarnArray,0,"Hard Drive Space Warning!",1+48)
    
    # Reset array.
    $WarnArray = @()
}

