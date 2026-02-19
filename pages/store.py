from dataclasses import dataclass
from framework.locator import Locator, LocatorType, DriverType
from framework.element import element, WebElement
from pages._base import BasePage


@dataclass
class FeedPageLocators:
    """All locators for the feed page"""

    # Main feed container
    FEED_CONTAINER = Locator(
        type=LocatorType.XPATH,
        value='//div[@role="main"]',
    )

    # Navigation bar
    NAV_BAR = Locator(
        type=LocatorType.XPATH,
        value='//nav[@role="navigation"]',
    )

    # Home button in navigation
    HOME_BUTTON = Locator(
        type=LocatorType.XPATH,
        value='//a[@href="/" and @aria-label="Home"]',
    )

    # Search button
    SEARCH_BUTTON = Locator(
        type=LocatorType.XPATH,
        value='//a[@aria-label="Search"]',
    )

    # Explore button
    EXPLORE_BUTTON = Locator(
        type=LocatorType.XPATH,
        value='//a[@href="/explore/" and @aria-label="Explore"]',
    )

    # Messages button
    MESSAGES_BUTTON = Locator(
        type=LocatorType.XPATH,
        value='//a[@aria-label="Messages" or @aria-label="Direct"]',
    )

    # Notifications button
    NOTIFICATIONS_BUTTON = Locator(
        type=LocatorType.XPATH,
        value='//a[@aria-label="Notifications"]',
    )

    # Create post button
    CREATE_POST_BUTTON = Locator(
        type=LocatorType.XPATH,
        value='//a[@aria-label="Create" or @aria-label="New post"]',
    )

    # Profile button
    PROFILE_BUTTON = Locator(
        type=LocatorType.XPATH,
        value='//a[@aria-label="Profile"]',
    )

    # More menu button
    MORE_BUTTON = Locator(
        type=LocatorType.XPATH,
        value='//a[@aria-label="Settings" or contains(text(), "More")]',
    )

    # Instagram logo
    INSTAGRAM_LOGO = Locator(
        type=LocatorType.XPATH,
        value='//a[@href="/"]//i[@aria-label="Instagram"]',
    )

    # Feed posts container
    POSTS_CONTAINER = Locator(
        type=LocatorType.XPATH,
        value='//article[@role="presentation"]',
    )

    # Individual post
    POST_ITEM = Locator(
        type=LocatorType.XPATH,
        value='//article[@role="presentation"]',
    )

    # Post author/username
    POST_AUTHOR = Locator(
        type=LocatorType.XPATH,
        value='//article//header//a[contains(@href, "/")]',
    )

    # Post image
    POST_IMAGE = Locator(
        type=LocatorType.XPATH,
        value="//article//img[@alt]",
    )

    # Post caption
    POST_CAPTION = Locator(
        type=LocatorType.XPATH,
        value='//article//span[contains(@class, "caption")]',
    )

    # Like button
    LIKE_BUTTON = Locator(
        type=LocatorType.XPATH,
        value='//article//button[@aria-label="Like" or @aria-label="Unlike"]',
    )

    # Comment button
    COMMENT_BUTTON = Locator(
        type=LocatorType.XPATH,
        value='//article//button[@aria-label="Comment"]',
    )

    # Share button
    SHARE_BUTTON = Locator(
        type=LocatorType.XPATH,
        value='//article//button[@aria-label="Share Post" or @aria-label="Share"]',
    )

    # Save button
    SAVE_BUTTON = Locator(
        type=LocatorType.XPATH,
        value='//article//button[@aria-label="Save" or @aria-label="Remove"]',
    )

    # Likes count
    LIKES_COUNT = Locator(
        type=LocatorType.XPATH,
        value='//article//button[contains(@class, "likes")]//span',
    )

    # Comments count
    COMMENTS_COUNT = Locator(
        type=LocatorType.XPATH,
        value='//article//a[contains(text(), "comment")]',
    )

    # Post timestamp
    POST_TIMESTAMP = Locator(
        type=LocatorType.XPATH,
        value="//article//time[@datetime]",
    )

    # Stories section
    STORIES_CONTAINER = Locator(
        type=LocatorType.XPATH,
        value='//div[@role="menu"]',
    )

    # Story item
    STORY_ITEM = Locator(
        type=LocatorType.XPATH,
        value='//div[@role="menuitem"]//canvas',
    )

    # Suggestions section (right sidebar)
    SUGGESTIONS_CONTAINER = Locator(
        type=LocatorType.XPATH,
        value='//div[contains(text(), "Suggestions For You")]',
    )

    # Suggestion user item
    SUGGESTION_USER = Locator(
        type=LocatorType.XPATH,
        value='//div[contains(text(), "Suggestions For You")]//following::a',
    )

    # Follow button in suggestions
    FOLLOW_BUTTON = Locator(
        type=LocatorType.XPATH,
        value='//button[text()="Follow"]',
    )

    # Comment input
    COMMENT_INPUT = Locator(
        type=LocatorType.XPATH,
        value='//article//textarea[@aria-label="Add a comment..."]',
    )

    # Post comment button
    POST_COMMENT_BUTTON = Locator(
        type=LocatorType.XPATH,
        value='//article//button[text()="Post"]',
    )

    # More options button (three dots)
    MORE_OPTIONS_BUTTON = Locator(
        type=LocatorType.XPATH,
        value='//article//button[@aria-label="More options"]',
    )


class FeedPage(BasePage):
    """Page Object Model for Feed Page"""

    def __init__(
        self,
        driver,
        driver_type: DriverType = DriverType.SELENIUM,
        timeout: int = 10000,
    ):
        super().__init__(driver, driver_type, timeout)
        self._locators = FeedPageLocators()

    # Elements as properties - Navigation
    @element("FEED_CONTAINER")
    def feed_container(self) -> WebElement:
        """Main feed container element"""
        pass

    @element("NAV_BAR")
    def nav_bar(self) -> WebElement:
        """Navigation bar element"""
        pass

    @element("HOME_BUTTON")
    def home_button(self) -> WebElement:
        """Home button element"""
        pass

    @element("SEARCH_BUTTON")
    def search_button(self) -> WebElement:
        """Search button element"""
        pass

    @element("EXPLORE_BUTTON")
    def explore_button(self) -> WebElement:
        """Explore button element"""
        pass

    @element("MESSAGES_BUTTON")
    def messages_button(self) -> WebElement:
        """Messages button element"""
        pass

    @element("NOTIFICATIONS_BUTTON")
    def notifications_button(self) -> WebElement:
        """Notifications button element"""
        pass

    @element("CREATE_POST_BUTTON")
    def create_post_button(self) -> WebElement:
        """Create post button element"""
        pass

    @element("PROFILE_BUTTON")
    def profile_button(self) -> WebElement:
        """Profile button element"""
        pass

    @element("MORE_BUTTON")
    def more_button(self) -> WebElement:
        """More menu button element"""
        pass

    @element("INSTAGRAM_LOGO")
    def instagram_logo(self) -> WebElement:
        """Instagram logo element"""
        pass

    # Elements as properties - Posts
    @element("POSTS_CONTAINER")
    def posts_container(self) -> WebElement:
        """Posts container element"""
        pass

    @element("POST_ITEM")
    def post_item(self) -> WebElement:
        """Individual post element"""
        pass

    @element("POST_AUTHOR")
    def post_author(self) -> WebElement:
        """Post author element"""
        pass

    @element("POST_IMAGE")
    def post_image(self) -> WebElement:
        """Post image element"""
        pass

    @element("POST_CAPTION")
    def post_caption(self) -> WebElement:
        """Post caption element"""
        pass

    @element("LIKE_BUTTON")
    def like_button(self) -> WebElement:
        """Like button element"""
        pass

    @element("COMMENT_BUTTON")
    def comment_button(self) -> WebElement:
        """Comment button element"""
        pass

    @element("SHARE_BUTTON")
    def share_button(self) -> WebElement:
        """Share button element"""
        pass

    @element("SAVE_BUTTON")
    def save_button(self) -> WebElement:
        """Save button element"""
        pass

    @element("LIKES_COUNT")
    def likes_count(self) -> WebElement:
        """Likes count element"""
        pass

    @element("COMMENTS_COUNT")
    def comments_count(self) -> WebElement:
        """Comments count element"""
        pass

    @element("POST_TIMESTAMP")
    def post_timestamp(self) -> WebElement:
        """Post timestamp element"""
        pass

    @element("COMMENT_INPUT")
    def comment_input(self) -> WebElement:
        """Comment input element"""
        pass

    @element("POST_COMMENT_BUTTON")
    def post_comment_button(self) -> WebElement:
        """Post comment button element"""
        pass

    @element("MORE_OPTIONS_BUTTON")
    def more_options_button(self) -> WebElement:
        """More options button element"""
        pass

    # Elements as properties - Stories and Suggestions
    @element("STORIES_CONTAINER")
    def stories_container(self) -> WebElement:
        """Stories container element"""
        pass

    @element("STORY_ITEM")
    def story_item(self) -> WebElement:
        """Story item element"""
        pass

    @element("SUGGESTIONS_CONTAINER")
    def suggestions_container(self) -> WebElement:
        """Suggestions container element"""
        pass

    @element("SUGGESTION_USER")
    def suggestion_user(self) -> WebElement:
        """Suggestion user element"""
        pass

    @element("FOLLOW_BUTTON")
    def follow_button(self) -> WebElement:
        """Follow button element"""
        pass
