let request = require("request");
const headers = {
//  'Authorization':'Bearer SFomXW9gmdhsF2AVYjsMReiDLf7XF7KTLECTbT87VJA.RXRJBDJjY_B0VFwWhPDhMTzb-p45uKW5RIbXCFwpVgs'
  'Authorization':'Bearer '+ process.env.REMO_API_TOKEN
}
const options = {
  //    url:'https://api.coindesk.com/v1/bpi/currentprice.json'
      url:'https://api.nature.global/1/appliances',
      headers:headers,
      json:true
}

const express = require('express');
const app = express();

//app.get('/remo/signals',
app.get('/',
    function(req,res){
      request.get(
        options,
        function(error,response,body){
          res.header('Access-Control-Allow-Origin','*')
          res.json(body[0].signals);
        }
      );
    }
  );

app.listen(3000, () => console.log('Listening on port 3000'));
