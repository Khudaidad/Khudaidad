import streamlit as st

# Sample dictionary data
dictionary = {
    "apple": "You are the apple of my eye! (^_^).",
 #  fruits = {
   # "apple": "سیب.",
    "banana": "موز یا کیله.",
    "orange": "نارنج.",
    "grape": "انگور.",
    "watermelon": "هندوانه.",
    "peach": "هلو.",
    "pear": "گلابی.",
    "strawberry": "توت فرنگی.",
    "blueberry": "زغال اخته.",
    "raspberry": "تمشک.",
    "mango": "مینگ.",
    "pineapple": "آناناس.",
    "kiwi": "کیوی.",
    "lemon": "لیمو.",
    "lime": "لیمو ترش.",
    "papaya": "پاپایا.",
    "cherry": "گیلاس.",
    "plum": "آلو.",
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

# Title of the app
st.title("Khudai_Dad__'s Online Dictionary")

# Input field for user to enter a word
word = st.text_input("لطفا لغت مورد نظر خود را وارد کنید:")

# Check if the word is in the dictionary
if word:
    # Normalize the input by converting it to lowercase
    definition = dictionary.get(word.lower(), "این لغت در دیکشنری موجود نیست.")
    st.write(f"   معنی   :  {definition}")
