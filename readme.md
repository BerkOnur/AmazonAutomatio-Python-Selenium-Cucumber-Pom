
Python Selenium ve Cucumber kullanarak POM yapısı ile yazılmıştır.

Yapılan otomasyonda login, sayfalar arası geçiş, add to list'e ürün ekleme ve silme ve ürün
kontrolü yapılmıştır.


## Features

- http://www.amazon.com sitesine gelecek ve anasayfanin acildigini onaylayacak,
- Login ekranini acip, bir kullanici ile login olacak ( daha once siteye uyeligi varsa o olabilir )
- Ekranin ustundeki Search alanina ‘samsung’ yazip Ara butonuna tiklayacak,
- Gelen sayfada samsung icin sonuc bulundugunu onaylayacak,
- Arama sonuclarindan 2. sayfaya tiklayacak ve acilan sayfada 2. sayfanin su an gosterimde oldugunu onaylayacak,
- Ekranin en ustundeki ‘List’ linkine tiklayacak içerisinden Wish listi seçecek,
- Acilan sayfada bir onceki sayfada izlemeye alinmis urunun bulundugunu onaylayacak,
- Favorilere alinan bu urunun yanindaki ‘Delete’ butonuna basarak, favorilerimden cikaracak,
- Sayfada bu urunun artik favorilere alinmadigini onaylayacak

## Tech

- [Python Download](https://www.python.org/downloads/)
- [Selenium Webdriver](https://selenium-python.readthedocs.io/installation.html)
- [Cucumber download](https://cucumber.io/docs/installation/)


## Installation
## 1.1- Python Kurulumu

[Python Download](https://www.python.org/downloads/) adresinden son sürümünü indirebilirsiniz.

## 1.2- Selenium Kurulumu

Python kurulumumuzu tamamladıktan sonra Selenium’u kuralım.

- [Selenium Webdriver](https://selenium-python.readthedocs.io/installation.html)

Terminal'e

- pip install selenium

eğer sorun yaşadıysanız ;

- pip3 install selenium

## Run Test

- Terminale "behave" yazmanız yeterli