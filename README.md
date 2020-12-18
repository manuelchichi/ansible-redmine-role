# Ansible Redmine Role + Molecule Testing + Vagrant

Se ha construido un rol de Ansible que se encarga de instalar MariaDB (motor de base de datos), Apache (servidor web HTTP), Passanger (servidor de aplicacion Ruby) y finalmente instala Redmine (sistemas de Tickets). Para utilizar este rol se ha planteado utilizar Vagrant para crear el entorno de desarrollo con VBox como driver. De esta forma, el entorno es aprovisionado con el playbook que implementa el rol descrito. Para las pruebas se utiliza Molecule, el cual se encarga de crear con Vagrant las maquinas virtuales donde se ejecutara el playbook y luego se hace una pequeña comprobacion de los servicios con TestInfra. Las pruebas realizadas se hacen con Ubuntu 20.04 y Ubuntu 18.04.

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

```
pip3 install molecule -U
pip3 install request -U
```

## Comandos

Si se quiere realizar una 

## Mejoras

- [ ] Utilizar RVM para manejar las versiones de Ruby.
- [ ] Hacer mas controles con las versiones de Ubuntu.
- [ ] Indicar correctamenta las dependencias.


