commands.on(
  {
    name: 'search',
    aliases: ['google', 'youtube'],
    description: 'searches things on the internet',
    onError: ({ message }) => {
      message.reply(
        new discord.Embed({
          title: `:x: Try again ${
            message.author.username + '#' + message.author.discriminator
          }`,
          description:
            'Invalid Options.\nTry !search [google, youtube] <queried search>',
        })
      );
    },
  },
  (args) => ({
    website: args.string({ choices: ['google', 'youtube'] }),
    search: args.text(),
  }),
  async (message, { search, website }) => {
    let user = await discord.getUser(message.author.id);
    let avatarurl = await user?.getAvatarUrl();
    let url;
    if (website == 'google') {
      url = 'https://www.google.com/search?q=';
    } else if (website == 'youtube') {
      url = 'https://www.youtube.com/results?search_query=';
    }
    const rep = search.replaceAll(' ', '+');
    message.reply(
      new discord.Embed({
        thumbnail: { url: `${avatarurl}` },
        title: `Website Search`,
        description: [
          `Search: [Click to see search](${url}${rep})`,
          `Illustrator: ${message.author.username}`,
          `Requested Search: ${search}`,
        ].join('\n'),
      })
    );
  }
);
