# mwBot

### package management
To install pakcages, clone this repository and run follow command.
```sh
pip install -r requirements.txt
```

To uodate pip package list, run `./script/update-requrements.sh`.
```sh
sh ./scripts/update-requrements.sh
```

This project use **venv** for package management.
```sh
python3 -m venv --prompt . .venv
source .venv/bin/activate
```
### .env
```.env
APP_BOT_TOKEN="your discord bot token"
NOTICE_CHANNEL_ID="your notice channel id"
```

### how to run
```sh
python main.py
```

## reference
### discord.py
- [discord.py](https://discordpy.readthedocs.io/ja/latest/index.html)
- [discord.py V2(2.0)のスラッシュコマンドを使えるようにする](https://qiita.com/Kodai0417/items/3abff9575e132e2955ec)
### yt-dlp
- [【Python/Tkinter】yt-dlpを使ってみた話](https://qiita.com/kuro_8193/items/31706b620d69993afd90)
### gigafile
- [gfile](https://github.com/fireattack/gfile)