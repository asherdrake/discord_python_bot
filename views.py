import discord
from discord.ui import Select, View

class reminder_view(discord.ui.View):
    async def reminder_menu(self, ctx, jobs):
        reminder_dropdown = Select(# the decorator that lets you specify the properties of the select menu
            placeholder = "Select a Reminder", # the placeholder text that will be displayed if nothing is selected
            min_values = 1, # the minimum number of values that must be selected by the users
            max_values = 1, # the maximum number of values that can be selected by the users
            options = [
                discord.SelectOption(
                    label="Vanilla",
                    description="Pick this if you like vanilla!"
                ),
                discord.SelectOption(
                    label="Chocolate",
                    description="Pick this if you like chocolate!"
                ),
                discord.SelectOption(
                    label="Strawberry",
                    description="Pick this if you like strawberry!"
                )
            ]
        )
        self.view = View()
        self.view.add(reminder_dropdown)

    async def select_callback(self, select, interaction): # the function called when the user is done selecting options
        await interaction.response.send_message(f"Awesome! I like {select.values[0]} too!")

class music_view(discord.ui.View):
    pass