#!/bin/bash
# Script untuk instal LuckyZip

scripts=("lucky-zip-cli" "lucky-zip-gui")
chmod +x "${scripts[@]}"
cek=$(uname -o)
if [[ "${cek}" == "Android" ]]; then
    path="/data/data/com.termux/files/usr/bin"
    mv "${scripts[@]}" "${path}"
    pip3 install -r android.txt
    echo "Proses instalasi selesai."
elif [[ "${cek}" == "GNU/Linux" ]]; then
    path="/usr/bin"
    mv "${scripts[@]}" "${path}" 
    pip3 install -r linux.txt
    echo "Proses instalasi selesai."
fi
    
   
