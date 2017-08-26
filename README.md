# rpi_oled_weather
Вывод данных яндекс информера на oled дисплей подключеный к raspberry pi.

По адресу выбераем https://yandex.ru/pogoda/veliky-novgorod/informer код информера:

<a href="https://clck.yandex.ru/redir/dtype=stred/pid=7/cid=1228/*https://yandex.ru/pogoda/24" target="_blank"><img src="https://info.weather.yandex.net/24/4_white.ru.png?domain=ru" border="0" alt="Яндекс.Погода"/><img width="1" height="1" src="https://clck.yandex.ru/click/dtype=stred/pid=7/cid=1227/*https://img.yandex.ru/i/pix.gif" alt="" border="0"/></a>

Из кода вытаскиваем адрес картинки и вставляем свой код:
url = "https://info.weather.yandex.net/24/4_white.ru.png?domain=ru"

Я сделал у себя скрипт для cron
$ cat /etc/cron.d/oled 
#
# cron-jobs for oled pogoda
#
#MAILTO=root
@reboot root sleep 15 && /usr/bin/python /home/pi/Python/oled_image.py >> /home/pi/debug.log
0 * * * * root /usr/bin/python /home/pi/Python/oled_image.py

Используется вот эта библиотека
https://github.com/adafruit/Adafruit_SSD1306
