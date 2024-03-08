#!/bin/bash

INSTALL_DIR="$(pwd)/WordListGenerator"

echo "Gerekli bağımlılıkları kontrol ediliyor ve kuruluyor..."
apt-get update
apt-get install -y python3 git

echo "Python dosyasının izinleri ayarlanıyor..."
chmod +x "$INSTALL_DIR/main.py"

echo "Yürütülebilir dosya PATH'e ekleniyor..."
sudo cp "$INSTALL_DIR/main.py" /usr/local/bin/hackrick

echo "Kurulum tamamlandı. Wordlist oluşturucu tool'unuz kullanıma hazır."

exit 0
