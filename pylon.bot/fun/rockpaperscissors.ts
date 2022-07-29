function random() {
  let num = Math.ceil(Math.random() * 3);
  return num;
}

commands.raw('rps', async (message) => {
  let rps = ['Rock', 'Paper', 'Scissors'];
  let m = await message.reply(
    'Welcome to Rock Paper Scissors\nPlease wait while we setup\nDont spam the command!'
  );
  await sleep(5000);
  message.delete();
  const msg = await message.reply(
    new discord.Embed({
      title: 'How to play',
      description: [
        'The user goes 1st with choosing either: Rock, Paper or Scissors',
        'The computer then replies with: Rock, Paper or Scissors',
        'U=User, C=Computer',
        ':x: to cancel',
        ':white_check_mark: to continue',
      ].join('\n'),
    })
  );
  msg.addReaction('✅');
  msg.addReaction('❌');
  discord.on('MESSAGE_REACTION_ADD', async (reaction) => {
    if (
      reaction.messageId == msg?.id &&
      reaction.member?.user.id == message.author.id
    ) {
      switch (reaction.emoji.name) {
        case '✅':
          msg.delete();
          m.delete();
          m = await message.reply(
            new discord.Embed({ title: 'Rock Paper Scissors....' })
          );
          m.addReaction('🪨');
          m.addReaction('🧻');
          m.addReaction('✂');
          discord.on('MESSAGE_REACTION_ADD', async (reaction) => {
            if (
              reaction.messageId == m?.id &&
              reaction.member?.user.id == message.author.id
            ) {
              let game, text;
              switch (reaction.emoji.name) {
                case '🪨':
                  game = 1;
                  break;
                case '🧻':
                  game = 2;
                  break;
                case '✂':
                  game = 3;
                  break;
              }
              m.deleteAllReactions();
              const compNum = random();
              if (compNum == 1) text = 'Computer: ' + rps[0];
              else if (compNum == 2) text = 'Computer: ' + rps[1];
              else text = 'Computer: ' + rps[2];
              m.edit(
                new discord.Embed({
                  title: 'Rock Paper Scissors....',
                  description: text,
                })
              );
              await sleep(2000);
              let results;
              if (compNum == game)
                results = {
                  gameAction: 'Tie! No one gets the point!',
                  win: 'No one',
                  colour: 0xdaf542,
                };
              else if (game == 1 && compNum == 2)
                results = {
                  gameAction: 'C:Paper Defeats U:Rock',
                  win: 'Computer',
                  colour: 0xff0000,
                };
              else if (game == 1 && compNum == 3)
                results = {
                  gameAction: 'U:Rock Defeats C:Scissors',
                  win: 'User',
                  colour: 0x00ff00,
                };
              else if (game == 2 && compNum == 1)
                results = {
                  gameAction: 'U:Paper Defeats C:Rock',
                  win: 'User',
                  colour: 0x00ff00,
                };
              else if (game == 2 && compNum == 3)
                results = {
                  gameAction: 'C:Scissors Defeats U:Paper',
                  win: 'Computer',
                  colour: 0xff0000,
                };
              else if (game == 3 && compNum == 1)
                results = {
                  gameAction: 'C:Rock Defeats U:Scissors',
                  win: 'Computer',
                  colour: 0xff0000,
                };
              else if (game == 3 && compNum == 2)
                results = {
                  gameAction: 'U:Scissors Defeats C:Paper',
                  win: 'User',
                  colour: 0x00ff00,
                };
              m.edit(
                new discord.Embed({
                  title: 'Rock Paper Scissors....',
                  description: [
                    `Game: ${results?.gameAction}`,
                    `Winner: ${results?.win}`,
                  ].join('\n'),
                  color: results?.colour,
                })
              );
            }
          });
          break;
        case '❌':
          msg.delete();
          message.delete();
          m.delete();
          m = await message.reply('Game ended.');
          await sleep(1000);
          m.delete();
          break;
      }
    }
  });
});
