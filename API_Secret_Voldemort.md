# API REST Secret Voldemort

## First Sprint: 15/10 to 03/11

| ENDPOINT     | METHOD | URI         | PARAMS       | RESPONSE      | COMMENTS |
| ---------    | ------ | ----------- | ------------ | ------------- | -------- |
| register     | POST   | `/user/register` | `{ e-mail: str, username: str, password: str, photo?: image }` | 409: Conflict if: `e-mail` already registered or `username` already registered \ 400wwwwwwwwwwwwwwwwwwwwwwwwwwwwwq:Bad Request if: can't parse `e-mail` | `password` is hash |
| validate email | POST | `/user/<id>/validation` | `{ validation_code: str }` | 200: `{ userId : int }` \ 403:Forbidden if `validation_code` is wrong | |
| login | POST | `/user/login` | `{ e-mail: str, password: str } ` | 200: `{ userId: int }` \ 400: Bad request: can't parse `e-mail` \ 401 Unauthorized: invalid `password` | `password` is a hash |
| get history | GET | `/user/<id>/history` | | 200: `{ phoenix_wins : int, phoenix_loses : int; death_eater_wins : int, death_eater_loses: int}` |
| list lobbies | GET | `/rooms` | `{ min_players?: int, max_players?: int }` | 200: `[ { id : int, lobby_name: str, current_players : int, max_players: int, min_players: int } ]` | |
| create lobby | POST |`/rooms` | `{ userId: int, lobby_name: str, min_players : int, max_players : int } ` | 200: `LOBBY` | |
| join lobby | POST |`/rooms/<id>` | `PLAYER_SHORT` | 200: `PLAYER` \ 409: Conflict if: `nick` already exists in this lobby | |
| get lobby state | GET | `/rooms/<id>` | | 200: `LOBBY` | if !started, then game_id == -1. When last player makes this call, lobby gets deleted |
| get owner | GET | `/rooms/<id>/owner` | | 200: `{ nick trrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr: str }` | |
| list players | GET | `/rooms/<id>/player`| | 200:`[ { nick: str} ]` | |
| change nick | PUT | `/rooms/<id>/player` | `{ nick: str }` | 200: `{ nick: str }` \ 409: Conflict if: `nick` already exists in this lobby | |
| kick player | POST | `/rooms/<id>/owner/kick` | `{ userId: int }` | | |
| start game | POST | `/rooms/<id>/owner/start` | | | Server stops more people from entering and starts the game. |
| avaliable candidates | GET | `/games/<id>/players` | | 200: `[ { nick : dfgggggggggggggggggggggstr } ]` | PRE : There's a Minister Selected |
| nominate director | POST | `/games/<id>/director` | `{ nick : str }` | 200: `{ nick : str }` \ 409:Conflict if nick submitted is not valid  |  |
| post proclamation | POST |`/games/<id>/proclamation` | `{ is_fenix_procl : bool }` | 200: `{ is_fenix_procl : bool }` \ 403: Forbidden : If the client is not the correct  |  | PRE : Minister and Director are selected
| end game | POST |`/games/<id>/end` | `{ user_id: int }` | 200: `ggdddddddddddddddddddddd[ROL]` | Updates Player History, and when the last player makes this request, then the game gets delerewqted |

-------------

`LOBBY = { lobby_id: int, lobby_name: str, game_id : int, creation_date: datetimestr, creator_username: str, min_players: int, max_players: int, started: bool }`

`PLAYER = { userId: int, nick: str, number_player: int, role: str, its_alive: bool, director: bool, minister: bool, chat_blocked: bool }`

`PLAYER_SHORT = { userId : int, nick : str }`

`ROL = { nick : str, rol : enum }`

-------------

## Descripción de los endpoints:
 
**login POST /login/** : éste endpoint toma como parámetros en primer lugar un `e-mail` que se supone registrado y único en el sistema, cuyo formato se debe validar (c/c se devuelve un staus code 400 con un mensaje informativo), y además validar que efectivamente exista registrado en el sistema (c/c se devuelve un 404 con un mensaje informativo); en segundo lugar una `password` la cual debe hashearse en la base de datos del sistema para validar que existe registrada (c/c se devuelve un status code de 401 con un mensaje informativo). 

**register POST /user**: este endpoint toma de parámetros `e-mail`, `username`, `password` y `photo`; éstos se encuentran en campos que el agente externo debe completar y el sistema validar. Los campos a llenar son: un `e-mail` que debe ser único, un `username` que también deber ser único, una `password` alfanumérica que debe ser entre 8 a 32 carácteres y una `photo` que es una imagen que se elige entre las predeterminadas en el sistema, con un valor por defecto. Como respuesta devuelve un status code 200 - Ok si no hubo errores de validación, un 409 si el e-mail o el `username` ya está registrado o un 400 como error en el formato del `e-mail` o `password` proporcionados.

**create lobby POST /rooms/new**: este endpoint toma los parámetros `userId`, `lobby_name`, `max_players?` y `min_players?`. El parámetro `userId` es el usuario que será creador de ese lobby lo que le permitirá iniciar la partida cuando desee, el parámetro `lobby_name` debe ser elegido por el usuario obligatatoriamente y es único. Los parámetros `min_players?` y `max_players?` en un futuro podrán asignarse opcionalmente por el usuario creador `userId`, que tendrán valores por default 5 y 10 respectivamente, de lo cual se encargará el front de garantizar que no va a ser menor a 5 ni mayor a 10; en éste sprint serán asignados ambos con valor 5 exclusivamente. En la respuesta de éste endpoint se incluirán además atributos tales como `started`, que será el cual pertenece a el estado de la partida, es decir, si la partida del lobby ha iniciado o no, por default inicia en false; luego `creation_date` que corresponderá a la fecha de creación del lobby.
