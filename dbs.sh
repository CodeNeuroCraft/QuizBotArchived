sudo systemctl start redis-server
surreal start memory -A --user root --pass root
sudo systemctl stop redis-server