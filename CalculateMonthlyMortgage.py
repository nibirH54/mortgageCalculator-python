

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.get("https://www.mortgagecalculator.org/")
driver.maximize_window()


#Enter home-value as $300000
driver.find_element(By.ID, "homeval").clear()
driver.find_element(By.ID, "homeval").send_keys("300000")

#Enter down-Payment as $60000
driver.find_element(By.ID, "downpayment").clear()
driver.find_element(By.ID, "downpayment").send_keys("60000")

#Enter lOAN Amount as $240000
driver.find_element(By.ID, "loanamt").clear()
driver.find_element(By.ID, "loanamt").send_keys("240000")

#Enter Interest Rate as 3%
driver.find_element(By.ID, "intrstsrate").clear()
driver.find_element(By.ID, "intrstsrate").send_keys("3")

#Enter loan term 30 years
driver.find_element(By.ID, "loanterm").clear()
driver.find_element(By.ID, "loanterm").send_keys("30")

#Select the start date month as December
select = Select(driver.find_element(By.NAME, "param[start_month]"))
select.select_by_visible_text("Apr")

#Enter year as 2023
driver.find_element(By.ID, "start_year").clear()
driver.find_element(By.ID, "start_year").send_keys("2023")

#Enter Property Tax as $5000 per year
driver.find_element(By.ID, "pptytax").clear()
driver.find_element(By.ID, "pptytax").send_keys("5000")

#Enter PMI as 0.5
driver.find_element(By.ID, "pmi").clear()
driver.find_element(By.ID, "pmi").send_keys("0.5")

#Enter HOI as 1000
driver.find_element(By.ID, "hoi").clear()
driver.find_element(By.ID, "hoi").send_keys("1000")

#Enter Monthly HOA as 100
driver.find_element(By.ID, "hoa").clear()
driver.find_element(By.ID, "hoa").send_keys("100")

#Select Loan Type as FHA
select = Select(driver.find_element(By.NAME, "param[milserve]"))
select.select_by_visible_text("FHA")

        #Select Buy Option
select = Select(driver.find_element(By.NAME, "param[refiorbuy]"))
select.select_by_visible_text("Buy")




#Click on calculate Button
driver.find_element(By.NAME, "cal").click()

expectedTotalMonthlyPayment = "1611.85"
formattedXpath = f"//h3[text()='$1,611.85']"

present = driver.find_element(By.XPATH, formattedXpath).is_displayed()

assert present, "Total Monthly Payment is not presented"


driver.quit()

