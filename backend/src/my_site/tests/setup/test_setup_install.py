from my_site import PACKAGE_NAME


class TestSetupInstall:
    def test_addon_installed(self, installer):
        """Test if my_site is installed."""
        assert installer.is_product_installed(PACKAGE_NAME) is True

    def test_browserlayer(self, browser_layers):
        """Test that IMySiteLayer is registered."""
        from my_site.interfaces import IMySiteLayer

        assert IMySiteLayer in browser_layers

    def test_latest_version(self, profile_last_version):
        """Test latest version of default profile."""
        assert profile_last_version(f"{PACKAGE_NAME}:default") == "20240401001"
