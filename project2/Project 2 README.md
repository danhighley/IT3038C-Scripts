* Project 2

==========

***For Project 1, I chose to do a PowerShell script for one of the listed suggestions:
"Write a script that tells you how much hard drive space you have left"
The script would accomodate multiple drives and display info on the console.

==========

***When i think of scripts, I envision something running in the background perfoming a function the user isn't normally thinking about. For Project 2, I chose to expand upon the Project 1 script and create a script that will alert the user with a warning if any hard drive on their computer falls below a specified remaining storage limit.

==========

The script name is spacewarning.ps1 in the Project 2 Github repository, and once copied can be ran from the PowerShell command line with ./spacewarning.ps1. While runing it this manner should work fine, the end goal is to set the script up to run automatically at windows startup, and have a pop up window be presented to the user should a hard drive fall below the specified remaining storage limit. I wrote the script on a Windows 11 system using Windows PowerShell and Windows PowerShell ISE.

==========

**Elements used in the script

The script is thoroughly commented but I'll touch on how the script flows.

The script first pulls some system information:   

```$env:COMPUTERNAME``` to pull the name of the computer   
```IP = ((ipconfig | findstr [0-9].\.)[0]).Split()[-1]``` to filter out just the ip address from ipconfig

Establishes the minimum disk size to raise a warning to 20GB

```$minSize = 20GB```   
```$minSize = [math]::Round($minSize/1GB,2)```

Find all the hard drives on the system by filtering through Get-WmiOject win32_volume data.
Then assign the found drive letters to an array.

``` $localVolumes = Get-WmiObject win32_volume
    $drives = @();
    foreach ($vol in $localVolumes) {
        if ($vol.DriveType -eq 3 -And $vol.DriveLetter -ne $null ) {
            $drives += $vol.DriveLetter[0];
        }
    }
```

Move through each element in the drive letter array and extract drive storage specs.

```foreach ($d in $drives) {
    $disk = Get-PSDrive $d;
    $diskFree = [math]::round($disk.Free/1GB,2)
    $diskUsed = [math]::round($disk.Used/1GB,2)
    $diskTotal = [math]::round($diskFree + $diskUsed)
    Write-Host "Drive:" $d "has a total of"$diskTotal "GB ("$diskUsed "Used /"$diskFree "Free )"
}
```

Set a flag to trigger warning to the user if available strorage space falls below threshold.

If warning needs to be sent, move through the drive letter array and store warning messages to new array. I didn't want multiple popups for each drive below the threshold, just one warning sent that would list all drives below threshold. The new array solves this.

``` foreach ($d in $drives) {
        $disk = Get-PSDrive $d;
        $diskFree = [math]::round($disk.Free/1GB,2)
        if ($diskFree -lt $minSize) {
            Write-Host "Warning > Drive:" $d "has less than" $minSize"GB space available."
            
            # Store warning text into an array in case of multiple warnings
            # to use in window pop up.
            $WarnText = ('Warning > Drive: ' + $d + ' has less than ' + $minSize + 'GB space available.')
            $WarnArray += @($WarnText)
        } 
```

Send warning array to a window pop up using Windows Scripting Host.

``` $wsh = New-Object -ComObject Wscript.Shell
    $wsh.Popup($WarnArray,0,"Hard Drive Space Warning!",1+48)
```
===========

* Getting the script to autorun at startup

