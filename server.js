const express = require('express');
const bodyParser = require('body-parser');
const app = express();

app.use(bodyParser.urlencoded({ extended: true }))

// parse requests of content-type - application/json
app.use(bodyParser.json())





app.listen(3000, () => {
    console.log("Server is listening on port 3000");
});


var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/local";


app.post('/post',function(req,res){
  

    MongoClient.connect(url,
        function(err, db) {
        if (err) throw err;
        
        var dbo = db.db("local");
        dbo.collection("notes").insert({"cfname":req.body.cfname,"clname":req.body.clname,"email":req.body.email}, function(err, res) {
            if (err) throw err;
            console.log("insert success");
            console.log(req.body.custid);
            db.close();
        });
    });
});

app.get('/get/:noteid',function(req,res) {
  

    MongoClient.connect(url,
        function(err, db) {
        if (err) throw err;
        
        var dbo = db.db("local");
        dbo.collection("notes").find({"_id":req.params.noteid}).toArray(function(err, result) {
        
            
            console.log("record found");
            console.log(result);
            console.log(typeof(req.params.noteid))
            
            db.close();
        });
    });
});



app.delete('/deletenote/:noteid',function(req, res) {
  

    MongoClient.connect(url,
        function(err, db) {
        if (err) throw err;
        
        var dbo = db.db("local");
        dbo.collection("notes").deleteOne({"_id":req.params.noteid}, function(err) {
            if (err) {
                res.send(err);
            
            };
            console.log("record deleted");
            
            db.close();
        });
    });
});   

app.put('/update/:noteid',function(req, res) {
  

    MongoClient.connect(url,
        function(err, db) {
        if (err) throw err;
        
        var dbo = db.db("local");
        dbo.collection("notes").updateOne({"_id":req.params.noteid}, {$set: { cfname :req.body.cfname, clname:req.body.clname,phone:req.body.phone }}, function(err, res) {
            if (err) throw err;
            console.log("recordupdated");
            console.log(req.params.noteid)
            db.close();
        });
    });
});     