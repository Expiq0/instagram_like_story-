import instaloader
import os
import random
from time import sleep

def login_with_sessionid():
    """
    Logs into Instagram using a session ID provided by the user.
    """
    L = instaloader.Instaloader(
        # Add some default settings for instaloader
        sleep=True,
        user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E302 Instagram 10.26.0 (iPhone7,2; iOS 12_3_1; en_US; en-US; scale=2.00; 750x1334) AppleWebKit/603.1.30",
        save_metadata=False,
        download_pictures=False,
        download_videos=False,
        download_video_thumbnails=False,
        download_geotags=False,
        download_comments=False,
        compress_json=False,
    )

    try:
        username = input("Enter your Instagram username: ")
        sessionid = input("Enter your sessionid cookie value: ")

        # Manually load the session cookie into the context
        L.context.load_session_from_file(username) # Try to load existing session first
    except FileNotFoundError:
        print("Session file not found. Creating a new one from sessionid.")
        L.context.session.cookies.set('sessionid', sessionid, domain='.instagram.com')
        # After setting the cookie, we need to "validate" the session.
        # A good way is to try to get our own profile.

    try:
        print("Attempting to log in and fetch profile...")
        profile = instaloader.Profile.from_username(L.context, username)
        # This call forces instaloader to check the login status
        if not L.context.is_logged_in:
             # Manually trigger the login check
            L.context.login(profile.username, sessionid)

        print(f"Login successful for user: {profile.username}")
        L.save_session_to_file()
        return L
    except Exception as e:
        print(f"Login failed. The sessionid might be invalid or expired. Error: {e}")
        return None

def get_user_choice():
    """
    Asks the user to choose an action.
    """
    print("\nPlease choose an action:")
    print("1: View stories only")
    print("2: Like stories only")
    print("3: View and Like stories")

    while True:
        choice = input("Enter your choice (1, 2, or 3): ")
        if choice in ['1', '2', '3']:
            return int(choice)
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def get_post_likers(L, shortcode):
    """
    Gets the list of users who liked a specific post.
    """
    print(f"\nFetching likers for post: {shortcode}")
    try:
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        likers = post.get_likes()
        print("Successfully fetched likers.")
        return likers
    except Exception as e:
        print(f"Could not fetch likers. The post may be private or the shortcode is wrong. Error: {e}")
        return []

def send_like_placeholder(story_item):
    """
    Placeholder for the story liking functionality.
    """
    print(f"--> [INFO] Liking story {story_item.mediaid} from user {story_item.owner_username}. (This feature is currently under review).")
    # In a real scenario, an API call would be made here.
    # For now, we just simulate the action.
    pass

def process_users(L, users, choice):
    """
    Processes a list of users: views and/or likes their stories.
    """
    print("\nStarting to process users...")
    total_users = 0
    for user in users:
        total_users += 1
        print(f"\n--- Processing user: {user.username} ---")
        try:
            if user.is_private:
                print(f"@{user.username} is private, skipping.")
                continue

            # Human-like delay before fetching stories
            sleep(random.uniform(5, 10))

            stories = L.get_stories(userids=[user.userid])
            story_items = [item for s in stories for item in s.get_items()]

            if not story_items:
                print(f"@{user.username} has no stories.")
                continue

            print(f"Found {len(story_items)} stories for @{user.username}.")

            for story in story_items:
                # Human-like delay between each story action
                sleep(random.uniform(15, 30))

                if choice == 1: # View only
                    print(f"--> Viewing story {story.mediaid} from @{user.username}")

                elif choice == 2: # Like only
                    send_like_placeholder(story)

                elif choice == 3: # View and Like
                    print(f"--> Viewing story {story.mediaid} from @{user.username}")
                    # Add a small delay between view and like
                    sleep(random.uniform(2, 5))
                    send_like_placeholder(story)

        except Exception as e:
            print(f"An error occurred while processing @{user.username}: {e}")
            continue

    print(f"\nFinished processing {total_users} users.")


def main():
    """
    Main function to run the bot.
    """
    print("--- Instagram Story Bot ---")
    L = login_with_sessionid()

    if not L:
        print("\nExiting due to login failure.")
        return

    choice = get_user_choice()

    while True:
        post_shortcode = input("\nEnter the post shortcode (e.g., C0SBieHggMm) or type 'exit': ")
        if post_shortcode.lower() == 'exit':
            break

        likers = get_post_likers(L, post_shortcode)
        if likers:
            process_users(L, likers, choice)

    print("\nBot finished. Goodbye!")


if __name__ == "__main__":
    main()
