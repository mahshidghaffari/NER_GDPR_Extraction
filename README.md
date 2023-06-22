
# Setup

To start the service:
```bash
sudo docker-compose up
```

When adding requirements make sure to add the `build` tag
```bash
sudo docker-compose up --build
```

If you want to inspect what is happening inside the docker container, first get the name of the running service:
```bash
sudo docker ps -a 
```
which will return the following:
```bash
CONTAINER ID   IMAGE                              COMMAND                  CREATED             STATUS                         PORTS                                                                                  NAMES
03da5cbc3f07   ner_gdpr_extraction_ner-gdpr-ext   "tini -g -- start-no…"   2 minutes ago       Up 2 minutes (healthy)         0.0.0.0:5000->5000/tcp, :::5000->5000/tcp, 0.0.0.0:8888->8888/tcp, :::8888->8888/tcp   ner_gdpr_extraction_ner-gdpr-ext_1
```

Then you can inspect the container with:
```bash
sudo docker exec -it [CONTAINER-NAME] bash
```

i.e. 
```bash
sudo docker exec -it ner_gdpr_extraction_ner-gdpr-ext_1 bash
```