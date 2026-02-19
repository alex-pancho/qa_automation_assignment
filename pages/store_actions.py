import time
from framework.logger import log_action, setup_logger
from pages.store import FeedPage


class FeedPageActions:

    def __init__(self, feed_page: FeedPage):
        """
        Initialize FeedPageActions with a FeedPage instance

        Args:
            feed_page: FeedPage object instance
        """
        self._page = feed_page
        self._logger = setup_logger(self.__class__.__name__)

    # Page state checks
    @log_action("Checking if feed page is displayed")
    def is_page_displayed(self) -> bool:
        """Check if feed page is displayed"""
        try:
            return self.feed_container.is_presented() and self.nav_bar.is_presented()
        except Exception as e:
            self._logger.error(f"Failed to check if page displayed: {e}")
            return False

    @log_action("Checking if navigation bar is visible")
    def is_nav_bar_visible(self) -> bool:
        """Check if navigation bar is visible"""
        try:
            return self.nav_bar.is_visible()
        except Exception as e:
            self._logger.error(f"Failed to check nav bar visibility: {e}")
            return False

    @log_action("Checking if posts are visible")
    def is_posts_visible(self) -> bool:
        """Check if posts are visible in feed"""
        try:
            return self.posts_container.is_visible()
        except Exception as e:
            self._logger.error(f"Failed to check posts visibility: {e}")
            return False

    @log_action("Checking if stories section is visible")
    def is_stories_visible(self) -> bool:
        """Check if stories section is visible"""
        try:
            return self.stories_container.is_visible()
        except Exception as e:
            self._logger.error(f"Failed to check stories visibility: {e}")
            return False

    @log_action("Checking if suggestions section is visible")
    def is_suggestions_visible(self) -> bool:
        """Check if suggestions section is visible"""
        try:
            return self.suggestions_container.is_visible()
        except Exception as e:
            self._logger.error(f"Failed to check suggestions visibility: {e}")
            return False

    @log_action("Getting number of posts")
    def get_posts_count(self) -> int:
        """Get number of posts visible in feed"""
        try:
            # This would need to be implemented based on your framework's ability to find multiple elements
            # For now, returning 0 as placeholder
            return 0
        except Exception as e:
            self._logger.error(f"Failed to get posts count: {e}")
            return 0

    @log_action("Getting post author name")
    def get_post_author_name(self) -> str:
        """Get the author name of the first post"""
        try:
            return self.post_author.get_text()
        except Exception as e:
            self._logger.error(f"Failed to get post author name: {e}")
            return None

    @log_action("Getting post caption text")
    def get_post_caption_text(self) -> str:
        """Get the caption text of the first post"""
        try:
            return self.post_caption.get_text()
        except Exception as e:
            self._logger.error(f"Failed to get post caption: {e}")
            return None

    @log_action("Getting likes count")
    def get_likes_count_text(self) -> str:
        """Get the likes count text of the first post"""
        try:
            return self.likes_count.get_text()
        except Exception as e:
            self._logger.error(f"Failed to get likes count: {e}")
            return None

    @log_action("Checking if home button is clickable")
    def is_home_button_clickable(self) -> bool:
        """Check if home button is clickable"""
        try:
            return self.home_button.is_clickable()
        except Exception as e:
            self._logger.error(f"Failed to check home button: {e}")
            return False

    @log_action("Checking if create post button is clickable")
    def is_create_post_button_clickable(self) -> bool:
        """Check if create post button is clickable"""
        try:
            return self.create_post_button.is_clickable()
        except Exception as e:
            self._logger.error(f"Failed to check create post button: {e}")
            return False

    @log_action("Checking if profile button is clickable")
    def is_profile_button_clickable(self) -> bool:
        """Check if profile button is clickable"""
        try:
            return self.profile_button.is_clickable()
        except Exception as e:
            self._logger.error(f"Failed to check profile button: {e}")
            return False

    @log_action("Taking screenshot")
    def screenshot(self, file_name: str = "feed_page.png") -> None:
        """Take a screenshot of the feed page"""
        try:
            self.feed_container.highlight_and_screenshot(file_name)
            self._logger.info(f"Screenshot saved: {file_name}")
        except Exception as e:
            self._logger.error(f"Failed to take screenshot: {e}")

    # Navigation actions
    @log_action("Clicking home button")
    def click_home(self) -> None:
        """Click the home button in navigation"""
        try:
            if not self._page.is_home_button_clickable():
                raise AssertionError("Home button not clickable")

            self._logger.debug("Clicking home button")
            self._page.home_button.click()

        except Exception as e:
            self._logger.error(f"Failed to click home button: {e}")
            raise

    @log_action("Clicking search button")
    def click_search(self) -> None:
        """Click the search button in navigation"""
        try:
            self._logger.debug("Clicking search button")
            self._page.search_button.click()

        except Exception as e:
            self._logger.error(f"Failed to click search button: {e}")
            raise

    @log_action("Clicking explore button")
    def click_explore(self) -> None:
        """Click the explore button in navigation"""
        try:
            self._logger.debug("Clicking explore button")
            self._page.explore_button.click()

        except Exception as e:
            self._logger.error(f"Failed to click explore button: {e}")
            raise

    @log_action("Clicking messages button")
    def click_messages(self) -> None:
        """Click the messages button in navigation"""
        try:
            self._logger.debug("Clicking messages button")
            self._page.messages_button.click()

        except Exception as e:
            self._logger.error(f"Failed to click messages button: {e}")
            raise

    @log_action("Clicking notifications button")
    def click_notifications(self) -> None:
        """Click the notifications button in navigation"""
        try:
            self._logger.debug("Clicking notifications button")
            self._page.notifications_button.click()

        except Exception as e:
            self._logger.error(f"Failed to click notifications button: {e}")
            raise

    @log_action("Clicking create post button")
    def click_create_post(self) -> None:
        """Click the create post button in navigation"""
        try:
            if not self._page.is_create_post_button_clickable():
                raise AssertionError("Create post button not clickable")

            self._logger.debug("Clicking create post button")
            self._page.create_post_button.click()

        except Exception as e:
            self._logger.error(f"Failed to click create post button: {e}")
            raise

    @log_action("Clicking profile button")
    def click_profile(self) -> None:
        """Click the profile button in navigation"""
        try:
            if not self._page.is_profile_button_clickable():
                raise AssertionError("Profile button not clickable")

            self._logger.debug("Clicking profile button")
            self._page.profile_button.click()

        except Exception as e:
            self._logger.error(f"Failed to click profile button: {e}")
            raise

    @log_action("Clicking more menu button")
    def click_more_menu(self) -> None:
        """Click the more menu button in navigation"""
        try:
            self._logger.debug("Clicking more menu button")
            self._page.more_button.click()

        except Exception as e:
            self._logger.error(f"Failed to click more menu button: {e}")
            raise

    # Post interaction actions
    @log_action("Liking a post")
    def like_post(self, wait_after: float = 0.5) -> None:
        """
        Like the first visible post

        Args:
            wait_after: Time to wait after liking (seconds)
        """
        try:
            self._logger.debug("Liking post")
            self._page.like_button.click()
            time.sleep(wait_after)

        except Exception as e:
            self._logger.error(f"Failed to like post: {e}")
            raise

    @log_action("Commenting on a post")
    def comment_on_post(self, comment_text: str, wait_after: float = 1.0) -> None:
        """
        Add a comment to the first visible post

        Args:
            comment_text: Text of the comment
            wait_after: Time to wait after posting comment (seconds)
        """
        try:
            self._logger.debug(f"Adding comment: {comment_text}")

            # Click comment button to focus input
            self._page.comment_button.click()
            time.sleep(0.3)

            # Enter comment text
            self._page.comment_input.send_keys(comment_text)

            # Post the comment
            self._page.post_comment_button.click()
            time.sleep(wait_after)

            self._logger.info("Comment posted successfully")

        except Exception as e:
            self._logger.error(f"Failed to comment on post: {e}")
            raise

    @log_action("Sharing a post")
    def share_post(self, wait_after: float = 0.5) -> None:
        """
        Share the first visible post

        Args:
            wait_after: Time to wait after sharing (seconds)
        """
        try:
            self._logger.debug("Sharing post")
            self._page.share_button.click()
            time.sleep(wait_after)

        except Exception as e:
            self._logger.error(f"Failed to share post: {e}")
            raise

    @log_action("Saving a post")
    def save_post(self, wait_after: float = 0.5) -> None:
        """
        Save the first visible post

        Args:
            wait_after: Time to wait after saving (seconds)
        """
        try:
            self._logger.debug("Saving post")
            self._page.save_button.click()
            time.sleep(wait_after)

        except Exception as e:
            self._logger.error(f"Failed to save post: {e}")
            raise

    @log_action("Opening post options menu")
    def open_post_options(self) -> None:
        """Open the more options menu for a post"""
        try:
            self._logger.debug("Opening post options menu")
            self._page.more_options_button.click()

        except Exception as e:
            self._logger.error(f"Failed to open post options: {e}")
            raise

    @log_action("Clicking on post author")
    def click_post_author(self) -> None:
        """Click on the author of the first post to visit their profile"""
        try:
            self._logger.debug("Clicking on post author")
            self._page.post_author.click()

        except Exception as e:
            self._logger.error(f"Failed to click post author: {e}")
            raise

    # Stories actions
    @log_action("Clicking on a story")
    def click_story(self) -> None:
        """Click on the first story"""
        try:
            self._logger.debug("Clicking on story")
            self._page.story_item.click()

        except Exception as e:
            self._logger.error(f"Failed to click story: {e}")
            raise

    # Suggestions actions
    @log_action("Following a suggested user")
    def follow_suggested_user(self, wait_after: float = 0.5) -> None:
        """
        Follow a suggested user from the suggestions section

        Args:
            wait_after: Time to wait after clicking follow (seconds)
        """
        try:
            self._logger.debug("Following suggested user")
            self._page.follow_button.click()
            time.sleep(wait_after)

        except Exception as e:
            self._logger.error(f"Failed to follow suggested user: {e}")
            raise

    # Complex actions
    @log_action("Interacting with first post")
    def interact_with_first_post(
        self,
        like: bool = True,
        comment: str = None,
        save: bool = False,
        wait_between_actions: float = 0.5,
    ) -> bool:
        """
        Perform multiple interactions with the first post

        Args:
            like: Whether to like the post
            comment: Comment text to add (None to skip commenting)
            save: Whether to save the post
            wait_between_actions: Time to wait between actions (seconds)

        Returns:
            True if all interactions succeeded, False otherwise
        """
        try:
            if like:
                self.like_post(wait_after=wait_between_actions)

            if comment:
                self.comment_on_post(comment, wait_after=wait_between_actions)

            if save:
                self.save_post(wait_after=wait_between_actions)

            self._logger.info("Post interaction completed successfully")
            return True

        except Exception as e:
            self._logger.error(f"Post interaction failed: {e}")
            return False

    @log_action("Validating feed page")
    def validate_feed_page(self) -> bool:
        """
        Validate that all main feed page elements are present and visible

        Returns:
            True if all elements are valid, False otherwise
        """
        try:
            checks = {
                "Feed container visible": self.is_page_displayed(),
                "Navigation bar visible": self.is_nav_bar_visible(),
                "Posts visible": self.is_posts_visible(),
                "Home button clickable": self.is_home_button_clickable(),
                "Create post button clickable": self.is_create_post_button_clickable(),
                "Profile button clickable": self.is_profile_button_clickable(),
            }

            all_valid = all(checks.values())

            for check_name, result in checks.items():
                status = "✓" if result else "✗"
                self._logger.info(f"{status} {check_name}: {result}")

            return all_valid

        except Exception as e:
            self._logger.error(f"Validation failed: {e}")
            return False

    @log_action("Scrolling feed")
    def scroll_feed(self, scroll_amount: int = 500) -> None:
        """
        Scroll the feed down

        Args:
            scroll_amount: Amount to scroll in pixels
        """
        try:
            self._logger.debug(f"Scrolling feed by {scroll_amount}px")
            # This would need to be implemented based on your framework
            # For now, it's a placeholder
            # self._page.feed_container.scroll_by(0, scroll_amount)

        except Exception as e:
            self._logger.error(f"Failed to scroll feed: {e}")
            raise
