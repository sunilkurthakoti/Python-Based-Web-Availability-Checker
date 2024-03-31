import unittest
import requests
import webbrowser

class TestWebsiteLoading(unittest.TestCase):

    def test_website_load(self):
        url = "https://atg.world"
        print("Connecting to", url)
        try:
            # Open the website in the default web browser
            webbrowser.open(url)
            
            # Send a request to the website
            response = requests.get(url)
            
            # Check if the website loads properly
            self.assertEqual(response.status_code, 200)
            print("Website loaded successfully!")
        except requests.exceptions.RequestException as e:
            print("Failed to load website:", e)
            self.fail("Website failed to load")

if __name__ == "__main__":
    unittest.main()
