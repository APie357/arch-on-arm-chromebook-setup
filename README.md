# Arch Linux on an arm64 Chromebook
It can be a difficult thing to use because the software library is limited, but is worth it if you don't want to bother with Google and their services on your Chromebook. Or perhaps you can't get updates for your Chromebook, as that is limited to 5 or 10 years and that amount of time has already passed.
## Installing Arch Linux on your Chromebook
To install Arch Linux on your arm64 Chromebook, find your Chromebook on [archlinuxarm.org/platforms](https://archlinuxarm.org/platforms) and follow the instructions. You will need an SD card with a USB adapter or a USB flash drive that is 16GB or more in size. I would recommend [this one on Amazon](https://www.amazon.com/Samsung-MUF-64AB-AM-Plus-64GB/dp/B07D7P4SY4/).
## Running the script
You must run the following command as root. If you don't have curl installed, install it with `pacman -S curl`. Make sure youi have access to the internet! Use `wifi-menu` if you are using wifi.
```sh
# Setup script doesn't exist yet. Will make one soon.
curl https://raw.githubusercontent.com/Genius-Format/arch-on-arm-chromebook-setup/main/setup.sh | bash
```
Default login:

Username: `root`

Password: `root`
