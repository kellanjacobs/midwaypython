# MacOS X Setup

Here is how I setup my mac for these lessons. If you have a different way you perfer feel free to do it.
I chose these methods due to my experience with OSX. If you know a better way feel free to let me know.

## Steps

1. Install Homebrew
2. Optional OSX Setup
3. Install Python
4. Install Docker
5. Install Pycharm or other text editor. 

## Setup Homebrew

[Homebrew](https://brew.sh/) is an excellent package manager for the Mac. It works similar to yum 
or apt on linux. It will allow you to install many open source packages on your mac without having
to figure out how to compile them yourself.

Open of the Macs built in terminal application It located at `/Applications/Utilities/Terminal`

```bash
# Install Homebrew
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
# Run brew doctor to check to make sure everything is setup correctly. 
```

When I did this in a VM on my work machine I ran into certificate errors. This was because my VM didn't 
have the certificate for our security software that was hijacking my connection if you have this 
problem just a k to the curl part of the command so it looks like `curl -fsSlk` and your install will 
work.

## Optional OSX Setup

These steps are totally 100% optional. These are my personal preferences to replace a couple of OSX default 
applications. 

Install iterm2 and a better monospace font
```bash
# install iterm2
brew cask install iterm2
```
Iterm is now installed in your application folder. When you open it for the first time it will ask
you to change permissions for full disk access. Go ahead and follow the instructions on the prompt
to enable disk access.

Next lets install a better monospace font. I like [source code pro](https://github.com/adobe-fonts/source-code-pro) 
from Adobe It is a free font that I find easier to read code in. 
```bash
brew tap homebrew/cask-fonts && brew cask install font-source-code-pro
```

# Install python
OSX comes with python 2.7.15 currently. First we want to use python3 for this project. Secondly the
OSX Python leaves out some parts of the python system that we will need to compile some python 
packages. Use your terminal app or iterm to install python

```bash
# Install python3
brew install python
# Verify that python3 is installed
python3
#Python 3.7.2 (default, Dec 27 2018, 07:35:06)
#[Clang 10.0.0 (clang-1000.11.45.5)] on darwin
#Type "help", "copyright", "credits" or "license" for more information.

#Type ctrl+d to or exit() to leave the python prompt
```

# Install Docker

While homebrew is great. Docker is used to better isolate applications in your system. Also this 
is the method we will use to deploy our application. 

Go to [Dockers Website](https://hub.docker.com/editions/community/docker-ce-desktop-mac)
They now requrie you to signup for a free account to download docker. Create the account and proceed 
to the download. 

You will have a file `docker.dmg` inside your download folder. Double Click on the file to open 
the installer. Drag the docker application icon on top of the application folder icon to install 
the docker

Go to your application folder and double click the docker icon. This will finish the docker install
and get it setup for your system. Follow the instructions typing your password when required

To verify that docker is working open a **new** terminal window and run the following commands. 

```bash
docker version
Client: Docker Engine - Community
 Version:           18.09.1
 API version:       1.39
 Go version:        go1.10.6
 Git commit:        4c52b90
 Built:             Wed Jan  9 19:33:12 2019
 OS/Arch:           darwin/amd64
 Experimental:      false

Server: Docker Engine - Community
 Engine:
  Version:          18.09.1
  API version:      1.39 (minimum version 1.12)
  Go version:       go1.10.6
  Git commit:       4c52b90
  Built:            Wed Jan  9 19:41:49 2019
  OS/Arch:          linux/amd64
  Experimental:     true
```

# Pull docker images we will need.
To save everyone trying to download huge files on the same wifi at the same time. Lets get the docker
images we will need to run this week. 

```bash
docker pull postgres
docker pull nginx
```
#Install Pycharm

First [download Pycharm](https://www.jetbrains.com/pycharm/download/#section=mac) In this class we will be using Pycharm professional. When the download has finished nagavate to your downloads folder and find the `pycharm-professional-2018.3.3.dmg` file. 

Double Click the file. Drag the pycharm application to the application folder and wait for it to install. 

Double Click the pycharm application from your applications folder. 

The first dialog select the option for not having any previous settings. 

![Pycharm Dialog Box 1](https://raw.githubusercontent.com/kellanjacobs/midwaypython/master/docs/000_Setup/images/pycharmdia1.png)

Next select the Darkula theme

![Pycharm Dialog Box 2](https://raw.githubusercontent.com/kellanjacobs/midwaypython/master/docs/000_Setup/images/pycharmdia2.png)

On the Launcher Script Dialog select the Featured Plugin button.

On the featured plugin page click to install the plugins for Markdown and BashSupport. Then click start using pycharm.

![Pycharm Dialog Box 3](https://raw.githubusercontent.com/kellanjacobs/midwaypython/master/docs/000_Setup/images/pycharmdia3.png)

If you want your editor to look like mine then continue along. 
![Pycharm Dialog Box 4](https://raw.githubusercontent.com/kellanjacobs/midwaypython/master/docs/000_Setup/images/pycharmdia4.png)

In the Welcome to Pycharm window select configure->preferences Under editor font change your font to source code pro. 
![Pycharm Dialog Box 5](https://raw.githubusercontent.com/kellanjacobs/midwaypython/master/docs/000_Setup/images/pycharmdia5.png)


#Install Postman

In a browser go to [Postman website](https://www.getpostman.com/downloads/) and download postman

You will find a file `Postman-osx-6.7.2.zip` in your downloads directory. 

Double click on the `Postman-osx-6.7.2.zip` to extract the zip file. This will create the postman application.
Drag the application to your Applications directory on your hard drive. 


