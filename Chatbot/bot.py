# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.

# Modified by: James Jeremiah
# james2.jeremiah@uwe.ac.uk
# Student number: 17042447
# 27/04/2021
# 
# Intialises the conversation when user joins
# Calls the read_message.py file when it receives a message

import read_message

from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount


class MyBot(ActivityHandler):
    """Handles functions and executes them on certain user activities."""

    #when user sends a message
    async def on_message_activity(
        self,
        turn_context: TurnContext
    ):
        #send response message to user
        await turn_context.send_activity(f"{read_message.main(turn_context.activity.text)}")
            

    #when user joins the chat with bot
    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                
                #get user email/name
                user_name = turn_context.activity.from_property.name
                
                #intialise conversation and store user name
                read_message.conversation(user_name)
            
                await turn_context.send_activity(f"Hello! Thank you for using this bot. How can I help you? 🤖")