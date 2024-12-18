import streamlit as st

# Sample dictionary data
dictionary = {
 #  fruits = {
    "apple": "سیب.",
    "banana": "موز یا کیله.",
    "orange": "نارنج.",
    "grape": "انگور.",
    "watermelon": "هندوانه.",
    "peach": "هلو.",
    "pear": "گلابی.",
    "strawberry": "توت فرنگی.",
    "blueberry": "زغال اخته.",
    "raspberry": "(شاه توت)استه یگان چیز دگه هههه.",
    "mango": "مینگ.",
    "pineapple": "آناناس.",
    "alidad": "He is khudaidad's my brother.",
    "lemon": "لیمو.",
    "aliakber": "He is Alidad's brother.",
    "papaya": "پاپایا.",
    "cherry": "گیلاس.",
    "ali akber": "He is Alidad's brother.",
    "avocado": "آووکادو.",
    "coconut": "نارگیل.",
    "apricot": "زردآلو.",
    "grapefruit": "گریپ فروت.",
    "cantaloupe": "خربزه.",
    "fig": "انجیر.",
    "cranberry": "زغال اخته قرمز.",
    "pomegranate": "انار.",
    "guava": "گواوا.",
    "passion fruit": "میوه عشق.",
    "lychee": "لیچی.",
    "dragon fruit": "میوه اژدها.",
    "blackberry": "توت سیاه.",
    "boysenberry": "توت بویسن.",
    "tangerine": "نارنگی.",
    "nectarine": "هلو بدون کرک.",
    "olive": "زیتون.",
    "date": "خرما.",
    "persimmon": "خرمالو.",
    "starfruit": "(کارامبولا) میوه ستاره‌ای.",
    "mulberry": "(توت) توت سفید یا سیاه.",
    "elderberry": "(بیدمشک) توت بیدمشک.",
    "gooseberry": "(انگور فرنگی) انگور فرنگی سبز یا قرمز.",
    "jackfruit": "(جکفروت) میوه جکفروت.",
    "plantain": "(موز پختنی) موز سبز یا پختنی.",
    "guanabana": "(سورسوپ) میوه گوانابانا.",
    "acerola cherry": "(آسرولا) گیلاس آسرولا.",
    # 50 more fruits
    # Continuing from 50 to 100
	"kumquat":"کومکوات",
	"ackee":"اکی",
	"breadfruit":"نان میوه",
	"barberry":"زردآلو",
	"longan":"لانگان",
	"durian":"درخت دوریان",
	"feijoa":"فیجوآ",
	"quince":"به",
	"horned melon":"ملون شاخدار",
	"ugli fruit":"میوه اوگلی",
	"custard apple":"سیب کستارد",
	"buddha's hand":"دست بودا",
	"miracle fruit":"میوه معجزه",
	"salak":"سالاک (میوه مار)",
	"jabuticaba":"جابوتیکابا",
	"chayote":"چایوت",
	"kiwano":"کیوانو (خیار شاخدار)",
	"black currant":"کرنت سیاه",
	"red currant":"کرنت قرمز",
	"white currant":"کرنت سفید",
	"cloudberry":"توت ابری",
	"lingonberry":"توت لینگون",
	"marionberry":"مارین بری",
	"tayberry":"تی بری",
	"loganberry":"لوگان بری",
	"acai berry":"توت آسايی",
	"camu camu ":"کامو کامو ",
	"kiwifruit ":"کیوی ",
	"blood orange ":"پرتقال خونی ",
	"tamarind ":"تمر هندی ",
	"pawpaw ":"پاپا ",
	"saskatoon berry ":"توت ساسکتون ",
	"huckleberry ":"هاکل بری ",
	"jujube ":"خرما ",
	"rambutan ":"رامبوتان ",
	"loquat ":"زردآلو چینی ",
	"star apple ":"سیب ستاره ای ",
	"mamey sapote ":"مامی ساپوت ",
	"soursop ":"سورسوپ ",
	"sapodilla ":"سپا دیلا ",
	"cempedak ":"سیمپدک ",
	# Common animals
    "dog": "سگ.",
    "cat": "گربه.",
    "horse": "اسب.",
    "cow": "گاو.",
    "sheep": "بره یا گوسفند.",
    "goat": "بز.",
    # Birds
    "chicken": "(مرغ) مرغ خانگی.",
    "duck": "(اردک) مرغابی.",
    "turkey": "(بوقلمون) بوقلمون.",
   
    "lion": "(شیر) شیر.",
    "elephant": "(فیل) فیل.",
    "bear": "(خرس) خرس.",
    "wolf": "(گرگ) گرگ.",
    "fox": "(روباه) روباه.",
    "deer": "(گوزن) گوزن.",
    "rabbit": "(خرگوش) خرگوش.",
    
   # Exotic and other wild animals
     "zebra":"(زیبرا) زیبرا.",  
    "giraffe":"(زرافه) زرافه.",  
    "monkey":"(میمون) میمون.",  
    "kangaroo":"(کانگورو) کانگورو.",  
    "panda":"(پاندا) پاندا.",  
    "hippopotamus":"(اسب آبی) اسب آبی.",  
    "rhinoceros":"(کرگدن) کرگدن.",  
    "crocodile":"(تمساح) تمساح.",  
    "alligator":"(تمساح آمریکایی) تمساح آمریکایی.",  
    "snake":"(مار) مار.",  
    "lizard":"(مارمولک) مارمولک.",  
    "frog":"(قورباغه) قورباغه.",  

   # Sea animals
    "dolphin":"(دلفین) دلفین.",  
    "shark":"(کوسه) کوسه.",  
    "whale":"(نهنگ) نهنگ.",  
    "octopus":"(هشت پا) هشت پا.",  
    "seal":"(فک) فک.",  
    "starfish":"(ستاره دریایی) ستاره دریایی."

}

# Biography entry for Khudaidad Zahidi
biography = """
**Khudaidad Zahidi** is a prominent figure known for his contributions to knowledge and music . With a deep commitment of making lifes happier, he has dedicated his life to improving the lives of others in his community.

Born and raised in Afghanistan, Khudaidad has witnessed firsthand the challenges faced by his country. His experiences have shaped his vision for a better future, motivating him to engage actively in cultural an educaltional programs. He is recognized for his leadership skills and ability to inspire others.

Throughout his career, Khudaidad has held various positions that reflect his dedication to his goals. His work has been instrumental in equality and loyalty.

In addition to his professional accomplishments, Khudaidad is passionate about music, football, engaging, teaming, and cultural events which enriches his life and allows him to connect with others on a personal level. He believes in the power of education and community engagement as tools for transformation.
"""
# Title of the app
st.title("Khudai_Dad__'s Online Dictionary")

# Input field for user to enter a word
word = st.text_input("لطفا لغت مورد نظر خود را وارد کنید:")

# Check if the word is in the dictionary
if word:
    # Normalize the input by converting it to lowercase
    if word.lower() == 'khudaidad':
        st.write(biography)
    else:
        definition = dictionary.get(word.lower(), "(این لغت در دیکشنری موجود نیست.)")
        st.write(f"(معنی): {definition}")
