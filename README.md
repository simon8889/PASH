# Pash

pash is an online password manager, which works with mongo atlas as the database and a locally generated cryptographic key to encrypt the passwords, it has the possibility of backing it up so as not to lose the passwords if the database or password fails, You can also generate passwords without storing them.

## Installation
Clone the [Github](https://github.com/simon8889/PASH) repo.
```bash
git clone https://github.com/simon8889/PASH
```
go to the project directory.
```bash
cd pash
```
install the python package.
```bash
pip install .
```
pash is ready.
```bash
pash 
```

## Basic config
the only requirement to use pash is a free mongo atlas cluster.
This configuration is essential for the operation of pash, since with this pash will connect to mongo, the cryptographic key will be generated and the directory for backups will be configured.
This configuration is done with the following command:
```bash
pash config set-db-url <mongo url>
```
<mongo url> is the url to connect to the mongo atlas cluster

## Commands
view all the commands.
```bash
pash 
```
add a password to the database.
```bash
pash add-pass
```
update a password.
```bash
pash update-pass
```
update a password 
delete a passs from the database.
```bash
pash delete-pass
```
search or get a password.
```bash
pash get-pas
```
view the config options.
```bash
pash config
```
view the backup options.
```bash
pash backup 
```
generate a password whitout store it.
```bash
pash generate 
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)