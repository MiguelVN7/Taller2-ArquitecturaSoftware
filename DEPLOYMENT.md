# Guía de Despliegue en AWS con Docker Swarm

## 1. Configuración de Security Group

Puertos necesarios:
- SSH (22) - Tu IP
- HTTP (80) - 0.0.0.0/0
- Custom TCP (5000) - 0.0.0.0/0 (Flask)
- Custom TCP (2377) - Security Group ID (Docker Swarm manager)
- Custom TCP (7946) - Security Group ID (Docker Swarm comunicación)
- Custom UDP (7946) - Security Group ID (Docker Swarm comunicación)
- Custom UDP (4789) - Security Group ID (Docker Swarm overlay)

## 2. User Data Script para EC2

```bash
#!/bin/bash
yum update -y
yum install -y docker
systemctl start docker
systemctl enable docker
usermod -a -G docker ec2-user
curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
systemctl restart docker
```

## 3. Inicializar Docker Swarm (Líder)

```bash
# Conectarse al líder
ssh -i tu-key.pem ec2-user@IP_PUBLICA_LIDER

# Inicializar swarm
docker swarm init --advertise-addr IP_PRIVADA_LIDER

# Obtener token de manager
docker swarm join-token manager
```

## 4. Unir Managers al Cluster

En cada una de las 3 instancias manager:

```bash
# Conectarse a cada manager
ssh -i tu-key.pem ec2-user@IP_PUBLICA_MANAGER

# Unirse al swarm (usa el token del paso anterior)
docker swarm join --token SWMTKN-1-XXXXX IP_PRIVADA_LIDER:2377
```

## 5. Verificar el Cluster

Desde el líder:

```bash
# Ver todos los nodos
docker node ls

# Deberías ver 4 nodos con rol Manager
```

## 6. Crear el Servicio con 10 Réplicas

```bash
docker service create \
  --name pokedex-pokeneas \
  --replicas 10 \
  --publish 5000:5000 \
  --env AWS_ACCESS_KEY_ID=TU_ACCESS_KEY \
  --env AWS_SECRET_ACCESS_KEY=TU_SECRET_KEY \
  --env AWS_REGION=us-east-2 \
  --env S3_BUCKET=pokedex-pokeneas-miguel-villegas \
  --env SECRET_KEY=tu-clave-secreta \
  miguelvn7/pokedex-pokeneas:latest
```

## 7. Comandos de Verificación

```bash
# Ver servicios
docker service ls

# Ver réplicas y en qué nodo están
docker service ps pokedex-pokeneas

# Ver logs del servicio
docker service logs pokedex-pokeneas -f

# Inspeccionar el servicio
docker service inspect pokedex-pokeneas

# Escalar el servicio (si necesitas cambiar réplicas)
docker service scale pokedex-pokeneas=10
```

## 8. Actualizar el Servicio

Si necesitas actualizar la imagen:

```bash
docker service update --image miguelvn7/pokedex-pokeneas:latest pokedex-pokeneas
```

## 9. Probar la Aplicación

Visita cualquiera de las IPs públicas en el puerto 5000:
- http://IP_PUBLICA_LIDER:5000
- http://IP_PUBLICA_MANAGER1:5000
- http://IP_PUBLICA_MANAGER2:5000
- http://IP_PUBLICA_MANAGER3:5000

El balanceo de carga se hace automáticamente entre las réplicas.

## 10. Verificar ID del Contenedor

En cada ruta de la aplicación verás el Container ID, que cambiará con cada request demostrando el balanceo de carga.

## Comandos Útiles

```bash
# Eliminar servicio
docker service rm pokedex-pokeneas

# Ver nodos
docker node ls

# Promover un nodo a manager
docker node promote NOMBRE_NODO

# Degradar un nodo a worker
docker node demote NOMBRE_NODO

# Ver recursos del swarm
docker system df

# Limpiar recursos no usados
docker system prune -a
```

## Troubleshooting

### Si las réplicas no se distribuyen:
```bash
# Ver por qué una réplica está fallando
docker service ps pokedex-pokeneas --no-trunc

# Ver logs de una tarea específica
docker service logs TASK_ID
```

### Si necesitas reiniciar el servicio:
```bash
docker service update --force pokedex-pokeneas
```

### Verificar conectividad entre nodos:
```bash
# En el líder
docker node ls

# Debe mostrar todos los nodos como "Ready"
```

