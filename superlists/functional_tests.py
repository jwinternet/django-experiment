from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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
		header_text = self.browser.find_element_by_tag_name("h1").text
		self.assertIn("To-Do", header_text)

		# He is invited to enter a to-do item
		inputbox = self.browser.find_element_by_id("id_new_item")
		self.assertEqual(
			inputbox.get_attribute("placeholder"),
			"Enter a to-do item"
		)

		# He types "Buy a zoot suit" into a text box (Jared's hobbies include collecting stray
		# serval cats)
		inputbox.send_keys("Buy a zoot suit")

		# When he hits enter, the page updates and now the page lists "1: Buy a zoot suit" as an
		# item in a to-do list
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)

		table = self.browser.find_element_by_id("id_list_table")
		rows = table.find_elements_by_tag_name("tr")
		self.assertTrue(
			any(row.text == "1: Buy zoot suit" for row in rows)
		)

		# There is still a text-box inviting him to add another item. He enters in "Collect some
		# giant insects"
		self.fail("Finish the test!")

		# The page updates again, and now it shows both items on his list

		# Jared wonders whether the site will remember the list. He then sees the site generated
		# a unique URL for him

		# He visits the URL - his to-do list is still there!


if __name__ == "__main__":
	unittest.main(warnings="ignore")
