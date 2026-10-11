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

  expect(page.get_by_test_id("select-major")).to_be_visible()
  expect(page.get_by_test_id("select-major")).to_have_value("")
  expect(page.get_by_test_id("input-academic-year")).to_be_visible()
  expect(page.get_by_test_id("input-academic-year")).to_be_empty()
  expect(page.get_by_test_id("select-term")).to_be_visible()
  expect(page.get_by_test_id("select-term")).to_have_value("")

  expect(page.locator("span.field-error")).to_be_hidden()

  page.get_by_test_id("button-continue-academic").click()

  expect(page).to_have_url("https://cs3002-26t3-workshop.onrender.com/academic")

  expect(page).to_have_title(re.compile("Academic info"))
  expect(page.locator("header")).to_contain_text("Academic info")
  expect(page.get_by_test_id("link-step-1")).to_contain_text("✓")
  expect(page.get_by_test_id("link-step-2")).to_contain_text("›")

  expect(page.get_by_text("Choose your major.")).to_be_visible()
  expect(page.get_by_text("Enter the academic year.")).to_be_visible()
  expect(page.get_by_text("Choose a term.")).to_be_visible()
  
  page.get_by_test_id("select-major").select_option("Computer Science")
  page.get_by_test_id("button-continue-academic").click()

  expect(page).to_have_url("https://cs3002-26t3-workshop.onrender.com/academic")

  expect(page).to_have_title(re.compile("Academic info"))
  expect(page.locator("header")).to_contain_text("Academic info")
  expect(page.get_by_test_id("link-step-1")).to_contain_text("✓")
  expect(page.get_by_test_id("link-step-2")).to_contain_text("›")

  expect(page.get_by_text("Enter the academic year.")).to_be_visible()
  expect(page.get_by_text("Choose a term.")).to_be_visible()
  expect(page.get_by_text("Choose your major.")).to_be_hidden()

  page.get_by_test_id("input-academic-year").fill("202 dfsdf")
  page.get_by_test_id("button-continue-academic").click()

  expect(page).to_have_url("https://cs3002-26t3-workshop.onrender.com/academic")

  expect(page).to_have_title(re.compile("Academic info"))
  expect(page.locator("header")).to_contain_text("Academic info")
  expect(page.get_by_test_id("link-step-1")).to_contain_text("✓")
  expect(page.get_by_test_id("link-step-2")).to_contain_text("›")

  expect(page.get_by_text("Choose a term.")).to_be_visible()
  expect(page.get_by_text("Enter the academic year.")).to_be_hidden()
  expect(page.get_by_text("Choose your major.")).to_be_hidden()

  page.get_by_test_id("select-term").select_option("T3-2025")
  page.get_by_test_id("button-continue-academic").click()

  expect(page).to_have_url("https://cs3002-26t3-workshop.onrender.com/subjects")
  '''
  page.get_by_test_id("input-student-id").click()
  page.get_by_test_id("input-school-name").click()'''

  # breakpoint()

def test_has_email_validation(page: Page):
  page.goto("https://cs3002-26t3-workshop-test.onrender.com/")

  expect(page).to_have_url("https://cs3002-26t3-workshop-test.onrender.com/")
  # Expect a title "to contain" a substring.
  expect(page).to_have_title(re.compile("Your details"))

  page.get_by_test_id("input-full-name").fill("testone test")
  page.get_by_test_id("input-student-id").fill("23abc234 dsf")
  page.get_by_test_id("input-school-name").fill("iit-m chennai")
  page.get_by_test_id("input-email").fill("testexamplecom")
  page.get_by_test_id("button-continue-student").click()

  expect(page).to_have_url("https://cs3002-26t3-workshop-test.onrender.com/")
  expect(page.get_by_text("Enter a valid email address.")).to_be_visible()

def test_no_email_validation(page: Page):
  page.goto("https://cs3002-26t3-workshop-test.onrender.com/")

  expect(page).to_have_url("https://cs3002-26t3-workshop-test.onrender.com/")
  expect(page).to_have_title(re.compile("Your details"))

  page.get_by_test_id("input-full-name").fill("testone test")
  page.get_by_test_id("input-student-id").fill("23abc234 dsf")
  page.get_by_test_id("input-school-name").fill("iit-m chennai")
  page.get_by_test_id("input-email").fill("testexamplecom")
  page.get_by_test_id("button-continue-student").click()

  expect(page).to_have_url("https://cs3002-26t3-workshop-test.onrender.com/academic")
  expect(page).to_have_title(re.compile("Academic info"))

def test_back_button_error_academic_info(page: Page):
  page.goto("https://cs3002-26t3-workshop-test.onrender.com/")

  expect(page).to_have_url("https://cs3002-26t3-workshop-test.onrender.com/")
  expect(page).to_have_title(re.compile("Your details"))

  page.get_by_test_id("input-full-name").fill("testone test")
  page.get_by_test_id("input-student-id").fill("23abc234 dsf")
  page.get_by_test_id("input-school-name").fill("iit-m chennai")
  page.get_by_test_id("input-email").fill("test@example.com")
  page.get_by_test_id("button-continue-student").click()

  expect(page).to_have_url("https://cs3002-26t3-workshop-test.onrender.com/academic")
  expect(page).to_have_title(re.compile("Academic info"))

  page.get_by_test_id("button-back-academic").click()

  expect(page).to_have_url("https://cs3002-26t3-workshop-test.onrender.com/")
  expect(page).to_have_title(re.compile("Your details"))

  expect(page.get_by_test_id("input-full-name")).to_be_empty()
  expect(page.get_by_test_id("input-student-id")).to_be_empty()
  expect(page.get_by_test_id("input-school-name")).to_be_empty()
  expect(page.get_by_test_id("input-email")).to_be_empty()

def test_good_back_button_academic_info(page: Page):
  page.goto("https://cs3002-26t3-workshop-test.onrender.com/")

  expect(page).to_have_url("https://cs3002-26t3-workshop-test.onrender.com/")
  expect(page).to_have_title(re.compile("Your details"))

  page.get_by_test_id("input-full-name").fill("testone test")
  page.get_by_test_id("input-student-id").fill("23abc234 dsf")
  page.get_by_test_id("input-school-name").fill("iit-m chennai")
  page.get_by_test_id("input-email").fill("test@example.com")
  page.get_by_test_id("button-continue-student").click()

  expect(page).to_have_url("https://cs3002-26t3-workshop-test.onrender.com/academic")
  expect(page).to_have_title(re.compile("Academic info"))

  page.get_by_test_id("button-back-academic").click()

  expect(page).to_have_url("https://cs3002-26t3-workshop-test.onrender.com/")
  expect(page).to_have_title(re.compile("Your details"))

  expect(page.get_by_test_id("input-full-name")).not_to_be_empty()
  expect(page.get_by_test_id("input-student-id")).not_to_be_empty()
  expect(page.get_by_test_id("input-school-name")).not_to_be_empty()
  expect(page.get_by_test_id("input-email")).not_to_be_empty()
  expect(page.get_by_test_id("input-full-name")).to_have_value("testone test")
  expect(page.get_by_test_id("input-student-id")).to_have_value("23abc234 dsf")
  expect(page.get_by_test_id("input-school-name")).to_have_value("iit-m chennai")
  expect(page.get_by_test_id("input-email")).to_have_value("test@example.com")

  # Click the get started link.
  # Expects page to have a heading with the name of Installation.
  # expect(page.get_by_role("heading", name="Installation")).to_be_visible()

def test_good_continue_button_your_details(page: Page):
  page.goto("https://cs3002-26t3-workshop-test.onrender.com/")

  expect(page).to_have_url("https://cs3002-26t3-workshop-test.onrender.com/")
  expect(page).to_have_title(re.compile("Your details"))

  page.get_by_test_id("input-full-name").fill("testone test")
  page.get_by_test_id("input-student-id").fill("23abc234 dsf")
  page.get_by_test_id("input-school-name").fill("iit-m chennai")
  page.get_by_test_id("input-email").fill("test@example.com")
  page.get_by_test_id("button-continue-student").click()

  expect(page).to_have_url("https://cs3002-26t3-workshop-test.onrender.com/academic")
  expect(page).to_have_title(re.compile("Academic info"))

  page.get_by_test_id("select-major").select_option("Computer Science")
  page.get_by_test_id("input-academic-year").fill("2023")
  page.get_by_test_id("select-term").select_option("T3-2025")

  page.get_by_test_id("button-back-academic").click()

  expect(page).to_have_url("https://cs3002-26t3-workshop-test.onrender.com/")
  expect(page).to_have_title(re.compile("Your details"))

  page.get_by_test_id("button-continue-student").click()

  expect(page).to_have_url("https://cs3002-26t3-workshop-test.onrender.com/academic")
  expect(page).to_have_title(re.compile("Academic info"))

  # expect(page.get_by_test_id("select-major")).not_to_be_empty()
  expect(page.get_by_test_id("input-academic-year")).not_to_be_empty()
  # expect(page.get_by_test_id("select-term")).not_to_be_empty()
  # expect(page.get_by_test_id("input-email")).not_to_be_empty()

  expect(page.get_by_test_id("select-major")).to_have_value("Computer Science")
  expect(page.get_by_test_id("input-academic-year")).to_have_value("2023")
  expect(page.get_by_test_id("select-term")).to_have_value("T3-2025")

  # Click the get started link.
  # Expects page to have a heading with the name of Installation.
  # expect(page.get_by_role("heading", name="Installation")).to_be_visible()

def test_continue_button_error_your_details(page: Page):
  page.goto("https://cs3002-26t3-workshop-test.onrender.com/")

  expect(page).to_have_url("https://cs3002-26t3-workshop-test.onrender.com/")
  expect(page).to_have_title(re.compile("Your details"))

  page.get_by_test_id("input-full-name").fill("testone test")
  page.get_by_test_id("input-student-id").fill("23abc234 dsf")
  page.get_by_test_id("input-school-name").fill("iit-m chennai")
  page.get_by_test_id("input-email").fill("test@example.com")
  page.get_by_test_id("button-continue-student").click()

  expect(page).to_have_url("https://cs3002-26t3-workshop-test.onrender.com/academic")
  expect(page).to_have_title(re.compile("Academic info"))

  page.get_by_test_id("select-major").select_option("Computer Science")
  page.get_by_test_id("input-academic-year").fill("2023")
  page.get_by_test_id("select-term").select_option("T3-2025")

  page.get_by_test_id("button-back-academic").click()

  expect(page).to_have_url("https://cs3002-26t3-workshop-test.onrender.com/")
  expect(page).to_have_title(re.compile("Your details"))

  page.get_by_test_id("button-continue-student").click()

  expect(page).to_have_url("https://cs3002-26t3-workshop-test.onrender.com/academic")
  expect(page).to_have_title(re.compile("Academic info"))

  # expect(page.get_by_test_id("select-major")).not_to_be_empty()
  expect(page.get_by_test_id("input-academic-year")).to_be_empty()
  # expect(page.get_by_test_id("select-term")).not_to_be_empty()
  # expect(page.get_by_test_id("input-email")).not_to_be_empty()

  expect(page.get_by_test_id("select-major")).to_have_value("")
  expect(page.get_by_test_id("select-term")).to_have_value("")
  # expect(page.get_by_test_id("input-academic-year")).to_have_value("")

  # Click the get started link.
  # page.get_by_role("link", name="Get started").click()
  # Expects page to have a heading with the name of Installation.
  # expect(page.get_by_role("heading", name="Installation")).to_be_visible()

def test_has_duplicate_subject_name(page: Page):
  page.goto("https://cs3002-26t3-workshop-test.onrender.com/")

  expect(page).to_have_url("https://cs3002-26t3-workshop-test.onrender.com/")
  expect(page).to_have_title(re.compile("Your details"))

  page.get_by_test_id("input-full-name").fill("testone test")
  page.get_by_test_id("input-student-id").fill("23abc234 dsf")
  page.get_by_test_id("input-school-name").fill("iit-m chennai")
  page.get_by_test_id("input-email").fill("test@example.com")
  page.get_by_test_id("button-continue-student").click()

  expect(page).to_have_url("https://cs3002-26t3-workshop-test.onrender.com/academic")
  expect(page).to_have_title(re.compile("Academic info"))

  page.get_by_test_id("select-major").select_option("Computer Science")
  page.get_by_test_id("input-academic-year").fill("2023")
  page.get_by_test_id("select-term").select_option("T3-2025")

  page.get_by_test_id("button-continue-academic").click()

  expect(page).to_have_url("https://cs3002-26t3-workshop-test.onrender.com/subjects")
  expect(page).to_have_title(re.compile("Subjects"))

  page.get_by_test_id("input-new-subject").fill("MathCS3002")
  page.get_by_test_id("input-new-score").fill("50")
  page.get_by_test_id("button-add-subject").click()

  page.get_by_test_id("input-new-subject").fill("MathCS3002")
  page.get_by_test_id("input-new-score").fill("60")
  page.get_by_test_id("button-add-subject").click()

  expect(page.get_by_test_id("status-feedback")).to_contain_text("Subject added.")
  expect(page.get_by_test_id("input-subject-name-1")).to_have_value("MathCS3002")
  # Click the get started link.
  # Expects page to have a heading with the name of Installation.
  # expect(page.get_by_role("heading", name="Installation")).to_be_visible()

def test_no_duplicate_subject_name(page: Page):
  page.goto("https://cs3002-26t3-workshop-test.onrender.com/")

  expect(page).to_have_url("https://cs3002-26t3-workshop-test.onrender.com/")
  expect(page).to_have_title(re.compile("Your details"))

  page.get_by_test_id("input-full-name").fill("testone test")
  page.get_by_test_id("input-student-id").fill("23abc234 dsf")
  page.get_by_test_id("input-school-name").fill("iit-m chennai")
  page.get_by_test_id("input-email").fill("test@example.com")
  page.get_by_test_id("button-continue-student").click()

  expect(page).to_have_url("https://cs3002-26t3-workshop-test.onrender.com/academic")
  expect(page).to_have_title(re.compile("Academic info"))

  page.get_by_test_id("select-major").select_option("Computer Science")
  page.get_by_test_id("input-academic-year").fill("2023")
  page.get_by_test_id("select-term").select_option("T3-2025")

  page.get_by_test_id("button-continue-academic").click()

  expect(page).to_have_url("https://cs3002-26t3-workshop-test.onrender.com/subjects")
  expect(page).to_have_title(re.compile("Subjects"))

  page.get_by_test_id("input-new-subject").fill("MathCS3002")
  page.get_by_test_id("input-new-score").fill("50")
  page.get_by_test_id("button-add-subject").click()

  page.get_by_test_id("input-new-subject").fill("MathCS3002")
  page.get_by_test_id("input-new-score").fill("60")
  page.get_by_test_id("button-add-subject").click()

  expect(page.get_by_test_id("status-feedback")).to_contain_text("has already been added.")
  expect(page.get_by_test_id("input-subject-name-1")).to_be_hidden()
