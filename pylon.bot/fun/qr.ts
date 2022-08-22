commands.on(
  'qr',
  (args) => ({ link: args.string() }),
  async (message, { link }) => {
    if (link.includes('https://'))
      message.reply(
        new discord.Embed({
          image: {
            url: `https://api.qrserver.com/v1/create-qr-code/?size=120x120&data={link}`,
          },
        })
      );
    else message.reply('Invald URL');
  }
);
