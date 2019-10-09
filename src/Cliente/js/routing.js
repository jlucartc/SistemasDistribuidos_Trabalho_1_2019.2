const express = require('express');
const fs = require('fs');
const router = express.Router();
const net = require('net');
const pb = require('protocol-buffers');
var mensagens = pb(fs.readFileSync('js/Msgs.proto'));

var dispositivos = [];

router.get('/',function(req,res){

  fs.readFile('html/index.html',function(err,data){
    if(err){
      res.write("Erro na leitura do arquivo.");
      res.end();
    }else{
      res.render('index',{});
    }

  });

});

router.get('/descobrir',function(req,res){

  var timeout = 3000;

  var conn = net.createConnection({ port : 9999, host: '127.0.0.1'},() => {

    msg = mensagens.MsgSrvCli.encode({ tipo : mensagens.MsgSrvCli.Tipo.DESREQ, id: "0", dado : '', disps : [] });

    conn.write(msg);

  });

  conn.setTimeout(timeout,function(){

    res.render('index',{testemsg: 'Timeout atingido',type : 'warning'})
    conn.end();

  });

  conn.on('data',function(data){

      msg = new mensagens.MsgSrvCli.decode(data)

      dispositivos = msg.disps

      var itens = msg.disps

      if(itens.length == 0){

        res.render('index',{testemsg : "Não há dispositivos conectados no momento", itens : itens, type: "info"});

      }else{

        res.render('index',{itens : itens});

      }


      conn.end();
  });

  conn.on('error',function(err){
      res.render('index',{testemsg : 'Falha na conexão', type: 'danger'})
  });

});

router.get('/ver/:id',function(req,res){

  var disp = [];

  for( i = 0; i < dispositivos.length ; i++ ){

    if(dispositivos[i].id == req.params.id){

      disp = dispositivos[i];

      break;

    }

  }

  res.render('index',{dispositivo: disp});

});

router.get('/teste',function(req,res){

  timeout = 3000;

  var conn = net.createConnection({ port : 9999, host: '127.0.0.1'},() => {

    conn.write("Fazendo requisição para o servidor");

  });

  conn.on('data',function(data){
      res.render('index',{testemsg : data.toString(), type: 'success'});
      conn.end();
  });

  conn.on('error',function(err){
      res.render('index',{testemsg : 'Falha na conexão', type: 'danger'})
  });

  conn.setTimeout(timeout,function(){
      res.render('index',{testemsg : 'Timeout atingido. Conexão estabelecida', type: 'success'});
      conn.end();
  });

});

router.post('/executar',function(req,res){

  var string = req.body.op.split("-");

  var op = string[1];
  var id = string[0];

  console.log("op: "+op);
  console.log("id: "+id);

  var timeout = 3000;

  var conn = net.createConnection({ port : 9999, host: '127.0.0.1'},() => {

    msg = mensagens.MsgSrvCli.encode({
      tipo : mensagens.MsgSrvCli.Tipo.OPREQ,
      id : id,
      dado : op
    });

    conn.write(msg);

  });

  conn.setTimeout(timeout,function(){

    res.render('index',{testemsg: 'Timeout atingido',type : 'warning'})
    conn.end();

  });

  conn.on('data',function(data){

      var msg = new mensagens.MsgSrvCli.decode(data);

      var id = msg.id;

      var resultado = msg.dado.split("-");

      var op = resultado[0];

      var resultado = resultado[1];

      var disp = [];

      for( i = 0; i < dispositivos.length; i++){

          if(dispositivos[i].id == id){

            disp = dispositivos[i];

            break;

          }

      }

      res.render('index',{dispositivo: disp, resultado: resultado});

      conn.end();
  });

});

module.exports = router;
