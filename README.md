# Projeto de Teste

Para configurar a comunicação MQTT com Python, é necessário ter o Python instalado e, em seguida, instalar a biblioteca paho-mqtt usando o pip . O projeto envolve dois arquivos: um publicador , que envia mensagens para um tópico MQTT , e um assinante , que recebe essas mensagens ao estar inscrito no mesmo tópico. Ambos utilizam um corretor MQTT , como o HiveMQ , para intermediar a comunicação.

Para testar, é preciso abrir dois terminais, executar primeiro a assinatura e depois o publicador. Quando uma mensagem for enviada pelo publicador, ela aparecerá automaticamente no terminal do assinante. Esse modelo de comunicação é amplamente usado em IoT , automação e sistemas distribuídos, pois permite a troca de mensagens leve e eficiente em tempo real.








