from time import sleep
from userbot.events import register


@register(outgoing=True, pattern='^.roif(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Hai Perkenalkan Namaku Roif`")
    sleep(3)
    await typew.edit("`16 Tahun`")
    sleep(1)
    await typew.edit("`Tinggal Dibekasi, Salam Kenal:)`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.sayang(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Cuma Mau Bilang`")
    sleep(3)
    await typew.edit("`Aku Sayang Kamu`")
    sleep(1)
    await typew.edit("`I LOVE YOU 💞`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Apapun Yang Terjadi`")
    sleep(3)
    await typew.edit("`Tetaplah Bernapas`")
    sleep(1)
    await typew.edit("`Dan Selalu Bersyukur`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.kiw(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Cewek`")
    sleep(3)
    await typew.edit("`Mau Gak Jadi Pacar Aku:v?`")
    sleep(1)
    await typew.edit("`xixixixix`")
# Create by myself @localheart


CMD_HELP.update({
    "KIW":
    ">`.kiw`"
    "\nUsage: lihat sendiri."
})
