#!/usr/bin/bash -e
# linux_amd64_executable_server.elfを作る
# 注: poetry runを介して実行すること。

python3 -m pip install PyInstaller
python3 -m PyInstaller --onefile server.py

arch="$(uname -m)"

if [ "$arch" == "x86_64" ]; then
    arch=amd64
fi

output_filename=linux_"$arch"_executable_server.elf

mv dist/server "$output_filename"
chmod +x "$output_filename"

# Clean up
rm -r dist build server.spec
