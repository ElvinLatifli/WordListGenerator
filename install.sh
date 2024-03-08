#!/bin/bash

echo "Gerekli bağımlılıkları kontrol ediliyor ve kuruluyor..."
apt-get update
apt-get install -y python3 git

echo "Python dosyasının izinleri ayarlanıyor..."
chmod +x "main.py"

echo "Yürütülebilir dosya PATH'e ekleniyor..."
sudo cp "main.py" /usr/local/bin/hackrick

echo "Kurulum tamamlandı. Wordlist oluşturucu tool'unuz kullanıma hazır."

exit 0
