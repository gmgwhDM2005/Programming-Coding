commands.raw('serverinfo', async (message) => {
  const c = await message.getGuild();
  const icon = c.getIconUrl();
  const afk = c.afkChannelId;
  const name = c.name;
  const description = c.description;
  const id = c.id;
  let defnotif;
  if (c.defaultMessageNotifications == 1) {
    defnotif = 'Mention Only';
  } else {
    defnotif = 'All Messages';
  }
  message.reply(
    new discord.Embed({
      thumbnail: { url: icon },
      title: `${name} Server Information`,
      description: [
        `Name - ${name}`,
        `Description - ${description}`,
        `Server ID - ${id}`,
        `Default Notifications - ${defnotif}`,
        `AFK Channel - ${afk}`,
      ].join('\n'),
    })
  );
});
