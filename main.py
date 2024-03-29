import discord
import os
from dotenv import load_dotenv
load_dotenv()

client = discord.Client(intents=discord.Intents.default())
tree = discord.app_commands.CommandTree(client)

# 起動確認
@client.event
async def on_ready():
    print("READY")
    await tree.sync()

# 通話が開始されるとメッセージを送信する
@client.event
async def on_voice_state_update(mem:discord.Member, bf:discord.VoiceState, af:discord.VoiceState):
    if bf.channel == None and len(af.channel.members) == 1:
        print(f'VC_NOTICE: [{mem.display_name}] join in [{af.channel.name}].')
        await client.get_channel(int(os.environ['NOTICE_CHANNEL_ID'])).send(f'{af.channel.name}に誰か来たようです！')

# YouTube ダウンロードコマンド
from yt_dlp import YoutubeDL
from gfile import GFile
@tree.command(name="youtube_dowonload", description="Download YouTube video.")
async def download_youtube_command(interaction: discord.Interaction, url:str):
    await interaction.response.send_message('リクエストを処理中...')
    opt = {
            'outtmpl': './download/%(title)s.%(ext)s',
            'format': 'best',
        }
    path = ""
    with YoutubeDL(opt) as ydl:
        inf = ydl.extract_info(url, download=True)
        path = ydl.prepare_filename(inf)
    gfile_url = GFile(path, progress=False).upload().get_download_page()
    os.remove(path)
    await interaction.followup.edit_message(content=f'処理が完了しました。[ダウンロード]({gfile_url})')

client.run(os.environ['APP_BOT_TOKEN'])