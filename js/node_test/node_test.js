console.log("test OK!");

let req = require("request");
const headers = {
  'Authorization':'Bearer SFomXW9gmdhsF2AVYjsMReiDLf7XF7KTLECTbT87VJA.RXRJBDJjY_B0VFwWhPDhMTzb-p45uKW5RIbXCFwpVgs'
}
const options = {
  //    url:'https://api.coindesk.com/v1/bpi/currentprice.json'
      url:'https://api.nature.global/1/appliances',
      headers:headers,
      json:true
}
req.get(
  options,
  function(error,response,body){
    console.log(body);
    console.log("ここからJSONの練習");
    console.log(body[0].id);
    console.log(body[0].signals);
  }
);
