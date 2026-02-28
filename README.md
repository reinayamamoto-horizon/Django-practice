### よく使うコマンドを bash エイリアスに登録する
`nano ~/.bashrc`
```
alias dcu='docker compose up -d --build'
alias dcm='docker compose exec web python manage.py'
alias dc='docker compose'
```