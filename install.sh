echo "Start installation"
sudo pip3 install flask
sudo pip3 install flask_selfdoc

sudo cp /home/pi/servo_demo/webpag.service /etc/systemd/system
systemctl enable webpag.service

sudo systemctl daemon-reload
systemctl start webpag.service
systemctl status webpag.service

echo "Installation is finished."