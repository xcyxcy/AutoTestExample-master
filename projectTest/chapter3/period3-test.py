from selenium import webdriver

edgeDriver = webdriver.Edge()
edgeDriver.get('http://localhost:63342/AutoTestExample-master/projectHtml/chapter3/period3.html?_ijt=vkt942n8igmie5gfgge82dgrh7&_ij_reload=RELOAD_ON_SAVE')
edgeDriver.maximize_window()
edgeDriver.implicitly_wait(3000)
#id定位
id_maxlength = edgeDriver.find_element(By.ID,'')