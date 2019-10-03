const express = require('express');
const fs = require('fs');
const router = express.Router();
const net = require('net');

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

//router.get('/descobrir',function(req,res){ /****/ });

//router.get('/ver/:id'),function(req,res){ /****/ });

router.get('/teste',function(req,res){

  var conn = net.createConnection({ port : 9999, host: '127.0.0.1'},() => {

    conn.write("Fazendo requisição para o servidor");

  });

  conn.on('data',function(data){
      res.render('index',{testemsg : data.toString()});
      conn.end();
  });

});

module.exports = router;
