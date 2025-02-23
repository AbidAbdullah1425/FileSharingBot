from pyrogram import Client
from config import LOGGER, FORCE_SUB_CHANNEL1, FORCE_SUB_CHANNEL2, FORCE_SUB_CHANNEL3, FORCE_SUB_CHANNEL4
import config

async def export_invite_links(client: Client):
    try:
        if config.FORCE_SUB_CHANNEL1:
            link = (await client.get_chat(config.FORCE_SUB_CHANNEL1)).invite_link
            if not link:
                await client.export_chat_invite_link(config.FORCE_SUB_CHANNEL1)
                link = (await client.get_chat(config.FORCE_SUB_CHANNEL1)).invite_link
            client.invitelink1 = link
    except Exception as e:
        client.LOGGER(__name__).warning(e)
        client.LOGGER(__name__).warning("Bot can't export invite link from Force Sub Channel 1!")
        client.LOGGER(__name__).warning(f"Please double-check the FORCE_SUB_CHANNEL1 value and make sure the bot is an admin in the channel with Invite Users via Link permission, current Force Sub Channel value: {config.FORCE_SUB_CHANNEL1}")

    try:
        if config.FORCE_SUB_CHANNEL2:
            link = (await client.get_chat(config.FORCE_SUB_CHANNEL2)).invite_link
            if not link:
                await client.export_chat_invite_link(config.FORCE_SUB_CHANNEL2)
                link = (await client.get_chat(config.FORCE_SUB_CHANNEL2)).invite_link
            client.invitelink2 = link
    except Exception as e:
        client.LOGGER(__name__).warning(e)
        client.LOGGER(__name__).warning("Bot can't export invite link from Force Sub Channel 2!")
        client.LOGGER(__name__).warning(f"Please double-check the FORCE_SUB_CHANNEL2 value and make sure the bot is an admin in the channel with Invite Users via Link permission, current Force Sub Channel value: {config.FORCE_SUB_CHANNEL2}")

    try:
        if config.FORCE_SUB_CHANNEL3:
            link = (await client.get_chat(config.FORCE_SUB_CHANNEL3)).invite_link
            if not link:
                await client.export_chat_invite_link(config.FORCE_SUB_CHANNEL3)
                link = (await client.get_chat(config.FORCE_SUB_CHANNEL3)).invite_link
            client.invitelink3 = link
    except Exception as e:
        client.LOGGER(__name__).warning(e)
        client.LOGGER(__name__).warning("Bot can't export invite link from Force Sub Channel 3!")
        client.LOGGER(__name__).warning(f"Please double-check the FORCE_SUB_CHANNEL3 value and make sure the bot is an admin in the channel with Invite Users via Link permission, current Force Sub Channel value: {config.FORCE_SUB_CHANNEL3}")

    try:
        if config.FORCE_SUB_CHANNEL4:
            link = (await client.get_chat(config.FORCE_SUB_CHANNEL4)).invite_link
            if not link:
                await client.export_chat_invite_link(config.FORCE_SUB_CHANNEL4)
                link = (await client.get_chat(config.FORCE_SUB_CHANNEL4)).invite_link
            client.invitelink4 = link
    except Exception as e:
        client.LOGGER(__name__).warning(e)
        client.LOGGER(__name__).warning("Bot can't export invite link from Force Sub Channel 4!")
        client.LOGGER(__name__).warning(f"Please double-check the FORCE_SUB_CHANNEL4 value and make sure the bot is an admin in the channel with Invite Users via Link permission, current Force Sub Channel value: {config.FORCE_SUB_CHANNEL4}")