import subprocess

# COLORS VARIABLE

PURPLE = '\033[95m'
BLUE = '\033[94m'
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
NC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


def execute(section, commands):
    splitted = commands.split(" ")
    splitted.append("--noconfirm")
    print(f"{YELLOW}{section}{NC}")
    try:
        subprocess.run(splitted, check=True, stdout=subprocess.DEVNULL)
    except Exception as err:
        print(f"{RED}Error when installing some packages, please retry{NC}")


title = f"""{PURPLE}*AETHER DOTFILES INSTALLER*
INSTALLER BY ilham25{NC}"""
selectText = """
Select your linux base :
1. Debian Based (Ubuntu, Linux Mint, KDE Neon, Elementary OS, etc)
2. Arch Based (Artix, Archcraft, Archlabs, Manjaro, etc)
"""


def dotfiles():
    print(f"{GREEN}INSTALLING DOTFILES CONFIG{NC}")
    execute("Creating temporary directory", "mkdir tmp")
    execute("Clone dotfiles-aether ",
            "git clone https://github.com/ilham25/dotfiles-aether")
    execute("Copy all dotfiles config to home directory",
            "cd dotfiles-aether/ && cp -r {.*,*} ~/")
    execute("Installing custom icon", "cd ~/.icons/")
    execute("--", "tar -Jxvf oomox-aesthetic-light.tar.xz && tar -Jxvf oomox-aesthetic-dark.tar.xz")
    execute("-- Copy all custom icons to /usr/share/icons directory",
            "sudo cp -r {oomox-aesthetic-light,oomox-aesthetic-dark} /usr/share/icons/")
    execute("-- Delete unnecessary files",
            "rm -r ~/.icons/{oomox-aesthetic-light,oomox-aesthetic-dark,*.tar.xz}")
    execute("Refresh font cache", "fc-cache -rv")


def debian():
    print(f"{GREEN}INSTALLING DOTFILES DEPENDENCIES${NC}")
    execute("Installing i3-Gaps Window Manager", "echo")
    execute("-- Add PPA repo for i3-gaps",
            "sudo add-apt-repository ppa:kgilmer/speed-ricer")
    execute("-- Update apt", "sudo apt-get update")
    execute("-- Installation", 'sudo apt-get install i3-gaps-wm i3-gaps-session')
    execute("Installing core dependencies", 'sudo apt install feh git rsync python psmisc wireless-tools alsa-utils brightnessctl nitrogen dunst tint2 gsimplecal rofi lxappearance qt5ct qt5-style-plugins lxpolkit xautolock rxvt-unicode xclip scrot thunar thunar-archive-plugin thunar-media-tags-plugin thunar-volman ffmpegthumbnailer tumbler w3m w3m-img geany viewnior mpv mpd mpc ncmpcpp pavucontrol parcellite neofetch htop imagemagick ffmpeg playerctl xsettingsd')
    execute("Installing oh-my-zsh & plugins", "sudo apt install zsh")
    execute("-- Change default shell to zsh for current user",
            "chsh -s `which zsh`")
    execute("-- Plugin install (oh-my-zsh)",
            'sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"')
    execute("-- Plugin install (zsh-syntax-highlighting)",
            'git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting')
    execute("-- Plugin install (zsh-autosuggestions)",
            'git clone https://github.com/zsh-users/zsh-autosuggestions.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions')
    execute('Installing picom compositor', "sudo apt install libxext-dev libxcb1-dev libxcb-damage0-dev libxcb-xfixes0-dev libxcb-shape0-dev libxcb-render-util0-dev libxcb-render0-dev libxcb-randr0-dev libxcb-composite0-dev libxcb-image0-dev libxcb-present-dev libxcb-xinerama0-dev libxcb-glx0-dev libpixman-1-dev libdbus-1-dev libconfig-dev libgl1-mesa-dev  libpcre2-dev  libevdev-dev uthash-dev libev-dev libx11-xcb-dev ninja-build meson")
    execute("-- Clone picom build source",
            "git clone https://github.com/yshui/picom.git && cd picom/")
    execute("-- Start building", "git submodule update --init --recursive")
    execute("-- ", "meson --buildtype=release . build")
    execute("-- ", "ninja -C build")
    execute("-- ", "ninja -C build install")
    execute("Installing psuinfo - Network & CPU Monitor, RAM Usage", "echo")
    execute("-- Clone psuinfo from it's repo",
            "git clone https://github.com/nwg-piotr/psuinfo.git && cd psuinfo/")
    execute("-- Copy psuinfo and icon to /usr/bin directory",
            "sudo cp -r {psuinfo,icons} /usr/bin")


def arch():
    print(f"{GREEN}INSTALLING DOTFILES DEPENDENCIES${NC}")
    print(f"{RED}Consider install yay AUR helper first if error acquired!{NC}")
    execute("Installing i3-Gaps Window Manager", "sudo pacman -S i3-gaps")
    execute("Installing audio", "")
    execute("Installing brightness", "yay -S brightnessctl")
    execute("Installing psuinfo - Network & CPU Monitor, RAM Usage",
            "yay -S psuinfo")
    execute("Installing wireless tools", "sudo pacman -S wireless_tools")
    execute("Installing git", "sudo pacman -S git")
    execute("Installing other utility (panel, notification, terminal, file manager, etc)",
            "yay -S dunst tint2 gsimplecal rofi feh lxappearance qt5ct qt5-styleplugins lxsession xautolock rxvt-unicode-patched xclip scrot thunar thunar-archive-plugin thunar-media-tags-plugin thunar-volman tumbler w3m geany nano vim viewnior pavucontrol parcellite neofetch htop picom-ibhagwan-git gtk2-perl xfce4-power-manager zsh zsh-completions imagemagick playerctl networkmanager-dmenu")
    execute("Installing oh-my-zsh & plugins", "echo")
    execute("-- Change default shell to zsh for current user",
            "chsh -s /usr/bin/zsh")
    execute("-- Plugin install (oh-my-zsh)",
            'sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"')
    execute("-- Plugin install (zsh-syntax-highlighting)",
            'git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting')
    execute("-- Plugin install (zsh-autosuggestions)",
            'git clone https://github.com/zsh-users/zsh-autosuggestions.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions')


options = {
    1: debian,
    2: arch,
}

print(title)
print(selectText)
choice = input("Select : ")

try:
    options[int(choice)]()
except:
    print(f"{RED}Input error")
