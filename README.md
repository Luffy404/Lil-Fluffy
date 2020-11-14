[![GitHub contributors][contributors-shield]][contributors-url] 
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![Discord][discord-shield]][discord-url]
<br />
<p align="center">
  <a href="https://github.com/Luffy404/Lil-Fluffy">
    <img src="https://cdn.discordapp.com/app-icons/771841748203733012/0604c3a7744e67df06be157071d972d4.png?size=256" alt="Logo" width="128" height="128">
  </a>
	<h3 align="center">Lil' Luffy</h3>
	  <p align="center">
    An awesome Bot created by Luffy404
    <br />
    <a href="https://github.com/Luffy404/Lil-Fluffy"><strong>Explore the docs »</strong></a>
    <br />
    <a href="https://github.com/Luffy404/Lil-Fluffy/issues">Report Bug</a>
    ·
    <a href="https://github.com/Luffy404/Lil-Fluffy/issues">Request Feature</a>
 </p>


## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Cogs](#cogs)
    * [core.py](#corepy)
    * [debug.py](#debugpy)
    * [fun.py](#funpy)
    * [information.py](#informationpy)
    * [listener.py](#listenerpy)
    * [music.py](#musicpy)
    * [say.py](#saypy)
    
## About the Project

This Project is a Discord Bot, was created on October 30, 2020.
I started writing Discord Bots 2 Years ago but stopped because I didn't have enough time.
I got interested in uploading Projects to Github and what would be better then to create Discord Bots?
This bot contains features I decided to keep from old Versions.

### Built with
This Bot bases on Python 3.9 

## Getting Started
To get started you should download the current ZIP (I **never** Push commits without testing them)
### Prerequisites
In order to get the bot Running you need to install the requirements in the requirements.txt file.
```cmd
python3 -m pip install -r requirements.txt -U
```
You also need [FFMPEG](https://ffmpeg.org) to use the [music.py](#musicpy) Extension


### Installation
After you downloaded the Bot, there are some files you should change / create.
* config.json
    * In this File you should change some Settings. The first three settings ('DESCRIPTION', 'PREFIXES' & 'QUESTIONMARK') 
can be changed.
    * **DESCRIPTION** will be the description of the Bot.
    * **PREFIXES** will be the Prefixes the Bot responds to. (The bot also responds to it being tagged)
    * **QUESTIONMARK** is the Emoji the bot reacts to when a Command is issued that havent been found.
* bot.db
    * You need to create a Database based on [SQLite](https://www.sqlite.org) called `bot.db`
    * After that you need to execute the Command:
    ```sql
    CREATE TABLE "counter" (
	"all_messages"	INTEGER,
	"all_commands"	INTEGER,
	"completed_commands"	INTEGER,
	"loc"	INTEGER,
	"highest_loc"	INTEGER,
	"chars_in_total"	INTEGER,
	"highest_chars_in_total"	INTEGER)
    ```
## Cogs
  
### core.py

### debug.py

### fun.py

### information.py

### listener.py

### music.py

### say.py

[contributors-shield]: https://img.shields.io/github/contributors/Luffy404/Lil-Fluffy.svg?style=flat-square
[contributors-url]: https://github.com/Luffy404/Lil-Fluffy/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Luffy404/Lil-Fluffy.svg?style=flat-square
[forks-url]: https://github.com/Luffy404/Lil-Fluffy/network/members
[stars-shield]: https://img.shields.io/github/stars/Luffy404/Lil-Fluffy.svg?style=flat-square
[stars-url]: https://github.com/Luffy404/Lil-Fluffy/stargazers
[issues-shield]: https://img.shields.io/github/issues/Luffy404/Lil-Fluffy.svg?style=flat-square
[issues-url]: https://github.com/Luffy404/Lil-Fluffy/issues
[license-shield]: https://img.shields.io/badge/License-MIT-yellow.svg
[license-url]: https://github.com/Luffy404/Lil-Fluffy/blob/main/LICENSE
[discord-shield]: https://img.shields.io/discord/677473028204134401.svg?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=vpEv3HJ
[discord-url]: https://discord.gg/XZazRvchjP
