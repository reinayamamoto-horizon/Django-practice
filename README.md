### よく使うコマンドを bash エイリアスに登録する
`nano ~/.bashrc`
```
alias dcu='docker compose up -d'
alias dcm='docker compose exec web python manage.py'
alias dc='docker compose'
```

### よく使うコマンド整理
```
docker compose exec web python manage.py makemigrations
docker compose exec web python manage.py migrate
```


Userテーブルで画像をアイコンとして使用したいからPillowをインストールした
`docker-compose exec web pip install Pillow`
