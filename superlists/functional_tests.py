from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Jared heard about a cool new online to-do app; he goes to check out the homepage
		self.browser.get("http://localhost:8000")

		# He notices the page title & header mention to-do lists
		self.assertIn("To-Do", self.browser.title)
		self.fail("Finish the test!")

		# He is invited to enter a to-do item

		# He types "Buy a zoot suit" into a text box (Jared's hobbies include collecting stray
		# serval cats)

		# When he hits enter, the page updates and now the page lists "1: Buy a zoot suit" as an
		# item in a to-do list

		# There is still a text-box inviting him to add another item. He enters in "Collect some
		# giant insects"

		# The page updates again, and now it shows both items on his list

		# Jared wonders whether the site will remember the list. He then sees the site generated
		# a unique URL for him

		# He visits the URL - his to-do list is still there!


if __name__ == "__main__":
	unittest.main(warnings="ignore")
