#!/usr/bin/sh
sudo wget https://github.com/shiftkey/desktop/releases/download/release-2.6.3-linux1/GitHubDesktop-linux-2.6.3-linux1.deb
sudo apt-get install gdebi-core
sudo gdebi GitHubDesktop-linux-2.6.3-linux1.deb
github-desktop
