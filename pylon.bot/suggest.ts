const suggestionChannel = 'SuggestionChannelID';
//Set your suggestion channel above.

discord.interactions.commands.register(
  {
    name: 'suggest',
    description: 'Send a suggestion for us!',
    options: (args) => ({ suggestion: args.string('Suggestion') }),
  },
  async (message, { suggestion }) => {
    const name = message.member.user.getTag();
    const AvatarUrl = message.member.user.getAvatarUrl();
    const channel = await discord.getGuildTextChannel(suggestionChannel);
    const msg = await channel?.sendMessage({
      embed: new discord.Embed({
        author: {
          name: name,
          iconUrl: `${AvatarUrl}`,
        },
        timestamp: new Date().toISOString(),
        description: [`Suggestion:`, `${suggestion}`].join('\n'),
        color: 0x000fff,
      }),
    });
    msg?.addReaction('💡');
    await sleep(5);
    msg?.addReaction('❌');
    await sleep(25);
    message.respondEphemeral(
      'Suggestion Submitted!\nTake a look as <#844226134526394439>'
    );
  }
);
