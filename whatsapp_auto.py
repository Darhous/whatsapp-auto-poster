from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# إعداد متصفح Chrome بدون واجهة
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)

# فتح واتساب ويب
driver.get("https://web.whatsapp.com/")
input("🚀 قم بمسح كود QR من هاتفك ثم اضغط Enter للمتابعة...")

# اسم القناة
channel_name = "CEO & Legal"

# المنشورات المجدولة
posts = [
    "مرحبًا بكم في CEO & Legal! 🚀",
    "📌 نصيحة قانونية: لا تبدأ مشروعك بدون تسجيل رسمي!",
    "⚠ هل تعرف الفرق بين السجل التجاري والبطاقة الضريبية؟ 🤔",
    "🚀 قصة نجاح: كيف بدأ ستيف جوبز من الصفر إلى المليارات؟",
    "💡 كيف تختبر فكرة مشروعك قبل تنفيذه؟ إليك 3 طرق فعالة!"
]

# البحث عن القناة
search_box = driver.find_element("xpath", '//div[@contenteditable="true"][@title="Search input textbox"]')
search_box.send_keys(channel_name)
time.sleep(3)
search_box.send_keys(Keys.RETURN)

# إرسال المنشورات تلقائيًا
for post in posts:
    text_box = driver.find_element("xpath", '//div[@contenteditable="true"][@title="Type a message"]')
    text_box.send_keys(post)
    text_box.send_keys(Keys.RETURN)
    time.sleep(86400)  # انتظار 24 ساعة بين كل منشور

print("🚀 تم إرسال جميع المنشورات بنجاح!")
driver.quit()
