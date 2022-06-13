commands.on(
  'topic',
  (args) => ({ text: args.text() }),
  async (message, { text }) => {
    const channel = await discord.getGuildTextChannel('844227038512807936');
    const topic = channel?.topic;
    channel?.edit({ topic: text });
    message.reply(
      new discord.Embed({
        title: '✍ topic was edited by ' + message.author.getTag(),
        fields: [
          { name: 'Old Topic:', value: `${topic}` },
          { name: 'New Topic:', value: `${text}` },
        ],
      })
    );
  }
);
