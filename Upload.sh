#!/bin/bash

#DEBUGLOG="/Volumes/DATA\ A/Installers/__EXPAND/pkg.log" [ -f "$DEBUGLOG" ] || touch "$DEBUGLOG"
#exec &> >(tee -a "$DEBUGLOG")


####### 	Logs Output & Errors to log file 		 		#######

#DEBUGLOG=/Volumes/DATA\ A/Installers/__EXPAND
#exec > >(tee "$DEBUGLOG/pkg.log") 2>&1


UPLOG=~/Documents/Scripts/Python/Upload/Upload.txt
DATE=`date '+%Y-%m-%d %H:%M:%S'`
#copylist=`find $filepath/`

exec > >(tee -a "$UPLOG") 2>&1


function copylist {

	ls -lahR $filepath

}





filepath=`/usr/bin/osascript <<EOT
tell application "System Events"
    activate
    set filepath to POSIX path of (choose folder with prompt "Choose folder to upload...") --with multiple selections allowed)
end tell
EOT`





#echo "$filepath"

echo Date of transfer : "$DATE"

echo User : "$USER" 

copylist

mv -f -v "$filepath" ~/DUMMYSHARE #&& echo "$USER" $date | tee -a "$UPLOG"

echo "Files included in copy : "
echo ""


