webapps mostly in AJAX techniques 

when page loads When a page is loaded by the browser, the elements within that page may load at different time intervals. This makes locating elements dfficult : if an element is not yet present in the DOM, a locate function will raise an ElementNotVisibleException exception, 

Using waits, we can solve this issue. 
Waiting provides some slack between actions performed - mostly locating an element or any other operation with the element.

Selenium Webdriver provides two types of waits - implicit & explicit. 

An explicit wait makes WebDriver wait for a certain condition to occur before proceeding further with execution. An implicit wait makes WebDriver poll the DOM for a certain amount of time when trying to locate an element.

Explicit Waits:

