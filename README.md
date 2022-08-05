# User API challenge

- Ana Rafaela
### Tech Stack
1. Postgresql
2. Redis
3. Flask
4. Swager

### API Features
- Sort DEFAULT asc
- User Pagination
```curl
curl --location --request GET 'http://localhost:5000/users?page_size=1000&sort=desc&page_number=1' \
--header 'Content-Type: application/JSON'
```
- User Filtering
```curl
curl --location --request GET 'http://localhost:5000/users' \
--header 'Content-Type: application/JSON' \
--data-raw '[
    {"lastname":"wagner"},
    {"name":"adam"}, 
    {"name":"sara"}
]'
```
## Total Database rows
- 1,100,000
## Installation Requirements
- [Docker](https://docs.docker.com/engine/) 

## APP Local Deploy

* Be sure to enable Docker installation for locally deploy

### Step 1
Clone APP from [GIT repo](https://github.com/annralf/test-power-to-fly.git) 
```bash
git clone https://github.com/annralf/test-power-to-fly.git
```
### Step 2
Build Docker image 
```bash
cd test-power-to-fly/
docker-compose build
```

### Step 3
Start Docker containers
```bash
docker-compose up -d
```
## Usage
* local deploy
```curl
curl --location --request GET 'http://localhost:8000/users' \
--header 'Content-Type: application/JSON'
```
## Public API EP
[Here](https://github.com/annralf/test-power-to-fly/blob/main/PowerToFlyChallenge.postman_collection.json) the API Postman Collection

```curl
curl --location --request GET 'http://3.95.219.79/users' \
--header 'Content-Type: application/JSON'
```
## License
[MIT](https://choosealicense.com/licenses/mit/)
