# Song Bird

Song Bird is a bot that plays music and posts memes to a Discord channel.

### Bot Features

- Instant music playback
- Pause/play/resume functionality
- Fresh memes

### Getting Started

Below are instructions on how to run Song Bird for yourself.

#### Prerequisites 

You will need [Git](https://git-scm.com/), [Python](https://www.python.org/downloads/), and [PIP](https://pypi.org/project/pip/) to pull from this repository and install the required dependencies on your own machine.

#### Cloning the Repository

First, go to the folder that you want to clone the repository into:
```bash
# Example:
cd C:\mydiscordbots
```
Where `mydiscordbots` is where you want to place the repository.  

Next, issue the following commands:
```bash
# Clone this repository
git clone https://github.com/Xx-Ashutosh-xX/SongBird.git
```
You should see that Git has created a folder called `SongBird` in `mydiscordbots`.

#### Running the Bot

1. Go to [Discord's Developer Portal](https://discord.com/developers/applications)
2. Create a new application 
3. Select the **bot** tab within the application settings and a new bot
4. Add permisions to it by selecting all the bot premissions below
5. Install the following python libraries:
    - Discord.py  `pip install discord.py`
    - youtube-dl  `pip install youtube-dl`
6. Add the bot to your Discord server
7. Genrate the token of your bot and replace it in `SongBird.py` file (which can be found in the `SongBird` folder)
8. Run the Python file `SongBird.py` to bring your bot online
9. Its prefix is `-` i.e 'dash', try calling `-h` or `-help` to get all the commands available yet.

### How is it made?

Song Bird is a Python file made with the Discord.py library and uses the generated token to connect to your bot.

### How does it look like?

![img](https://github.com/Xx-Ashutosh-xX/SongBird/blob/main/assets/Example.png)
