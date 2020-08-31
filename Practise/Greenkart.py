from selenium import webdriver
import time

itemlist=[]
driver = webdriver.Firefox(executable_path="D:\Edu_Soft\webdriver\geckodriver-v0.26.0-win64\geckodriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(5)
item = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert item == 3

time.sleep(5)
itemnames=driver.find_elements_by_xpath("//div[@class='product']/h4")
for itemname in itemnames:
    itemlist.append(itemname.text)
print(itemlist)

buttons=driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in buttons:
    button.click()


#add to cart
driver.find_element_by_css_selector("img[alt='Cart']").click()

#Proceed to check out
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

time.sleep(5)
#before coupan code amount
originalAmount=driver.find_element_by_class_name("discountAmt").text
print("Orginal amount",originalAmount)

#apply coupan code
driver.find_element_by_xpath("//input[@class='promoCode']").send_keys("rahulshettyacademy")

#click on apply button
driver.find_element_by_css_selector(".promoBtn").click()

time.sleep(5)
#afterdiscount price
AfterDiscount=driver.find_element_by_class_name("discountAmt").text
print("After discount amount",AfterDiscount)

#must be change in price
assert int(originalAmount) != float(AfterDiscount)

#final list
kartlist=[]
kartitems=driver.find_elements_by_xpath("//p[@class='product-name']")
for item in kartitems:
    kartlist.append(item.text)
print(kartlist)

#comparision of final list and add to cart item
assert kartlist == itemlist

#check sum
sum=0
total=driver.find_elements_by_xpath("//tr/td[5]/p")
for amount in total:
    sum=sum+int(amount.text)
print(sum)


#total amout as per site
totalamount=driver.find_element_by_class_name("totAmt").text

assert sum == int(totalamount)