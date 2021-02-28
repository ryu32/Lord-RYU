from time import sleep
from userbot import CMD_HELP, bot
from userbot.events import register
from telethon import events
import asyncio


@register(outgoing=True, pattern='^.halo(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`hai kamu`")
    sleep(3)
    await typew.edit("`salken ya`")
    sleep(1)
    await typew.edit("`xixixixi`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.ldr(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Kasihan`")
    sleep(1)
    await typew.edit("`Cantik Cantik Kok`")
    sleep(1)
    await typew.edit("`Pacaran`")
    sleep(1)
    await typew.edit("`Online`")
    sleep(1)
    await typew.edit("`Aoakaowkowkw`")
    sleep(1)
    await typew.edit("`Canda Online`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.g(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`ganteng doang`")
    sleep(3)
    await typew.edit("`Tukang Ghosting`")
    sleep(1)
    await typew.edit("`Canda Setan:v`")
# Create by myself @localheart


@register(outgoing=True, pattern="^.kasihan$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("yahhahah")
        await e.edit("kasian")
        await e.edit("jadi")
        await e.edit("bahan")
        await e.edit("gabut")
        await e.edit("dia")
        await e.edit("xixixixi")
        await e.edit("mana masih muda")
        await e.edit("Aoakaowkowkw")
        await e.edit("kasihan")
        await e.edit("udah")
        await e.edit("virtual")
        await e.edit("masih")
        await e.edit("berharap")
        await e.edit("dia serius:v")
        await e.edit("padahal")
        await e.edit("cuma")
        await e.edit("tempat gabut")
        await e.edit("xixixix")
        await e.edit("<TAMAT>")
        
       
