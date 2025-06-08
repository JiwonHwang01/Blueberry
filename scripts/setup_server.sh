#!/bin/bash

# 시스템 업데이트
sudo apt update
sudo apt upgrade -y

# 필요한 패키지 설치
sudo apt install -y python3-pip python3-venv nginx

# 프로젝트 디렉토리 생성
mkdir -p /home/ubuntu/blueberry
cd /home/ubuntu/blueberry

# Python 가상환경 생성
python3 -m venv venv
source venv/bin/activate

# Git 설치 및 프로젝트 클론
sudo apt install -y git
git clone https://github.com/YOUR_USERNAME/blueberry.git .

# 의존성 설치
pip install -r requirements.txt
pip install gunicorn

# Gunicorn 서비스 설정
sudo tee /etc/systemd/system/blueberry.service << EOF
[Unit]
Description=Blueberry Gunicorn Service
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/blueberry
Environment="PATH=/home/ubuntu/blueberry/venv/bin"
ExecStart=/home/ubuntu/blueberry/venv/bin/gunicorn --workers 2 --bind unix:/home/ubuntu/blueberry/blueberry.sock blueberry.wsgi:application

[Install]
WantedBy=multi-user.target
EOF

# Nginx 설정
sudo tee /etc/nginx/sites-available/blueberry << EOF
server {
    listen 80;
    server_name _;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        root /home/ubuntu/blueberry;
    }

    location /media/ {
        root /home/ubuntu/blueberry;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/blueberry/blueberry.sock;
    }
}
EOF

# Nginx 설정 활성화
sudo ln -s /etc/nginx/sites-available/blueberry /etc/nginx/sites-enabled
sudo rm -f /etc/nginx/sites-enabled/default

# 권한 설정
sudo chown -R ubuntu:www-data /home/ubuntu/blueberry
sudo chmod -R 755 /home/ubuntu/blueberry

# 서비스 시작
sudo systemctl start blueberry
sudo systemctl enable blueberry
sudo systemctl restart nginx

# 방화벽 설정
sudo ufw allow 'Nginx Full'
sudo ufw allow OpenSSH
sudo ufw --force enable 