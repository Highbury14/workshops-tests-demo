import re
from playwright.sync_api import Page, expect

def test_main_version(page: Page):
  page.goto("https://cs3002-26t3-workshop.onrender.com/")

  # Add assertions for the main version test
  expect(page).to_have_url("https://cs3002-26t3-workshop.onrender.com/")
  
  expect(page).to_have_title(re.compile("Your details"))
  expect(page.locator("header")).to_contain_text("Your details")
  expect(page.get_by_test_id("link-step-1")).to_contain_text("›")

  expect(page.get_by_test_id("form-student")).to_be_visible()
  
  expect(page.get_by_test_id("input-full-name")).to_be_visible()
  expect(page.get_by_test_id("input-student-id")).to_be_visible()
  expect(page.get_by_test_id("input-email")).to_be_visible()
  expect(page.get_by_test_id("input-school-name")).to_be_visible()
  expect(page.get_by_test_id("input-full-name")).to_be_empty()
  expect(page.get_by_test_id("input-student-id")).to_be_empty()
  expect(page.get_by_test_id("input-email")).to_be_empty()
  expect(page.get_by_test_id("input-school-name")).to_be_empty()

  form_error = page.locator("span.field-error").filter(has_text="Enter your")
  expect(form_error).to_be_hidden()

  page.get_by_test_id("button-continue-student").click()
  
  expect(page).to_have_url("https://cs3002-26t3-workshop.onrender.com/")
  
  expect(page).to_have_title(re.compile("Your details"))
  expect(page.locator("header")).to_contain_text("Your details")
  expect(page.get_by_test_id("link-step-1")).to_contain_text("›")

  expect(page.get_by_text("Enter your full name.")).to_be_visible()
  expect(page.get_by_text("Enter your student ID.")).to_be_visible()
  expect(page.get_by_text("Enter your email address.")).to_be_visible()
  expect(page.get_by_text("Enter your university name.")).to_be_visible()
  '''expect(page.get_by_test_id("form-student")).to_contain_text("Enter your full name.")
  expect(page.get_by_test_id("form-student")).to_contain_text("Enter your student ID.")
  expect(page.get_by_test_id("form-student")).to_contain_text("Enter your email address.")
  expect(page.get_by_test_id("form-student")).to_contain_text("Enter your university name.")'''

  page.get_by_test_id("input-full-name").fill("testone test")
  page.get_by_test_id("button-continue-student").click()
  
  expect(page).to_have_url("https://cs3002-26t3-workshop.onrender.com/")

  expect(page).to_have_title(re.compile("Your details"))
  expect(page.locator("header")).to_contain_text("Your details")
  expect(page.get_by_test_id("link-step-1")).to_contain_text("›")

  expect(page.get_by_text("Enter your full name.")).to_be_hidden()
  expect(page.get_by_text("Enter your student ID.")).to_be_visible()
  expect(page.get_by_text("Enter your email address.")).to_be_visible()
  expect(page.get_by_text("Enter your university name.")).to_be_visible()

  page.get_by_test_id("input-student-id").fill("23abc234 dsf")
  page.get_by_test_id("button-continue-student").click()

  expect(page).to_have_url("https://cs3002-26t3-workshop.onrender.com/")

  expect(page).to_have_title(re.compile("Your details"))
  expect(page.locator("header")).to_contain_text("Your details")
  expect(page.get_by_test_id("link-step-1")).to_contain_text("›")

  expect(page.get_by_text("Enter your full name.")).to_be_hidden()
  expect(page.get_by_text("Enter your student ID.")).to_be_hidden()
  expect(page.get_by_text("Enter your email address.")).to_be_visible()
  expect(page.get_by_text("Enter your university name.")).to_be_visible()
  
  page.get_by_test_id("input-school-name").fill("iit-m chennai")
  page.get_by_test_id("button-continue-student").click()

  expect(page).to_have_url("https://cs3002-26t3-workshop.onrender.com/")

  expect(page).to_have_title(re.compile("Your details"))
  expect(page.locator("header")).to_contain_text("Your details")
  expect(page.get_by_test_id("link-step-1")).to_contain_text("›")

  expect(page.get_by_text("Enter your full name.")).to_be_hidden()
  expect(page.get_by_text("Enter your student ID.")).to_be_hidden()
  expect(page.get_by_text("Enter your email address.")).to_be_visible()
  expect(page.get_by_text("Enter your university name.")).to_be_hidden()
  
  page.get_by_test_id("input-email").fill("teset234")
  page.get_by_test_id("button-continue-student").click()

  expect(page).to_have_url("https://cs3002-26t3-workshop.onrender.com/")

  expect(page).to_have_title(re.compile("Your details"))
  expect(page.locator("header")).to_contain_text("Your details")
  expect(page.get_by_test_id("link-step-1")).to_contain_text("›")

  expect(page.get_by_text("Enter your full name.")).to_be_hidden()
  expect(page.get_by_text("Enter your student ID.")).to_be_hidden()
  expect(page.get_by_text("Enter your university name.")).to_be_hidden()
  expect(page.get_by_text("Enter a valid email address.")).to_be_visible()
  # expect(page.get_by_role("alert")).to_contain_text("Enter a valid email address.")
  
  page.get_by_test_id("input-email").fill("teset234@iitm")
  page.get_by_test_id("button-continue-student").click()
  
  expect(page).to_have_url("https://cs3002-26t3-workshop.onrender.com/")

  expect(page).to_have_title(re.compile("Your details"))
  expect(page.locator("header")).to_contain_text("Your details")
  expect(page.get_by_test_id("link-step-1")).to_contain_text("›")
  
  expect(page.get_by_text("Enter a valid email address.")).to_be_visible()
  expect(page.get_by_text("Enter your full name.")).to_be_hidden()
  expect(page.get_by_text("Enter your student ID.")).to_be_hidden()
  expect(page.get_by_text("Enter your university name.")).to_be_hidden()
  # expect(page.get_by_role("alert")).to_contain_text("Enter a valid email address.")
  
  page.get_by_test_id("input-email").fill("teset234@iitm.in")
  page.get_by_test_id("button-continue-student").click()

  expect(page).to_have_url("https://cs3002-26t3-workshop.onrender.com/academic")

  expect(page).to_have_title(re.compile("Academic info"))
  expect(page.locator("header")).to_contain_text("Academic info")
  expect(page.get_by_test_id("link-step-1")).to_contain_text("✓")
  expect(page.get_by_test_id("link-step-2")).to_contain_text("›")

  expect(page.get_by_test_id("form-academic")).to_be_visible()

  expect(page.get_by_test_id("select-major")).to_be_empty()

  '''page.get_by_test_id("input-full-name").click()
  page.get_by_test_id("input-full-name").fill("testone")
  page.get_by_test_id("input-email").click()
  page.get_by_test_id("input-student-id").click()
  page.get_by_test_id("input-school-name").click()'''

  breakpoint()

'''def test_has_title(page: Page):
  page.goto("https://playwright.dev/")

  # Expect a title "to contain" a substring.
  expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
  page.goto("https://playwright.dev/")

  # Click the get started link.
  page.get_by_role("link", name="Get started").click()

  # Expects page to have a heading with the name of Installation.
  expect(page.get_by_role("heading", name="Installation")).to_be_visible()'''
