
# Django SSR con postgress y mongodb (previo)

Este proyecto consiste en crear una arquitectura que perimta crear aplicaciones web empresariales con las siguientes
caracteristicas:

- Indexable por todos los buscadores: el servidor renderiza todo el JavaScript retornando un documentl html completo.
- Alta interactividad: se utiliza VUE.JS como framework para manejar la vista.
- Alta escalabilidad: se utilizan contenedores docker que se pueden replicar falcilmente.

# Listado de commandos
Todos los comandos de este projecto estan en un Makefile. Los comandos
disponibles són:

| Commando      | Acción                                    |
|---------------|-------------------------------------------|
| make b        | hace un 'build' de todos los contenedores |
| make b-django | to                                        |
| make u        |                                           |
| u-node        |                                           |
| d             |                                           |
| s-django      |                                           |
| s-node        |                                           |
| r-django      |                                           |
| g-remove-all  |                                           |
| g-stop-all    |                                           |

