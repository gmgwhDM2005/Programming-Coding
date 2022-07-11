commands.on(
  {
    name: 'triggered',
  },
  (args) => ({ member: args.guildMemberOptional() }),
  async (message, { member }) => {
    let av;
    if (member == message.member) {
      av = message.member.user.getAvatarUrl();
    } else {
      av = member?.user.getAvatarUrl();
    }
    await message.reply(
      new discord.Embed({
        image: {
          url: `https://api.resetxd.xyz/triggered.gif?avatar=${av}`,
        },
      })
    );
  }
);

commands.on(
  {
    name: 'burn',
  },
  (args) => ({ member: args.guildMemberOptional() }),
  async (message, { member }) => {
    let av;
    if (member == message.member) {
      av = message.member.user.getAvatarUrl();
    } else {
      av = member?.user.getAvatarUrl();
    }
    await message.reply(
      new discord.Embed({
        image: {
          url: `https://api.resetxd.xyz/burn?avatar=${av}`,
        },
      })
    );
  }
);

commands.on(
  {
    name: 'web',
  },
  (args) => ({ member: args.string() }),
  async (message, { member }) => {
    await message.reply(
      new discord.Embed({
        image: {
          url: `https://api.resetxd.xyz/webshot?website=${member}`,
        },
      })
    );
  }
);

commands.on(
  {
    name: 'emojify',
  },
  (args) => ({ text: args.text() }),
  async (message, { text }) => {
    text = text.replaceAll(' ', '+');
    const req = await fetch(`https://api.resetxd.xyz/emojify?text=${text}`);
    const data = await req.json();
    await message.reply(new discord.Embed({ description: data['emojified'] }));
  }
);
