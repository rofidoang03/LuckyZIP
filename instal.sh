#!/bin/bash
# Script untuk instal LuckyZip

scripts=("lucky-zip-cli" "lucky-zip-gui")
chmod +x "${scripts[@]}"
path="/usr/bin/"
mv "${scripts[@]}" "${path}"
echo "Proses instalasi selesai."
