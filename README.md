# ERD - Entity Relationship Diagram



[![ERD](https://www.jooq.org/img/sakila.png)](https://www.jooq.org/sakila)



## Install MySQL

```bash
sudo apt install mysql-server
```

and then on terminal write 

```bash
sudo mysql
```

See all users

```sql
select user, host from mysql.user;

```

If you don't see your name add this

```sql
create user 'username'@'localhost' identified by 'password';
grant all privileges on *.* to 'username'@'localhost';
flush privilages;

exit;
```


And Then Create a DataBase

```bash
mysql -u username -h localhost -P port -p

```

```sql
create database sakilla;
```

