# Ansible Redmine Role + Molecule Testing + Vagrant

Se ha construido un rol de Ansible que se encarga de instalar MariaDB (motor de base de datos), Apache (servidor web HTTP), Passanger (servidor de aplicacion Ruby) y finalmente instala Redmine (sistemas gestor de Tickets). Para utilizar este rol se ha planteado utilizar Vagrant para crear el entorno de desarrollo con VBox como driver. De esta forma, el entorno es aprovisionado con el playbook que implementa el rol descrito. Para las pruebas se utiliza Molecule, el cual se encarga de crear con Vagrant las maquinas virtuales donde se ejecutara el playbook y luego se hace una pequeña comprobacion de los servicios con TestInfra. Las pruebas realizadas se hacen con Ubuntu 20.04 y Ubuntu 18.04.

## Requerimientos

Para instalar se debe contar con los siguientes paquetes:

Ansible (2.9.6)

```
sudo apt-get install ansible
```

Vagrant (2.2.14)
```
sudo apt-get install vagrant.
```

Python (3.8.5)
```
sudo apt-get install python python3-pip
```

En cuanto a las librerias Python necesarias se encuentran las siguientes.
```
pip3 install molecule -U
pip3 install request -U
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


Una vez clonado el repositorio nos debemos dirigir la carpeta que contiene el rol (roles/redmine/). Alli se debe ejecutar el siguiente comando para realizar el set de pruebas completo y luego borrar las instancias.

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

## Mejoras

- [ ] Utilizar RVM para manejar las versiones de Ruby.
- [ ] Hacer mas controles con las versiones de Ubuntu.
- [ ] Indicar correctamenta las dependencias.
- [ ] Mejorar documentacion del README.
- [ ] Agregar mas variables al rol Redmine.

