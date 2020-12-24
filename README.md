# Ansible Redmine Role + Molecule Testing + Vagrant

Se ha construido un rol de Ansible que se encarga de instalar MariaDB (motor de base de datos), Nginx (servidor web HTTP), Puma (servidor de aplicacion Ruby) y finalmente instala Redmine (sistemas gestor de Tickets). Para utilizar este rol se ha planteado utilizar Vagrant para crear el entorno de desarrollo con VBox como driver. De esta forma, el entorno es aprovisionado con el playbook que implementa el rol descrito. Para las pruebas se utiliza Molecule, el cual se encarga de crear con Vagrant las maquinas virtuales donde se ejecutara el playbook y luego se hace una pequeña comprobacion de los servicios con TestInfra. Las pruebas realizadas se hacen con Ubuntu 20.04 y Ubuntu 18.04.

## Requerimientos

Para instalar se debe contar con los siguientes paquetes:

Vagrant (2.2.14) [DESCARGA](https://www.vagrantup.com/downloads.html)

En ubuntu 18.04 o 20.04:
```
sudo apt-get install vagrant qemu
```

Ansible (2.9.6) [DESCARGA](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)

En ubuntu 18.04 o 20.04:
```
sudo apt-get install ansible 
```

Python (3.8.5) [DESCARGA](https://www.python.org/downloads/)

En ubuntu 18.04 o 20.04:
```
sudo apt-get install python python3-pip
```

En cuanto a las librerias Python necesarias se deben ejecutar los siguientes comandos.
```
python3 -m venv env
source env/bin/activate
pip3 install -r requeriments.txt
```

## Comandos

### Utilizar el despliegue en Vangrant

Si se quiere levantar el entorno con Vagrant se debe clonar el repositorio y ejecutar el comando up de Vagrant en la carpeta que se encuentra el Vagrantfile.

```
git clone https://github.com/manuelchichi/ansible-redmine-role
cd ansible-redmine-role/
vagrant up
```

Esto levantara la maquina virtual (ubuntu 20.04), la aprovisionara con el rol de redmine y una vez finalizado se podra acceder en la siguiente direccion myprojects.example.com:8082. Las credenciales del usuario por defecto son (usuario: admin, contraseña: admin).


### Realizar pruebas


Una vez clonado el repositorio e inicializado el entorno en Python nos debemos dirigir la carpeta que contiene el rol (roles/redmine/). Alli se debe ejecutar el siguiente comando para realizar el set de pruebas completo y luego borrar las instancias.

```
cd roles/redmine/
molecule test
```

Si se desea crear las instancias y correr los playbooks sin realizar las pruebas ni destruir las instancias.

```
molecule converge
```

Luego sobre este podremos realizar la verificacion con el siguiente comando.

```
molecule verify
```

### Variables de entorno

Se han agregado una serie de variables de entorno para personalizar la instalacion de Redmine segun se desee. Se lista a continuacion algunas de ellas.

+ redmine_version: (Version de redmine)
+ redmine_user_password: (Contraseña del usuario Redmine de la base de datos)
+ mariadb_root_password: (Contraseña del usuario Root de la base de datos)
+ redmine_url: (URL a la que sera accesible el proyecto)
+ ruby_version: (Indica la version de Ruby que se instalara)


## Mejoras

- [X] Utilizar RVM para manejar las versiones de Ruby.
- [X] Cambiar a Nginx + Puma.
- [ ] Hacer mas controles con las versiones de Ubuntu.
- [ ] Indicar correctamenta las dependencias.
- [X] Agregar documentacion de Variables de entorno en el README.
- [ ] Agregar mas variables al rol Redmine.

