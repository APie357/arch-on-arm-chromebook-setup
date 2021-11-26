from getpass import getpass, getuser
import os

def main():
    print("Arch on an arm64 Chromebook Setup")
    print("  v0.1a - Genius-Format\n  This script is still a WIP!")

    print("Set a hostname for your device: ")
    hostname = input("Hostname")

    print("Set your locale:")
    locale = input("Locale [en_US]: ")
    if(locale == ""):
        locale = "en_US"
    
    print("Set your timezone:")
    region = input("Region [America]: ")
    city = input("City [Chicago]: ")
    if(region == ""):
        region = "America"
    if(city == ""):
        city == "Chicago"
    
    print("Set your root password (If you mess up, you won't be able to change it again from the script. Input your password carefully!):")
    os.system("passwd root")

    print("Create a new user with sudo rights:")
    newuser = getuser("Username: ")
    os.system(f"useradd -m {newuser}")
    os.system(f"passwd {newuser}")


    print("Configuring system...")

    print("Setting time...")
    os.system("timedatectl set-ntp true")
    os.system(f"ln -sf \"/usr/share/zoneinfo/{region}/{city}\" /etc/localtime")
    os.system("hwclock --systohc")
    print("OK")

    print("Seting locale...")
    with open("/etc/locale.gen", "a") as localeFile:
        localeFile.write(f"\n{locale}.UTF-8 UTF-8")
    os.system("locale-gen")
    print("OK")

    print("Setting hostname...")
    with open("/etc/hostname", "w") as hostnameFile:
        hostnameFile.write(hostname)
    print("OK")

    print("Setting hosts...")
    with open("/etc/hosts", "a") as hostsFile:
        hostsFile.write("# Localhost")
        hostsFile.write("127.0.0.1    localhost")
        hostsFile.write("::1          localhost")
        hostsFile.write(f"127.0.1.1    {hostname}")
        hostsFile.write(f"127.0.1.1    {hostname}.localdomain")
    print("OK")

    print(f"Configuring account {newuser}...")
    os.system(f"usermodd -aG wheel,audio,video,optical,storage {newuser}")
    print("OK")

    print("Installing software...")
    os.system("pacman -Syu sudo vim nano git base-devel")
    with open("/etc/sudoers", "a") as sudoersFile:
        sudoersFile.write("\n%wheel ALL=(ALL) ALL\nUSER_NAME HOST_NAME= NOPASSWD: /usr/bin/halt,/usr/bin/poweroff,/usr/bin/reboot,/usr/bin/shutdown")
    os.system("chown -c root:root /etc/sudoers && chmod -c 0440 /etc/sudoers")
    os.system("userdel alarm")
    os.system("git clone https://aur.archlinux.org/yay-git.git /tmp/yay && cd /tmp/yay")
    os.system("makepkg -siy")
    os.system("cd ~")
    os.system("yay -Syu firefox exa-git i3-git i3status dmenu xorg xorg-xinit lightdm lightdm-webkit-greeter")


if(__name__ == "__main__"):
    if(os.environ["USER"] == "root"):
        main()
    else:
        os.error("You must run the script as root.")
