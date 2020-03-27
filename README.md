# Proxecto Odoo Andrés Pérez Villar

- [Proxecto Odoo Andrés Pérez Villar](#proxecto-odoo-andr-s-p-rez-villar)
    + [Texnoloxias usadas](#texnoloxias-usadas)
    + [Instalacion de Odoo](#instalacion-de-odoo)
    + [Comandos Docker-Compose](#comandos-docker-compose)
  * [Proxecto: Aluger de Kayaks](#proxecto--aluger-de-kayaks)
      - [Pasos dun Aluger](#pasos-dun-aluger)

### Texnoloxias usadas

	- Odoo 12.0
	- Postgres 9.5
	- Docker-Compose

> Debido a que na casa son usuario de Manjaro, e non de Ubuntu, a forma mais comoda que tiven de instalar odoo foi a traves de docker-compose. Neste repositorio atopase toda a informacion para iniciar Odoo 12 de forma rapida e sinxela.

### Instalacion de Odoo

1. Descargamos ou clonamos o repositorio.
2. Damos permisos aos directorios.

```bash
$ sudo chmod -R 777 addons
$ sudo chmod -R 777 etc
```

3. Arrancamos o contedor.

   ```bash
   $ docker-compose up
   ```

   > Na carpeta **addons** meteremos os nosos modulos.
   >
   > A configuracion de Odoo esta na carpeta **etc**, así como os logs.

4. Para crear un novo modulo entramos na terminal do contedor

   ```bash
   $ docker exec -ti -u root [contedor] bash
   ```

   > Dentro do contedor os modulos atopanse na carpeta **/mnt/extra-addons**

5. Unha vez na terminal do contedor, executamos odoo scaffold

   ```bash
   $ odoo scaffold andresperez /mnt/extra-addons
   ```

Unha vez realizados estes pasos teremos na carpeta **addons** da nosa maquina real un novo modulo, que no meu caso se chama *andresperez*

### Comandos Docker-Compose

**Comandos de interese:**

- Crear e Iniciar os contedores

``` bash
docker-compose up
```

- Parar e borrar os contedores, imaxes e volumes

```
docker-compose down
```

- Comezar, parar e reiniciar os contedores

```
docker-comopse start | stop | restart
```



## Proxecto: Aluger de Kayaks

Para este proyecto decidín facer un modulo de Odoo para a xestion dun aluger de kayaks. Xa que levo "traballando" nel no vrán desde fai un par de anos.

A forma de traballo e sinxela:

	- Hay que levar un rexistro dos clientes, asi como os diferentes alugeres que fan.
	- Cada cliente debe cubrir unha ficha coa sua informacion, asi como asinar o seu consentemento e responsabilidade
	- O empregado do aluger daralle un chaleco salvavidas a cada menor obrigatoriamente, asi como a os adultos que o pidan. Hay que levar a conta, para asegurarse de que non falta nigun.
	- Tamen se lle ofrecen a os nosos clientes uns bidóns estancos, en caso de que haxa disponibilidade de eles.
	- Para realizar unha reserva ( a traves do correo electronico ou do telefono), o cliente debe  deixar un telefono de contacto, unha fecha, e unha hora estimada.

#### Pasos dun Aluger

1. Chega un cliente que quere alugar un kayak, este cubrir a sua ficha de Cliente.

   ![](/home/andres/Imágenes/ficha_cliente.png)

2. Tras equipar a os clientes có que necesiten, estes baixarán a auga coa axuda do empregado.

3.  Ao voltar, o emppregado anotara a hora de salida final do cliente, na seguinte ficha:

   ![](/home/andres/Imágenes/ficha_alquiler.png)

4. Canto o cliente termina o aluger, o empregado completa os datos que faltan (*hora fin, tempo total, e TOTAL*)