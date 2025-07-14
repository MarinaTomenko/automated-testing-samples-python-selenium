# page:  https://hyperskill.org/tracks
# Header
LOGO = ("xpath", "//ul[@class='navbar-nav']")
LOGIN_BUTTON = ("xpath", "//button[.//text()[contains(., 'Sign in')]]")
STARTFORFREE_BUTTON = ("xpath", "//button[.//text()[contains(., 'Start for free')]]")
CATALOG_BUTTON = ("xpath", "//a[.//text()[contains(., 'Catalog')]]")
PRICING = ("xpath", "//a[.//text()[contains(., 'Pricing')]]")
FOR_BUSINESS =("xpath", "//a[.//text()[contains(., 'For Business')]]")

# Main content
TRACKS_HEADER = ("xpath", "//h1[contains(text(), 'What')]")
ALL_TRACKS_TAB = ("xpath", "//a[.//text()[contains(., 'All courses')]]")
POPULAR_TRACKS_TAB = ("xpath", "//a[.//text()[contains(., 'Most popular')]]")
TRACK_CARDS = ("xpath", "//div[contains(@class, 'track-card')]")
TRACK_TITLES = ("xpath", "//h5[.//text()[contains(., 'Python Developer')]]")
TRACK_DESCRIPTIONS = ("xpath", "//span[contains(@class, 'track-description')]")
TRACK_DURATION = ("xpath", "//span[.//text()[contains(., 'hours')]]")

# Footer
FOOTER_LINKS = ("xpath", "//footer//a")
SOCIAL_MEDIA_LINKS = ("xpath", "//footer//a[contains(@aria-label, 'Hyperskill on')]")