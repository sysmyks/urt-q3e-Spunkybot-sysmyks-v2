# Q3e Urban Terror Jump Server with Modified SpunkyBot

This project combines an Urban Terror server specially modified for Jump mode with an adapted version of the SpunkyBot administration bot. This solution is optimized to provide a smooth parkour experience and simplified administration features.

![Urban Terror Jump](pngegg.png)

## 📋 About the Project

This server is based on a modified version of [`urbanterror-slim`](urbanterror-slim-sysmyks), derived from Q3e, with significant improvements for Jump mode. SpunkyBot has been adapted to be fully compatible with the Q3e server and offer simplified administration features.

### ✨ Server Features

- **Optimized Q3e base**: Using the Q3e engine for better performance
- **Multi-architecture**: Support for x86_64, ARM64 (Raspberry Pi 64bit)
- **DoS protection**: Enhanced security against denial of service attacks
- **Extended limits**: Support for up to 20,000 maps in a single directory
- **Server-side demo recording**: add server demo recording 

## 🎮 Custom Client Commands

| Command | Description |
|----------|-------------|
| `/noclip` | Allows players to pass through walls |
| `/save` | Improved version to save player position with race mode handling |
| `/load` | Improved version to load position with protection during races |
| `/help` | Displays the list of commands available to players |
| `/modinfo` | Displays information about the server version and credits |

## 🛠️ RCON Administrator Commands

| Command | Description |
|----------|-------------|
| `/rcon saveplayerpos <player-name>` | Saves the position of a specific player |
| `/rcon loadplayerpos <player-num> <x> <y> <z> <pitch> <yaw> <roll>` | Loads a precise position for a player |
| `/rcon infinitestamina <player-name>`  | full stamina |

## 🏃 Race Tracking System

The server includes an advanced race tracking system with:
- `isReady` variable to check if a player is in Ready mode
- `isRunning` variable to monitor if a player is in the middle of a race
- Warnings before allowing position loading during a race
- Protection against accidental teleportations that could compromise race integrity

## 🤖 Modified SpunkyBot

This version of SpunkyBot has been specially adapted to work with the modified Q3e server:

- **Lightweight libraries**: Optimized version of the main libraries
- **Q3e compatible**: Complete adaptation to work with our server version
- **Simplified interface**: Streamlined administrator commands
- **Record tracking**: Storage and display of best times by map

## 📦 Installation

### Prerequisites

- ou must have a mapcycle.txt file, spunkybot only recognizes maps listed in mapcycle.txt
- Python 3
- Linux/Windows/Raspberry Pi 64bit 

## Dependencies 

| Package | Version | Purpose |
|---|---|---|
| `deep-translator` | 1.11.4 | Google Translate, no API key required |
| `unidecode` | 1.4.0 | Kept from previous setup |
