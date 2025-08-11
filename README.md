# Instagram Story Viewer Bot

This bot automates viewing stories from users who have liked a specific Instagram post. It logs in using your `sessionid` for improved security and stability.

## Features

- **Login with Session ID**: Securely log in using your browser's session cookie instead of your password.
- **Targeted Viewing**: Fetches usernames from the likers of a specific post.
- **Action Selection**: Choose to only view stories. (Liking is currently disabled as the feature is unstable on Instagram's private API).
- **Human-like Behavior**: Uses randomized delays between actions to mimic human behavior and reduce the risk of account flagging.

## Requirements

- Python 3
- `instaloader`

You can install the required library using pip:
```bash
pip install instaloader
```

## How to Use

### 1. Get Your `sessionid`

You need to get your `sessionid` cookie from your web browser after logging into Instagram.

**For Chrome/Edge:**
1. Go to [instagram.com](https://www.instagram.com) and log in.
2. Press `F12` to open Developer Tools.
3. Go to the **Application** tab.
4. On the left side, under **Storage**, expand **Cookies** and select `https://www.instagram.com`.
5. Find the cookie named `sessionid` in the list.
6. Copy the long string from the **Value** column. This is your `sessionid`.

**For Firefox:**
1. Go to [instagram.com](https://www.instagram.com) and log in.
2. Press `Shift + F9` or right-click the page and select **Inspect** -> **Storage**.
3. On the left side, expand **Cookies** and select `https://www.instagram.com`.
4. Find the cookie named `sessionid`.
5. Copy the long string from the **Value** column.

### 2. Run the Bot

Execute the script from your terminal:
```bash
python Bot_Like.py
```

The script will then prompt you for:
1. Your Instagram username.
2. Your `sessionid` value that you copied.
3. Your choice of action (viewing stories).
4. The shortcode of the post you want to target (e.g., `C0SBieHggMm` from a URL like `https://www.instagram.com/p/C0SBieHggMm/`).

The bot will then start its process.
