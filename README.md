DisplayErgonomia
================

Display que muestra valores del entorno

### AP/Station WiFi
Se utiliza el contenedor de docker: https://github.com/cjimti/iotwifi


### comando, limita los archivos log, estaban llenando el espacio disponiible

docker run -d --name wifipanel --privileged --net host --restart=unless-stopped       -v $(pwd)/wificfg.json:/cfg/wificfg.json --log-opt max-size=10m --log-opt max-file=5 davidfigcas/iotwifi
