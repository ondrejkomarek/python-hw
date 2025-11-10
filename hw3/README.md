Vytvořím docker bridge: docker network create -d bridge mynetwork

Vytvořím mongo db: docker run -d -p 27017:27017 --name "mymongo" --network mynetwork mongo:latest

Buildnu image pro načítání csv: docker build -t read_csv_app .
Pustim ho: docker run -d --name read_csv-cont --network mynetwork read_csv_app
Načte mi data z csv a insertne je do db

bonus:
sločím do složky: cd bonus/
Buildnu rest api server appku a pustim ji:
docker build -t myserver_app .
docker run -d --name myserver -p 8080:80 --network mynetwork myserver_app

v prohlížeči zavolám http://localhost:8080/data a dostanu JSON odpověď s daty