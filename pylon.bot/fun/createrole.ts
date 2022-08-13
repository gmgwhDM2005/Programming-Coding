discord.interactions.commands.register(
  {
    name: 'role',
    description: 'Create a role for your guild',
    options: (args) => ({
      name: args.string('name'),
      mention: args.boolean({
        name: 'mentionable',
        description: 'All members can mention this role',
      }),
      hex: args.integer({
        name: 'colour',
        description: 'Hexidemical Role Colour (Num only)',
      }),
      hoistable: args.boolean('hoist'),
    }),
  },
  async (message, { name, mention, hex, hoistable }) => {
    const guild = await discord.getGuild();
    const role = await guild.createRole({
      name: name,
      mentionable: mention,
      color: hex,
      hoist: hoistable,
    });
  }
);
