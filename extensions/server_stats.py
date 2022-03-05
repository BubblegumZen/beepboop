import discord
from discord.ext import commands


class ServerStats(commands.Cog):
    """Command category for server stats."""
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.channels = {}

    @staticmethod
    async def __get_guild_and_channel(ctx: commands.Context):
        return ctx.guild, ctx.channel

    @staticmethod
    async def __update_member_count(member: discord.Member, channels_: dict) -> None:
        guild = member.guild # Get the guild

        if guild not in channels_.keys(): # If this channel has not been set as a member count channel
            return

        channel = channels_[guild]
        await channel.edit(name=f"Total Members: {guild.member_count}")

    @commands.command(name="setmembercount", aliases=["setcount"], description="Sets a channel as the member count channel.")
    @commands.has_permissions(manage_channels=True)
    async def set_member_count(self, ctx: commands.Context):
        """Sets a channel as the member count channel.
        Locks the channel and displays the member count as its name.
        """
        guild, channel = await ServerStats.__get_guild_and_channel(ctx)

        if guild not in self.channels.keys():
            self.channels[guild] = channel # Store the server and channel in self.channels
            await ctx.send("✅ This channel has been removed as the member count channel.")
            return
        if channel == self.channels[guild]:
            await ctx.send("❌ This channel is already counting members.")

        await self.__update_member_count(ctx.author, self.channels)

    @commands.command(name="removemembercount", aliases=["removecount"], description="Sets a channel as the member count channel.")
    @commands.has_permissions(manage_channels=True)
    async def remove_member_count(self, ctx: commands.Context):
        """Removes a channel as the member count channel.
        Unlocks the channel and stops displaying the member count as its name.
        """
        guild, channel = await ServerStats.__get_guild_and_channel(ctx) # Get guild and channel

        if guild in self.channels.keys():
            del self.channels[guild] # Delete the entry from the dictionary
            await ctx.send("✅ This channel has been removed as the member count channel.")
            return
        if channel == self.channels[guild]:
            await ctx.send("❌ This channel cannot be removed as the member count channel again.")

        await self.__update_member_count(ctx.author, self.channels) # Update member counts

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        """Updates the member count channel.
        Requires the user to have used .membercount.
        """
        await self.__update_member_count(member, self.channels) # Update member counts

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        """Updates the member count channel.
        Requires the user to have used .membercount.
        """
        await self.__update_member_count(member, self.channels) # Update member counts


def setup(bot: commands.Bot):
    """Adds the ServerStats cog to the bot."""
    bot.add_cog(ServerStats(bot))