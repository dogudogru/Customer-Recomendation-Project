import pandas as pd
import numpy as np
from PIL import Image,ImageDraw,ImageFont
from pandas.core.frame import DataFrame
import requests
import time
from requests.api import options
import streamlit as st
from PIL import Image
import requests

from PIL import Image
import requests
import base64


data = pd.read_csv("data1.csv")
data2 = data.drop(data.columns[0],axis=1)

data_b = pd.read_csv("data2.csv")
data2_b = data_b.drop(data_b.columns[0],axis=1)


url_cam = "https://www.bekokibris.com/wp-content/uploads/2020/04/BK9102EYS1.jpg"
url_bul = "https://statics.vestel.com.tr/productimages/20264045_r1_900_1254.jpg"
url_buzdo = "https://cdn.akakce.com/samsung/samsung-rb50rs334sa-a-kombi-no-frost-x.jpg"

im = Image.open(requests.get(url_cam, stream=True).raw)
#im = im.resize((500,500))
im2 = Image.open(requests.get(url_bul, stream=True).raw)
#im2 = im2.resize((500,500))
im3 = Image.open(requests.get(url_buzdo, stream=True).raw)
#im3 = im3.resize((500,500))

st.set_page_config(page_title='Customer Recommendation Project', page_icon=':house_with_garden')

#Menü gizleme
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

#Tek sayfaya sığdırma
padding = 0
st.markdown(f""" <style>
    .reportview-container .main .block-container{{
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
    }} </style> """, unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://www.birbeymetal.com.tr/wp-content/uploads/2019/02/Savin-NY-Website-Background-Web.jpg")
    }
   .sidebar .sidebar-content {
        background: url("https://www.birbeymetal.com.tr/wp-content/uploads/2019/02/Savin-NY-Website-Background-Web.jpg")
    }
    </style>
    """,
    unsafe_allow_html=True
)

options_m = [' ','Çamaşır Makinesi', 'Bulaşık Makinesi']
machine = st.sidebar.selectbox('Ne arıyorsunuz? 👉', options=options_m)

dil = ["TR", "EN"]

col1, col2, col3, col4, col5,col6,col7,col8,col9,col10,col11,col12 = st.columns([1,1,1,1,1,1,1,1,1,1,1,5])



with col12:
    dil_secenek = st.radio("Language",dil)
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    


dataf = data2
dataf_b = data2_b
##ÇAMAŞIR

brand1 = ["Bosch", "Siemens","Samsung","Electrolux"]
brand2 = ["Arçelik", "Vestel","LG","Profilo","Beko"]

data4 = data2.copy()
for i in range(len(data2['brand'])):
    if (data2['brand'][i] in brand1):
        data4['brand'][i] = 3
    elif (data2['brand'][i] in brand2):
        data4['brand'][i] = 2
    else:
        data4['brand'][i] = 1

for i in range(len(data2['capacity'])):
    if data2['capacity'][i] == "Yüksek Kapasite":
        data4['capacity'][i] = 3
    elif data2['capacity'][i] == "Orta Kapasite":
        data4['capacity'][i] = 2
    else:
        data4['capacity'][i] = 1
        
for i in range(len(data2['cycle'])):
    if data2['cycle'][i] == "Yüksek Devir":
        data4['cycle'][i] = 3
    elif data2['cycle'][i] == "Orta Devir":
        data4['cycle'][i] = 2
    else:
        data4['cycle'][i] = 1
        
for i in range(len(data2['size'])):
    if data2['size'][i] == "Standart üstü":
        data4['size'][i] = 3
    elif data2['size'][i] == "Standart Boyut":
        data4['size'][i] = 2
    else:
        data4['size'][i] = 1
        
for i in range(len(data2['energy_usage'])):
    if data2['energy_usage'][i] == "Çok önemli":
        data4['energy_usage'][i] = 3
    elif data2['energy_usage'][i] == "Önemli":
        data4['energy_usage'][i] = 2
    else:
        data4['energy_usage'][i] = 1
        
for i in range(len(data2['blanket'])):
    if data2['blanket'][i] == "VAR":
        data4['blanket'][i] = 2
    else:
        data4['blanket'][i] = 1
        
for i in range(len(data2['wifi'])):
    if data2['wifi'][i] == "VAR":
        data4['wifi'][i] = 2
    else:
        data4['wifi'][i] = 1

for i in range(len(data2['load_sensor'])):
    if data2['load_sensor'][i] == "VAR":
        data4['load_sensor'][i] = 2
    else:
        data4['load_sensor'][i] = 1
        
for i in range(len(data2['delay'])):
    if data2['delay'][i] == "VAR":
        data4['delay'][i] = 2
    else:
        data4['delay'][i] = 1

for i in range(len(data2['control_panel'])):
    if data2['control_panel'][i] == "VAR":
        data4['control_panel'][i] = 2
    else:
        data4['control_panel'][i] = 1
        
for i in range(len(data2['vapor'])):
    if data2['vapor'][i] == "VAR":
        data4['vapor'][i] = 2
    else:
        data4['vapor'][i] = 1
        
for i in range(len(data2['vapor'])):
    if data2['vapor'][i] == "VAR":
        data4['vapor'][i] = 2
    else:
        data4['vapor'][i] = 1
        
for i in range(len(data2['anti_alergy'])):
    if data2['anti_alergy'][i] == "VAR":
        data4['anti_alergy'][i] = 2
    else:
        data4['anti_alergy'][i] = 1
        
for i in range(len(data2['baby_p'])):
    if data2['baby_p'][i] == "VAR":
        data4['baby_p'][i] = 2
    else:
        data4['baby_p'][i] = 1
        
for i in range(len(data2['sensitive_p'])):
    if data2['sensitive_p'][i] == "VAR":
        data4['sensitive_p'][i] = 2
    else:
        data4['sensitive_p'][i] = 1
        
for i in range(len(data2['child_lock'])):
    if data2['child_lock'][i] == "VAR":
        data4['child_lock'][i] = 2
    else:
        data4['child_lock'][i] = 1
        
puan = 0
data4["puan"] = ""
for k in range(len(data2['full_name'])):
    for j in data4.drop(["full_name","price","image","puan"],axis=1).columns:
        if j != "child_lock":
            puan = puan + data4[j][k]
        else:
            puan = puan + data4[j][k]
            data4["puan"][k] = puan
            puan = 0
dataf["puan"] = data4["puan"]

len_lst1 = []
len_lst2 = []


##BULAŞIK
brand1 = ["Bosch", "Siemens","Samsung","Electrolux"]
brand2 = ["Arçelik", "Vestel","LG","Profilo","Beko"]
data4_b = data2_b.copy()
for i in range(len(data2_b['brand'])):
    if (data2_b['brand'][i] in brand1):
        data4_b['brand'][i] = 3
    elif (data2_b['brand'][i] in brand2):
        data4_b['brand'][i] = 2
    else:
        data4_b['brand'][i] = 1

for i in range(len(data2_b['capacity'])):
    if data2_b['capacity'][i] == "Yüksek Kapasite":
        data4_b['capacity'][i] = 3
    elif data2_b['capacity'][i] == "Orta Kapasite":
        data4_b['capacity'][i] = 2
    else:
        data4_b['capacity'][i] = 1
        
for i in range(len(data2_b['type_'])):
    if data2_b['type_'][i] == "Ankastre":
        data4_b['type_'][i] = 3
    elif data2_b['type_'][i] == "Solo":
        data4_b['type_'][i] = 2
    else:
        data4_b['type_'][i] = 1
        
for i in range(len(data2_b['size'])):
    if data2_b['size'][i] == "Standart üstü":
        data4_b['size'][i] = 3
    elif data2_b['size'][i] == "Standart Boyut":
        data4_b['size'][i] = 2
    else:
        data4_b['size'][i] = 1
        
for i in range(len(data2_b['energy_usage'])):
    if data2_b['energy_usage'][i] == "Çok önemli":
        data4_b['energy_usage'][i] = 3
    elif data2_b['energy_usage'][i] == "Önemli":
        data4_b['energy_usage'][i] = 2
    else:
        data4_b['energy_usage'][i] = 1
        
for i in range(len(data2_b['wifi'])):
    if data2_b['wifi'][i] == "VAR":
        data4_b['wifi'][i] = 2
    else:
        data4_b['wifi'][i] = 1
        
for i in range(len(data2_b['control_panel'])):
    if data2_b['control_panel'][i] == "VAR":
        data4_b['control_panel'][i] = 2
    else:
        data4_b['control_panel'][i] = 1        

for i in range(len(data2_b['box'])):
    if data2_b['box'][i] == "Çekmeceli":
        data4_b['box'][i] = 2
    else:
        data4_b['box'][i] = 1
        
for i in range(len(data2_b['number_of_program'])):
    if data2_b['number_of_program'][i] == "9+":
        data4_b['number_of_program'][i] = 3
    elif data2_b['number_of_program'][i] == "5-8 Program":
        data4_b['number_of_program'][i] = 2
    else:
        data4_b['number_of_program'][i] = 1 

for i in range(len(data2_b['water_consumption'])):
    if data2_b['water_consumption'][i] == "Düşük Tüketim":
        data4_b['water_consumption'][i] = 3
    elif data2_b['water_consumption'][i] == "Orta Tüketim":
        data4_b['water_consumption'][i] = 2
    else:
        data4_b['water_consumption'][i] = 1     
        
puan = 0
data4_b["puan"] = ""
for k in range(len(data2_b['full_name'])):
    for j in data4_b.drop(["full_name","price","image","puan"],axis=1).columns:
        if j != "water_consumption":
            puan = puan + data4_b[j][k]
        else:
            puan = puan + data4_b[j][k]
            data4_b["puan"][k] = puan
            puan = 0
dataf_b["puan"] = data4_b["puan"]
dataf_b["puan"] = dataf_b.puan.astype(int)
dataf_b["price"] = dataf_b.price.astype(float)


if dil_secenek == "TR":
    if machine ==" ":
        col1, col2, col3, col4, col5,col6,col7,col8,col9,col10,col11,col12 = st.columns([1,1,1,1,1,1,1,1,1,1,1,5])



        with col12:
            if dil_secenek == "TR":
                button = st.button("Beğen 👍")
                if button:
                    st.write("Teşekkür ederiz 💗")
                    file1 = open("counter.txt","r")
                    count = file1.read()
                    count_int = count.replace("'","")
                    count_int = int(count_int) + 1
                    with open('counter.txt', 'w') as f:
                        f.write(str(count_int))
            
        st.title("Proje hakkında")
        st.markdown("<b><i>Tüketici Ürün Rehberi </i></b>, beyaz eşya ihtiyacı bulunan tüketicilerin, kendileri için en iyi ürünü seçmesine yardım etmeyi amaçlayan bir Python projesidir.", unsafe_allow_html=True)

        st.markdown("İnsanlar, etkileşimde bulundukları e-ticaret web sitelerinin, kim olduklarını ve neyle ilgilendiklerini hatırlamalarını ve önceki etkinliklerine dayalı olarak yeni içerik ve ürünler ile kendi ihtiyaçlarına uygun önerilerde bulunulmasını bekler. Bu talepleri karşılayamayan herhangi bir uygulama veya web sitesi, kullanıcılarının hızla azaldığını görecektir.")

        st.markdown("Tüketici Ürün Rehberi, belirli bir kullanıcının ihtiyaçlarına göre satın almak istediği eşyalar için öneriler oluşturmak amacı ile tasarlanmış bir yazılım aracıdır.")

        st.markdown(" ")
        st.title("Proje Geliştiricileri")
        st.markdown(" ")
        col1, col2, col3, col4, col5,col6,col7 = st.columns([1,1,1,1,1,1,1])

        with col1:
            st.markdown("<b><i>Mert Türkyılmaz</i></b>", unsafe_allow_html=True)
            st.markdown("[![Foo](data:image/png;base64,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)](https://www.linkedin.com/in/mertturkyilmaz/)")
            st.markdown("[![Foo](data:image/png;base64,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)](https://github.com/mertturkyilmaz)")

        with col4:
            st.markdown("<b><i>Sarper Yılmaz</i></b>", unsafe_allow_html=True)
            st.markdown("[![Foo](data:image/png;base64,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)](https://www.linkedin.com/in/sarperyilmaz/)")
            st.markdown("[![Foo](data:image/png;base64,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)](https://github.com/sarperyilmaz)")
        with col7:
            st.markdown("<b><i>Doğukan Doğru</i></b>", unsafe_allow_html=True)
            st.markdown("[![Foo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAAAXNSR0IArs4c6QAAEWtJREFUaEPVWXl019WV/3zuNyF7AgFCAgmIyhoWBRcCilqhajvWDeiMSyuIOi1dXOrYOq069rTO6bRje7pbDNa6VMClteJSC1XZBBTZt0QgCSQkIRASyPq9nzkvUQ4JUJdO/+g7h3M437zfe+/z7r2fe+/nEf/kg//k58c/FMAtL6xJbW9uuwCmooYYD2ZGNg2u/q62YkNCHB3o0fDwrWe1/T2X+P8O4Kb5y89pS4hKo9hvE5lEoMSEBFFXOxSb+BhMfQnbH8Vtr8eWMDaOsOHRq4p2fRIgnxjArD8szVBbNJNCdoLai9uYcDMN7QRiCec6vJaKKgkNh5AjQwkdo2H6vYAKgBNNOCJgfYP0bF+0RA0JPVJ/d/Wk6o8D5GMDuP9+WdnoFTMVczYjbJE0mFSC3P5q9N6C9SbQKikZxFCSqyANk9sRmL8AcKyEmSR+ASgCsFvA5yH2AfGTedOKHvqHAZg+f36UYfkvgFaDGP1EXUjDk3TUyDBQMdJItIsaCHAbnamghot4DcB7dE6GxSMFWyEoj87+MLWA1mqKF0sBJBLN8frc6UV//ShAPrIFvjB/+YAE41fdcboZPgvgHQjvwpgOVwagLICtoNQB0L3IxfUW4U+SCgG7HK7tZnIXz5C42+jtIPoAWAm3QTDvKdmvYVqHKKpJjGz/w5efdeRvAflIAGYuWP4vlN0k+lnhhkF7Q5II9hA03KAyd2aaYY8cwxxsoukZgqmS/l2GfRbzgOhnEDgE49sQCgFVCDwAcLzkJSRySTYiRptMCQSa0lIPXvXTz3ym5WQgPhTATQtXXC4pMMoZAF42eAS3DBkKCB1050EaGwHvKWCgga8K2ALgxuD7MG50aSCBfDiXEkgPLCTYYoMPcWE8yVSHdhpY6dJgI3pL9qM44o8SY01Vj/Y3iq84b++JQJwUwA2PrUtLSD1yCxyX01ADMAY0SpCFhQxc60BMKQ3AOJi9DfgrEIskXE9qm5PNJhVKrO2wgjBG8ldBa6QwRUA7qXSB7XSUyjACjo2MuBCODTKdYa6dIk6h45FHZkys6w7ipABmLVx+F8mhilnwfuAJUhLNXoHUkp3So399S9uouB1rEWGpHIF9viSL2+lcD6BA4EBSlQCyBVYb/M+AfVpANhC+sy+kwD5HHKgmbAngRQTaBNQBlmfCXNDrCjYWPXr//fSPBODL85ekN0UpPwQwRu6nGJkgaDdg60/LTu1/89lDJuekJ6e2xd76Rmn14ic27CwAMJTOd52qNvIcQT0BNhBIAfQ7OvPdNJViKYiQfYcASAbQLPDJQKmEzpaQCTKV0CGAiYLeMkbFUY9oCZqQ+PCMs+qPBXFCC8xcsGK2DDebMASSA3zDDUcsZtr3Lx1zSb+MlJQPFpGAB/+6sa60tnELTL0AnI6O22OSS8tJ7uyMB+wXtc2AfImnkUiC4zVG2CVpIoR+IDKkQGOqM6AHwKdBlodgFvzfKL7+yPSiu08KICSp8sIV14j8jqBCkWtM2EUoycGBOek91vz3JeNu7m7G5zdV1L+wtewQZIc79u+IET0r8HLIBsqwhe5Nwa1ADCJY7sBSOkaKGECi3/trRgj0Jm6iYbGEDdbJdPdBWC9y9bzpE+45OYAlSxIqDqRcJPc5DuTT2YyAni7SXo7Mxv7sc2dd2yOyhGMXefydnWsXl+6roPkwKFoEem+E7ArsFa2S7n1A5ndSLxY5kUlxFKmQA0JgZgBMk9BAYj7EBkBrAFwv4nQDVgrcZM6nPamtJcGSD36QH45zoRsXvHW+QX+EtEadLrGEChkVfRzq+enT88791zGDssjOn+491LTv/r+sL4kdZZC2g/gyoFRAe+TW2nHjRAboSxFHtbB4vGQ9CYW/lQgcwhDkjhcYoTZkddAzXPwiwAjCchiLCV0IoFbQunnTJj71wQV2AXDDs8tyEhX9j2IVEKwHtQ7mF0O2V9BpEEYA7DE8J2PLmXnZVt3QrDd3V9e1O54VdRWEC4LFAJSEYCQxKPA7hM0EzgLYk4QArwHsIIBcOfaZ+Zvuli/z/aboSsCzRByCsxyGTAgicUjA0xA3ktGG4mlnvxdAdAEwe+HKMS7MFNQow2CTst15xAxDQ5CJKodUBzJYpjG4A8E8h75CMJFAqZPVVJwPMIvAOoflAB4YJ2zWBFmbqFoIqSRegjBADOW1cgArELSGbvtp6OdSL0KlJAe5o4zkEhH71ND02KMzLwru3RVAoM+WKPk2l64lsKYj49KLjGyMpa0Ue6clRa0JCbbWiIrm1niOwFPa4rgqlvZQyDRjdkpiwgEQLRCGC4ia27wl9jgO1iPRIGJpsqGhJcZlgFoA5nZmYiyScyBMpxNsd6mMwNiwBs12USoHUFU8rejrXV1I4qxnV8yCcDOhdxxspfNCGU4TsTmKUetAyuBeaQ3fmTL6c91Z6NXtlYee3hD6EbYU9s1qumPyiIHHzvnxsi2H9hxqzrxyxIC6MXm9ElMTo/TIjM1t7dp98HC8qbr+Ly9uqdwCabJTeWbc7jFppvfJQv0BbhSU3mF1RpsfuebcF49aYPr85SnpxMXWETAoFjgR8GaIOyTmkNhB8vVTs9PH3XNR4Re6A3h5e2XT/PW7D1CoGd4vc8Bdk0cGdjk6nt9c0XTZ0LyEpIQo8WRF2YqymubfrC7Z2ZmFLcngWwEb5FIOobyQ/AQuBANDAZHwi7nTJqw/GgOzn1k5weU/BnCmhAMdGxFbKFsMqo8cnyromVr/X1PHTOp+iMUlVfueWLerVML4UblZe+84b8TgY+c44BZSw4eMX7+1/eCqsro1IBooJMFCZas+cG4h0CjTAABHAM6ZN63oraMW+NITb/ZqSYreIfmaS9MB7CD0BmTJYKAvbiRceRnpI7776TFjjnOhHZUHf79uVwtgxePyek3+yqShx4H84DfucLMTg9lcfbDyh29sXt05l1MobpJxA4BJgFJIL4PsIIEdh7z8rgUzZsQdFrhx4fLh5q6BfdtKy/enhCzcE/RxUGAW7nBoPJz1+T1TMh6YOrawO4DVFbWrfrWy5E1QNxf2y6q947yRp3afs3Zv3YFF2yt/UFrTcEVuZsrI2WefmnZqdkZoKY+Oprb25q+8sGY9xR6ANop+CmSFEPaB2glnPzesQkPz7cexUOi4ItocWnw+QqsnvidjATvSp6ogDs3LSE783iVn9O1+uD+XVO1/at2uA4Be/NTg3MTrxw3+8rFzmtviw7e/+Pa81tiv62B0ug3ITKt6YOqYod3X+tof1jx/pL2tt4Ph4M2g9sIZOreOZorUTXGcsPjRGedUHXWh8J+ZC1ecS2gOgPHvLzpIsAoiTu3gZ3LFoMyU5vumjLmo+6bLdtdsfGRNyQKK7aPzel5726ThXay0qry2/lerSoK5KWA/oHoC7Q99dvzozOQeqceud+eid+oPNLVGhIdOLfwLlS4kNFGoQoTtov1m3tXnLu4CYNaCld8B/EbR2oK/gZ5KWR9BWwiWij6hX2pK7wcvPfO48mP93rrFP1m+LdTvU4b2zUi6+4KRR6vVsMlL2/YcWbix/AActTDUSn4YFvX91uQR5wzpk9nFje55eW31vsNNByVLB5BDeqXEHoQlSVrLiLWQDhVPK5p9FMD0+Rt7ZFjDLxysI3GeoMiEFHdsN2AwTKMgVAzISjnwwNQzPrDQ0Yt7dUdl/dPrdzfKcWB8fq/aOUXDQt1ydPxpa8X+5zZUbCVQL0MSwd6AMu6bMjqxICutS8749ivrqiobm3IltJBeTUT7JU8j9VrslmOm8Qa7IlDoUQCdIlXCFQaNix2hizqPxiUunWuCQCUK1is/K2XnA1PGju7uQq+VVNU8uW7nmwQGDOubOfY/JheGRuXoeHFrRe1zm/ZUiNgB12gSayT0uf384ZeO6tezy3IBQFVj0+GY2G+S4Ewm8ZSEGSBSRTyemJT40Amr0SALxsS9JFpE5lsMwjRWYBXIl0b0yWi8a/LIO7sDeP29fbt/+87O3PC9sF9mzZ3nj8zvZoGa5zaVvxeCMSh0AK4JddG9F49uGdQzrcvc/3x1bXlVQxMkc6M/7mA6wBsovA5yFeGvPDJt4toP1u/iz0GM9db20Hj/AGB/l/JothDwtS7rX5CZMuWBqWPO7A7gxW178OyG8q2h6yrM7Vlwx/nDu7jFi1v31Dy7qXyJoNEEBwN6LEguX5807LrRub26nCFYYE9j0/ORWOrQ7aRaAfs1iBGUJon8ZfE1E350QgCzFqy4jOQEwW+D8CrMVkJxf8CGCsrNTU8Z/f1Lzkg63gLVO3+7tnR/uOGR/TIKvjG5MGTMo2PRtj2Vz2woy4XxaUi7Qs0loOmBqWPi/Ky0QcfO/fHSbd/euK/uEgcDW/wcQqiHbgiND+lLHrlm4hwwkFnn6IJ+1sLVp9LbDBH7CcqRcM/7Yu2AIGKNzM0svvO8kd88DkBphwtVkhoyOq9XVXcafWVH5c75G8p+jlg3hAIRwKNBqbhj0vDPj8rt2YWFvvny2vbqwy1PgNhM4Wsh2OV824xveoLNnXflOaEiPTqOo8RO/bPgexBvBdQaJBARc43Y3D8t9RvfvWRMF/cIKwUW+v263aHWaRiWk5Fz9+TCLi3n4veqNjyxdtdIAY+bsM+pWwm2fuvCUdHpvdOzjz3QQ8u23rdh78HLaKGMZhng7QRXAvDiaybceuztH2eB8OGmZ1beAMXDxGgo5U+KdhVcl4pKys9KrXpgythhJ4qBZzaUh342YWifjJS7L+habfx5R1XJU+t3/VTEdUHoCoo0gLcfvPTMcTlpyV0mf+vld9uqDzftDworiGQCjwdVpMEznl8wY1Rr971PKKvcNH95ttO+IaqXQVeG7ElgWSKZl5OeMsSBqN19sIGHQ3pvbG2vb2hpD11VelJi9PiQ7MySmqaWWyC1Z6cmPVbZ2JRx4HDrVaLcnHtlehXgqVnJiVfmZiTPc9Hqm1pnU2qobW5RHKMXoJrQixi5J6m5/c5fXnd+Z4XcbZxUmevQRIlToNBMBAPamTLPhzgwtJwkqwgkKLR9ZD7Bd0UVK8ZVHXUL8L+w0ILyyk5JEocBe4sKva1m0LhM0lJKX5cpk0KdxECpDSBb2LnH8giJ9z58zVlB3TvhOCmAW55c06c9OR7A2K916jCF6zuaCoXGPFBbR32SA9MRk/1OwABB09jRdOAlQKci5qWdYhUqzXyrwyYE0B1BLH0W5EQ4toEIDQsBxep86GimUCHyoXnTJjx8ssOfMAaOnXzj/FW5iNoKTHZvKG/jSHOt3f4S9ByJTmg1aPsABSWhPPA1wSxJIVtPCiIAxTIQiYCPBbAAsAxBNxLcGoRigqH0bpTQK8QQoEMElrQ55jw2Y+Kev3X4DwUQJsxcsHImIu6GvC9jzgR1BMQ5oTBT5AMoSyPwDIAa0c+GWx+RpGMXTBVOjKZUEV5oIE7v0INM++Q2lkQzoCSAmYLqg6BrwFYz3jn36qIg0X/o+ND3gbDC7PlvDUaSjrS3ea9Ei1yuZAc+I3S0eNmSLjKqPYi5Luw0BjmSWbFzoBHvkD7ewUGQbyOsIKgQoO99/12sd3joo0MifzZv2rmPdqfKT+xC3X/Y+WZw+HN07YoSEvbH7rNc+oIRaQT/GDNsrRR6qOFZ51AjTONCi2rO0EiOFVkCeSbRUSAepocXH6yW2u6fN2NyzYde+UdloRMt9NVFi5J6r7qs7f77oFkL3npJ1HAQy2j2A3r79MBU3vHuZQUdIhbR5jFqaRpJoRJiEoghnW7IlZ1g7btzZ0x4++Me/IP5H8mFui/eIYAl9DglZmvFo1dddPCLzy07zeLoYoOvdtrPCb0CaD3AfLlPoUUHIR8W+msJ+yQWN6JsW2jKP+nB/y4A3TedNX/psOIZ520L30M9BcWnk14Tyt6ZC1Ze0aiyP6UgP/ejsMrHBfSJLPBxN/lHzv+nB/B/jzziqZ3jZRgAAAAASUVORK5CYII=)](https://www.linkedin.com/in/do%C4%9Fukando%C4%9Fru/)")
            st.markdown("[![Foo](data:image/png;base64,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)](https://github.com/dogudogru)")
            
    elif machine =="Çamaşır Makinesi":
        with st.sidebar:
            capacity_options = [' ','Düşük Kapasite','Orta Kapasite', 'Yüksek Kapasite']
            capacity_help = '''Düşük kapasite: 0-6 KG , Orta Kapasite: 7-10 KG, Yüksek Kapasite: 10+ KG'''.strip()
            capacity = st.sidebar.selectbox('Almak istediğiniz çamaşır makinesinin kapasitesi ne kadar olmalı?',options=capacity_options,help=capacity_help)

            cycle_options = [' ',"Düşük Devir","Orta Devir","Yüksek Devir"]
            cycle_help = '''Düşük devir: 1000'e kadar, 
            Orta devir: 1000 - 1200, 
            Yüksek Kapasite: 1200+'''.strip(",")
            cycle = st.sidebar.selectbox('Almak istediğiniz çamaşır makinesinin devir sayısı ne olmalı?',options=cycle_options,help=cycle_help)

            size_options = [' ',"Küçük boyut","Standart Boyut","Standard üstü"]
            size = st.sidebar.selectbox('Almak istediğiniz çamaşır makinesinin büyüklüğü ne kadar olmalı?',options=size_options)

            energy_usage_options = [' ','Çok önemli', 'Önemli', 'Az önemli', 'Önemsiz']
            energy_usage_help = '''Çok Önemli: A+++ A++, Önemli : A+ A, Az Önemli: B C, Önemsiz: D E F G)'''.strip()
            energy_usage = st.sidebar.selectbox('Almak istediğiniz çamaşır makinesinin tükettiği enerji miktarı sizin için önemli mi?',options=energy_usage_options,help=energy_usage_help)

            soru_list = [capacity,cycle,size,energy_usage]


            soru_list1 = ["capacity","cycle","size","energy_usage"]
            soru_list2 = [capacity,cycle,size,energy_usage]
                
        
        if all([i == " " for i in soru_list2]):
            st.title('Bakalım sizin için nelerimiz var?')
            col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1])
            data3 = data2.sample(frac=1).drop_duplicates(['brand']).sample(10).reset_index()
            im1 = Image.open(requests.get(data3.image[0], stream=True).raw).resize((100,150))
            im2 = Image.open(requests.get(data3.image[1], stream=True).raw).resize((100,150))
            im3 = Image.open(requests.get(data3.image[2], stream=True).raw).resize((100,150))
            im4 = Image.open(requests.get(data3.image[3], stream=True).raw).resize((100,150))
            im5 = Image.open(requests.get(data3.image[4], stream=True).raw).resize((100,150))
            im6 = Image.open(requests.get(data3.image[5], stream=True).raw).resize((100,150))
            im7 = Image.open(requests.get(data3.image[6], stream=True).raw).resize((100,150))
            im8 = Image.open(requests.get(data3.image[7], stream=True).raw).resize((100,150))
            im9 = Image.open(requests.get(data3.image[8], stream=True).raw).resize((100,150))
            im10 = Image.open(requests.get(data3.image[9], stream=True).raw).resize((100,150))

            with col1:
                b1 = st.image(im1, width=120)
                st.markdown(data3.brand[0])
                b6 = st.image(im6, width=120)
                st.markdown(data3.brand[5])
            with col2:
                b2 = st.image(im2, width=120) 
                st.markdown(data3.brand[1])
                b7 = st.image(im7, width=120)
                st.markdown(data3.brand[6])
            with col3:
                b3 = st.image(im3, width=120)
                st.markdown(data3.brand[2])
                b8 = st.image(im8, width=120)
                st.markdown(data3.brand[7])
            with col4:
                b4 = st.image(im4, width=120)
                st.markdown(data3.brand[3])
                b9 = st.image(im9, width=120)
                st.markdown(data3.brand[8])
            with col5:
                b5 = st.image(im5, width=120)
                st.markdown(data3.brand[4])
                b10 = st.image(im10, width=120)
                st.markdown(data3.brand[9])
          
        elif any([i != " " for i in soru_list2]):
            for m in soru_list2:
                if m == " ":
                    pass
                else:
                    m_index = soru_list2.index(m)
                    len_lst1.append(soru_list1[m_index])
                    len_lst2.append(m)

                    for k in range(0,len(len_lst2)):
                        dataf = dataf[dataf[len_lst1[k]] == len_lst2[k]]

            if len(dataf) == 0:
                st.title("Seçilen Kriterlere Uygun Bir Ürün Bulunamadı")

            elif len(dataf) == 1:
                st.title("Seçilen Kriterlere Uygun Bir Ürün Bulundu")
                dataf = dataf.reset_index()
                im1 = Image.open(requests.get(dataf.image[0], stream=True).raw).resize((100,150))
                b1 = st.image(im1, width=120)
                st.title(dataf.brand[0])
                st.title("Fiyat")
                st.title(dataf.price[0])

            elif len(dataf) == 2:
                st.title("Seçilen Kriterlere Uygun İki Ürün Bulundu")
                col1, col2 = st.columns([1,1])
                dataf = dataf.reset_index()
                im1 = Image.open(requests.get(dataf.image[0], stream=True).raw).resize((100,150))
                im2 = Image.open(requests.get(dataf.image[1], stream=True).raw).resize((100,150))
                with col1:
                    b1 = st.image(im1, width=120)
                    st.title(dataf.brand[0])
                    st.title("Fiyat")
                    st.title(dataf.price[0])
                with col2:
                    b2 = st.image(im2, width=120)
                    st.title(dataf.brand[1])
                    st.title("Fiyat")
                    st.title(dataf.price[1])


            elif len(dataf) == 3:
                st.title("Seçilen Kriterlere Uygun Üç Ürün Bulundu")
                col1, col2, col3 = st.columns([1,1,1])
                dataf = dataf.reset_index()
                im1 = Image.open(requests.get(dataf.image[0], stream=True).raw).resize((100,150))
                im2 = Image.open(requests.get(dataf.image[1], stream=True).raw).resize((100,150))
                im3 = Image.open(requests.get(dataf.image[2], stream=True).raw).resize((100,150))

                with col1:
                    b1 = st.image(im1, width=120)
                    st.title(dataf.brand[0])
                    st.title("Fiyat")
                    st.title(dataf.price[0])
                with col2:
                    b2 = st.image(im2, width=120)
                    st.title(dataf.brand[1])
                    st.title("Fiyat")
                    st.title(dataf.price[1])
                with col3:
                    b3 = st.image(im3, width=120)
                    st.title(dataf.brand[2])
                    st.title("Fiyat")
                    st.title(dataf.price[2])


            elif len(dataf) >3:
                st.title("Seçilen Kriterlere En Uygun Ürünler")
                ucuz = dataf.sort_values(by="price", ascending=True).reset_index()
                fp1 = dataf[dataf["puan"] > dataf["puan"].quantile(0.25)].sort_values(by="puan", ascending=False).reset_index()
                fp1 = fp1.drop(["index"],axis=1)
                fp2 = fp1[fp1["price"] <dataf["price"].quantile(0.75)].sort_values(by="puan", ascending=False).reset_index()
                fp2 = fp2.drop(["index"],axis=1)
                fp3 = fp2.sort_values(by="puan", ascending=False).reset_index()
                fp3 = fp3.drop(["index"],axis=1)
                if len(fp3.puan) == 2:
                    col1, col2 = st.columns([1,1])
                    im1 = Image.open(requests.get(ucuz.image[0], stream=True).raw).resize((100,150))
                    im2 = Image.open(requests.get(fp3.image[0], stream=True).raw).resize((100,150))
                    im3 = Image.open(requests.get(fp3.image[1], stream=True).raw).resize((100,150))

                    with col1:
                        b1 = st.image(im1, width=120)
                        b2 = st.image(im2, width=120)
                        b3 = st.image(im3, width=120)
                    with col2:
                        st.title("En Ucuz")
                        st.markdown("Ürün Adı : " + ucuz.full_name[0], unsafe_allow_html=True)
                        st.markdown("Fiyat : " + str(ucuz.price[0]))

                        st.title("Fiyat Performans")
                        st.markdown("Ürün Adı : " + fp3.full_name[0] )
                        st.markdown("Fiyat : " + str(fp3.price[0]) )
                        st.title(" ")
                        st.title("Çok Satılan")
                        st.markdown("Ürün Adı : " + fp3.full_name[1] )
                        st.markdown("Fiyat : " + str(fp3.price[1]) )
                elif len(fp3.puan) == 1:
                    col1, col2 = st.columns([1,1])
                    im1 = Image.open(requests.get(ucuz.image[0], stream=True).raw).resize((100,150))
                    im2 = Image.open(requests.get(fp3.image[0], stream=True).raw).resize((100,150))
                    im3 = Image.open(requests.get(fp1.image[0], stream=True).raw).resize((100,150))

                    with col1:
                        b1 = st.image(im1, width=120)
                        b2 = st.image(im2, width=120)
                        b3 = st.image(im3, width=120)
                    with col2:
                        st.title("En Ucuz")
                        st.markdown("Ürün Adı : " + ucuz.full_name[0], unsafe_allow_html=True)
                        st.markdown("Fiyat : " + str(ucuz.price[0]))

                        st.title("Fiyat Performans")
                        st.markdown("Ürün Adı : " + fp3.full_name[0] )
                        st.markdown("Fiyat : " + str(fp3.price[0]) )
                        st.title(" ")
                        st.title("Çok Satılan")
                        st.markdown("Ürün Adı : " + fp1.full_name[0] )
                        st.markdown("Fiyat : " + str(fp1.price[0]) )
                        
                elif len(fp3.puan) > 2:
                    col1, col2 = st.columns([1,1])
                    im1 = Image.open(requests.get(ucuz.image[0], stream=True).raw).resize((100,150))
                    im2 = Image.open(requests.get(fp3.image[0], stream=True).raw).resize((100,150))
                    im3 = Image.open(requests.get(fp1.image[0], stream=True).raw).resize((100,150))

                    with col1:
                        b1 = st.image(im1, width=120)
                        b2 = st.image(im2, width=120)
                        b3 = st.image(im3, width=120)
                    with col2:
                        st.title("En Ucuz")
                        st.markdown("Ürün Adı : " + ucuz.full_name[0], unsafe_allow_html=True)
                        st.markdown("Fiyat : " + str(ucuz.price[0]))

                        st.title("Fiyat Performans")
                        st.markdown("Ürün Adı : " + fp3.full_name[0] )
                        st.markdown("Fiyat : " + str(fp3.price[0]) )
                        st.title(" ")
                        st.title("Çok Satılan")
                        st.markdown("Ürün Adı : " + fp3.full_name[1] )
                        st.markdown("Fiyat : " + str(fp3.price[1]) )

                        
                        
                        
                        
    elif machine =="Bulaşık Makinesi":
        capacity_options = [' ','Düşük Kapasite','Orta Kapasite', 'Yüksek Kapasite']
        capacity_help = '''Düşük kapasite: 12 Kişilik ve Altı , Orta Kapasite: 13 Kişilik, Yüksek Kapasite: 14 Kişilik ve Üstü'''.strip()
        capacity = st.sidebar.selectbox('Almak istediğiniz bulaşık makinesinin kapasitesi ne kadar olmalı?',options=capacity_options,help=capacity_help)

        type_options = [' ',"Solo","Ankastre"]
        type_help = '''Kullanım Tipi'''.strip(",")
        type_ = st.sidebar.selectbox('Almak istediğiniz bulaşık makinesinin kullanım tipi nasıl olmalı?',options=type_options,help=type_help)

        size_options = [' ',"Küçük boyut","Standart Boyut","Standard üstü"]
        size = st.sidebar.selectbox('Almak istediğiniz bulaşık makinesinin büyüklüğü ne kadar olmalı?',options=size_options)

        energy_usage_options = [' ','Çok önemli', 'Önemli', 'Az önemli', 'Önemsiz']
        energy_usage_help = '''Çok Önemli: A+++ A++, Önemli : A+ A, Az Önemli: B C, Önemsiz: D E F G)'''.strip()
        energy_usage = st.sidebar.selectbox('Almak istediğiniz bulaşık makinesinin tükettiği enerji miktarı sizin için önemli mi?',options=energy_usage_options,help=energy_usage_help)
                         
        box_options = [' ',"Sepetli","Çekmeceli"]
        box_help = '''Çatal Kaşık Bölmesi Tipi'''.strip(",")
        box = st.sidebar.selectbox('Almak istediğiniz bulaşık makinesinin çatal kaşık bölmesi nasıl olmalı?',options=box_options,help=box_help)

        soru_list = [capacity,type_,size,energy_usage,box]


        soru_list1 = ["capacity","type_","size","energy_usage","box"]
        soru_list2 = [capacity,type_,size,energy_usage,box]
        
        if all([i == " " for i in soru_list2]):
            st.title('Bakalım sizin için nelerimiz var?')
            col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1])
            data2_b = data2_b[data2_b.image != "YOK"]
            data3 = data2_b.sample(frac=1).drop_duplicates(['brand']).sample(10).reset_index()
            im1 = Image.open(requests.get(data3.image[0], stream=True).raw).resize((100,150))
            im2 = Image.open(requests.get(data3.image[1], stream=True).raw).resize((100,150))
            im3 = Image.open(requests.get(data3.image[2], stream=True).raw).resize((100,150))
            im4 = Image.open(requests.get(data3.image[3], stream=True).raw).resize((100,150))
            im5 = Image.open(requests.get(data3.image[4], stream=True).raw).resize((100,150))
            im6 = Image.open(requests.get(data3.image[5], stream=True).raw).resize((100,150))
            im7 = Image.open(requests.get(data3.image[6], stream=True).raw).resize((100,150))
            im8 = Image.open(requests.get(data3.image[7], stream=True).raw).resize((100,150))
            im9 = Image.open(requests.get(data3.image[8], stream=True).raw).resize((100,150))
            im10 = Image.open(requests.get(data3.image[9], stream=True).raw).resize((100,150))

            with col1:
                b1 = st.image(im1, width=120)
                st.markdown(data3.brand[0])
                b6 = st.image(im6, width=120)
                st.markdown(data3.brand[5])
            with col2:
                b2 = st.image(im2, width=120) 
                st.markdown(data3.brand[1])
                b7 = st.image(im7, width=120)
                st.markdown(data3.brand[6])
            with col3:
                b3 = st.image(im3, width=120)
                st.markdown(data3.brand[2])
                b8 = st.image(im8, width=120)
                st.markdown(data3.brand[7])
            with col4:
                b4 = st.image(im4, width=120)
                st.markdown(data3.brand[3])
                b9 = st.image(im9, width=120)
                st.markdown(data3.brand[8])
            with col5:
                b5 = st.image(im5, width=120)
                st.markdown(data3.brand[4])
                b10 = st.image(im10, width=120)
                st.markdown(data3.brand[9])
          
        elif any([i != " " for i in soru_list2]):
            for m in soru_list2:
                if m == " ":
                    pass
                else:
                    m_index = soru_list2.index(m)
                    len_lst1.append(soru_list1[m_index])
                    len_lst2.append(m)

                    for k in range(0,len(len_lst2)):
                        dataf_b = dataf_b[dataf_b[len_lst1[k]] == len_lst2[k]]

            if len(dataf_b) == 0:
                st.title("Seçilen Kriterlere Uygun Bir Ürün Bulunamadı")

            elif len(dataf_b) == 1:
                st.title("Seçilen Kriterlere Uygun Bir Ürün Bulundu")
                dataf_b = dataf_b.reset_index()
                im1 = Image.open(requests.get(dataf_b.image[0], stream=True).raw).resize((100,150))
                b1 = st.image(im1, width=120)
                st.title(dataf_b.brand[0])
                st.title("Fiyat")
                st.title(dataf_b.price[0])

            elif len(dataf_b) == 2:
                st.title("Seçilen Kriterlere Uygun İki Ürün Bulundu")
                col1, col2 = st.columns([1,1])
                dataf_b = dataf_b.reset_index()
                im1 = Image.open(requests.get(dataf_b.image[0], stream=True).raw).resize((100,150))
                im2 = Image.open(requests.get(dataf_b.image[1], stream=True).raw).resize((100,150))
                with col1:
                    b1 = st.image(im1, width=120)
                    st.title(dataf_b.brand[0])
                    st.title("Fiyat")
                    st.title(dataf_b.price[0])
                with col2:
                    b2 = st.image(im2, width=120)
                    st.title(dataf_b.brand[1])
                    st.title("Fiyat")
                    st.title(dataf_b.price[1])


            elif len(dataf_b) == 3:
                st.title("Seçilen Kriterlere Uygun Üç Ürün Bulundu")
                col1, col2, col3 = st.columns([1,1,1])
                dataf_b = dataf_b.reset_index()
                im1 = Image.open(requests.get(dataf_b.image[0], stream=True).raw).resize((100,150))
                im2 = Image.open(requests.get(dataf_b.image[1], stream=True).raw).resize((100,150))
                im3 = Image.open(requests.get(dataf_b.image[2], stream=True).raw).resize((100,150))

                with col1:
                    b1 = st.image(im1, width=120)
                    st.title(dataf_b.brand[0])
                    st.title("Fiyat")
                    st.title(dataf_b.price[0])
                with col2:
                    b2 = st.image(im2, width=120)
                    st.title(dataf_b.brand[1])
                    st.title("Fiyat")
                    st.title(dataf_b.price[1])
                with col3:
                    b3 = st.image(im3, width=120)
                    st.title(dataf_b.brand[2])
                    st.title("Fiyat")
                    st.title(dataf_b.price[2])


            elif len(dataf_b) >3:
                st.title("Seçilen Kriterlere En Uygun Ürünler")
                ucuz = dataf_b.sort_values(by="price", ascending=True).reset_index()
                fp1 = dataf_b[dataf_b["puan"] > dataf_b["puan"].quantile(0.25)].sort_values(by="puan", ascending=False).reset_index()
                fp1 = fp1.drop(["index"],axis=1)
                fp2 = fp1[fp1["price"] <dataf_b["price"].quantile(0.75)].sort_values(by="puan", ascending=False).reset_index()
                fp2 = fp2.drop(["index"],axis=1)
                fp3 = fp2.sort_values(by="puan", ascending=False).reset_index()
                fp3 = fp3.drop(["index"],axis=1)
                if len(fp3.puan) == 2:
                    col1, col2 = st.columns([1,1])
                    im1 = Image.open(requests.get(ucuz.image[0], stream=True).raw).resize((100,150))
                    im2 = Image.open(requests.get(fp3.image[0], stream=True).raw).resize((100,150))
                    im3 = Image.open(requests.get(fp3.image[1], stream=True).raw).resize((100,150))

                    with col1:
                        b1 = st.image(im1, width=120)
                        b2 = st.image(im2, width=120)
                        b3 = st.image(im3, width=120)
                    with col2:
                        st.title("En Ucuz")
                        st.markdown("Ürün Adı : " + ucuz.full_name[0], unsafe_allow_html=True)
                        st.markdown("Fiyat : " + str(ucuz.price[0]))

                        st.title("Fiyat Performans")
                        st.markdown("Ürün Adı : " + fp3.full_name[0] )
                        st.markdown("Fiyat : " + str(fp3.price[0]) )
                        st.title(" ")
                        st.title("Çok Satılan")
                        st.markdown("Ürün Adı : " + fp3.full_name[1] )
                        st.markdown("Fiyat : " + str(fp3.price[1]) )
                elif len(fp3.puan) == 1:
                    col1, col2 = st.columns([1,1])
                    im1 = Image.open(requests.get(ucuz.image[0], stream=True).raw).resize((100,150))
                    im2 = Image.open(requests.get(fp3.image[0], stream=True).raw).resize((100,150))
                    im3 = Image.open(requests.get(fp1.image[0], stream=True).raw).resize((100,150))

                    with col1:
                        b1 = st.image(im1, width=120)
                        b2 = st.image(im2, width=120)
                        b3 = st.image(im3, width=120)
                    with col2:
                        st.title("En Ucuz")
                        st.markdown("Ürün Adı : " + ucuz.full_name[0], unsafe_allow_html=True)
                        st.markdown("Fiyat : " + str(ucuz.price[0]))

                        st.title("Fiyat Performans")
                        st.markdown("Ürün Adı : " + fp3.full_name[0] )
                        st.markdown("Fiyat : " + str(fp3.price[0]) )
                        st.title(" ")
                        st.title("Çok Satılan")
                        st.markdown("Ürün Adı : " + fp1.full_name[0] )
                        st.markdown("Fiyat : " + str(fp1.price[0]) )
                        
                elif len(fp3.puan) > 2:
                    col1, col2 = st.columns([1,1])
                    im1 = Image.open(requests.get(ucuz.image[0], stream=True).raw).resize((100,150))
                    im2 = Image.open(requests.get(fp3.image[0], stream=True).raw).resize((100,150))
                    im3 = Image.open(requests.get(fp1.image[0], stream=True).raw).resize((100,150))

                    with col1:
                        b1 = st.image(im1, width=120)
                        b2 = st.image(im2, width=120)
                        b3 = st.image(im3, width=120)
                    with col2:
                        st.title("En Ucuz")
                        st.markdown("Ürün Adı : " + ucuz.full_name[0], unsafe_allow_html=True)
                        st.markdown("Fiyat : " + str(ucuz.price[0]))

                        st.title("Fiyat Performans")
                        st.markdown("Ürün Adı : " + fp3.full_name[0] )
                        st.markdown("Fiyat : " + str(fp3.price[0]) )
                        st.title(" ")
                        st.title("Çok Satılan")
                        st.markdown("Ürün Adı : " + fp3.full_name[1] )
                        st.markdown("Fiyat : " + str(fp3.price[1]) )
            
if dil_secenek == "EN":
    if machine ==" ":
        col1, col2, col3, col4, col5,col6,col7,col8,col9,col10,col11,col12 = st.columns([1,1,1,1,1,1,1,1,1,1,1,5])



        with col12:
            
            if dil_secenek == "EN":
                button = st.button("Like 👍")
                if button:
                    st.write("Appreciated 💗")
                    file1 = open("counter.txt","r")
                    count = file1.read()
                    count_int = count.replace("'","")
                    count_int = int(count_int) + 1
                    with open('counter.txt', 'w') as f:
                        f.write(str(count_int))
        st.title("About")

        st.markdown("With <b><i> Customer Recommendation Project</i></b>, we aim to help consumers choose best white goods for them.", unsafe_allow_html=True)

        st.markdown("People expect the e-commerce websites they engage with to remember who they are and what they’re interested in, and make relevant, individualized, and accurate recommendations for new content and new products based on their previous activities. Any app or website that fails to deliver on these demands will quickly see its users flocking out the digital door.")

        st.markdown("Customer recommendation system is a software tool designed to generate and provide suggestions for items or content a specific user would like to purchase or engage with based on their needs.")

        st.markdown(" ")
        st.title("Project Developers")
        st.markdown(" ")
        col1, col2, col3, col4, col5,col6,col7 = st.columns([1,1,1,1,1,1,1])

        with col1:
            st.markdown("<b><i>Mert Türkyılmaz</i></b>", unsafe_allow_html=True)
            st.markdown("[![Foo](data:image/png;base64,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)](https://www.linkedin.com/in/mertturkyilmaz/)")
            st.markdown("[![Foo](data:image/png;base64,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)](https://github.com/mertturkyilmaz)")

        with col4:
            st.markdown("<b><i>Sarper Yılmaz</i></b>", unsafe_allow_html=True)
            st.markdown("[![Foo](data:image/png;base64,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)](https://www.linkedin.com/in/sarperyilmaz/)")
            st.markdown("[![Foo](data:image/png;base64,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)](https://github.com/sarperyilmaz)")
        with col7:
            st.markdown("<b><i>Doğukan Doğru</i></b>", unsafe_allow_html=True)
            st.markdown("[![Foo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAAAXNSR0IArs4c6QAAEWtJREFUaEPVWXl019WV/3zuNyF7AgFCAgmIyhoWBRcCilqhajvWDeiMSyuIOi1dXOrYOq069rTO6bRje7pbDNa6VMClteJSC1XZBBTZt0QgCSQkIRASyPq9nzkvUQ4JUJdO/+g7h3M437zfe+/z7r2fe+/nEf/kg//k58c/FMAtL6xJbW9uuwCmooYYD2ZGNg2u/q62YkNCHB3o0fDwrWe1/T2X+P8O4Kb5y89pS4hKo9hvE5lEoMSEBFFXOxSb+BhMfQnbH8Vtr8eWMDaOsOHRq4p2fRIgnxjArD8szVBbNJNCdoLai9uYcDMN7QRiCec6vJaKKgkNh5AjQwkdo2H6vYAKgBNNOCJgfYP0bF+0RA0JPVJ/d/Wk6o8D5GMDuP9+WdnoFTMVczYjbJE0mFSC3P5q9N6C9SbQKikZxFCSqyANk9sRmL8AcKyEmSR+ASgCsFvA5yH2AfGTedOKHvqHAZg+f36UYfkvgFaDGP1EXUjDk3TUyDBQMdJItIsaCHAbnamghot4DcB7dE6GxSMFWyEoj87+MLWA1mqKF0sBJBLN8frc6UV//ShAPrIFvjB/+YAE41fdcboZPgvgHQjvwpgOVwagLICtoNQB0L3IxfUW4U+SCgG7HK7tZnIXz5C42+jtIPoAWAm3QTDvKdmvYVqHKKpJjGz/w5efdeRvAflIAGYuWP4vlN0k+lnhhkF7Q5II9hA03KAyd2aaYY8cwxxsoukZgqmS/l2GfRbzgOhnEDgE49sQCgFVCDwAcLzkJSRySTYiRptMCQSa0lIPXvXTz3ym5WQgPhTATQtXXC4pMMoZAF42eAS3DBkKCB1050EaGwHvKWCgga8K2ALgxuD7MG50aSCBfDiXEkgPLCTYYoMPcWE8yVSHdhpY6dJgI3pL9qM44o8SY01Vj/Y3iq84b++JQJwUwA2PrUtLSD1yCxyX01ADMAY0SpCFhQxc60BMKQ3AOJi9DfgrEIskXE9qm5PNJhVKrO2wgjBG8ldBa6QwRUA7qXSB7XSUyjACjo2MuBCODTKdYa6dIk6h45FHZkys6w7ipABmLVx+F8mhilnwfuAJUhLNXoHUkp3So399S9uouB1rEWGpHIF9viSL2+lcD6BA4EBSlQCyBVYb/M+AfVpANhC+sy+kwD5HHKgmbAngRQTaBNQBlmfCXNDrCjYWPXr//fSPBODL85ekN0UpPwQwRu6nGJkgaDdg60/LTu1/89lDJuekJ6e2xd76Rmn14ic27CwAMJTOd52qNvIcQT0BNhBIAfQ7OvPdNJViKYiQfYcASAbQLPDJQKmEzpaQCTKV0CGAiYLeMkbFUY9oCZqQ+PCMs+qPBXFCC8xcsGK2DDebMASSA3zDDUcsZtr3Lx1zSb+MlJQPFpGAB/+6sa60tnELTL0AnI6O22OSS8tJ7uyMB+wXtc2AfImnkUiC4zVG2CVpIoR+IDKkQGOqM6AHwKdBlodgFvzfKL7+yPSiu08KICSp8sIV14j8jqBCkWtM2EUoycGBOek91vz3JeNu7m7G5zdV1L+wtewQZIc79u+IET0r8HLIBsqwhe5Nwa1ADCJY7sBSOkaKGECi3/trRgj0Jm6iYbGEDdbJdPdBWC9y9bzpE+45OYAlSxIqDqRcJPc5DuTT2YyAni7SXo7Mxv7sc2dd2yOyhGMXefydnWsXl+6roPkwKFoEem+E7ArsFa2S7n1A5ndSLxY5kUlxFKmQA0JgZgBMk9BAYj7EBkBrAFwv4nQDVgrcZM6nPamtJcGSD36QH45zoRsXvHW+QX+EtEadLrGEChkVfRzq+enT88791zGDssjOn+491LTv/r+sL4kdZZC2g/gyoFRAe+TW2nHjRAboSxFHtbB4vGQ9CYW/lQgcwhDkjhcYoTZkddAzXPwiwAjCchiLCV0IoFbQunnTJj71wQV2AXDDs8tyEhX9j2IVEKwHtQ7mF0O2V9BpEEYA7DE8J2PLmXnZVt3QrDd3V9e1O54VdRWEC4LFAJSEYCQxKPA7hM0EzgLYk4QArwHsIIBcOfaZ+Zvuli/z/aboSsCzRByCsxyGTAgicUjA0xA3ktGG4mlnvxdAdAEwe+HKMS7MFNQow2CTst15xAxDQ5CJKodUBzJYpjG4A8E8h75CMJFAqZPVVJwPMIvAOoflAB4YJ2zWBFmbqFoIqSRegjBADOW1cgArELSGbvtp6OdSL0KlJAe5o4zkEhH71ND02KMzLwru3RVAoM+WKPk2l64lsKYj49KLjGyMpa0Ue6clRa0JCbbWiIrm1niOwFPa4rgqlvZQyDRjdkpiwgEQLRCGC4ia27wl9jgO1iPRIGJpsqGhJcZlgFoA5nZmYiyScyBMpxNsd6mMwNiwBs12USoHUFU8rejrXV1I4qxnV8yCcDOhdxxspfNCGU4TsTmKUetAyuBeaQ3fmTL6c91Z6NXtlYee3hD6EbYU9s1qumPyiIHHzvnxsi2H9hxqzrxyxIC6MXm9ElMTo/TIjM1t7dp98HC8qbr+Ly9uqdwCabJTeWbc7jFppvfJQv0BbhSU3mF1RpsfuebcF49aYPr85SnpxMXWETAoFjgR8GaIOyTmkNhB8vVTs9PH3XNR4Re6A3h5e2XT/PW7D1CoGd4vc8Bdk0cGdjk6nt9c0XTZ0LyEpIQo8WRF2YqymubfrC7Z2ZmFLcngWwEb5FIOobyQ/AQuBANDAZHwi7nTJqw/GgOzn1k5weU/BnCmhAMdGxFbKFsMqo8cnyromVr/X1PHTOp+iMUlVfueWLerVML4UblZe+84b8TgY+c44BZSw4eMX7+1/eCqsro1IBooJMFCZas+cG4h0CjTAABHAM6ZN63oraMW+NITb/ZqSYreIfmaS9MB7CD0BmTJYKAvbiRceRnpI7776TFjjnOhHZUHf79uVwtgxePyek3+yqShx4H84DfucLMTg9lcfbDyh29sXt05l1MobpJxA4BJgFJIL4PsIIEdh7z8rgUzZsQdFrhx4fLh5q6BfdtKy/enhCzcE/RxUGAW7nBoPJz1+T1TMh6YOrawO4DVFbWrfrWy5E1QNxf2y6q947yRp3afs3Zv3YFF2yt/UFrTcEVuZsrI2WefmnZqdkZoKY+Oprb25q+8sGY9xR6ANop+CmSFEPaB2glnPzesQkPz7cexUOi4ItocWnw+QqsnvidjATvSp6ogDs3LSE783iVn9O1+uD+XVO1/at2uA4Be/NTg3MTrxw3+8rFzmtviw7e/+Pa81tiv62B0ug3ITKt6YOqYod3X+tof1jx/pL2tt4Ph4M2g9sIZOreOZorUTXGcsPjRGedUHXWh8J+ZC1ecS2gOgPHvLzpIsAoiTu3gZ3LFoMyU5vumjLmo+6bLdtdsfGRNyQKK7aPzel5726ThXay0qry2/lerSoK5KWA/oHoC7Q99dvzozOQeqceud+eid+oPNLVGhIdOLfwLlS4kNFGoQoTtov1m3tXnLu4CYNaCld8B/EbR2oK/gZ5KWR9BWwiWij6hX2pK7wcvPfO48mP93rrFP1m+LdTvU4b2zUi6+4KRR6vVsMlL2/YcWbix/AActTDUSn4YFvX91uQR5wzpk9nFje55eW31vsNNByVLB5BDeqXEHoQlSVrLiLWQDhVPK5p9FMD0+Rt7ZFjDLxysI3GeoMiEFHdsN2AwTKMgVAzISjnwwNQzPrDQ0Yt7dUdl/dPrdzfKcWB8fq/aOUXDQt1ydPxpa8X+5zZUbCVQL0MSwd6AMu6bMjqxICutS8749ivrqiobm3IltJBeTUT7JU8j9VrslmOm8Qa7IlDoUQCdIlXCFQaNix2hizqPxiUunWuCQCUK1is/K2XnA1PGju7uQq+VVNU8uW7nmwQGDOubOfY/JheGRuXoeHFrRe1zm/ZUiNgB12gSayT0uf384ZeO6tezy3IBQFVj0+GY2G+S4Ewm8ZSEGSBSRTyemJT40Amr0SALxsS9JFpE5lsMwjRWYBXIl0b0yWi8a/LIO7sDeP29fbt/+87O3PC9sF9mzZ3nj8zvZoGa5zaVvxeCMSh0AK4JddG9F49uGdQzrcvc/3x1bXlVQxMkc6M/7mA6wBsovA5yFeGvPDJt4toP1u/iz0GM9db20Hj/AGB/l/JothDwtS7rX5CZMuWBqWPO7A7gxW178OyG8q2h6yrM7Vlwx/nDu7jFi1v31Dy7qXyJoNEEBwN6LEguX5807LrRub26nCFYYE9j0/ORWOrQ7aRaAfs1iBGUJon8ZfE1E350QgCzFqy4jOQEwW+D8CrMVkJxf8CGCsrNTU8Z/f1Lzkg63gLVO3+7tnR/uOGR/TIKvjG5MGTMo2PRtj2Vz2woy4XxaUi7Qs0loOmBqWPi/Ky0QcfO/fHSbd/euK/uEgcDW/wcQqiHbgiND+lLHrlm4hwwkFnn6IJ+1sLVp9LbDBH7CcqRcM/7Yu2AIGKNzM0svvO8kd88DkBphwtVkhoyOq9XVXcafWVH5c75G8p+jlg3hAIRwKNBqbhj0vDPj8rt2YWFvvny2vbqwy1PgNhM4Wsh2OV824xveoLNnXflOaEiPTqOo8RO/bPgexBvBdQaJBARc43Y3D8t9RvfvWRMF/cIKwUW+v263aHWaRiWk5Fz9+TCLi3n4veqNjyxdtdIAY+bsM+pWwm2fuvCUdHpvdOzjz3QQ8u23rdh78HLaKGMZhng7QRXAvDiaybceuztH2eB8OGmZ1beAMXDxGgo5U+KdhVcl4pKys9KrXpgythhJ4qBZzaUh342YWifjJS7L+habfx5R1XJU+t3/VTEdUHoCoo0gLcfvPTMcTlpyV0mf+vld9uqDzftDworiGQCjwdVpMEznl8wY1Rr971PKKvcNH95ttO+IaqXQVeG7ElgWSKZl5OeMsSBqN19sIGHQ3pvbG2vb2hpD11VelJi9PiQ7MySmqaWWyC1Z6cmPVbZ2JRx4HDrVaLcnHtlehXgqVnJiVfmZiTPc9Hqm1pnU2qobW5RHKMXoJrQixi5J6m5/c5fXnd+Z4XcbZxUmevQRIlToNBMBAPamTLPhzgwtJwkqwgkKLR9ZD7Bd0UVK8ZVHXUL8L+w0ILyyk5JEocBe4sKva1m0LhM0lJKX5cpk0KdxECpDSBb2LnH8giJ9z58zVlB3TvhOCmAW55c06c9OR7A2K916jCF6zuaCoXGPFBbR32SA9MRk/1OwABB09jRdOAlQKci5qWdYhUqzXyrwyYE0B1BLH0W5EQ4toEIDQsBxep86GimUCHyoXnTJjx8ssOfMAaOnXzj/FW5iNoKTHZvKG/jSHOt3f4S9ByJTmg1aPsABSWhPPA1wSxJIVtPCiIAxTIQiYCPBbAAsAxBNxLcGoRigqH0bpTQK8QQoEMElrQ55jw2Y+Kev3X4DwUQJsxcsHImIu6GvC9jzgR1BMQ5oTBT5AMoSyPwDIAa0c+GWx+RpGMXTBVOjKZUEV5oIE7v0INM++Q2lkQzoCSAmYLqg6BrwFYz3jn36qIg0X/o+ND3gbDC7PlvDUaSjrS3ea9Ei1yuZAc+I3S0eNmSLjKqPYi5Luw0BjmSWbFzoBHvkD7ewUGQbyOsIKgQoO99/12sd3joo0MifzZv2rmPdqfKT+xC3X/Y+WZw+HN07YoSEvbH7rNc+oIRaQT/GDNsrRR6qOFZ51AjTONCi2rO0EiOFVkCeSbRUSAepocXH6yW2u6fN2NyzYde+UdloRMt9NVFi5J6r7qs7f77oFkL3npJ1HAQy2j2A3r79MBU3vHuZQUdIhbR5jFqaRpJoRJiEoghnW7IlZ1g7btzZ0x4++Me/IP5H8mFui/eIYAl9DglZmvFo1dddPCLzy07zeLoYoOvdtrPCb0CaD3AfLlPoUUHIR8W+msJ+yQWN6JsW2jKP+nB/y4A3TedNX/psOIZ520L30M9BcWnk14Tyt6ZC1Ze0aiyP6UgP/ejsMrHBfSJLPBxN/lHzv+nB/B/jzziqZ3jZRgAAAAASUVORK5CYII=)](https://www.linkedin.com/in/do%C4%9Fukando%C4%9Fru/)")
            st.markdown("[![Foo](data:image/png;base64,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)](https://github.com/dogudogru)")
            
    elif machine =="Çamaşır Makinesi":
        with st.sidebar:
            capacity_options = [' ','Düşük Kapasite','Orta Kapasite', 'Yüksek Kapasite']
            capacity_help = '''Düşük kapasite: 0-6 KG , Orta Kapasite: 7-10 KG, Yüksek Kapasite: 10+ KG'''.strip()
            capacity = st.sidebar.selectbox('Almak istediğiniz çamaşır makinesinin kapasitesi ne kadar olmalı?',options=capacity_options,help=capacity_help)

            cycle_options = [' ',"Düşük Devir","Orta Devir","Yüksek Devir"]
            cycle_help = '''Düşük devir: 1000'e kadar, 
            Orta devir: 1000 - 1200, 
            Yüksek Kapasite: 1200+'''.strip(",")
            cycle = st.sidebar.selectbox('Almak istediğiniz çamaşır makinesinin devir sayısı ne olmalı?',options=cycle_options,help=cycle_help)

            size_options = [' ',"Küçük boyut","Standart Boyut","Standard üstü"]
            size = st.sidebar.selectbox('Almak istediğiniz çamaşır makinesinin büyüklüğü ne kadar olmalı?',options=size_options)

            energy_usage_options = [' ','Çok önemli', 'Önemli', 'Az önemli', 'Önemsiz']
            energy_usage_help = '''Çok Önemli: A+++ A++, Önemli : A+ A, Az Önemli: B C, Önemsiz: D E F G)'''.strip()
            energy_usage = st.sidebar.selectbox('Almak istediğiniz çamaşır makinesinin tükettiği enerji miktarı sizin için önemli mi?',options=energy_usage_options,help=energy_usage_help)

            soru_list = [capacity,cycle,size,energy_usage]


            soru_list1 = ["capacity","cycle","size","energy_usage"]
            soru_list2 = [capacity,cycle,size,energy_usage]
                
        
        if all([i == " " for i in soru_list2]):
            st.title('Bakalım sizin için nelerimiz var?')
            col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1])
            data3 = data2.sample(frac=1).drop_duplicates(['brand']).sample(10).reset_index()
            im1 = Image.open(requests.get(data3.image[0], stream=True).raw).resize((100,150))
            im2 = Image.open(requests.get(data3.image[1], stream=True).raw).resize((100,150))
            im3 = Image.open(requests.get(data3.image[2], stream=True).raw).resize((100,150))
            im4 = Image.open(requests.get(data3.image[3], stream=True).raw).resize((100,150))
            im5 = Image.open(requests.get(data3.image[4], stream=True).raw).resize((100,150))
            im6 = Image.open(requests.get(data3.image[5], stream=True).raw).resize((100,150))
            im7 = Image.open(requests.get(data3.image[6], stream=True).raw).resize((100,150))
            im8 = Image.open(requests.get(data3.image[7], stream=True).raw).resize((100,150))
            im9 = Image.open(requests.get(data3.image[8], stream=True).raw).resize((100,150))
            im10 = Image.open(requests.get(data3.image[9], stream=True).raw).resize((100,150))

            with col1:
                b1 = st.image(im1, width=120)
                st.markdown(data3.brand[0])
                b6 = st.image(im6, width=120)
                st.markdown(data3.brand[5])
            with col2:
                b2 = st.image(im2, width=120) 
                st.markdown(data3.brand[1])
                b7 = st.image(im7, width=120)
                st.markdown(data3.brand[6])
            with col3:
                b3 = st.image(im3, width=120)
                st.markdown(data3.brand[2])
                b8 = st.image(im8, width=120)
                st.markdown(data3.brand[7])
            with col4:
                b4 = st.image(im4, width=120)
                st.markdown(data3.brand[3])
                b9 = st.image(im9, width=120)
                st.markdown(data3.brand[8])
            with col5:
                b5 = st.image(im5, width=120)
                st.markdown(data3.brand[4])
                b10 = st.image(im10, width=120)
                st.markdown(data3.brand[9])
          
        elif any([i != " " for i in soru_list2]):
            for m in soru_list2:
                if m == " ":
                    pass
                else:
                    m_index = soru_list2.index(m)
                    len_lst1.append(soru_list1[m_index])
                    len_lst2.append(m)

                    for k in range(0,len(len_lst2)):
                        dataf = dataf[dataf[len_lst1[k]] == len_lst2[k]]

            if len(dataf) == 0:
                st.title("Seçilen Kriterlere Uygun Bir Ürün Bulunamadı")

            elif len(dataf) == 1:
                st.title("Seçilen Kriterlere Uygun Bir Ürün Bulundu")
                dataf = dataf.reset_index()
                im1 = Image.open(requests.get(dataf.image[0], stream=True).raw).resize((100,150))
                b1 = st.image(im1, width=120)
                st.title(dataf.brand[0])
                st.title("Fiyat")
                st.title(dataf.price[0])

            elif len(dataf) == 2:
                st.title("Seçilen Kriterlere Uygun İki Ürün Bulundu")
                col1, col2 = st.columns([1,1])
                dataf = dataf.reset_index()
                im1 = Image.open(requests.get(dataf.image[0], stream=True).raw).resize((100,150))
                im2 = Image.open(requests.get(dataf.image[1], stream=True).raw).resize((100,150))
                with col1:
                    b1 = st.image(im1, width=120)
                    st.title(dataf.brand[0])
                    st.title("Fiyat")
                    st.title(dataf.price[0])
                with col2:
                    b2 = st.image(im2, width=120)
                    st.title(dataf.brand[1])
                    st.title("Fiyat")
                    st.title(dataf.price[1])


            elif len(dataf) == 3:
                st.title("Seçilen Kriterlere Uygun Üç Ürün Bulundu")
                col1, col2, col3 = st.columns([1,1,1])
                im1 = Image.open(requests.get(dataf.image[0], stream=True).raw).resize((100,150))
                im2 = Image.open(requests.get(dataf.image[1], stream=True).raw).resize((100,150))
                im3 = Image.open(requests.get(dataf.image[2], stream=True).raw).resize((100,150))

                with col1:
                    b1 = st.image(im1, width=120)
                    st.title(dataf.brand[0])
                    st.title("Fiyat")
                    st.title(dataf.price[0])
                with col2:
                    b2 = st.image(im2, width=120)
                    st.title(dataf.brand[1])
                    st.title("Fiyat")
                    st.title(dataf.price[1])
                with col3:
                    b3 = st.image(im3, width=120)
                    st.title(dataf.brand[2])
                    st.title("Fiyat")
                    st.title(dataf.price[2])


            elif len(dataf) >3:
                st.title("Seçilen Kriterlere En Uygun Ürünler")
                ucuz = dataf.sort_values(by="price", ascending=True).reset_index()
                fp1 = dataf[dataf["puan"] > dataf["puan"].quantile(0.25)].sort_values(by="puan", ascending=False).reset_index()
                fp1 = fp1.drop(["index"],axis=1)
                fp2 = fp1[fp1["price"] <dataf["price"].quantile(0.75)].sort_values(by="puan", ascending=False).reset_index()
                fp2 = fp2.drop(["index"],axis=1)
                fp3 = fp2.sort_values(by="puan", ascending=False).reset_index()
                fp3 = fp3.drop(["index"],axis=1)
                if len(fp3.puan) == 2:
                    col1, col2 = st.columns([1,1])
                    im1 = Image.open(requests.get(ucuz.image[0], stream=True).raw).resize((100,150))
                    im2 = Image.open(requests.get(fp3.image[0], stream=True).raw).resize((100,150))
                    im3 = Image.open(requests.get(fp3.image[1], stream=True).raw).resize((100,150))

                    with col1:
                        b1 = st.image(im1, width=120)
                        b2 = st.image(im2, width=120)
                        b3 = st.image(im3, width=120)
                    with col2:
                        st.title("En Ucuz")
                        st.markdown("Ürün Adı : " + ucuz.full_name[0], unsafe_allow_html=True)
                        st.markdown("Fiyat : " + str(ucuz.price[0]))

                        st.title("Fiyat Performans")
                        st.markdown("Ürün Adı : " + fp3.full_name[0] )
                        st.markdown("Fiyat : " + str(fp3.price[0]) )
                        st.title(" ")
                        st.title("Çok Satılan")
                        st.markdown("Ürün Adı : " + fp3.full_name[1] )
                        st.markdown("Fiyat : " + str(fp3.price[1]) )
                elif len(fp3.puan) == 1:
                    col1, col2 = st.columns([1,1])
                    im1 = Image.open(requests.get(ucuz.image[0], stream=True).raw).resize((100,150))
                    im2 = Image.open(requests.get(fp3.image[0], stream=True).raw).resize((100,150))
                    im3 = Image.open(requests.get(fp1.image[0], stream=True).raw).resize((100,150))

                    with col1:
                        b1 = st.image(im1, width=120)
                        b2 = st.image(im2, width=120)
                        b3 = st.image(im3, width=120)
                    with col2:
                        st.title("En Ucuz")
                        st.markdown("Ürün Adı : " + ucuz.full_name[0], unsafe_allow_html=True)
                        st.markdown("Fiyat : " + str(ucuz.price[0]))

                        st.title("Fiyat Performans")
                        st.markdown("Ürün Adı : " + fp3.full_name[0] )
                        st.markdown("Fiyat : " + str(fp3.price[0]) )
                        st.title(" ")
                        st.title("Çok Satılan")
                        st.markdown("Ürün Adı : " + fp1.full_name[0] )
                        st.markdown("Fiyat : " + str(fp1.price[0]) )
                        
                elif len(fp3.puan) > 2:
                    col1, col2 = st.columns([1,1])
                    im1 = Image.open(requests.get(ucuz.image[0], stream=True).raw).resize((100,150))
                    im2 = Image.open(requests.get(fp3.image[0], stream=True).raw).resize((100,150))
                    im3 = Image.open(requests.get(fp1.image[0], stream=True).raw).resize((100,150))

                    with col1:
                        b1 = st.image(im1, width=120)
                        b2 = st.image(im2, width=120)
                        b3 = st.image(im3, width=120)
                    with col2:
                        st.title("En Ucuz")
                        st.markdown("Ürün Adı : " + ucuz.full_name[0], unsafe_allow_html=True)
                        st.markdown("Fiyat : " + str(ucuz.price[0]))

                        st.title("Fiyat Performans")
                        st.markdown("Ürün Adı : " + fp3.full_name[0] )
                        st.markdown("Fiyat : " + str(fp3.price[0]) )
                        st.title(" ")
                        st.title("Çok Satılan")
                        st.markdown("Ürün Adı : " + fp3.full_name[1] )
                        st.markdown("Fiyat : " + str(fp3.price[1]) )

                        
                        
                        
                        
    elif machine =="Bulaşık Makinesi":
        capacity_options = [' ','Düşük Kapasite','Orta Kapasite', 'Yüksek Kapasite']
        capacity_help = '''Düşük kapasite: 12 Kişilik ve Altı , Orta Kapasite: 13 Kişilik, Yüksek Kapasite: 14 Kişilik ve Üstü'''.strip()
        capacity = st.sidebar.selectbox('Almak istediğiniz bulaşık makinesinin kapasitesi ne kadar olmalı?',options=capacity_options,help=capacity_help)

        type_options = [' ',"Solo","Ankastre"]
        type_help = '''Kullanım Tipi'''.strip(",")
        type_ = st.sidebar.selectbox('Almak istediğiniz bulaşık makinesinin kullanım tipi nasıl olmalı?',options=type_options,help=type_help)

        size_options = [' ',"Küçük boyut","Standart Boyut","Standard üstü"]
        size = st.sidebar.selectbox('Almak istediğiniz bulaşık makinesinin büyüklüğü ne kadar olmalı?',options=size_options)

        energy_usage_options = [' ','Çok önemli', 'Önemli', 'Az önemli', 'Önemsiz']
        energy_usage_help = '''Çok Önemli: A+++ A++, Önemli : A+ A, Az Önemli: B C, Önemsiz: D E F G)'''.strip()
        energy_usage = st.sidebar.selectbox('Almak istediğiniz bulaşık makinesinin tükettiği enerji miktarı sizin için önemli mi?',options=energy_usage_options,help=energy_usage_help)
                         
        box_options = [' ',"Sepetli","Çekmeceli"]
        box_help = '''Çatal Kaşık Bölmesi Tipi'''.strip(",")
        box = st.sidebar.selectbox('Almak istediğiniz bulaşık makinesinin çatal kaşık bölmesi nasıl olmalı?',options=box_options,help=box_help)

        soru_list = [capacity,type_,size,energy_usage,box]


        soru_list1 = ["capacity","type_","size","energy_usage","box"]
        soru_list2 = [capacity,type_,size,energy_usage,box]
        
        if all([i == " " for i in soru_list2]):
            st.title('Bakalım sizin için nelerimiz var?')
            col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1])
            data2_b = data2_b[data2_b.image != "YOK"]
            data3 = data2_b.sample(frac=1).drop_duplicates(['brand']).sample(10).reset_index()
            im1 = Image.open(requests.get(data3.image[0], stream=True).raw).resize((100,150))
            im2 = Image.open(requests.get(data3.image[1], stream=True).raw).resize((100,150))
            im3 = Image.open(requests.get(data3.image[2], stream=True).raw).resize((100,150))
            im4 = Image.open(requests.get(data3.image[3], stream=True).raw).resize((100,150))
            im5 = Image.open(requests.get(data3.image[4], stream=True).raw).resize((100,150))
            im6 = Image.open(requests.get(data3.image[5], stream=True).raw).resize((100,150))
            im7 = Image.open(requests.get(data3.image[6], stream=True).raw).resize((100,150))
            im8 = Image.open(requests.get(data3.image[7], stream=True).raw).resize((100,150))
            im9 = Image.open(requests.get(data3.image[8], stream=True).raw).resize((100,150))
            im10 = Image.open(requests.get(data3.image[9], stream=True).raw).resize((100,150))

            with col1:
                b1 = st.image(im1, width=120)
                st.markdown(data3.brand[0])
                b6 = st.image(im6, width=120)
                st.markdown(data3.brand[5])
            with col2:
                b2 = st.image(im2, width=120) 
                st.markdown(data3.brand[1])
                b7 = st.image(im7, width=120)
                st.markdown(data3.brand[6])
            with col3:
                b3 = st.image(im3, width=120)
                st.markdown(data3.brand[2])
                b8 = st.image(im8, width=120)
                st.markdown(data3.brand[7])
            with col4:
                b4 = st.image(im4, width=120)
                st.markdown(data3.brand[3])
                b9 = st.image(im9, width=120)
                st.markdown(data3.brand[8])
            with col5:
                b5 = st.image(im5, width=120)
                st.markdown(data3.brand[4])
                b10 = st.image(im10, width=120)
                st.markdown(data3.brand[9])
          
        elif any([i != " " for i in soru_list2]):
            for m in soru_list2:
                if m == " ":
                    pass
                else:
                    m_index = soru_list2.index(m)
                    len_lst1.append(soru_list1[m_index])
                    len_lst2.append(m)

                    for k in range(0,len(len_lst2)):
                        dataf_b = dataf_b[dataf_b[len_lst1[k]] == len_lst2[k]]

            if len(dataf_b) == 0:
                st.title("Seçilen Kriterlere Uygun Bir Ürün Bulunamadı")

            elif len(dataf_b) == 1:
                st.title("Seçilen Kriterlere Uygun Bir Ürün Bulundu")
                dataf_b = dataf_b.reset_index()
                im1 = Image.open(requests.get(dataf_b.image[0], stream=True).raw).resize((100,150))
                b1 = st.image(im1, width=120)
                st.title(dataf_b.brand[0])
                st.title("Fiyat")
                st.title(dataf_b.price[0])

            elif len(dataf_b) == 2:
                st.title("Seçilen Kriterlere Uygun İki Ürün Bulundu")
                col1, col2 = st.columns([1,1])
                dataf_b = dataf_b.reset_index()
                im1 = Image.open(requests.get(dataf_b.image[0], stream=True).raw).resize((100,150))
                im2 = Image.open(requests.get(dataf_b.image[1], stream=True).raw).resize((100,150))
                with col1:
                    b1 = st.image(im1, width=120)
                    st.title(dataf_b.brand[0])
                    st.title("Fiyat")
                    st.title(dataf_b.price[0])
                with col2:
                    b2 = st.image(im2, width=120)
                    st.title(dataf_b.brand[1])
                    st.title("Fiyat")
                    st.title(dataf_b.price[1])


            elif len(dataf_b) == 3:
                st.title("Seçilen Kriterlere Uygun Üç Ürün Bulundu")
                col1, col2, col3 = st.columns([1,1,1])
                im1 = Image.open(requests.get(dataf_b.image[0], stream=True).raw).resize((100,150))
                im2 = Image.open(requests.get(dataf_b.image[1], stream=True).raw).resize((100,150))
                im3 = Image.open(requests.get(dataf_b.image[2], stream=True).raw).resize((100,150))

                with col1:
                    b1 = st.image(im1, width=120)
                    st.title(dataf_b.brand[0])
                    st.title("Fiyat")
                    st.title(dataf_b.price[0])
                with col2:
                    b2 = st.image(im2, width=120)
                    st.title(dataf_b.brand[1])
                    st.title("Fiyat")
                    st.title(dataf_b.price[1])
                with col3:
                    b3 = st.image(im3, width=120)
                    st.title(dataf_b.brand[2])
                    st.title("Fiyat")
                    st.title(dataf_b.price[2])


            elif len(dataf_b) >3:
                st.title("Seçilen Kriterlere En Uygun Ürünler")
                ucuz = dataf_b.sort_values(by="price", ascending=True).reset_index()
                fp1 = dataf_b[dataf_b["puan"] > dataf_b["puan"].quantile(0.25)].sort_values(by="puan", ascending=False).reset_index()
                fp1 = fp1.drop(["index"],axis=1)
                fp2 = fp1[fp1["price"] <dataf_b["price"].quantile(0.75)].sort_values(by="puan", ascending=False).reset_index()
                fp2 = fp2.drop(["index"],axis=1)
                fp3 = fp2.sort_values(by="puan", ascending=False).reset_index()
                fp3 = fp3.drop(["index"],axis=1)
                if len(fp3.puan) == 2:
                    col1, col2 = st.columns([1,1])
                    im1 = Image.open(requests.get(ucuz.image[0], stream=True).raw).resize((100,150))
                    im2 = Image.open(requests.get(fp3.image[0], stream=True).raw).resize((100,150))
                    im3 = Image.open(requests.get(fp3.image[1], stream=True).raw).resize((100,150))

                    with col1:
                        b1 = st.image(im1, width=120)
                        b2 = st.image(im2, width=120)
                        b3 = st.image(im3, width=120)
                    with col2:
                        st.title("En Ucuz")
                        st.markdown("Ürün Adı : " + ucuz.full_name[0], unsafe_allow_html=True)
                        st.markdown("Fiyat : " + str(ucuz.price[0]))

                        st.title("Fiyat Performans")
                        st.markdown("Ürün Adı : " + fp3.full_name[0] )
                        st.markdown("Fiyat : " + str(fp3.price[0]) )
                        st.title(" ")
                        st.title("Çok Satılan")
                        st.markdown("Ürün Adı : " + fp3.full_name[1] )
                        st.markdown("Fiyat : " + str(fp3.price[1]) )
                elif len(fp3.puan) == 1:
                    col1, col2 = st.columns([1,1])
                    im1 = Image.open(requests.get(ucuz.image[0], stream=True).raw).resize((100,150))
                    im2 = Image.open(requests.get(fp3.image[0], stream=True).raw).resize((100,150))
                    im3 = Image.open(requests.get(fp1.image[0], stream=True).raw).resize((100,150))

                    with col1:
                        b1 = st.image(im1, width=120)
                        b2 = st.image(im2, width=120)
                        b3 = st.image(im3, width=120)
                    with col2:
                        st.title("En Ucuz")
                        st.markdown("Ürün Adı : " + ucuz.full_name[0], unsafe_allow_html=True)
                        st.markdown("Fiyat : " + str(ucuz.price[0]))

                        st.title("Fiyat Performans")
                        st.markdown("Ürün Adı : " + fp3.full_name[0] )
                        st.markdown("Fiyat : " + str(fp3.price[0]) )
                        st.title(" ")
                        st.title("Çok Satılan")
                        st.markdown("Ürün Adı : " + fp1.full_name[0] )
                        st.markdown("Fiyat : " + str(fp1.price[0]) )
                        
                elif len(fp3.puan) > 2:
                    col1, col2 = st.columns([1,1])
                    im1 = Image.open(requests.get(ucuz.image[0], stream=True).raw).resize((100,150))
                    im2 = Image.open(requests.get(fp3.image[0], stream=True).raw).resize((100,150))
                    im3 = Image.open(requests.get(fp1.image[0], stream=True).raw).resize((100,150))

                    with col1:
                        b1 = st.image(im1, width=120)
                        b2 = st.image(im2, width=120)
                        b3 = st.image(im3, width=120)
                    with col2:
                        st.title("En Ucuz")
                        st.markdown("Ürün Adı : " + ucuz.full_name[0], unsafe_allow_html=True)
                        st.markdown("Fiyat : " + str(ucuz.price[0]))

                        st.title("Fiyat Performans")
                        st.markdown("Ürün Adı : " + fp3.full_name[0] )
                        st.markdown("Fiyat : " + str(fp3.price[0]) )
                        st.title(" ")
                        st.title("Çok Satılan")
                        st.markdown("Ürün Adı : " + fp3.full_name[3] )
                        st.markdown("Fiyat : " + str(fp3.price[3]) )

