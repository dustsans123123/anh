#!/bin/bash
cd
if [ -e "/data/data/com.termux/files/home/storage" ]; then
	rm -rf /data/data/com.termux/files/home/storage
fi
termux-setup-storage
yes | pkg update
. <(curl https://cdn.quanghuynopro.com/store/termux-change-repo.sh)
yes | pkg upgrade
yes | pkg i python
yes | pkg i python-pip
pip install requests prettytable pycryptodome asyncio pyjwt ecdsa cachetools rich
curl -Ls "https://raw.githubusercontent.com/dustsans123123/anh/refs/heads/main/main.py" -o /sdcard/Download/main.py
