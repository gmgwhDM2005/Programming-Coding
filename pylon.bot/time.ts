commands.on(
  'time',
  () => ({}),
  async (message) => {
    let dt = new Date();
    dt.setHours(dt.getHours());
    message.reply(`<t:${Math.round(dt.getTime() / 1000)}:F>`);
  }
);
